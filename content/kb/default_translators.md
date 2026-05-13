---
tags:
  - kb
  - entry
---

#### Default translators

Zotero has four translators that attempt to find useful bibliographic data on pages that are not recognized by any of the more specific site translators. You can tell what translator detected bibliographic data on a page by placing the cursor over the document icon in the address bar; the name of the translator will show up as a tooltip. A similar name is usually saved to the "Library Catalog" field of created items.

-   DOI. Zotero tries to detect one or more pieces of text that could be DOIs. The DOI translator provides fairly passable support for many academic databases and sites that don't have a dedicated Zotero translator. Metadata for DOIs is retrieved through [CrossRef](http://www.crossref.org); the data never includes full text or abstracts. Sometimes DOI-based saves will fail because of incomplete data in the CrossRef database.
-   [COinS](dev/exposing_metadata/coins) can include information on a limited number of item types. It never supports full text.
-   Embedded Metadata and unAPI *can* support all of Zotero's item types and fields, as well as full text attachments. Embedded Metadata, however, will often detect minimal metadata on webpages, and the items it saves from such pages are frequently not very useful.

For details on how Zotero uses default translators, see the [developer's documentation](dev/exposing_metadata#using_an_open_standard_for_exposing_metadata).


