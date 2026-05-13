# Importing a Mendeley Library Into Zotero (Alternative Local Method)

Zotero can [import from an online Mendeley library](kb/mendeley_import), and we recommend using that method if possible.

If for some reason you're unable to perform an online import, it's possible to import from a local Mendeley Desktop database, but you'll first need to install an old version of Mendeley Desktop. Later versions of Mendeley Desktop began [encrypting the local database](kb/mendeley_import#mendeley_database_encryption), preventing you from getting your own data out of the app.

To perform a local import, follow these steps:

1.  Make sure you've synced all data *and* files to Mendeley servers in your current version of Mendeley. The only way to get existing data into a pre-encryption version of the app is by syncing it from Mendeley servers, and Mendeley sync doesn't make any information about attached files available unless you actually sync the files themselves.
2.  If you're already using Mendeley Desktop, make a [backup of your Mendeley database](https://service.elsevier.com/app/answers/detail/a_id/18153/).
3.  Close Mendeley Desktop
4.  Download and install Mendeley Desktop 1.18 using the [links below](#Mendeley 1.18 installers).
5.  Open Mendeley Desktop 1.18 and perform a fresh sync to pull down your Mendeley data and files from the Mendeley servers. (If Mendeley doesn't open, you may need to go to your Mendeley data directory and move the file ending with `@www.mendeley.com.sqlite` out of the way.)
6.  Verify that all your data and files are available locally. If some files are unavailable, it may help to add all items in the library to a folder and restart Mendeley Desktop.
7.  Make sure you're running the latest version of Zotero.
8.  Start the import in Zotero by going to File → “Import…”, choosing the file option, navigating to your Mendeley Desktop data directory, and selecting the file with the filename `<your email>@www.mendeley.com.sqlite`.

By default, the Mendeley data directory can be found at the following locations:

-   Windows: `%LOCALAPPDATA%\Mendeley Ltd.\Mendeley Desktop\`
-   macOS: `/Users/<username>/Library/Application Support/Mendeley Desktop/`
-   Linux: `~/.local/share/data/Mendeley Ltd./Mendeley Desktop/`

### Mendeley 1.18 installers

*Mendeley 1.18 installers are no longer available from Elsevier.*
