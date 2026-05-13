# Using The Zotero Word Plugin

**Note:** The instructions below refer to the "classic" (original) Add Citation interface for Zotero's word processor plugins. In current versions of Zotero, a newer interface that is faster, more flexible, and easier to use is enabled by default. The newer interface is also currently receiving development for new features and improved performance. In general, using the newer (default) interface is recommended. Instructions for the default interface are available for [Word](word_processor_plugin_usage) and [LibreOffice](libreoffice_writer_plugin_usage).

**Browsing:** The one feature of the Classic citation interface that is not yet implemented in the default interface is the ability to browse through the list of items and collections in one's libraries. If you need to browse for an item, you can access the Classic citation interface from the default interface by clicking on the "Z" icon on the left size of the Add Citation box and choosing "Classic View".

## Using the Classic View Citation Window

The Classic View citation window is divided into divided into two panes. The left pane lists the libraries and collections in your Zotero database. The right pane lists the items in the currently selected library/collection. You can browse, search, and sort in the Classic View citation dialog in the same way as in the main Zotero app. Select the item you want to cite and click "OK" or type Enter/Return to insert the citation.

![](/_media/classic_addcitation.png){ .align-right width=800 }

#### Customizing Cites

At the bottom of the Classic View citation window are options to customize the appearance of citations.

![](/_media/classic_customizing_cites.png){ .align-right width=500 }

  
##### Pages and Other Locators

![classic_locators.png](/_media/classic_locators.png){ .align-left width=115 }

To add a page number to a citation, as in "(Schumpeter, 1962, p. 32)", enter the page numbers in the locator field on the bottom right of the Classic View citation window add citation window.

You can add other locators, such as chapter, paragraph, verse, etc. by selecting the label from the dropdown menu. Zotero will add the appropriate label in the citation—e.g., "(Schumpeter, 1962, ch. 1)". To add a locator that is not available from the dropdown menu, use the Suffix field.

##### Prefix and Suffix

The “Prefix” and “Suffix” fields in the lower-left corner of the Classic View citation window allow you to specify text to respectively precede and follow the automatically generated cite. For example, instead of “Tribe 1999”, you might want “cf. Tribe 1999, see also…”.

Any text in the prefix and suffix fields can be formatted with the HTML tags <i> (for italics), <b> (bold), <sub> (subscript), and <sup> (superscript). For example, typing ”<i>cf</i>. the classic example“ will be displayed as ”cf. the classic example“.

Modifying citations by entering text into the Prefix and Suffix fields is always preferable to directly typing in the citation fields in your document or using the "Show Editor" button (see below). Manual modifications will prevent Zotero from automatically updating the citation.

##### Suppress Authors: Using Authors in the Text

With author-date styles, authors are often moved into the text and omitted from the following parentheses-enclosed citation. For example: ”…according to Smith (1776) the division of labor is crucial…“. To omit the authors from the cite, check the “Suppress Author” box (this will result in a cite like ”(1776)“ instead of ”(Smith, 1776)“) and write the author's name (“Smith”) as part of the regular text in your document.

#### Using Multiple Sources in a Citation

To include multiple sources in a citation, (e.g., [2,4,7] for numerical citations; (Smith 1776, Schumpeter 1962) for author-date citations; or multiple works in a single footnote for note-based citation styles) click the "Multiple Sources…" button.

![classic_multiple_sources.png](/_media/classic_multiple_sources.png){ .align-center }

In the multiple sources view, add an item to a citation by selecting it in the middle pane and clicking the arrow pointing toward the right-right hand pane. To remove an item from the citation, select it in the right-hand pane and click the arrow pointing left toward the center pane.

##### Sorting for Multiple Sources

Change the order items appear in a citation by selecting an item in the right-hand pane and clicking the up or down arrow. Some citation styles specify the order of items in a citation (e.g., chronologically, alphabetically). You can disable automatic sorting by moving items using the arrow buttons or by unchecking the "Keep Sources Sorted" box above the right-hand pane. *The checkbox only appears for citation styles that specify a sort order for citations.* To restore automatic sorting, re-check the "Keep Sources Sorted" box.

##### Prefix and Suffix for Multiple Sources

Prefixes and suffixes can be applied to each individual item in a multiple citation. This allows you to create complex citations. For example: ”(see Smith 1776 for the classic example; Marx 1867 presents and alternate view)“.

Modifying citations by entering text into the Prefix and Suffix fields is always preferable to directly typing in the citation fields in your document or using the "Show Editor" button (see below). Manual modifications will prevent Zotero from automatically updating the citation.

#### Show Editor Button

You can preview the citation by clicking on the "Show Editor" button.

While it is possible to edit the citation text here (including adding/deleting text or applying/removing bold, italics, or underlining), doing so is strongly discouraged. Modifying the text in the Show Editor field will prevent Zotero from automatically updating the citation and may also cause the items to not appear correctly in the Bibliography.
