---
tags:
  - kb
---

# Why can't Zotero find a stored file?

There are a few reasons why a [stored file](attaching_files#stored_files_and_linked_files) might not be found:

1.  You created the file on another computer and it hasn't yet synced to this computer. See [Files Not Syncing](kb/files_not_syncing).
2.  The individual file was moved or deleted outside of Zotero. You can use the Locate button in the File Not Found dialog to select the file. When using Locate, if you select a file that was renamed within the original storage directory, Zotero will update the database to point to the new file; if you select a file elsewhere, it will copy the file to the correct storage directory.
3.  You moved or deleted the 'storage' directory within the [Zotero data directory](zotero_data).
4.  You somehow ended up using a different Zotero data directory from the one you were using previously on this computer, and you're either viewing a different database or you synced down data — but not files, which might not be available online — from the online library. In this case, it's better to [locate the correct Zotero data directory](zotero_data#locating_missing_zotero_data) on this computer.

Note that Zotero never deletes files on disk while their corresponding attachment items still exist in the database, so if your files are missing, either they haven't synced or something happened outside of Zotero.


