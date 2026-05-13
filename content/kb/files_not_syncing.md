---
tags:
  - kb
  - sync
---

## Why am I getting “The attached file could not be found” when I try to open a file in Zotero?

### Short Answer

Sync the device **where you added the file**. Unless you deleted the file outside of Zotero, you will still be able to open it on that device. After syncing, check for a sync error in the Zotero toolbar.

You may have just reached your [Zotero Storage quota](/settings/storage), preventing additional files from being synced. You'll need to add a storage subscription or delete some files. If you added a subscription recently, syncing the device where you added the file will allow the file to be uploaded and make it available to other devices.

If the file can't be opened in the online library (or isn't on your WebDAV server, if you're using WebDAV), **any device where you can't open the file is irrelevant**.

### Long Answer

If you're unable to open a file in Zotero, it was almost certainly never uploaded to Zotero servers. [File syncing](sync#file_syncing) may not be set up or working properly on one of your devices, or you may have reached your online [file storage quota](/settings/storage). You may see one of the following errors:

-   Desktop: *"The attached file could not be found at the following path. It may have been moved or deleted outside of Zotero, or, if the file was added on another computer, it may not yet have been synced to or from zotero.org."*
-   iOS/Android: *"The attached file could not be found. Please check that the file has synced on the device where it was added."*

Follow these steps to diagnose and fix the problem:

1.  Make sure the attachment file can be opened from Zotero on at least one of your devices. We'll refer to the device that has the file as Device A and the device that doesn't as Device B.
2.  If Device A is a computer and this is a personal library, make sure the attachment is stored within your [Zotero data directory](zotero_data), not linked to a location elsewhere on your disk. Zotero syncs [stored files](attaching_files#stored_files_and_linked_files); linked files need to be synced outside of Zotero. Linked files are indicated by a chain in the attachment icon. You can use Tools → Manage Attachments → Convert Linked Files to Stored Files to make the files syncable. (All files in a group are stored files.)
3.  Make sure the device is syncing properly:
    -   If Device A is a computer, check that file syncing is enabled in the Sync pane of the settings, and check whether you're getting a sync error, indicated by an error icon to the left of the green sync button in the Zotero toolbar. If you're getting a sync error, click the sync error icon and follow the instructions. If you need help, please post to the [Zotero Forums](/forum) with a [Report ID](reporting_problems) and the message you're seeing in the sync error popup.
    -   If Device A is an iOS/Android device, pull down on the items list and check whether you're getting a sync error at the bottom of the screen. Tap on the sync error for more information. If you need help, please post to the [Zotero Forums](/forum) with a [Debug ID](debug_output#zotero_for_ios) for pulling down on the items list.
4.  If you're not getting a sync error on Device A, verify that the file has been uploaded to the server. The steps vary depending on whether you're using [Zotero Storage](/storage) or WebDAV:
    -   **Zotero Storage:** Check to see if the attachment file can be opened from your library on zotero.org. Attachment files will be directly viewable if they have been uploaded — the presence of an attachment item isn't an indication that the file itself has been uploaded. If you're using a group, the group must have File Editing enabled in its settings on zotero.org, which isn't possible for Public, Open Membership groups.
    -   **WebDAV:** If Device A is a computer, right-click on the item and choose Show File to reveal the file in the OS file manager (Finder on macOS, Explorer on Windows, etc.). Look at the name of the file's parent directory, which should be a string of characters such as 'F81VWFP2'. Load your WebDAV URL in your browser or another WebDAV client and look for corresponding .prop and .zip files (e.g., F81VWFP2.prop and F81VWFP2.zip) on the server.
5.  If the file hasn't been uploaded:
    -   If Device A is a computer, go to the Sync → Reset pane of the Zotero settings on Computer A and select Reset File Sync History for the library in question. (**Do not** use any other options in the Reset pane.) Resetting file sync history shouldn't be necessary under normal usage, but it will cause Zotero to check every attachment to make sure that it has been uploaded to the server. If the file becomes available online, continue to the next step. If not, generate a [Debug ID](debug_output#debug_output_logging) for the first sync after performing Reset File Sync History, followed by a successful opening of the file locally, and post it to the [Zotero Forums](/forum). For Zotero Storage, include the URL from the web library where you're not able to access the file.
    -   If Device A is an iOS/Android device, generate a [Debug ID](debug_output#debug_output_logging) for adding a file and the sync that immediately follows. If the file isn't uploaded, post the Debug ID to the [Zotero Forums](/forum). For Zotero Storage, include the URL from the web library where you're not able to access the file.
6.  If the file has been uploaded, check to see if it is available on Device B. If not, there may be a problem on that device. Check the file sync settings on that device to confirm that they match the settings on Device A. For example, if one device is set to use Zotero Storage and another is set to use WebDAV, or if they're configured with different Zotero accounts (for personal library files) or different WebDAV URLs, files won't transfer between the two.
7.  Sync Device B and check if there's a sync error. If so, you'll need to resolve that before file syncing will work.
8.  If you've performed all these steps, you've confirmed that the file is available on the server, and you still can't access the file on Device B:
    -   If Device B is a computer, go to the Sync → Reset pane of the Zotero settings, choose Reset File Sync History, generate a [Debug ID](debug_output#debug_output_logging) for the next sync attempt and an attempt to open the file, and post the Debug ID to the [Zotero Forums](/forum). **Do not** use any other options in the Reset pane.
    -   If Device B is an iOS/Android device, generate a [Debug ID](debug_output#zotero_for_ios) for an attempt to open the file and post it to the [Zotero Forums](/forum).


