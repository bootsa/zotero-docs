---
tags:
  - kb
---

# Why does Zotero store PDF annotations in its database instead of in the PDF file?

The new [PDF reader](pdf_reader) in Zotero 6 makes PDF reading and annotation a first-class part of the Zotero experience.

To enable this tight integration, Zotero stores annotations in the Zotero database, not in the PDF file. This allows for fast, conflict-free syncing, including in groups, and enables advanced functionality that wouldn't be possible otherwise.

Zotero annotations can be exported to PDFs with embedded annotations at any time and will never be locked in Zotero.

## Benefits of Zotero Annotations

With annotations stored in the database, Zotero is able to quickly sync just the details of each new or updated annotation. By contrast, with standard PDF annotations, the entire PDF file needs to be transferred after every change, so if two people in a group added an annotation at the same time, or even if a PDF was just left open on one computer, it would create an unresolvable file conflict, forcing the user to choose one side or the other. This happened regularly in earlier versions of Zotero, both in personal and group libraries, and we expect PDF annotation to get far more usage as part of the app.

Storing annotations in the database also enables advanced functionality, such as being able to tag annotations and filter for them throughout the Zotero interface. We plan to add other extended features like this going forward.

There are major performance benefits as well. For syncing, as discussed above, saving annotations back to the file requires Zotero to transfer the entire file — which could be many megabytes — after every change, whereas transferring just an individual annotation is instantaneous. It's also harder for Zotero to track changes to external files, so if you annotate something externally, there may be a delay before you can search for those annotations in Zotero or before the updated file syncs — you might need to wait for Zotero to notice the file modification or manually trigger reprocessing and syncing.

We'll always try to support external workflows as efficiently as possible, but it will never match the seamless experience we're able to provide when everything is done within the app.

## Interacting with Embedded Annotations

While Zotero saves its own annotations to its database, it's possible to interact with annotations embedded in a PDF file in much the same way, as well as to export PDFs with embedded annotations.

Embedded annotations show up in the Zotero PDF reader, and you can [add them to Zotero notes](pdf_reader#adding_annotations_to_notes) in exactly the same ways as Zotero-created annotations. External annotations are read-only by default — indicated by a lock icon — but you can transfer them into Zotero by selecting File → "Import Annotations…" from within the PDF reader, after which they'll be fully editable. The annotations are removed from the PDF to avoid conflicts and duplicates. (Early versions of Zotero 6 included a "Store Annotations in File…" option as well, but it could result in file conflicts and lost data, and it [was removed](https://forums.zotero.org/discussion/comment/404140/#Comment_404140).)

You can export a copy of the PDF with annotations embedded by using File → "Export PDF…" from the library view or "Save As…" from the PDF reader. (To export the original file, drag the attachment item from the items list to your filesystem or use right-click → Show File and copy the file from there.)

When exporting metadata (e.g., BibTeX or RIS) from your library, there's an “Include Annotations” option under “Export Files” that will embed annotations in all exported PDFs. We plan to support other ways to export annotations in future updates.

## Using an External PDF Reader

While we've tried to create a new, better PDF experience within Zotero, which requires annotations to be stored within the database, you can always choose to use a different PDF reader if you decide one works better for you. You can set the default PDF reader from the General pane of the Zotero preferences.

If you'd like to keep the Zotero PDF reader as the default but occasionally open a PDF externally, simply right-click on the PDF in Zotero and choose Show File, and then double-click the PDF in your filesystem. (Annotations of course won't show up, and some changes, such as moving or deleting pages, may cause problems with existing annotations in Zotero, which is why we don't expose this option directly. Rotating and deleting individual pages can be done safely from the thumbnails tab of the Zotero PDF reader sidebar.)

## Data Portability

Data portability is one of Zotero's founding principles, and we've gone to great lengths to ensure that, if you choose to use the built-in PDF reader, your annotations will never be locked within Zotero.

If you choose to stop using Zotero in the future, you can trivially export your entire library with annotations embedded in your PDFs.

In addition to the methods detailed above for exporting annotations, annotations are stored locally in Zotero's open SQLite database and are extractable using standard open-source tools. They are also accessible to plugins within Zotero and to external tools via the Zotero web API.


