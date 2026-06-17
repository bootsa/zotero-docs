# Syncing

While Zotero stores all data locally on your computer by default, Zotero's sync functionality allows you to access your Zotero library on any computer with internet access. Zotero syncing has two parts: data syncing and file syncing.

## Data Syncing

Data syncing merges library items, notes, links, tags, etc. — everything except attachment files — between your local computer and the Zotero servers, allowing you to work with your data from any computer with Zotero installed and to view your library online on zotero.org. Data syncing is free and unlimited, and it can be used without file syncing.

The first step to syncing your Zotero library is to [create a Zotero account](/user/register/) (which is also used for the Zotero Forums). Then, open the Sync pane of the [Zotero preferences](preferences) and enter your login information in the Data Syncing section.

![](https://www.zotero.org/static/images/support/quick_start/small/sync.png){ .align-left width=160 }

By default, Zotero will sync your local data with the Zotero servers whenever changes are made. To disable automatic syncing, uncheck the "Sync automatically" checkbox in this section. You can sync manually at any time by clicking the "Sync with zotero.org" button on the right-hand side of the Zotero toolbar.

When Zotero syncs, it automatically applies changes in both directions — any changes you make in one place will be applied to all other synced computers. If an item has changed in multiple places in conflicting ways between syncs, you'll receive a conflict resolution dialog asking which version you'd like to keep. If you find yourself using a new computer, you can simply set up syncing and Zotero will automatically download all data from your online library.

## File Syncing

Data syncing syncs library items, but doesn't sync attached files (PDFs, audio and video files, images, etc.). To sync these files, you can [set up file syncing](preferences/sync#file_syncing) to accompany data syncing, using either Zotero Storage or WebDAV.

### Zotero Storage

Zotero Storage is the recommended file sync option. It has several advantages over WebDAV syncing, including syncing of files in [group libraries](groups), web-based access to PDFs and other attachments, easier setup, guaranteed compatibility, and improved upload performance for certain files. Each Zotero user is given 300 MB of free Zotero Storage for attached files, with [larger storage plans](storage#storage_pricing) available for purchase.

See the [Zotero Storage](storage) documentation for more information.

### WebDAV

WebDAV is a standard protocol for transferring files over the web, and it can be used to sync files in your personal library. (Group libraries cannot use WebDAV.) Your employer or research institution may be able to provide WebDAV storage. Otherwise, there are many third-party options, both free and paid (see [WebDAV providers known to work with Zotero](kb/webdav_services)).

Once you have your WebDAV account info, enter the URL provided by the service, your username, and your password in the [Sync preferences tab](preferences/sync#file_syncing). Be sure to select 'http' or 'https' as appropriate — if you're not sure, try 'https' first. After entering the information, click "Verify Server". If Zotero successfully verifies the WebDAV account, you're all set to use file syncing via WebDAV.

Zotero file sync should work with any correctly functioning WebDAV server. Zotero developers cannot provide support for third-party WebDAV servers.

## Syncing In Practice

If Zotero is set to sync automatically, changes will be synced within a few seconds of being made. Otherwise, you can start a manual sync by clicking the sync button on the right-hand side of the Zotero toolbar.

If you enter the same login information into the Sync preferences on multiple computers, Zotero will sync everything transparently. Your attention should only be needed if the same item or file is edited in conflicting ways in two different places before Zotero has a chance to sync them. If that happens, you'll be presented with a conflict resolution window, where you can decide which changes to accept.

If you sync from only one computer, you can still view your online library at zotero.org from any computer. Should something happen to your computer or should you want to start using Zotero on another computer, simply set up your account info on the new computer. Zotero will pull down your entire library from the server.

## Alternative Syncing Solutions

If, for whatever reason, you are unable to use Zotero's syncing features, there are some alternative ways to sync your data, though there are significant risk and limitations depending on the approach that you choose.

**Storing the Zotero data directory directly in a cloud storage folder is [extremely likely to corrupt your Zotero database](kb/data_directory_in_cloud_storage_folder) and should not be done.**

If you want to avoid syncing any data to Zotero servers:

-   You can close Zotero, manually copy your entire [Zotero data directory](zotero_data) to a synced folder on one computer, and then restore it — again with Zotero closed — on another computer, as if you were performing a [backup and restore](zotero_data#backing_up_your_zotero_library) of your data.

If you want to use Zotero data syncing but use an external service to sync just your Zotero attachment files:

-   You can use [linked files](attaching_files#stored_files_and_linked_files), rather than stored copies of files, with only your attachment files in the externally synced folder.
