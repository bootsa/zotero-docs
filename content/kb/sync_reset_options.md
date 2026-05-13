---
tags:
  - kb
  - sync
---

# Zotero Sync Reset Options

This page documents the special sync operations available from the Sync → Reset pane of the Zotero preferences.

**Please note:** These operations are for use only in rare, specific situations and are not necessary during normal usage or for general troubleshooting. In many cases, resetting will cause additional problems. If you're not sure what these options do, please ask for help on the [Zotero Forums](/forum) before using them.

Before using any options on this page, make sure to first [back up your Zotero library](zotero_data#backing_up_your_zotero_library).

## Replace Online Library

"Replace Online Library" allows you to overwrite an online Zotero library with data from your local Zotero database. This can be useful if you've made unwanted changes to a Zotero library locally and those changes have already synced to the online library, or if unwanted changes were made on another computer and uploaded to the online library but those changes haven't yet been synced to your current computer.

Note that "Replace Online Library" is only necessary when you want to undo changes already applied to the online library. It isn't necessary if you've simply made changes locally that you want to sync. For example, if the online library is empty and you add many items locally, those items will automatically be uploaded — the local items won't be deleted simply because they don't exist in the online library. Similarly, if you delete many items locally, those deletions will automatically be synced to the online library without your needing to take any special action.

### If both the online library and your local database contain unwanted changes

1.  Temporarily disable auto-sync in the Sync pane of the Zotero preferences.
2.  Restore your local data from either an external backup you made or one of the automatic backups in the [Zotero data directory](zotero_data).
3.  Use "Replace Online Library" to upload the local version of your library.

See [Restoring Your Zotero Library from a Backup](zotero_data#restoring_your_zotero_library_from_a_backup) for specific instructions for your situation.

### If the online library contains unwanted changes that haven't yet synced to your current computer

1.  If Zotero isn't yet open and you want to prevent it from syncing, temporarily disable your computer's network connection (e.g., by disabling wifi), open Zotero, and then ensure that auto-sync is disabled in the Sync pane of the Zotero preferences.
2.  Make a backup of your [Zotero data directory](zotero_data).
3.  Ensure that other computers are fully in sync with the online library. (The specific data being synced doesn't matter, as you'll be overwriting online library with the local version, but for the restore to apply to other computers without potential conflicts they need to already be in sync. It may be a good idea to make a backup of the Zotero data directory on any other computers before performing the restore.)
4.  Use "Replace Online Library" to upload the local version of your library. Be sure to choose the correct library from the drop-down. If you need to overwrite more than one online library, perform the restore separately for each library.

If the restore was successful, you can re-enable auto-sync. Keep a backup of your Zotero data directory until all applicable computers have had a chance to sync the restored version.

## Reset File Syncing History

If changes made to attachment files are not being synced (e.g., edits, annotations, deleting an attachment, adding a new attachment), this option will reset the file syncing history between your local Zotero database and your storage service (either the Zotero servers or your WebDAV provider). This will cause Zotero to compare all attachment files on your local computer with the ones on your storage service, making the most recent changes to files.

Resetting file sync history should not be necessary, so if you find that files aren't syncing correctly, see [Files Not Syncing](kb/files_not_syncing) for help troubleshooting and reporting the issue.


