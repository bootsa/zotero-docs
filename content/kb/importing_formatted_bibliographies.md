---
tags:
  - kb
  - entry
---

## I have bibliographies in Microsoft Word documents, PDFs, and other text files. Can I import them into my Zotero library?

### Citations inserted using Zotero or Mendeley Desktop

Zotero can read existing citations created by the Zotero and Mendeley Desktop (not Mendeley Cite) word processor plugins, allowing you to continue using those citations in the same document even if the items don't exist in your Zotero library. Simply click Add/Edit Citation, search for an existing citation, and select it from the Cited section of the search results. (This applies to the default citation dialog only, not the "classic" dialog.)

If a document contains Zotero or Mendeley Desktop citations not in your library and you need to make changes to the metadata or include them in other documents, you'll need to extract the citations into your library. For Word .docx documents, you can use [Reference Extractor](https://rintze.zelle.me/ref-extractor/). Note that to continue using the same document, you'll want to replace all instances of the original citation with the new item from your library, being sure to select from the library section of the citation dialog's search results rather than the Cited section. (In an upcoming version of Zotero, it will be possible to relink orphaned citations without needing to reinsert them.)

If you still have the references in the reference manager, you can import them into Zotero:

-   Zotero has a [built-in Mendeley importer](kb/mendeley_import) that can import all data and automatically relink citations in existing documents.
-   For other programs, export your data in a format such as RIS or BibTeX and then [import the file](adding_items_to_zotero#Importing_Records_from_Other_Reference_Tools) into Zotero. You'll need to replace all existing citations in any document for which you want Zotero to generate a correct bibliography.

### Citations inserted using Microsoft Word’s built-in citation feature

If you used Word's built-in citation feature, you can follow these steps to format the bibliography as BibTeX, which Zotero can import:

1.  Download this [Word bibliography stylesheet](https://gist.githubusercontent.com/JaimeChavarriaga/40166befb14f2fe5dac390688d9eaf03/raw/faf4aa3f72e553095f81f1440c3dce744c2755a2/bibtex.xsl).
2.  Save the stylesheet to Word's bibliography styles folder:
    -   *Word 2016/2019/Office 365 for Windows:* `C:\Users\<currentusername>\AppData\Roaming\Microsoft\Bibliography\Style`
    -   *Word 2010 for Windows:* `C:\Program Files\Microsoft Office\<Office version>\Bibliography\Style` or `C:\Program Files (x86)\Microsoft Office\<Office version>\Bibliography\Style`
    -   *Mac:* Go to the Applications folder. Right-click on Microsoft Word and choose "Show Package Contents". Navigate to: `Content/Resources/Style`
3.  In Word, change your bibliography style to "BibTeX export" and copy the bibliography to the clipboard.
4.  Use Zotero's [Import from Clipboard](kb/import_from_clipboard) function.

To continue using the same document, you'll want to replace all instances of the original citations so that Zotero can generate a correct bibliography.

### Plain-text citations and bibliographies

If the references have ISBNs, DOIs, or PubMed IDs, you can use the [Add Item by Identifier](adding_items_to_zotero#add_item_by_identifier) function in Zotero to quickly add these items to your Zotero library.

If you have many references, you can use [AnyStyle](http://anystyle.io), ​an online bibliography ​parser written by a Zotero developer. Export parsed citations as BibTeX or CSL-JSON and import them into Zotero. Some people have also had success asking ChatGPT or other AI systems to parse bibliographies and generate BibTeX or CSL-JSON, though if you try this, you should check the output carefully for errors.

Otherwise, your best option is to find the items online in a repository that Zotero supports — most likely just by searching the web for the citation — and saving to Zotero [with the Zotero Connector](adding_items_to_zotero#via_your_web_browser). This will help ensure that you get high-quality data that includes all fields that might be necessary in the citation style you're using.

As a last resort, you can manually enter the references in Zotero.

In all cases, you'll need to replace all existing citations in any document for which you want Zotero to generate a correct bibliography.


