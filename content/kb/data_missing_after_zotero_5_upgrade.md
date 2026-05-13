---
tags:
  - kb
  - basics
---

### I upgraded to Zotero 5.0 and now my data is missing! How do I get it back?

Zotero 4.0 and earlier stored data by default in a 'zotero' directory within either the [Zotero profile directory](kb/profile_directory) or the [Firefox profile directory](https://support.mozilla.com/kb/Profiles).

When you first start Zotero 5.0, it attempts to migrate your data directory to a new default location, a "Zotero" directory in your home directory. (See [Zotero Data](zotero_data) for the default location on your platform.) If you previously used both Zotero for Firefox and Zotero Standalone and chose not to share a data directory, you may have a Zotero database in both profile directories, and Zotero will automatically use whichever database was modified more recently.

In some cases, Zotero may not copy the correct directory and instead either create a new data directory or migrate the data directory from the wrong profile, potentially leaving you with an empty or outdated database.

If Zotero 5.0 then syncs with your online library, it will update that database, but if your online library is out of date — for example, if you haven't synced in several months — you could still end up with missing local data.

#### Restoring Your Data

If you used Zotero for Firefox at any point in the past, your data may be stored in the Firefox profile directory, and you may need to temporarily disable security software so that Zotero can access that directory on startup and offer to restore your data.

Otherwise, to restore your data manually, first identify your current Zotero data directory from the Advanced → Files and Folders pane of the Zotero preferences. (Again, this will generally be "Zotero" within your home directory, but it could also be 'zotero' within your Zotero profile directory.)

Then find your [Zotero profile directory](kb/profile_directory) and/or [Firefox profile directory](https://support.mozilla.com/kb/Profiles) and look for a 'zotero' subdirectory. If you find one, check the timestamp of the zotero.sqlite file and confirm that there's a 'storage' directory with other directories below it, corresponding to the range of dates that you added items to Zotero. (These are your attachment files.)

If you ever used Firefox's "Refresh Firefox" feature, you can also look for your Zotero data in a 'zotero' folder folder located in the "Old Firefox Data" folder on your desktop.

To restore the data directory you located, follow these steps:

1.  Close Zotero
2.  Rename your current data directory in your home directory from "Zotero" to "Zotero-Old"
3.  Move the 'zotero' directory from the profile directory (or from "Old Firefox Data") to your home directory and rename it to "Zotero" (with a capital "Z").
4.  When you then start up Zotero 5.0 again, you should see your previous data.

If there isn't a 'zotero' directory within either profile directory or in the "Old Firefox Data" folder on your desktop, it's possible you were previously using a custom data directory location, which Zotero 5.0 also wouldn't be able to locate automatically if it was blocked from accessing the Firefox preferences file. If you know the location, you can simply point Zotero to it from the Advanced → Files and Folders pane of the Zotero preferences. Otherwise, open the prefs.js file in your Firefox profile in a text editor and search for `dataDir` to see if a custom path was set.

#### Further Assistance

If you're still having trouble locating your previous data, post to the [Zotero forums](/forum) with the following information:

-   Your current data directory location from the Advanced → Files and Folders pane of the Zotero preferences
-   The timestamp and sizes of zotero.sqlite\* files within that directory
-   Which version of Zotero you were using previously
-   The names of a few files you see in your Firefox profile directory


