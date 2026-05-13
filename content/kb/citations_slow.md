---
tags:
  - kb
  - word_processors
---

#### Why is Zotero slow to insert citations or update the bibliography?

When you insert a citation into a document using Zotero’s word processor plugin, Zotero needs to scan the entire document for citations to ensure correct formatting. Citation style requirements such as *ibid* or name disambiguation mean that the format of a given citation may depend on the citations that precede it, and bibliographies depend on the presence of, and in some cases the order of, all citations in the document, including any that may have been deleted or moved around since a citation was last inserted.

In longer documents, scanning the entire document can take multiple seconds or even minutes, and these updates can become disruptive to the writing process. Word for Mac 2008 and Google Docs are especially prone to slow down due to technical limitations of those programs.

To speed up your writing, you can disable automatic updates and defer citation updating until a manual refresh is triggered. With automatic updates disabled, citation inserts will remain instantaneous regardless of the size of the document.

To disable automatic updates, click the Document Preferences button in the word processor plugin and uncheck “Automatically Update Citations”:

![](/_media/kb/word_disable_automatic_updates.png){ .align-right width=500 }

To illustrate how citation inserting works with updates disabled, let’s look at an example. Say we’ve added a citation for a paper by Jessica Smith using APA style:

![](/_media/kb/delayed-citations-1.png){ width=200 }

If we then insert a paper by James Smith, Zotero will create a citation in the default format required by the style without taking into account other citations in the document:

![](/_media/kb/delayed-citations-2.png){ width=200 }

Zotero adds a dashed underline below newly added citations to remind us that they haven’t been updated (though keep in mind that existing citations later in the document might also now be incorrect).

It also replaces the bibliography with a warning:

![](/_media/kb/delayed-citations-3.png){ width=400 }

We can quickly insert citations this way without waiting for each update. When we’re ready to submit our document, we click the Zotero plugin’s Refresh button:

![](/_media/kb/delayed-citations-4.png){ width=200 }

Zotero scanned the document and updated the citations and bibliography to conform to the style rules, which in this case require disambiguation for lead authors with the same last name.

To avoid accidentally submitting a paper with unformatted citations, we recommend leaving automatic updates enabled unless you find that inserts are taking too long for a given document.

Alternative methods to speed up citing if you want to keep automatic updates enabled are to split long documents into chapters or to use a less-demanding citation style, such as [Annual Reviews (author-date)](https://www.zotero.org/styles/annual-reviews-author-date) during writing to increase the speed of citation inserts.


