---
tags:
  - kb
---

# Why can't Zotero find a linked file?

There are a few possible reasons why a linked file might not be found:

1.  The file was moved or deleted outside of Zotero. Find the file and move it back to its original location, or use the Locate button in the File Not Found dialog to point Zotero to the new location.
2.  A [Linked Attachment Base Directory](preferences/advanced#linked_attachment_base_directory) is set incorrectly on one or more of your computers. If the Linked Attachment Base Directory is set correctly on your current computer but Zotero is still looking for a file at an absolute path from another computer, you must correct the Linked Attachment Base Directory setting on the other computer, which will convert attachments under the specified directory to use relative paths, and then sync both computers.
3.  Zotero is looking in the right place, but the file hasn't yet synced from another computer. Zotero syncs only stored files, not linked files, so linked files must be synced using another tool.

If necessary, the third-party [Zutilo plugin](https://github.com/willsALMANJ/Zutilo) can be used to fix attachment paths in batch.


