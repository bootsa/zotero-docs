# RTF Scan

Zotero's RTF Scan feature allows users to create a fully cited document without having to use the [word processor plugin](word_processor_integration). Many writers know the creator and date of a work they wish to cite off the top of their heads. Using the plugin might slow them down. Zotero can still format all the citations after the fact, however.

To use RTF Scan, create a new document in the Rich Text Format (RTF) and start writing. Whenever you wish to create a citation, write it in one of the following formats:

      {Smith, 2009}
      Smith {2009}
      {Smith et al., 2009}
      {John Smith, 2009}
      {Smith, 2009, 10-14}
      {Smith, "Title", 2009}
      {Jones, 2005; Smith, 2009}

You can also install the [RTF Scan](https://www.zotero.org/styles?q=id%3Artf-scan) citation style into Zotero and use [Quick Copy](creating_bibliographies#quick_copy) to easily copy citations in the expected format into your document without typing.

If you wish a bibliography to appear somewhere other than at the end of the document, type {Bibliography} where you wish it to appear.

Once you have finished writing, save the document (make sure it's .RTF) and open Zotero. From the Tools menu, select "RTF Scan…". Under Input File, select the document you've just created. In Output File, specify the name and location where you want the new, formatted file to be saved. Click Continue.

![](https://www.zotero.org/static/images/support/rtf_scan.png){ .align-right }

The Verify Cited Items screen will tell you which citations were mapped properly and which remain ambiguous. To fix an improperly mapped citation, click the icon to its right and select the correct citation in the dialog that appears. Zotero will provide suggestions for citations it is unsure of. Clicking the icon with the green arrow to the right of the suggestion will map it to that citation. Once all the citations are mapped properly, you can click Continue.

At the next screen, select the citation style you wish to use and click Continue. Zotero will then create your properly cited document. In the Output File, all the citations should be formatted properly for the selected style and, if the style calls for it, a bibliography will be included at the end, unless you specified another location.

It is important to note that, if you selected a citation format which calls for footnotes or endnotes, they will only appear properly if you open the Output File in a full-featured word processor, such as Microsoft Word or LibreOffice.

A more robust version of the RTF Scan feature that reduces the possibility of ambiguous citations and allows more flexibility for including prefixes, suffixes, and locator (page, chapter, verse, etc.) numbers in citations is provided by the [RTF/ODF-Scan for Zotero](plugins#other_programs) plugin. This plugin requires LibreOffice for use.
