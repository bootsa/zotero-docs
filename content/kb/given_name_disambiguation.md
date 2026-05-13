---
tags:
  - kb
  - styles
---

## Why do some citations include first names or initials?

Sometimes you'll see Zotero produce citations like "(J. Doe, 2004)" even though your citation style normally only shows the author's last name ("Doe, 2004"). In these cases, Zotero is disambiguating different authors according to the rules of your selected citation style. This is generally what you want it to do, and if you think otherwise, you should carefully review your style's requirements. (APA style, for example, requires this sort of disambiguation when you cite different authors with the same last name.)

Disambiguation can also occur if a certain author is inconsistently named in your Zotero library. For example, Zotero treats the names

-   Jeff Smith
-   J. Smith
-   J. R. Smith

as distinct individuals and will disambiguate them according to the style rules. You can fix this by going through your library and changing all names that refer to the same person to the exact same form, which will allow Zotero to disambiguate authors correctly in this style and other styles you use in the future.

If you don't want to update the names in your library, you can also simply use a style that doesn't disambiguate names. A step-by-step guide to disable given name disambiguation in a CSL citation style can be found [here](dev/citation_styles/style_editing_step-by-step).

Zotero and CSL support [sophisticated disambiguation rules](http://citationstyles.org/downloads/specification.html#disambiguation). If you think citations are being disambiguated incorrectly, please post to the [Zotero Forums](/forum) and provide documentation in the form of a style guide or a published article in the publication in question. *Note that these changes do not address the issue of inconsistently named authors.*

### Other Causes

#### Deleted Items

If you've made sure that the author's name is formatted consistently in Zotero, one or more of your items may be pointing to an item that you've deleted from Zotero. When this happens, Zotero uses metadata embedded in the document instead. To check whether an item is still linked to your Zotero library, click on the citation, click Add/Edit Citation, click the blue bubble in the citation dialog (red bar, not classic), and look for an "Open in [Library]" button at the bottom of the popup. If the button doesn't appear, the citation is no longer linked to Zotero, and you will need to delete the citation and reinsert it, being sure to select from the appropriate library rather than the "Cited" section in the citation dialog search results.

If you're having trouble finding the relevant citations, it may help to [display Word field codes](kb/word_field_codes) and search for the title or author in the field code. Each citation's field code will include a `uris` field with a URL like `http://zotero.org/users/6/items/WDLWGFMA`. If two URLs don't match, those are pointing at different items. Follow the steps above to identify or reinsert a citation from your library and then make sure that all similar citations in the document match the URL from that citation.

#### Duplicate Items

If you have more than one copy of an item and cite both in separate places, Zotero will treat the authors as separate and disambiguate them in the text. Within the same library, you can fix this by merging the items in Zotero, either via the Duplicate Items view or by selecting the items in the main items list, right-clicking, and choosing "Merge Items…", and then clicking the plugin's Refresh button. If you’ve cited items from different libraries, use Add/Edit Citation as described in the previous section to identify the associated item for each citation and make sure each one is pointing to the same item in just one of the libraries.

#### Disabled Automatic Citation Updates

If you're seeing citations with dashed underlines, you've disabled [Automatic Citation Updates](/blog/zotero-5-0-36/#faster-citing-in-large-documents). You can either press Refresh to update citations manually or re-enable Automatic Citation Updates in the plugin's document preferences.


