<p id="zotero-5-update-warning" style="color: red; font-weight: bold">We’re
in the process of updating the documentation for
<a href="https://www.zotero.org/blog/zotero-5-0">Zotero 5.0</a>. Some documentation
may be outdated in the meantime. Thanks for your understanding.</p>

# JSON Objects in the API

The Zotero [write API](dev/web_api/write_api) and the JSON payloads of the [read API](dev/web_api/read_api) are built around JSON representations of Zotero's collections, items, notes, and attachments.

FIXME This is a work in progress will be augmented with examples and explanations

## Items

tagMode (for attachments and notes too)
fieldMode (for creators)
link to valid creatortype and field lists

## Collections

## Attachments

linkMode

    this.LINK_MODE_IMPORTED_FILE = 0;
    this.LINK_MODE_IMPORTED_URL = 1;
    this.LINK_MODE_LINKED_FILE = 2;
    this.LINK_MODE_LINKED_URL = 3;

## Notes
