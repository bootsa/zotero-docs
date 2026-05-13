---
tags:
  - kb-obsolete
  - zotero_for_firefox
---

**This article applies to the deprecated Zotero for Firefox (pre-Zotero 5.0) plugin. It no longer applies to the current versions of Zotero.**

# Sharing data directory between Zotero Standalone and Zotero for Firefox

When you install both Zotero Standalone and Zotero for Firefox, you will be asked if you want to share your data directory. The general recommendation is to respond "Yes", because this will usually do what you expect Zotero to do. Here's some more detail on what's going on.

### Why share the data directory

When you add new items to your Zotero library, the metadata for those items is stored inside Zotero's database (zotero.sqlite) and file attachments are placed inside a special "storage" folder both of which are located inside your [Zotero data directory](zotero_data). By default, the data directory is located inside the [profile_directory](kb/profile_directory). When Zotero for Firefox and Zotero Standalone are using distinct data directories, they are not "aware" of each other's presence and data between the two does not transfer as smoothly (or at all).

If Zotero Standalone and Zotero for Firefox share the same data directory, you will observe the following benefits:

1\. Since items are saved to the same database, your data is always in-sync. Furthermore, if you open Zotero for Firefox and Zotero Standalone at the same time, Zotero for Firefox switches into a light-weight connector mode (very similar to Chrome/Opera/Safari connectors), where all the heavy lifting involving the database is performed inside Zotero Standalone. This may help speed up Firefox performance, but it also means that you *cannot* open up Zotero for Firefox pane while Zotero Standalone is open (if you try, this will simply focus the Zotero Standalone window).

If the two were not sharing the same data directory, you would notice that adding an item to, say, Zotero for Firefox, does not immediately cause the item to appear in Zotero Standalone. If you have sync enabled in both Zotero Standalone and Zotero for Firefox, items do transfer eventually. This is because Zotero for Firefox ends up uploading the new item to zotero.org and Zotero Standalone, in turn, downloads it back onto your computer. As you can imagine, this is a slow process that results in useless utilization of your internet bandwidth.

2\. In addition to "instant sync", sharing the data directory ensures that your data is not needlessly duplicated on your computer. When directories are shared, both metadata and file attachments are stored in one central location. Without sharing the data directory, both Zotero for Firefox and Zotero Standalone keep individual copies of each. Depending on the size of your library, this could result in gigabytes of duplicated data.

3\. Under rare circumstances, because the data is not instantaneously synced and you are able to edit your library in both Zotero for Firefox and Zotero Standalone, *not* sharing the data directory could result in sync conflicts. Sharing the data directory eliminates this possibility.

### Sharing the data directory manually

Normally sharing the data directory happens automatically. When you install both Zotero for Firefox and Zotero Standalone, whichever you open up second asks if you want Zotero to share the data directory. Click "Yes" (the default) and everything is configured automatically.

However, if the prompt never appears or the data directories end up separate for some other reason, you can follow these steps to share the data directory between Zotero Standalone and Zotero for Firefox.

1\. Determine which data directory you want to use. Usually you can just pick either Zotero Standalone or Zotero for Firefox at random. If, however, the two databases are not the same (e.g. you did not have sync set up and you added a bunch of metadata to Zotero for Firefox, but it did not show up in Zotero Standalone), you should pick the more complete database.

If neither database is complete, first merge them by [syncing](preferences/sync) both applications (make sure that the sync completes without errors or you may end up losing some data!). Once the databases are in sync, you can pick either one of them to be the main database.

2\. Open up Preferences for the application that you chose to keep the data directory. Under Advanced -> Files and Folders, click Show Data Directory. Note the path of the directory that is displayed.

3\. Open the other application (either Zotero for Firefox or Zotero Standalone) and navigate to Preferences -> Advanced -> Files and Folders. In the "Data Directory Location" section, select Custom and choose the directory that you noted in step 2 (this should contain a zotero.sqlite file). The application will tell you that it needs to be restarted. Do so.

The data directories between Zotero Standalone and Zotero for Firefox should now be shared. See below for ways to confirm this.

### How do I know if my data directories are shared?

The simplest way to confirm this is by opening both Zotero Stadalone and Firefox and then clicking the Zotero icon in Firefox. If the data directories are shared, this should bring Zotero Standalone window into focus. Otherwise, Zotero will open up inside Firefox.

### Why \*not\* share the data directory?

You may want to opt against sharing the data directory if you require two entirely separate Zotero libraries. One way to accomplish this is to have separate data directories for Zotero Standalone and Zotero for Firefox. You can then use them as separate libraries with completely different sets of items. (An alternative to such an approach is using [Firefox/Zotero Standalone profiles](https://support.mozilla.org/en-US/kb/profile-manager-create-and-remove-firefox-profiles)).

### Preferences are not shared

While all your data is stored inside the data directory, your preferences are stored inside your profile directory. Sharing your data directory does *not* share your profile directory, so preferences are not shared between Zotero for Firefox and Zotero Standalone. This means that if sometimes you use Zotero Standalone and sometimes you're using Zotero for Firefox on its own, you need to set up preferences (most importantly, sync under Preferences -> Sync) for both of them separately.


