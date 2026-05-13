---
tags:
  - kb
---

# How can I use multiple profiles in Zotero?

Zotero allows you to create multiple profiles, each with its own settings and associated [data directory](zotero_data). This is an advanced configuration and not recommended for most users, but if you're familiar with using multiple profiles in Firefox, Zotero works the same way and supports the same command-line flags.

A default profile is created when you first start Zotero. To create an additional profile, start Zotero from the command line and pass the `-P` flag to open the Profile Manager:

### macOS

-   Open Terminal via Spotlight or /Applications/Utilities.
-   Paste `/Applications/Zotero.app/Contents/MacOS/zotero -P` into the Terminal window.
-   Press Return

### Windows

-   Open the Run dialog (Search/Cortana → type “Run” → Run (Windows 10) or Start → Run (Windows 7)
-   Paste `C:\\Program Files (x86)\\Zotero\\zotero.exe -P `
-   Press Enter

### Linux

-   Start Zotero via the command line, adding the `-P` command-line flag.

The Profile Manager window should appear, allow you to select, create, and delete Zotero profiles.

When you create a new profile (e.g., "Work"), if there's already a profile pointing to the default data directory location, Zotero will create a new data directory named after the new profile (e.g., "Zotero Work") when you first start it. Your original data directory won't be affected. [**Note, June 2023:** This seems to currently not always happen. If you see your existing data directory in the new profile, create a new data directory manually and point the new profile to there from the Advanced → Files and Folders pane of the Zotero preferences.]

You can open a specific profile from the command line with the `-p` flag (e.g., `-p Work`), which may be useful for creating shortcuts that automatically open a given profile. (On a Mac, you can save [an AppleScript with command-line flags embedded](https://superuser.com/a/116237) as an application in Script Editor.)

Additional configuration may be required when running [multiple instances](kb/multiple_instances) of Zotero at a time.


