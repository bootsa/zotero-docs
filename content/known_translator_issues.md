# Known Translator Issues

Zotero uses "translators" to allow you to save items from the websites you visit. When you get the "An error occurred while saving this item" message while trying to save an item, first check the list of known translator issues below. If the translator you've been using is already listed, you don't need to take any action (unless you have some programming experience and want to help [fix the translator](dev/translators)). Otherwise, try going through the steps for [troubleshooting translator issues](troubleshooting_translator_issues).

You can see which translator Zotero tries to use by hovering your cursor over the "Save to Zotero" icon in the address bar of your browser. The tooltip shows the translator name between parentheses.

## Translators with Major Issues

-   ASCE
    -   Currently completely broken.
-   DOI
    -   The DOI translator is a translator that scans webpages for [DOIs](http://www.doi.org/), and collects the item metadata by using Crossref's [DOI lookup service](http://www.crossref.org/guestquery/). If the DOI translator gives an error, either the translator mistook something on the webpage for a DOI, or Crossref doesn't (yet) have any item metadata available for the DOI.
-   EBSCO
    -   Doesn't work for items in "My Folder".
-   JSTOR
    -   Only saves PDFs after manually clicking "OK" to the terms and conditions once in the session. Workaround: Manually download one PDF during each session; all subsequent ones should work fine.
-   Old Baileys
    -   Frequently fails silently, due to an issue with google ads. Works reliably with an ad-blocker add-on enabled. See [this thread](http://forums.zotero.org/discussion/20488/old-bailey-court-cases-not-downloading/) for developments
-   Google Scholar
        * Google Scholar will lock you out to protect its data against automated downloads when you use its service a lot (which may be as quickly as saving three pages of results). See [[ adding_items_to_zotero#large-scale_imports_from_databases|here for a workaround]] for large downloads

## Translators with Minor Issues

-   Proquest
    -   When downloading large amounts of articles from search results, ProQuest starts to require users to input a captcha to continue to articles. Once that point is reached, grabbing items from search results is no longer possible with Zotero. Individual items will continue to work.
