## Zotero Style Editor

*This window is also called the Zotero Reference Test Pane, Zotero CSL Editor, or csledit.xul.*

The Zotero Style Editor is a tool to edit CSL styles. It can be opened using the "Style Editor" button at the bottom of the [Cite pane](preferences/cite) of the Zotero preferences.

![](/_media/preferences_cite_csl_editor.png){ .align-right width=800 }

The Style Editor provides instant processing of a CSL style, using items selected in your local Zotero library. The Style Editor Window is divided into two parts. The upper portion of the window shows the CSL style code. You can load an installed style by selecting it from the dropdown menu in the upper-right corner. You can also paste CSL style code from your clipboard. The lower portion of the Style Editor window shows formatted citations and bibliography references for the style you are editing. Choose items to format by selecting one or more items in your local Zotero library and clicking the "Refresh" button.

You can preview the style's behavior for several types of citation modifications. A locator (page number, chapter, verse, etc.) can be specified using the pull-down menu and adjoining text-box on the left of the toolbar (e.g., to obtain "(Doe 2002, p.52)"). The "Omit Author" option can be checked (so that a "(Doe 2002)" citation gets rendered as "(2002)"). Finally, the position of the cites can be changed, so it is possible to see how cites to previously cited items are rendered (e.g., if a citation should be rendered as "(Doe, Jones, & Smith, 2002)" the first time, but "(Doe et al., 2002)" subsequently). You can also change the language of the formatted citations and bibliography.

As you edit the CSL code in the upper window, the citations and bibliographic entries in the lower window are automatically updated. The test pane shows an error if the CSL code is invalid XML. If the code is valid XML but invalid CSL, you may see an error, or the preview in the lower window will stop updating. After editing a style, always [validate](https://github.com/citation-style-language/styles/wiki/Validation) your style.

**Important** When you close the test pane, or select a style from the pull-down menu, any edits will be lost. If you are making extensive changes to a CSL style, save your edited code often.
