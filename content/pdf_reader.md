# Zotero PDF Reader and Note Editor

![](https://www.zotero.org/static/images/blog/6.0/pdf-reader.jpg)

## Creating Annotations

### Highlights and Underlines

The reader supports two highlighting/underlining modes. You can use whichever mode works best for your workflow.

In the default, **unlocked mode**, with nothing selected in the annotation toolbar, whenever you select text in the document, a popup will appear with a selection of colors, and you can click a color to create a highlight or underline on the selected text.

To quickly make many highlights or underlines, you can turn on **locked mode**: click the highlight or underline tool in the toolbar, and then choose a color using the color-picker button. Then, every time you select text in the document, a highlight or underline will be automatically created in the color you've picked.

## Adding Annotations to Notes

You can add annotations to notes in various ways. Annotations added to notes will automatically include links back to the PDF page as well as citations that you can later add to a Word, LibreOffice, or Google Docs document with one of the word processor plugins.

### In the PDF reader

You can easily add annotations to notes right from the PDF reader.

First, use the Notes button in the top-right corner to open the Notes pane, where you can create a new note or open an existing note.

To create a new note from all annotations in the current PDF, click one of the "+" buttons and select Add Item Note from Annotations or Add Standalone Note from Annotations.

If you already have a note open in the Notes pane, you can drag individual annotations from the PDF or from Annotations tab in the left-hand sidebar as you type your note. Alternatively, you can select one or more annotations in PDF or in the the Annotations tab of the left-hand sidebar, right-click one of the annotations, and select Add to Note.

You can also drag annotations from the PDF reader to a note that's opened in a separate window.

If you're sure you won't use a quote more than once, it's also possible to add quotes to Zotero notes without creating an annotation first. Simply select text in the PDF and drag it to an open Zotero note.

### In the items list

You can create a child note from all annotations in a PDF by right-clicking on the parent item in the items list and choosing Add Note from Annotations.

You can also create a standalone note with annotations from multiple items by selecting the parent items, right-clicking, and choosing Create Note from Annotations.

![](https://www.zotero.org/static/images/blog/6.0/add-note-from-annotations.png){ width=310 }

## Customizing Annotations in Notes

You can customize how annotations are added to notes by using [note templates](note_templates).

## Working with Annotations in Notes

### Viewing an Annotation in Context

When you [add an annotation to a note](#adding_annotations_to_notes), it will add both an annotation and a citation by default.

To view the annotation in context, click the annotation and click "Show on Page" in the popup that appears. This will open the original PDF in either the built-in PDF reader or an external PDF reader if you've configured one in the General pane of the preferences. When possible, Zotero will open the PDF to the page where the annotation was made — this works for the built-in PDF reader and most, but not all, popular external PDF readers (e.g., Acrobat on Windows, Preview on macOS, evince on Linux). If Zotero isn't opening to appropriate page PDF in your external PDF reader, let us know in the Zotero Forums.

To view the associated item in your library, click the citation and select "Show Item".

### Displaying Annotation Colors

To show annotation colors in your note, click the "..." button in the top-right corner of the note editor and select "Show Annotation Colors". You can remove colors later with "Hide Annotation Colors".

### Hiding or Showing Citations

To hide or show all citations in a note, click the "..." button in the top-right corner of the note editor and select "Hide Annotation Citations" or "Show Annotation Citations".

You can hide an individual citation by clicking on it in the editor and selecting "Hide Citation" from the popup, or simply by deleting the citation completely. You can add the citation back at any time by clicking on the highlighted text and selecting "Add Citation" from the popup or by using "Show Annotation Citations" in the "..." menu.

## Using an External PDF Reader

If you'd prefer to open PDFs in an external PDF reader, you can choose one from the General pane of the Zotero preferences.

To open a single PDF in an external reader, right-click on the item and choose Show File, and then open the PDF from your OS file manager. Some changes you make in external PDF readers will cause problems in the built-in reader — e.g., adding, deleting, reordering, or rotating pages will cause annotations to appear on the wrong page or in the wrong position. (Pages can be deleted or rotated from the Annotations tab in the Zotero reader sidebar.)

Note that annotations created in the built-in PDF reader are stored in the Zotero database, so they won't be visible in external PDF readers unless you export a PDF with embedded annotations. See [Annotations in Database](kb/annotations_in_database) for more info.
