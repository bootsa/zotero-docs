---
tags:
  - kb
  - styles
---

# Missing Italics (or Italics-Only) in Word Bibliographies

On rare occasions, you will find that your Zotero bibliography in Word is missing italics, even though those are required for book titles in the citation style you've chosen. Sometimes you will find the reverse: the entire bibliography is in italics.

First, verify that this is not an issue with the citation style. The citation should display correct formatting when hovering your mouse over it at the [Zotero style repository](https://www.zotero.org/styles).

If the style is displaying correctly there, you are very likely facing a [known issue with Microsoft Word](http://shaunakelly.com/word/styles/stylesoverridedirectformatting.html), which will change the formatting of the entire bibliography when more than half of the first entry in the bibliography is italicized.

## Workaround

Insert a "dummy" reference that will appear at the beginning of the bibliography and contains little italicized text (e.g. short book title). For bibliographies sorted alphabetically by first author, for example, insert a fake reference by Abu Aardvark. You would then remove this reference after finalizing the document and converting Zotero citations to plain text (we highly recommend saving a copy of the document before doing this).

Unfortunately, for numeric citation styles where the bibliography is sorted in order of first occurrence, inserting a fake reference would adjust the numbering for all other citations. Removing the fake reference at the end, would then make the bibliography start from 2 rather than 1. The best workaround we can suggest in this case is to duplicate the first reference in your Zotero library (so you still have an untouched original), reduce the length of the field that is italicized (e.g. delete some of the book title), and re-insert the shortened version of the reference into your document instead of the original. The reference would then have to be manually fixed in the document after finalizing it.


