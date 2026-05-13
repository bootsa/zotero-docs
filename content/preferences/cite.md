---
tags:
  - pref
---

# Cite

The Cite pane has two tabs: "Styles" and "Word Processors".

## Styles

![](/_media/preferences_cite_styles.png){ width=600 }

#### Style Manager

The Style Manager displays the currently installed citation styles and the date they were last updated. You can download additional styles directly from the [Zotero Style Repository](http://zotero.org/styles) by clicking the "Get additional styles…" link. You can also install a local [Citation Style Language](http://citationstyles.org/) (CSL) style file by clicking the "+" button and locating the style file on your computer. To delete a style, select the style and click the "-" button.

If you aren't sure what style you need, you can [Search by Example](http://editor.citationstyles.org/searchByExample/) to find a style. Note that this tool requires you to format the reference data shown on the page, not just any example reference.

#### Citation Options

-   **Include URLs of paper articles in references:** When this option is unchecked, Zotero will only include a URL when citing journal, magazine, and newspaper articles when the article does not have a page range specified.

#### Tools

-   **Style Editor:** Opens Zotero's [CSL Editor window](dev/citation_styles/reference_test_pane) for editing and testing CSL citation styles. You can also edit styles using a plain text editor program on your computer (e.g., Notepad, Text Edit) or the [CSL Visual Editor](http://editor.citationstyles.org/visualEditor/).
-   **Style Preview:** Opens Zotero's [CSL Preview window](dev/citation_styles/preview_pane) to preview how the references selected in your library will be formatted using installed styles.

## Word Processors

![](/_media/preferences_cite_processors.png){ width=600 }

Zotero's [word processor plugins](word_processor_integration) integrate Zotero into either Microsoft Word or LibreOffice. Zotero will install plugins into Word and LibreOffice automatically when you install Zotero. You can re-install the word processor plugins from this pane. Reinstalling the LibreOffice plugin may be helpful if upgrading LibreOffice causes the path to the LibreOffice program files to change.

If one of the Install buttons is disabled, check that the respective word processor extension is installed and enabled in Zotero Add-ons window (click "Tools -> Add-ons").

-   **Use classic Add Citation dialog:** By default, the Zotero word processor plugins will use a [Quick Citation interace](word_processor_plugin_usage#citing) that lets you intuitively search for items across all of your libraries, add multiple items to the same citation, and easily add page numbers, prefixes, and suffixes. To browse your libraries and collections for an item, you can click the "Z" on the left of the window to switch to the ["Classic View"](word_processor_plugin_usage_classic) citation dialog. Check this option to switch the default interface to the Classic View. Note that some features are not supported in the Classic View.


