---
tags:
  - kb
  - entry
---

# How can I import from Citavi?

The best format for importing records from Citavi into Zotero is Citavi XML. This format will import the item bibliographic metadata, as well as quotations, tasks, attachments, etc. Beginning in Zotero 6, Zotero will also import PDF annotations. Zotero can import files exported from Citavi 5 and Citavi 6.

## Citavi XML format (recommended)

##### Special case: Cloud project

If your project is a cloud project, you need to make a local copy of it, as preparation for the export:

1.  In Citavi click on `File` -> `This project` -> `Save a copy of this project...`
2.  In the following dialog, click on `Create local project copy`, put a meaningful name (e.g. *myproject_local*) in the `Project name` field and click on `Next`.
3.  In the next dialog, click on `Keep the cloud project` and click on `Next`.
4.  As soon as the local copy is finished, the local project will open in a new Citavi window. From there, resume with the following procedure.

##### Local project

1.  In Citavi click on `File` -> `This project` -> `Create backup...`
2.  The backup is saved in a file with the file ending with `ctv5bak` or `ctv6bak` and lies normally in your [home directory](https://en.wikipedia.org/wiki/Home_directory) under `Documents\Citavi 5\Backup` or `Documents\Citavi 6\Backup` (i.e., follow this format `C:\Users\<username>\Documents\Citavi 5\Backup\<projectname>`). Alternatively, you can look up the backup folder under Tools / Options / Folders and there click on "Open folder with Windows Explorer", see <https://www.citavi.com/sub/manual5/en/101_backing_up_your_projects.html>.
3.  The `ctv5bak` or `ctv6bak` file is a ZIP file, which cannot be processed directly — you must first unzip it and continue with the resulting unzipped file. To unzip it, either change the extension to .zip or use software dedicated to archiving/unarchiving files, such as 7zip. Note that file extensions are often hidden by the operating system, so to change the extension you might need to enable extension visibility.
4.  To import attached files (e.g., PDFs) into Zotero, you have to make sure that they are in the same folder as the `ctv5` or `ctv6` file you are importing. Citavi will save all attachments in the project folder (e.g., `C:\Users\<username>\Documents\Citavi 5\Projects\<projectname>\Citavi Attachments`). Copy them from there.
5.  Import the `ctv5` or `ctv6` file in Zotero.

## Limitations

-   Nested collections in Citavi will not be nested anymore in Zotero. However, the numbers for the collections names should represent the nesting and adjusting this then manually should be easy.
-   To import PDF annotations, you must be running Zotero 6.

## RIS format (alternative)

As an alternative to the above procedure, you can export your Citavi library in the RIS format. This format will only retain item bibliographic metadata. Any additional item elements, such as citations from the "knowledge management" functionalities in Citavi, will not be included.


