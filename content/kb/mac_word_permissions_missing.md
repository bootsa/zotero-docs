---
tags:
  - kb
  - word_processors
---

# Zotero does not have permission to control Word

Recent macOS versions include new security measures when a program attempts to control another program on the system. Zotero's Word for Mac plugin requires the permission for Zotero to be able to control Word. When you first interact with the Zotero Word plugin, you'll get a prompt asking for this permission:

![](/_media/kb/zotero-wants-control-word.png){ width=260 }

If you press "Don't allow", Zotero won't be able to provide the Word plugin functionality and every subsequent attempt to use the plugin will trigger the "Missing Permissions" prompt, until you follow the steps in the prompt:

### macOS 13 Ventura and later

1.  Open System Settings
2.  Select "Privacy & Security" in the left column
3.  Select "Automation"
4.  Find "Zotero" and click the arrow to expand it
5.  Make sure "Microsoft Word" is enabled under "Zotero"
6.  Restart Word

### macOS 12 Monterey and earlier

1.  Open System Preferences
2.  Select "Security & Privacy"
3.  Find and select "Automation" on the left
4.  Check the checkbox for "Microsoft Word" under "Zotero"
5.  Restart Word

### Word 2011

If you're running Word 2011, be sure you've updated to the latest version, 14.7.7, for compatibility with the new permissions system in Mojave and above.


