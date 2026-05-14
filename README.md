# Zotero Documentation

Source for the Zotero documentation at <https://www.zotero.org/support>.

The site is built with [MkDocs](https://www.mkdocs.org/) using a custom theme.
Local previews render with a minimal theme; the live site is served inside
the standard zotero.org page chrome.

Merged changes will be automatically deployed to the live site in about a
minute.

## Repository layout

- `content/` — Markdown sources, one file per page. URLs follow the file
  layout (e.g. `content/kb/files_not_syncing.md` → `/support/kb/files_not_syncing`).
- `theme/` — Custom MkDocs theme. Produces fragments rather than full HTML
  pages.
- `hooks.py` — MkDocs build hooks: builds a tag index from page frontmatter,
  expands `{{topic>...}}`-style index macros on KB pages, and flags links to
  missing pages or anchors at build time.
- `mkdocs.yml` — Build config (curated sidebar nav, Markdown extensions,
  syntax-highlighting options).
- `requirements.txt` — Pinned Python dependencies for reproducible builds.

## Local development

```
pip install -r requirements.txt
mkdocs serve
```

Open <http://127.0.0.1:8000>. Edits to Markdown files reload the browser
automatically.

`mkdocs build` produces the static fragments under `build/`.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md).

## License

Code in this repository (theme, build hooks, and CI configuration) is licensed
under the **GNU Affero General Public License, version 3** — see
[LICENSE](LICENSE).

Documentation content under `content/` is licensed under
**Creative Commons Attribution-ShareAlike 4.0 International (CC BY-SA 4.0)**
— see [LICENSE-CONTENT](LICENSE-CONTENT).
