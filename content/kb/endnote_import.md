---
tags:
  - kb
  - entry
---

# How do I import from EndNote?

## Exporting Your Library from EndNote

Zotero can't directly import ".enl" EndNote libraries, so the first step is exporting your library from EndNote. The best export format for this is XML.

With older EndNote libraries, it may be necessary to convert figures to attachments before you export. This is done by going to the References menu → Figure and selecting "Convert Figures to File Attachments…".

1.  If you wish to export a subset of your EndNote library, select the entries you wish to export.
2.  Go to the File menu → Export. A dialog box will pop up asking you where to save the export file.
3.  Navigate to your EndNote data directory (typically, My Documents\\endnote.Data). This directory contains a 'PDF' folder, but you should be sure to select the data directory rather than any subfolder.
    -   **This is important!** Zotero will look for file attachments in a directory relative to the location of the exported XML file. If you save this file in the wrong spot, file attachments won't be included when you import into Zotero.
4.  For "Save as type:", choose "XML".
5.  If you only want to export a subset of your library, check the "Export Selected References" box. Otherwise, make sure it is unchecked.
6.  Click "Save".
7.  Close EndNote.

## Importing into Zotero

If you are not importing into an empty library, we **highly recommend** [making a backup of you Zotero data directory](zotero_data#backing_up_your_zotero_library). This can avoid frustration if you do not like the way your library has transferred. In that event, simply [restore your library from the backup](zotero_data#restoring_your_zotero_library_from_a_backup1).

You should also temporarily disable automatic sync in Zotero's [Sync preferences](preferences/sync). After you have imported your library and checked to be sure you are satisfied with the imported data, you can re-enable automatic sync.

In Zotero, click "Import…" in the File menu. A dialog box will appear asking you to select the file to import. Navigate to the location where you exported your EndNote library (if you followed the above instructions, this should be My Documents\\endnote.Data) and select the .xml file. Click Open.

Note that, if Zotero encounters any fields in the EndNote XML data that it does not support (e.g., custom fields, author address, author affiliation), it will add these data to a note attached to the imported item. These notes will be tagged with "\_EndnoteXML import". If the import adds many of these notes, Zotero's performance can be negatively impacted. You should review each of these notes to determine if the data needs to be retained and delete any unnecessary notes. Additionally, you should check these notes to determine if any data could be migrated to proper Zotero fields (which is particularly important if you were using EndNote fields in non-standard ways).

You can quickly display all of the notes generated during import by clicking on the "\_EndnoteXML import" tag in the tag selector in the lower-left corner of the Zotero window. You can quickly delete all of these notes by selecting the tag in the tag selector, clicking in the items list and typing Cmd+A (Mac) or Ctrl+A (Windows/Linux) to select all matching items, and then right-clicking on a selected item and choosing "Move Items to Trash…".

## Getting Further Help

If you have any issues related to importing and exporting references, feel free to ask for help on the [Zotero Forums](forums).

## RIS format (alternative)

Instead of EndNote XML, it is also possible to export items from EndNote using RIS. The only benefit of RIS over XML is that the EndNote database ID can be retained for each item. If this is required, then, in Zotero, open the Advanced pane of [Zotero preferences](kb/preferences) and click the "Config Editor" button on the "General" tab. Search for "RIS.import.keepID" and double-click to set it to **true**. If you want data for unknown fields to be retained in notes (as described above), also search for "RIS.import.ignoreUnknown" and set this option to **false**.

In EndNote, export your library as above, setting "Save as type:" to "Text file (.txt)". Set "Output style:" to "RefMan (RIS)". Navigate to your EndNote data folder (as described above), save the export file, then import into Zotero as described above.

With this setup, RIS will retain EndNote database IDs, but any italics, bold, or other formatting set in fields will be lost. XML should always be used unless EndNote database IDs are needed for a specific reason.


