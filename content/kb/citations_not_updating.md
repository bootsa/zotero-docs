---
tags:
  - kb
  - word_processors
---

# Why is a citation not updated in my document after editing the item in Zotero?

When you make changes to item data (title, author, date, etc.) in your Zotero library, those changes will be reflected in citations to those items in your word processor the next time you use the Zotero plugin's Refresh button.

If your citations are flat text and aren't being detected at all, see [Existing Citations Not Detected](kb/existing_citations_not_detected).

If you still have active citations (e.g., highlighted in gray when you click on them in Word or LibreOffice, or showing the "Edit in Zotero" popup in Google Docs) but changes you make in Zotero aren't being reflected in the document, either you edited the citation text manually and told Zotero not to make further updates or the citation in your document is no longer linked to the item in your Zotero library.

Click the citation and click Add/Edit Citation. If you edited the citation, Zotero will notify you that the citation was modified and give you the option to reset it, after which the citation will update automatically. You should generally avoid manual edits in the document and [customize the citation](word_processor_plugin_usage#customizing_cites) to add page numbers, prefixes, etc.

If the citation hasn't been modified, the citation dialog will open with the citation shown. To check whether the citation is still linked to your library, click the blue bubble and look for the "Open in My Library [or the group library name]" button in the popup:

![citation-dialog-affixes-5.png](/_media/word_integration/citation-dialog-affixes-5.png){ width=350 }

If the "Open in…" button doesn't appear, the citation isn't linked to any of your Zotero libraries and Zotero is using the item metadata embedded in the document to generate the citation and bibliography entry. You will need to delete the citation from your document and reinsert it, being sure to select from the library section of the citation dialog search results rather than from the Cited section.

Citations can become orphaned for a number of reasons:

1.  You have duplicate items in your library, cite one of the duplicates, and then delete it rather than merging the items
2.  You delete an item from your library and then reimport it
3.  You cite an item with Mendeley and then edit the document with Zotero (though Zotero can [relink Mendeley Desktop citations](kb/mendeley_import#using_mendeley_citations) after you import your Mendeley library)


