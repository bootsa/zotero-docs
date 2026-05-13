---
tags:
  - pref
---

# Advanced

The Advanced pane has four tabs: "General", "Files and Folders", "Shortcuts", and "Feeds".

## General

![preferences_advanced_general.png](/_media/preferences_advanced_general.png){ width=600 }

#### Miscellaneous

-   **Automatically check for updated translators:** Allow Zotero to automatically update its translators (for detecting and saving bibliographic data from different websites) and citation styles. You manually check for updates immediately by clicking the "Update now" button.
-   **Report broken site translators:** Allow Zotero to notify its developers when a translator fails to save an item. This information is submitted anonymously.

#### Language

Set the language for the Zotero interface.

#### OpenURL

Here you can specify a different OpenURL resolver for use with Zotero's [Library Lookup](locate#library_lookup) feature.

If you are on an institution network, you can click the "Search for resolvers" button. If Zotero finds an OpenURL resolver belonging to your institution, you can select it using the "Custom…" drop-down menu.

You can also enter an OpenURL URL by hand in the Resolver field. Most resolvers use OpenURL version 1.0, but 0.1 is still in use. Ask your librarian for more information, or check our own [list of OpenURL resolvers](locate/openurl_resolvers).

#### Advanced Configuration

Click the "Config Editor" button to configure Zotero's [hidden preferences](preferences/hidden_preferences).

## Files and Folders

![preferences_advanced_files.png](/_media/preferences_advanced_files.png){ width=600 }

#### Linked Attachment Base Directory

*If you store attached files in Zotero — the default — this setting does not affect you. It only applies to *linked* files.*

This setting allows you to access [linked files](attaching_files#stored_files_and_linked_files) on multiple computers even when they're stored in different locations on each computer. You should set the base directory to the folder on each computer under which you store linked files. For example, if the folder with your linked files is at `/Users/Sarah/Dropbox/PDFs` on your laptop and at `C:\Users\Sarah\Dropbox\PDFs` on your work computer, set those paths as the base directory on each respective machine. If you add a linked file within the base directory, Zotero stores a relative path to that base directory rather than an absolute path.

Note that this setting does not control where files are stored — only whether linked files within the specified folder are referenced by absolute or relative paths. If you're using a plugin to help with a linked-file workflow, you should configure it to store linked files within the base directory you've configured.

Note that linked files are an advanced configuration, and we're not able to help troubleshoot problems with specific setups. We recommend that most people use stored files instead.

##### Automatic Linked-File Relinking

If you previously added linked files on another computer without having set a base directory and your files are now in a different location on your current computer, you can simply set your base directory to the desired containing folder on your current computer (e.g., `C:\Users\Sarah\Dropbox\PDFs`). When you next open a missing file with an absolute path (e.g., `/Users/Sarah/Dropbox/PDFs/Smith - 2019 - Foo.pdf`), Zotero will automatically locate the file within your specified base directory and offer to relink all files that have the same base path (`/Users/Sarah/Dropbox/PDFs`).

#### Data Directory Location

By default, Zotero stores your [data directory](zotero_data) (which contains your library database, attachment files, and several other files) in your user home folder on your computer. This is the best location for most users, but it is possible to change the location. After changing the data directory location, Zotero will store newly created data in the new location.

Note that Zotero will not, however, copy over existing data to the new location. If you want to keep your data, you need to move the files manually. Click the "Show Data Directory" button to open the Zotero folder in your computer's file browser. You will need to move everything in the folder (including 'zotero.sqlite', 'storage', 'styles', and all other files) to the new location.

##### Unsafe Data Directory Locations

There are several data directory locations that are **likely to lead to database corruption or even data loss**.

-   **Cloud storage folders**: Storing your Zotero data directory in a cloud storage folder (e.g., Dropbox, Google Drive, or other similar folder synchronization services) is [extremely unsafe](kb/data_directory_in_cloud_storage_folder) and will almost certainly lead to database corruption and potentially data loss.
-   **Network drives**: If you store your Zotero data directory on a network drive and then access it from multiple computers at the same time, you are very likely to encounter database corruption. For example, if you leave Zotero open on your laptop, then open the same Zotero database on the network drive from your work computer, you will likely experience corruption. You should never use a network drive to permit multiple users to access the same Zotero database on different machines (use [groups](/groups) or [Zotero syncing](sync) for that).
-   **Virtual machines**: Similar to issues with network drives, it can be unsafe to use the same Zotero database file from both a virtual machine and the computer's host operating system (or another virtual machine). If the same Zotero database is accessed from two locations at the same time (e.g., if Zotero is open on both the virtual machine and the host operating system), corruption is likely. If you want to use Zotero in a virtual machine, it is better to set up a separate Zotero data directory in the virtual machine and to keep it up to date using [Zotero syncing](sync).
-   **External disks**: While keeping your data directory on an external disk is usually safe, your database could become corrupted if, say, the disk becomes unmounted while Zotero is open.

#### Database Maintenance

-   **Check Database Integrity:** This function checks your Zotero database for invalid data and database corruption. Database corruption is rare, and in most cases is caused by storing your data directory in an [unsafe location](#unsafe_data_directory_locations). Checking database integrity can take a long time if your database is very large. If your database is corrupted, you can try to use the [Database Repair Tool](utils/dbfix) to repair the corruption.
-   **Reset Translators…:** Reset web and import/export translators to the versions bundled with the application or provided as updates from Zotero servers.
-   **Reset Styles…:** Reset citation styles to the versions bundled with the application or provided as updates from Zotero servers.

## Shortcuts

![preferences_advanced_shortcuts.png](/_media/preferences_advanced_shortcuts.png){ width=600 }

This tab allows you to change Zotero's default keyboard shortcuts.

-   **Create a New Item:** Create a new blank item in the current collection.
-   **Create a New Note:** Create a new standalone note in the current collection.
-   **Focus Libraries Pane:** Sets the focus in Zotero to left (libraries, collections, and feeds) pane.
-   **Quick Search:** Sets the focus to the [Quick search](preferences/searching) box. `Ctrl/Cmd`-`F` will also focus the Quick search box.
-   **Copy Selected Item Citations to Clipboard:** Copies an inline citation for the selected item(s) to the clipboard. (Depending on the style, this could be long and detailed or, if the style demands footnotes, simply a number.)
-   **Copy Selected Items to Clipboard:** Copies the full bibliographic reference for the selected item(s) to the clipboard.
-   **Toggle Tag Selector:** Shows/hides the tag selector.
-   **Mark All Feed Items As Read/Unread:** Marks all items in the selected [feed](preferences/feeds) as read/unread.

Any changes made to this page will only take effect after you restart Zotero. a new browser window is opened.

#### Windows Defaults

| Function                                  | Command      |
|-------------------------------------------|--------------|
| Create a New Item                         | Ctrl-Shift-N |
| Create a New Note                         | Ctrl-Shift-O |
| Focus Libraries Pane                      | Ctrl-Shift-L |
| Quick Search                              | Ctrl-Shift-K |
| Copy Selected Item Citations to Clipboard | Ctrl-Shift-A |
| Copy Selected Items to Clipboard          | Ctrl-Shift-C |
| Toggle Tag Selector                       | Ctrl-Shift-T |
| Mark All Feed Items As Read/Unread        | Ctrl-Shift-R |

#### Mac OS X Defaults

| Function                                  | Command     |
|-------------------------------------------|-------------|
| Create a New Item                         | Cmd-Shift-N |
| Create a New Note                         | Cmd-Shift-O |
| Focus Libraries Pane                      | Cmd-Shift-L |
| Quick Search                              | Cmd-Shift-K |
| Copy Selected Item Citations to Clipboard | Cmd-Shift-A |
| Copy Selected Items to Clipboard          | Cmd-Shift-C |
| Toggle Tag Selector                       | Cmd-Shift-T |
| Mark All Feed Items As Read/Unread        | Cmd-Shift-R |

## Feeds

![preferences_advanced_feeds.png](/_media/preferences_advanced_feeds.png){ width=600 }

This tab contains preferences for Zotero's [Feeds](feeds) feature.

-   **Sorting:** Change between sorting newest or oldest items first.
-   **Feed Defaults:** Change how frequently feeds are checked for new items and how long read and unread items are kept in your database before being removed.


