---
tags:
  - kb
---

# How can I move my Zotero library to a different computer?

## Option A: Use Zotero Sync

The easiest way to transfer your library between between computers is by using [Zotero Sync](sync#syncing). Set up syncing from the Sync pane of the Zotero preferences, making sure you use the same username on all computers.

You'll need enough online storage space to fit all files in your library. Zotero will warn you if you hit your quota, in which case you may need to delete some files, add a [storage plan](/storage), or transfer your library using Option B below.

## Option B: Copy the data folder

If you're comfortable moving files between devices, you can transfer your library by copying the [Zotero data folder](zotero_data) from your first computer to your new computer — e.g., by using an external hard drive or a local network connection. If switching to a new computer, your OS may provide a way to automatically transfer all data (e.g., Migration Assistant on a Mac).

To move your data manually, first locate your data by opening the [Zotero preferences](preferences), going to Advanced → Files and Folders, and clicking “Show Data Directory”.
See [here](zotero_data#default_locations) for the default locations of the data folder.

Be sure to close Zotero on both machines before copying the Zotero files. If you've already opened Zotero on the new computer, there will already be a Zotero data folder with an empty database, and you should delete the whole data folder before copying the new folder to the same location.

## Don't Use Export/Import

Exporting and importing your library (for instance via Zotero RDF) is not a recommended option. None of the available export formats allow for a complete transfer of your library data, reimporting will break connections with any existing word processor documents, and if you use syncing later you will end up with duplicates of any imported items.


