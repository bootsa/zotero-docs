# Using the Zotero LibreOffice Plugin

These are instructions for using the Zotero LibreOffice Plugin. For plugins for Word or Google Docs, see [Word Processor Plugins](word_processor_integration).

## Zotero Plugin Toolbar

![zotero-toolbar-libreoffice-5.png](/_media/word_integration/zotero-toolbar-libreoffice-5.png){ .align-right width=200 }

[Installing the Zotero LibreOffice plugin](word_processor_plugin_installation) adds a Zotero toolbar to LibreOffice.

The Zotero toolbar contains these icons:

<table>
<tbody>
<tr class="header">
<td>Add/Edit Citation</td>
<td><img alt="zotero-toolbar-libreoffice-add-edit-citation-5.png" src="/_media/word_integration/zotero-toolbar-libreoffice-add-edit-citation-5.png"></td>
<td>Add a new citation or edit an existing citation in your document at the cursor location.</td>
</tr>
<tr class="odd">
<td>Add/Edit Bibliography</td>
<td><img alt="zotero-toolbar-libreoffice-add-edit-bibliography-5.png" src="/_media/word_integration/zotero-toolbar-libreoffice-add-edit-bibliography-5.png"></td>
<td>Insert a bibliography at the cursor location or edit an existing bibliography.</td>
</tr>
<tr class="even">
<td>Document Preferences</td>
<td><img alt="zotero-toolbar-libreoffice-doc-prefs-5.png" src="/_media/word_integration/zotero-toolbar-libreoffice-doc-prefs-5.png"></td>
<td>Open the Document Preferences window, e.g. to change the citation style.</td>
</tr>
<tr class="odd">
<td>Refresh</td>
<td><img alt="zotero-toolbar-libreoffice-refresh-5.png" src="/_media/word_integration/zotero-toolbar-libreoffice-refresh-5.png"></td>
<td>Refresh all citations and the bibliography, updating any item metadata that has changed in your Zotero library.</td>
</tr>
<tr class="even">
<td>Unlink Citations</td>
<td><img alt="zotero-toolbar-libreoffice-unlink-citations-5.png" src="/_media/word_integration/zotero-toolbar-libreoffice-unlink-citations-5.png"></td>
<td>Unlink Zotero citations in the document by removing the field codes and converting citations to regular text. This prevents any further automatic updates of the citations and bibliographies.<br />
Note that removing unlinking citations is <strong>irreversible</strong>, and should usually only be done in a final copy of your document.</td>
</tr>
</tbody>
</table>

## Citing

You can begin citing with Zotero by clicking the "Add/Edit Citation" (![zotero-toolbar-word-add-edit-citation-5.png](/_media/word_integration/zotero-toolbar-word-add-edit-citation-5.png){ width=16 }) button. Pressing the button brings up the citation dialog.

The citation dialog is used to select items from your Zotero library, and create a citation.

![citation-dialog-select-5.png](/_media/word_integration/citation-dialog-select-5.png){ .align-right width=294 }

Start typing part of a title, the last names of one or more authors, and/or a year in the dialog box. Matching items will instantly appear below the dialog box.

Matching items will be shown for each library in your Zotero database (My Library and any groups you are part of). Items you have already cited in the document will be shown at the top of the list under "Cited".

Select an item by clicking on it or by pressing Enter/Return when it is highlighted. The item will appear in the dialog box in a shaded bubble. Press Enter/Return again to insert the citation and close the Add Citation box.

In the Add Citation dialog box, you can click on the bubble for a cited item, then click "Open in My Library (or the Group Library's name)" to view the item in Zotero. Items that are orphaned (not connected to any items in your Zotero database) will not have an "Open in My Library" button. Orphaned items can exist if they were inserted by a collaborator from their My Library or a group you don't have access to or if you they were deleted from your Zotero library.

## Bibliography

Clicking the “Add/Edit Bibliography” (![zotero-toolbar-word-add-edit-bibliography-5.png](/_media/word_integration/zotero-toolbar-word-add-edit-bibliography-5.png){ width=16 }) button inserts a bibliography at the cursor location.

You can edit which items appear in the bibliography by clicking the “Add/Edit Bibliography” button again, which will open the bibliography editor. See [below](#editing_the_bibliography). Manual edits made to the bibliography in LibreOffice will be overwritten the next time Zotero refreshes the document.

## Document Preferences

![document-preferences-5-0.png](/_media/word_integration/document-preferences-5-0.png){ .align-right width=370 }

The "Document Preferences" window lets you set the following document-specific preferences:

1.  The [citation style](styles).
2.  The language to use to format citations and bibliography.
3.  For note-based styles (e.g., "Chicago Manual of Style (Note)"), whether citations are inserted in footnotes or endnotes.
    -   Note that Word, not Zotero, controls the style and format of footnotes and endnotes.
4.  Whether to store citations as **ReferenceMarks** or **Bookmarks**.
    -   Unless you need to collaborate with colleagues using Word, you should always choose ReferenceMarks.
5.  For styles that abbreviate journal titles (e.g., "Nature"), whether to use the **MEDLINE** abbreviations list to abbreviate titles.
    -   If this option is selected (the default), the contents of the "Journal Abbr" field in Zotero will be ignored.

<div style="clear: both;"></div>

## Customizing Cites

Citations can be customized in various ways.

If a citation is simply incorrect or missing data, start by making sure that the item metadata in Zotero is correct and complete, and then click Refresh in the plugin to update your document with any changes.

Other customizations can be made via the citation dialog. Click an existing citation in your document and click Add/Edit Citation to open the citation dialog, and then click the citation bubble to open the cite options window, where you can make the following changes.

##### Page and Other Locators

![citation-dialog-affixes-5.png](/_media/word_integration/citation-dialog-affixes-5.png){ .align-right width=350 }

In some cases you want to cite a certain part of an item, e.g. a certain page, page range or volume. This additional cite-specific information (e.g. "pp. 4-7" in the cite "Doe et al. 2001, p. 4-7") is called the "locator".

The cite options windows has a drop-down list of the different locator types ("Page" is the default), and a text box in which you can enter the locator value (e.g. "4-7"). To cite a locator other than the ones listed (e.g., "Table), use the Suffix field.

You can also add page numbers from the keyboard as you insert citations. Search for an item, press Enter once to add to the citing dialog, and then, before pressing Enter again to insert it into the document, simply type "p.34" or similar, and the page number will be added to the citation.

##### Prefix and Suffix

The "Prefix" and "Suffix" text boxes allow you to specify text to respectively precede and follow the automatically generated cite. For example, instead of "Tribe 1999", you might want "cf. Tribe 1999, see also…".

Any text in the prefix and suffix fields can be formatted with the HTML tags `<i>` (for italics), `<b>` (bold), `<sub>` (subscript), and `<sup>` (superscript). For example, typing "`<i>`cf`</i>`. the classic example" will be displayed as "*cf*. the classic example".

Prefixes and suffixes can be applied to each item in a citation to create complex citations. For example: "(see Smith 1776 for the classic example; Marx 1867 presents and alternate view)". Modifying citations by entering text into the Prefix and Suffix fields is always preferable to directly typing in the citation fields in LibreOffice. Manual modifications will prevent Zotero from automatically updating the citation.

##### Omitting Authors: Using Authors in the Text

With author-date styles, authors are often moved into the text and omitted from the following parentheses-enclosed citation, e.g.: "...according to Smith (1776) the division of labor is crucial...". To omit the authors from the cite, check the "Omit Author" box (this will result in a cite like "(1776)" instead of "(Smith, 1776)") and write the author's name ("Smith") as part of the regular text in your document.

#### Citations with Multiple Cited Items

![citation-dialog-select-multiple-5.png](/_media/word_integration/citation-dialog-select-multiple-5.png){ .align-right width=300 }

To create a citation containing multiple cites (e.g., "[2,4-6]" for numeric styles or "(Smith 1776, Schumpeter 1962)" for author-date styles), add them one after the other in the Add Citation box. After selecting the first item, don't press Enter/Return, but type the author, title, or year of the next item.

![citation-dialog-options-5.png](/_media/word_integration/citation-dialog-options-5.png){ .align-right width=300 }

Some citation styles require that items within one in-text citations are ordered either alphabetically (e.g., "(Doe 2000, Grey 1994, Smith 2008)") or chronologically ("(Grey 1994, Doe 2000, Smith 2008)"). Zotero will follow these sort rules automatically.

-   To disable automatic sorting of the cites in the citation, drag the citations to rearrange them in the Add Citation box. You can also click the "Z" icon on the left side of the Add Citation box and uncheck the "Keep Sources Sorted" option. *This option only appears for citation styles that specify a sort order for citations.* To restore automatic sorting, re-check the "Keep Sources Sorted" option.

#### Switching to the "Classic View"

You can switch to the ["Classic View"](word_processor_plugin_usage_classic) citation dialog by clicking the "Z" icon on the left side of the Add Citation box, and selecting "Classic View". To permanently switch to the classic view check the "Use classic Add Citation view" checkbox in the [Cite](preferences/cite) pane of Zotero [preferences](preferences).

## Editing the Bibliography

After you've inserted the bibliography using the “Add/Edit Bibliography” (![zotero-toolbar-word-add-edit-bibliography-5.png](/_media/word_integration/zotero-toolbar-word-add-edit-bibliography-5.png){ width=16 }) button, click the button again to open the Edit Bibliography window.

![](/_media/word_processor_edit_bibliography.png){ .align-right width=700 }

In this window, you can add uncited sources to your bibliography (e.g., items included in a review but not cited in the paper) or remove items that are cited in text but which should not be included in the bibliography (e.g., personal communications).

While it is also possible to edit the text or formatting of bibliography references in this window, doing so is discouraged. References edited here will not be automatically updated by Zotero if you change the data in your library. Editing references here is also somewhat unreliable; several users have reported that modifications made here sometimes do not persist when Zotero references, among other issues.

If you need to edit items in your bibliography, it is best to do this as a final step before submitting the document. First, save a backup copy of the document. Then, click the "Unlink Citations" button (![zotero-toolbar-word-unlink-citations-5.png](/_media/word_integration/zotero-toolbar-word-unlink-citations-5.png){ width=18 }) to disconnect your document from Zotero and convert all citations and the bibliography to regular text. Finally, make your adjustments to the bibliography text.

This process can be used for a variety of minor modifications to the bibliography, including:

-   Adding asterisks \* before references included in a review or meta-analysis
-   Setting the names of particular authors in bold, italics, or all caps
-   Adding annotations or comments about an item
-   Adding headings for bibliography subsections (e.g., primary versus secondary sources)

**Note:** General corrections to style formatting should be made in the [CSL Citation Style](styles), not here. Corrections to item data should be made in your Zotero library, not here.

## Keyboard Commands

The Zotero LibreOffice plugin can be used with just the keyboard for improved accessibility and faster use.

-   [Keyboard shortcuts](word_processor_plugin_shortcuts#libreoffice) can be set up for all the buttons in the Zotero tab.
-   In the Citation dialog
    -   Use the up and down arrow keys to move between search results. Press Enter to select an item.
    -   Type "p.45-48" or ":45-48" after a citation to cite a specific page or page range.
    -   Type "ibid" to automatically select the last cited work. This works with all citation styles, regardless of whether "ibid" is actually used in citations. If you use Zotero in a language other than English, use the corresponding abbreviation instead of ibid., e.g. "ebd." in German.
    -   Press Ctrl/Cmd-↓ (down arrow key) to open the cite options dialog for the citation selected with the cursor. Use Tab and Shift-Tab to move between the different elements, use the up and down arrow keys to change the locator type in the locator drop-down list, and the space bar to toggle the "Suppress Author" checkbox.

## Troubleshooting

If you run into problems while trying to use the Zotero LibreOffice plugin, make sure to check out the [word processor plugin troubleshooting](word_processor_plugin_troubleshooting) page.
