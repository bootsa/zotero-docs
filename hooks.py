"""
MkDocs hooks for handling Dokuwiki `{{topic>...}}` index macros.

After conversion, KB index pages contain placeholder comments like:

    <!-- dokuwiki-plugin: topic>kb +basics&nouser&nodate -->

At build time, this hook scans every Markdown source file's YAML frontmatter
for a `tags:` list, builds a tag index, and substitutes each topic comment
with a Markdown bullet list of matching pages.

Topic spec grammar:
  - bare token  | +token : require that tag
  - -token              : exclude that tag
  - &option             : display option (ignored)
"""

import json
import posixpath
import re
import subprocess
import urllib.parse
from pathlib import Path

import yaml
from markdown.extensions.toc import slugify, unique


URL_PREFIX = '/support/'
TOPIC_RE = re.compile(r'<!--\s*dokuwiki-plugin:\s*topic>([^>]+?)\s*-->')
HEADING_RE = re.compile(r'^#{1,6}\s+(.+?)\s*$', re.MULTILINE)
# Matches an opening <a> tag with an href into our docs namespace. Separates
# the URL path from any `#anchor` so we can check each independently.
INTERNAL_LINK_RE = re.compile(
    r'<a(?P<pre>\s[^>]*?)'
    r'href="(?P<url>' + re.escape(URL_PREFIX) + r'[^"#?]*)'
    r'(?:\?[^"#]*)?'
    r'(?:#(?P<anchor>[^"]*))?"'
    r'(?P<post>[^>]*)>'
)

_tag_index: dict = {}
_valid_urls: set = set()
_page_anchors: dict = {}  # url (no trailing slash) -> set of anchor ids
_last_modified: dict = {}  # repo-relative path -> ISO date string


def _build_last_modified(repo_root):
    """Build the last-modified date for every tracked file by walking
    `git log` once. Files whose newest commit is the initial commit fall
    back to the legacy DokuWiki dates from `dokuwiki_dates.json`, so the
    site shows real edit dates for the pre-migration history.

    Requires the full git history — in CI, make sure actions/checkout
    uses `fetch-depth: 0`."""
    if _last_modified:
        return
    try:
        initial = subprocess.run(
            ['git', '-C', str(repo_root), 'rev-list', '--max-parents=0', 'HEAD'],
            capture_output=True, text=True, check=True,
        ).stdout.strip().split('\n')[0] or None
    except (subprocess.CalledProcessError, FileNotFoundError):
        initial = None

    try:
        proc = subprocess.run(
            ['git', '-C', str(repo_root), 'log',
             '--name-only', '--format=COMMIT %H %cs'],
            capture_output=True, text=True, check=True,
        )
    except (subprocess.CalledProcessError, FileNotFoundError):
        return

    # First sighting of each file in the reverse-chronological log == newest
    seen = {}  # repo-relative path -> (sha, iso-date)
    cur_sha = None
    cur_date = None
    for line in proc.stdout.splitlines():
        if line.startswith('COMMIT '):
            rest = line[len('COMMIT '):]
            cur_sha, _, cur_date = rest.partition(' ')
        elif line and cur_sha and cur_date and line not in seen:
            seen[line] = (cur_sha, cur_date)

    # DokuWiki fallback map: { "kb/foo": "YYYY-MM-DD", ... }
    dw_path = repo_root / 'dokuwiki_dates.json'
    try:
        dw_dates = json.loads(dw_path.read_text()) if dw_path.is_file() else {}
    except (json.JSONDecodeError, OSError):
        dw_dates = {}

    for f, (sha, date) in seen.items():
        if sha == initial and f.startswith('content/') and f.endswith('.md'):
            key = f[len('content/'):-len('.md')]
            if key in dw_dates:
                _last_modified[f] = dw_dates[key]
                continue
        _last_modified[f] = date


def _extract_anchors(body):
    """Replicate Python-Markdown's toc extension to derive the heading IDs a
    page will have. Uses the same `slugify`/`unique` helpers and our underscore
    separator config."""
    seen = set()
    anchors = set()
    for m in HEADING_RE.finditer(body):
        text = m.group(1).strip()
        # Strip inline markdown so slugify sees plain text (mirrors what toc
        # does after the page's inline parser has run).
        text = re.sub(r'`([^`]+)`', r'\1', text)
        text = re.sub(r'\*\*([^*]+)\*\*', r'\1', text)
        text = re.sub(r'\*([^*]+)\*', r'\1', text)
        text = re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', text)
        text = re.sub(r'!\[[^\]]*\]\([^)]+\)', '', text)
        anchors.add(unique(slugify(text, '_'), seen))
    return anchors


def _read_frontmatter(path):
    """Return (frontmatter dict, body str) for a Markdown file."""
    try:
        with open(path, encoding='utf-8') as fp:
            content = fp.read()
    except OSError:
        return {}, ''
    if not content.startswith('---\n'):
        return {}, content
    end = content.find('\n---\n', 4)
    if end < 0:
        return {}, content
    try:
        meta = yaml.safe_load(content[4:end]) or {}
    except yaml.YAMLError:
        meta = {}
    if not isinstance(meta, dict):
        meta = {}
    return meta, content[end + 5:]


def _page_title(body, fallback):
    m = HEADING_RE.search(body)
    return m.group(1) if m else fallback


def _content_relpath(src_path):
    """Content-root-relative path without extension. E.g.
    'kb/changes_not_syncing.md' → 'kb/changes_not_syncing'. Used as the
    docs-internal link form authors write in source."""
    return src_path[:-3] if src_path.endswith('.md') else src_path


def _page_url(src_path):
    # E.g. 'kb/changes_not_syncing.md' → '/support/kb/changes_not_syncing'
    return URL_PREFIX + _content_relpath(src_path)


# Markdown link with [text](target) form
_LINK_RE = re.compile(r'\[([^\]]*)\]\(([^)]+)\)')

# Schemes / forms that aren't candidates for internal docs resolution
_NON_INTERNAL = re.compile(r'^([a-z][a-z0-9+\-.]*://|mailto:|#|/)')


def _resolve_internal_link(text, target, page_dir, content_root):
    """Translate a docs-internal link like `kb/foo` (content-root-relative,
    no extension) to the relative `.md` form MkDocs validates natively.
    Returns the rewritten `[text](rel.md#anchor)` string, or None if the
    link isn't an internal docs reference or doesn't resolve."""
    if not target or _NON_INTERNAL.match(target):
        return None
    path_part, sep, anchor = target.partition('#')
    if not path_part or '?' in path_part:
        return None
    suffix = ('#' + anchor) if sep else ''
    candidate = content_root / (path_part + '.md')
    if candidate.exists():
        target_md = path_part + '.md'
        rel = posixpath.relpath(target_md, page_dir) if page_dir else target_md
        return f'[{text}]({rel}{suffix})'
    # Unresolved internal-looking link: emit an absolute /support/<path>
    # URL so it doesn't get treated as relative-to-current-page by mkdocs
    # (which produces wrong paths on deep pages, e.g. /support/foo/bar
    # instead of /support/bar). The .htaccess legacy redirects can still
    # catch known-renamed pages; truly missing links produce a clean 404.
    return f'[{text}](' + URL_PREFIX + path_part + suffix + ')'


def on_files(files, config):
    """Build a tag → [(url, title)] index from all pages' frontmatter, a set
    of all valid in-corpus URLs, and per-page anchor ID sets — all used by
    the missing-link detector and the KB topic expander."""
    global _tag_index, _valid_urls, _page_anchors
    _tag_index = {}
    _valid_urls = set()
    _page_anchors = {}
    for f in files:
        if not f.is_documentation_page():
            continue
        url = _page_url(f.src_path)
        url_key = url.rstrip('/')
        _valid_urls.add(url_key)
        meta, body = _read_frontmatter(f.abs_src_path)
        _page_anchors[url_key] = _extract_anchors(body)
        tags = meta.get('tags') or []
        if isinstance(tags, list) and tags:
            title = _page_title(body, f.src_path)
            relpath = _content_relpath(f.src_path)
            for tag in tags:
                _tag_index.setdefault(str(tag), []).append((relpath, title))
    return files


_EXTERNAL_HREF = re.compile(r'^(https?://|#|mailto:|javascript:|data:|tel:|ftp://)')


def _absolutize_urls(html, page, files):
    """Rewrite href/src values so the rendered HTML works regardless of the
    URL the PHP wrapper serves it at. MkDocs emits relative paths like
    `../installation/` that only resolve when the page is served at its
    mkdocs-computed URL (e.g. /support/start/) — our wrapper serves start.md
    at /support/ and accepts URLs without trailing slash, which breaks that
    assumption. So we anchor every relative path at /support/<page.url>/,
    and we rewrite `/`-prefixed paths that match a built docs file (typically
    images) to `/support/<path>` so they don't leak out to the site root.
    Paths that don't match anything in the build pass through unchanged."""
    page_base = URL_PREFIX + page.url
    file_urls = {f.url.rstrip('/') for f in files}

    def repl(m):
        attr, val = m.group(1), m.group(2)
        if not val or _EXTERNAL_HREF.match(val):
            return m.group(0)
        if val.startswith('/'):
            path_only = val.split('#', 1)[0].split('?', 1)[0].lstrip('/').rstrip('/')
            if path_only in file_urls:
                return f'{attr}="{URL_PREFIX.rstrip("/")}{val}"'
            return m.group(0)
        return f'{attr}="{urllib.parse.urljoin(page_base, val)}"'

    return re.sub(r'\b(href|src)="([^"]*)"', repl, html)


def on_page_content(html, page, config, files):
    """Absolutize relative links to /support/..., then tag in-corpus links
    whose target page (or in-page anchor) doesn't exist with a
    `missing-link` class. Styled CSS-side like Dokuwiki's dangling-link
    affordance."""
    html = _absolutize_urls(html, page, files)

    def repl(m):
        url = m.group('url').rstrip('/')
        anchor = m.group('anchor')
        page_ok = url in _valid_urls
        anchor_ok = (not anchor) or (page_ok and anchor in _page_anchors.get(url, set()))
        if page_ok and anchor_ok:
            return m.group(0)
        # Inject `missing-link` into an existing class= or add a new attribute
        pre = m.group('pre') or ' '
        post = m.group('post') or ''
        for chunk_name in ('pre', 'post'):
            chunk = m.group(chunk_name) or ''
            if 'class="' in chunk:
                chunk = re.sub(r'class="', 'class="missing-link ', chunk, count=1)
                if chunk_name == 'pre':
                    pre = chunk
                else:
                    post = chunk
                href = m.group('url')
                if anchor:
                    href += '#' + anchor
                return f'<a{pre}href="{href}"{post}>'
        href = m.group('url')
        if anchor:
            href += '#' + anchor
        return f'<a class="missing-link"{pre}href="{href}"{post}>'
    return INTERNAL_LINK_RE.sub(repl, html)


def _expand_topic(spec):
    """Resolve a topic spec to a Markdown bullet list of matching pages."""
    spec = re.sub(r'&\w+', '', spec)  # strip display options
    required = set()
    excluded = set()
    for tok in spec.split():
        if tok.startswith('+'):
            required.add(tok[1:])
        elif tok.startswith('-'):
            excluded.add(tok[1:])
        elif tok:
            required.add(tok)

    if not required:
        return ''

    candidates = None
    for tag in required:
        pages = set(_tag_index.get(tag, []))
        candidates = pages if candidates is None else candidates & pages
    for tag in excluded:
        for ex in _tag_index.get(tag, []):
            candidates.discard(ex)

    if not candidates:
        return '*(no pages match this topic yet)*'
    # Emit content-root-relative paths; the link-resolution pass turns them
    # into proper relative `.md` paths so MkDocs can validate them.
    lines = [f'- [{title}]({relpath})' for relpath, title in sorted(candidates, key=lambda p: p[1].lower())]
    return '\n'.join(lines)


# Short words that stay lowercase in title-case headings (except as the
# first word). Used when auto-deriving a title from a file slug.
_TITLE_LOWER = frozenset([
    'a', 'an', 'and', 'as', 'at', 'but', 'by', 'for', 'from', 'in', 'nor',
    'of', 'on', 'or', 'so', 'the', 'to', 'up', 'via', 'with', 'yet',
])


def _slug_to_title(slug):
    """Convert a file slug (e.g. 'tips_and_tricks') to a title-case
    string ('Tips and Tricks'). Underscores become spaces; common short
    words stay lowercase except as the first word."""
    words = slug.replace('_', ' ').title().split(' ')
    return ' '.join(
        w.lower() if i > 0 and w.lower() in _TITLE_LOWER else w
        for i, w in enumerate(words)
    )


def on_page_markdown(markdown, page, config, files):
    # Auto-inject an H1 derived from the file slug when the page has none.
    # `<namespace>/start.md` uses the namespace name (e.g. dev/start.md →
    # "Dev") since the literal slug "start" wouldn't be meaningful.
    body = markdown
    fm_end = 0
    if body.startswith('---\n'):
        m = body.find('\n---\n', 4)
        if m > 0:
            fm_end = m + 5

    if not HEADING_RE.search(body[fm_end:]):
        src = page.file.src_path
        slug = src[:-3] if src.endswith('.md') else src
        parts = slug.split('/')
        base = parts[-2] if len(parts) > 1 and parts[-1] == 'start' else parts[-1]
        body = body[:fm_end] + '# ' + _slug_to_title(base) + '\n\n' + body[fm_end:]

    # Last-modified date from git, for the page footer. Cheap once cached.
    docs_dir = config['docs_dir']
    repo_root = Path(docs_dir).resolve().parent
    _build_last_modified(repo_root)
    repo_rel = posixpath.join(Path(docs_dir).name, page.file.src_path)
    if repo_rel in _last_modified:
        page.meta['last_modified'] = _last_modified[repo_rel]

    # Expand topic macros first — they produce internal `[title](kb/foo)`
    # links, which the link-resolution pass below turns into proper relative
    # `.md` paths for MkDocs to validate.
    body = TOPIC_RE.sub(lambda m: _expand_topic(m.group(1)), body)

    # Resolve docs-internal links: `[X](kb/foo)` → `[X](../kb/foo.md)`
    page_dir = posixpath.dirname(page.file.src_path)
    content_root = Path(config['docs_dir'])

    def _resolve(m):
        rewritten = _resolve_internal_link(m.group(1), m.group(2), page_dir, content_root)
        return rewritten if rewritten is not None else m.group(0)

    return _LINK_RE.sub(_resolve, body)
