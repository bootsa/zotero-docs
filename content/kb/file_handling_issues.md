---
tags:
  - kb
  - basics
---

# File Handling Issues

### Unexpected behavior (wrong action, gibberish ("%PDF..."), etc.) when opening files from Zotero

Deleting handlers.json from your [profile directory](kb/profile_directory) and restarting Zotero may help fix file handling issues. handlers.json stores file handling associations and will be recreated automatically the next time you restart Zotero.

### PDFs opening in wrong application on Linux systems

While Zotero be configured to use the system-default PDF reader, file handling on Linux can be affected by many settings. If you find that PDFs open in, say, Gimp even though you've set the file handler to be Okular in Dolphin/Nautilus/etc., the easiest solution is to choose a specific PDF reader from the General pane of the Zotero preferences.

If you'd like to keep the setting as "System Default", you can try the following:

Open the file

    ~/.local/share/applications/defaults.list

in a text editor and look for the line "application/pdf=...". Change it to

    application/pdf=kde4-okularApplication_pdf.desktop

If the file does not exist, create it and enter the following content:

    [Default Applications]
    application/pdf=kde4-okularApplication_pdf.desktop

Note: On some systems, you might need to use

    application/pdf=kde-okularApplication_pdf.desktop

instead.

For other PDF readers you might use one of the following:

    application/pdf=evince.desktop

    application/pdf=acroread.desktop

    application/pdf=Foxit-Reader.desktop


