# Contributing

Thanks for helping improve the Zotero documentation.

The documentation is maintained primarily by Zotero developers and long-time
contributors who have been helping Zotero users in the Zotero Forums for years.
If you're not a regular forums contributor, it's usually best to open an issue
to discuss a significant change before investing time in it.

- Typo fixes, spelling/grammar, broken links — open a PR directly.
- Clarifications or expansions of existing content — open a PR.
- Larger restructurings, renaming or removing pages — please open an issue
  first

By contributing, you agree to license your changes under the same terms as
the rest of the content (CC BY-SA 4.0 for Markdown, AGPLv3 for code).

## Style

- U.S. English spelling
- Title case for most headings (e.g. "Adding Items to Zotero"). Knowledge base
  entries are usually phrased as a question in sentence case ("Can I store my
  Zotero data directory in a cloud storage folder?").
- Keep code samples in fenced blocks with a language tag where possible.

## Screenshots and images

For consistency and the highest image quality, new screenshots should be
generated on macOS on a Retina display if possible.

- **New images** go under `content/images/`, organized by topic (e.g.
  `content/images/searching/advanced_search.png`). Reference them with a
  leading slash so the path is resolved from the docs root: `![Advanced
  Search](/images/searching/advanced_search.png)`.
- **Legacy DokuWiki images** carried over from the original wiki live under
  `content/_media/`, preserving the original namespace layout (e.g.
  `content/_media/quick_start/zotero_pane.png`). These keep the existing
  `_media/...` URLs working for any external links pointing at them.
  Reference with `/_media/<namespace>/<filename>`. Don't add new images here.

## Local preview

```
pip install -r requirements.txt
mkdocs serve
```

Then open <http://127.0.0.1:8000>. The page you're editing reloads on save.

## Adding a KB page

1. Create `content/kb/<slug>.md`. The slug becomes the URL.
2. Start the file with frontmatter that lists relevant tags — these drive the
   KB index pages:

   ```yaml
   ---
   tags:
     - basics
     - syncing
   ---
   ```

3. Below the frontmatter, write the page content starting with a single H1.

The page will show up automatically under any KB index page whose
`{{topic>kb +tag}}` macro matches the tags you set.

## Deploy timing

Merging a PR doesn't update the live site instantly — there's about a
minute delay while CI rebuilds and the new content is pushed out.
