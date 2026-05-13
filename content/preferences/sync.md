---
tags:
  - pref
---

# Sync

For information on how to set up and use Zotero's syncing features, see [Syncing](sync). This page describes the settings in the Sync pane of the Zotero preferences.

The Sync pane has two tabs: "Settings" and "Reset"

## Settings

![](/_media/preferences_sync_empty.png){ width=600 }

To set up Zotero syncing, you first need to set up data syncing (for item metadata, notes, and the full-text content) using your [zotero.org](/) username and password. After you link your Zotero account with the Zotero client program, you will see settings for managing data syncing and file syncing.

![](/_media/preferences_sync_settings_user.png){ width=600 }

#### Data Syncing

-   **Unlink Account…:** Disconnect the client from your Zotero account. This will prevent syncing. You will be given an option to remove the local Zotero data or keep it. If you later link this Zotero client with another username, the local library will be replaced with the new username's library from [zotero.org](/).
-   **Choose Libraries…:** This option lets you choose which of the [Group libraries](/groups) you are a member of to sync automatically with the Zotero servers. If you uncheck a library that is present in your local Zotero client, you can still manually sync the library by right-clicking on it in the left Zotero pane and choosing "Sync Library". It is not currently possible to remove an unsynced library from the local Zotero client.
-   **Sync automatically:** When check, Zotero will start a sync every time you make a change to your library. You can manually start a sync by clicking the sync button (circular green arrow) in the upper-right corner of the Zotero window.
-   **Sync full-text content:** When checked, Zotero will sync the extracted text contents of your PDFs and other files, allowing you to perform searches across devices regardless of whether files have been downloaded to a particular device. This also allows for full-text searches in the [web library](/mylibrary).

See [Data Syncing](sync#data_syncing) for more information.

#### File Syncing

-   **Sync attachment files in My Library using:** Enable/disable file syncing for your personal Zotero library.
    -   **Zotero:**
        -   Sync file attachments using [Zotero File Storage](sync#zotero_file_storage).
    -   **WebDAV:**
        -   Sync file attachments using [WebDAV storage](sync#webdav).
        -   Enter the URL for your WebDAV server (note that `/zotero` is added to the end of the URL automatically), your username, and your password.
        -   Click "Verify Server" to check whether Zotero can connect with the server for file syncing.

![preferences_sync_webdav.png](/_media/preferences_sync_webdav.png){ .align-center width=400 }

-   **Sync attachment files in group libraries using Zotero storage:**
    -   Enable/disable file syncing for your group libraries.
    -   Only [Zotero File Storage](sync#zotero_file_storage) is supported for group libraries.
-   **Download files:**
    -   **At sync time:** Download all attachment files not already in your local Zotero file storage on your computer each time Zotero syncs.
    -   **As needed:** Only download attachment files when the user attempts to open the file. Useful for reducing the amount of hard disk space Zotero uses for attachments.

See [File Syncing](sync#file_syncing) for more information.

## Reset

![](/_media/preferences/preferences_sync_reset.png){ width=600 }

The options in this tab allow you to reset Zotero's file sync history with [zotero.org](/). These options are not intended for regular troubleshooting and should not be used unless directed to on the [Zotero forums](/forum). For more information, see [Sync Reset](kb/sync_reset_options).


