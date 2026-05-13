<p id="zotero-5-update-warning" style="color: red; font-weight: bold">We’re
in the process of updating the documentation for
<a href="https://www.zotero.org/blog/zotero-5-0">Zotero 5.0</a>. Some documentation
may be outdated in the meantime. Thanks for your understanding.</p>

# Elements of the Zotero ecosystem

## Translators

1.  Import
2.  Export
3.  Web
4.  Search

### Citation

1.  citeproc-js
2.  citeproc-node

#### Desktop

1.  Quick-copy can be site-specific, and can use export translators...
2.  Could be used to provide drag-and-drop item submission, metadata submission, for a curated data thingie for Zotero

##### Lookup Engines

1.  Defined in terms of OpenURL ContextObjects, with some augmentation
2.  Some documentation, not very extensively exploited (Pubget wrote it...)

Integration Plugins

1.  Exist for WinWord, MacWord, [Open|Libre|Neo]Office
2.  No documentation. Each one requires a Firefox plugin. But could be written for more systems
3.  Rtfscan also exists-- a means of scanning a text file and finding references to items, then turning them into citations, using a specific style. This is underdeveloped, and it could be used in conjunction with something like Gnotero to provide facility much like Papers2's Magic Manuscripts (the bulk of which is already provided by Gnoter)

Connector Server

1.  Designed to support Standalone
2.  Plugins for browsers send URLs, page source to Zotero
3.  Designed to be ported to other browsers (and other programs too!)
4.  Could be used for a central Zotero instance, with port forwarding...
5.  Could be used to force-feed items to Zotero
6.  But only one-way (write to DB)
7.  Attempt to write some docs before Madison-- maybe an example client that sends items to Zotero?

Sqlite

1.  Concurrent read-only access is fine: used by Mendeley and Gnotero
2.  Write access is asking for trouble. But connector or server API can be used to push items into Zotero; the latter can even modify existing items

Z(ot)eroConf

1.  Defunct (?) code in the source tree
2.  Allowed browsing of other libraries on a local network

Fulltext parsers

1.  Dan says not to touch this yet
2.  Due to be replaced by Libertexto, we hope
3.  But really... could be extended now.

**Provided by the server**

Metadata Syncing

File syncing

1.  Zotero File Storage
2.  WebDAV

Server API

1.  read item data, styled citations (and sets of citations)
2.  write item data
3.  with the caveat of possible latency, this is a pretty promising direction. Syncing is pretty speedy now, so reading from Sqlite and writing to the server may be possible.

N.B. Preceding three are currently open-source, but no one has really gotten things going outside of CHNM
Devs not providing support for this as a project, but encourage people to experiment. Unfortunately, docs at zitation.org seem to be gone (indeed, why were they ever hosted not on zotero.org? No one said the docs would be discouraged... just not a project that they can do tech support on)

Website

1.  Supposed to be improving greatly very soon
2.  Not currently open-source, don't know if it will be. But the commits are showing up in Trac now

**Other stuff**
A data interchange format approximately equivalent to the one currently fed to citeproc-js is on its way to standardizing (and making interoperable) citations in word processed documents, between Z and Mendeley
