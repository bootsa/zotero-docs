---
tags:
  - kb
  - word_processors
---

# Why isn’t Zotero detecting my existing citations?

If you've previously used one of Zotero's word processor plugins to insert citations into a document and later find that 1) the plugin says "You must insert a citation before performing this operation", 2) the bibliography doesn't contain all citations in the document, and/or 3) references in a numeric citation style start from 1 instead of from an appropriate higher number, the existing citations in the document may no longer be active fields.

To check whether fields in a document are active, click them and looking for a gray highlight (Word/LibreOffice) or "Edit with Zotero" popup (Google Docs). If you then click Add/Edit Citation, the Zotero citation dialog should appear with the citation shown. If the citation dialog is empty, the citation is no longer active. In Word and LibreOffice, you can also try [toggling field codes](kb/word_field_codes).

Your citations may have become inactive for a few reasons:

1.  You used the "Unlink Citations" button. This button will disconnect your document from Zotero and convert all citations and bibliographies to plain text.
2.  You (or someone else) saved the document in an unsupported file type:
    -   When using Word, you need to save your document as .docx. If you save as .odt, active citations will be lost.
    -   When using LibreOffice, if you are storing citations as ReferenceMarks (the default), you must save your document as .odt. If storing citations as Bookmarks, you must save your document as .docx.
3.  You (or someone else) opened and saved your document using an unsupported word processor or without following proper steps to move active citations between supported word processors:
    -   **Google Docs:** If you want to open a Word or LibreOffice document in Google Docs, or vice versa, you must follow an extra step to [transfer the document](kb/moving_documents_between_word_processors). Directly opening a Word or LibreOffice document in Google Docs, or vice versa, will break existing citations.
    -   **Other online word processors**: Most online word processors do not support Fields/ReferenceMarks/Bookmarks. Opening an existing document in these tools will break connections with Zotero. Microsoft's Word Online does support Fields and so can be used safely with Word documents containing Zotero fields, though a Zotero plugin is not currently available for Word Online.
    -   **Pages:** Apple Pages does not support Fields/ReferenceMarks/Bookmarks. Opening a document in Pages will break connections with Zotero.
    -   **Word:** If you open an .odt file (created by LibreOffice) in Word, Zotero references stored as ReferenceMarks (the default) will be broken. To share a document between Word and LibreOffice users, change the "Store Citations as:" option in the Zotero Document Preferences to Bookmarks. (Bookmarks can cause errors if accidentally modified, so they should only be used if compatibility between Word and LibreOffice is necessary. You can also choose to [transfer the document](kb/moving_documents_between_word_processors#word_and_libreoffice) instead.)
    -   **LibreOffice:** If you open a .docx or .doc file (created by Word) in LibreOffice, Zotero references stored as Fields (the default) will be broken. To share a document between Word and LibreOffice users, change the "Store Citations as:" option in the Zotero Document Preferences to Bookmarks. (Bookmarks can cause errors if accidentally modified, so they should only be used if compatibility between Word and LibreOffice is necessary. You can also choose to [transfer the document](kb/moving_documents_between_word_processors#word_and_libreoffice) instead.)
4.  If you're using Google Docs, see [Why isn’t Zotero detecting my existing Google Docs citations?](https://www.zotero.org/support/kb/google_docs_citations_unlinked) for other possible reasons.

If you find that your citations have been flattened, your only options are to restore the document from a backup, re-insert the citations using the plugin, or manually edit the document's citations going forward and generate a final bibliography from a collection in Zotero without using the plugin. If reinserting citations, it may help to adjust Word field settings to always highlight fields in gray rather than only doing so when they are selected.

If your bibliography is flattened but your citations are still active, you can simply insert a new bibliography by clicking Add/Edit Bibliography.


