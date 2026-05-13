# Why do attachments have names like “PDF” or “Accepted Version” instead of their filenames in the items list?

Attachments have two separate names: the attachment title shown in the items list and the filename of the file on disk.

Zotero automatically renames files on disk based on parent item metadata such as the title and authors. Since the parent item row in the items list already displays that metadata, Zotero doesn't show the filename directly in the items list. Instead, it uses simpler attachment titles such as "PDF" or "Ebook" for the first file of a given type or includes additional information about the source of the file (e.g., "ScienceDirect Full Text PDF" for a file saved from ScienceDirect, or "Accepted Version" or "Submitted Version" for [open-access files](/blog/improved-pdf-retrieval-with-unpaywall-integration/)). These separate titles avoid cluttering the items list with redundant metadata and prevent parent items from being unnecessarily expanded when searching for titles or creators.

Subsequent files added to an item from the filesystem will still get titles named after the filename (without the file extension), since those are likely to be supplementary files and the filename may be informative.

You can view and change the title and filename by clicking on the attachment and looking in the item pane.

While we recommend the default behavior in order to avoid redundant information in the items list, if you really prefer to view filenames instead of titles, you can enable “Show attachment filenames in the items list” option in the General pane of the settings.

### Changes in Zotero 7

Zotero has always automatically renamed files on disk, and it has always used separate, simpler titles such as "ScienceDirect Full Text PDF" when saving attachments from the web, for the reasons explained above.

Zotero 7 changed attachment-title handling in a couple particular cases:

1.  Prior to Zotero 7, if you **manually** ran Rename File from Parent Metadata, the attachment title was changed to match the new filename. This was a bug that led many people to believe that files weren't being automatically renamed and that it was necessary to run Rename File from Parent Metadata on every new attachment. In Zotero 7, the title is no longer changed, and titles remain as "PDF", "ScienceDirect Full Text PDF", or whatever they were set to originally. Files are still renamed as always, as you can see if you click on the attachment item and look in the item pane.
2.  When dragging a file from the filesystem or creating a parent item, Zotero now sets the title of the first attachment of a given type to "PDF", "EPUB", etc., instead of setting the title based on the filename, in order to match titles of attachments saved from the web.

People who were unnecessarily running Rename File from Parent Metadata on every attachment, predominantly adding local files rather than saving from the web, or using the ZotFile plugin (which also set the title to the filename) might be used to seeing filenames in the items list, but we'd encourage people to give the new behavior a try.

#### Updating Titles Changed Before Zotero 7

Zotero 8 provides an option to convert attachments previously changed to match the filename to use simpler "PDF" titles instead. Simply select the attachments or their parent items and go to Tools → Management Attachments → Normalize Attachment Titles.
