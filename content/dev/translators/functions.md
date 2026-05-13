<p id="zotero-5-update-warning" style="color: red; font-weight: bold">We’re
in the process of updating the documentation for
<a href="https://www.zotero.org/blog/zotero-5-0">Zotero 5.0</a>. Some documentation
may be outdated in the meantime. Thanks for your understanding.</p>

# Functions and objects in the translator sandbox

This is a list of the functions and objects exposed to translators running in the sandbox. As it was generated from the existing translators, this list is probably not complete, and some of the functions may be deprecated or unavailable in certain types of translators. Most of the below are described in the general [Translator Coding documentation](dev/translators/coding), or the [Translator overview](dev/translators). Others are rarely used-- search in the code of existing translators for usage guidance.

#### Objects

-   Zotero.Collection
-   Zotero.Item

#### Functions

-   Zotero.debug
-   ~~Zotero.done~~ [DEPRECATED since 3.0](dev/client_coding/changes_in_zotero_3.0#zoterodone_and_zoterowait_are_deprecated)
-   Zotero.getOption
-   Zotero.getXML
-   Zotero.loadTranslator
-   Zotero.monitorDOMChanges [NEW since 4.0](https://www.zotero.org/support/4.0_changelog#developer-specific_changesfixes12)
-   Zotero.nextCollection
-   Zotero.nextItem
-   Zotero.read
-   Zotero.selectItems
-   Zotero.setCharacterSet
-   Zotero.setProgress
-   ~~Zotero.wait~~ [DEPRECATED since 3.0](dev/client_coding/changes_in_zotero_3.0#zoterodone_and_zoterowait_are_deprecated)
-   Zotero.write

#### Utility functions

-   Zotero.Utilities.capitalizeTitle
-   Zotero.Utilities.cleanAuthor
-   Zotero.Utilities.cleanTags
-   Zotero.Utilities.createContextObject
-   Zotero.Utilities.doGet
-   Zotero.Utilities.doPost
-   Zotero.Utilities.formatDate
-   Zotero.Utilities.gatherElementsOnXPath
-   Zotero.Utilities.getCreatorsForType
-   Zotero.Utilities.getItemArray
-   Zotero.Utilities.getLocalizedCreatorType
-   Zotero.Utilities.getPageRange
-   Zotero.Utilities.getVersion
-   Zotero.Utilities.htmlSpecialChars
-   Zotero.Utilities.HTTP.doGet
-   Zotero.Utilities.HTTP.doPost
-   Zotero.Utilities.itemTypeExists
-   Zotero.Utilities.loadDocument
-   Zotero.Utilities.lpad
-   Zotero.Utilities.parseContextObject
-   Zotero.Utilities.processAsync
-   Zotero.Utilities.processDocuments
-   Zotero.Utilities.removeDiacritics [NEW since 3.0](dev/client_coding/changes_in_zotero_3.0#zuremovediacritics)
-   ~~Zotero.Utilities.retrieveDocument~~ [unavailable since 3.0](dev/client_coding/changes_in_zotero_3.0#retrievesource_and_retrievedocument_are_unavailable)
-   ~~Zotero.Utilities.retrieveSource~~ [unavailable since 3.0](dev/client_coding/changes_in_zotero_3.0#retrievesource_and_retrievedocument_are_unavailable)
-   Zotero.Utilities.strToDate
-   Zotero.Utilities.strToISO
-   Zotero.Utilities.superCleanString
-   Zotero.Utilities.text2html
-   ~~Zotero.Utilities.trim~~ DEPRECATED use ".trim()" instead
-   Zotero.Utilities.trimInternal
-   Zotero.Utilities.unescapeHTML
-   Zotero.Utilities.xpath [NEW since 2.1](dev/client_coding/changes_in_zotero_2.1#xpath_utility_functions)
-   Zotero.Utilities.xpathText [NEW since 2.1](dev/client_coding/changes_in_zotero_2.1#xpath_utility_functions)

The utility functions are defined in [utilities.js](https://github.com/zotero/zotero/blob/4.0/chrome/content/zotero/xpcom/utilities.js).

#### RDF functions

-   Zotero.RDF.addContainerElement
-   Zotero.RDF.addNamespace
-   Zotero.RDF.addStatement
-   Zotero.RDF.getAllResources
-   ~~Zotero.RDF.getArcsIn~~ DEPRECATED since 2.1, use Z.RDF.getStatementsMatching(undefined, undefined, .)
-   ~~Zotero.RDF.getArcsOut~~ DEPRECATED since 2.1, use Z.RDF.getStatementsMatching(., undefined, undefined)
-   Zotero.RDF.getContainerElements
-   Zotero.RDF.getResourceURI
-   ~~Zotero.RDF.getSources~~ DEPRECATED since 2.1, use Z.RDF.getStatementsMatching(undefined, ., .)
-   Zotero.RDF.getStatementsMatching
-   ~~Zotero.RDF.getTargets~~ DEPRECATED since 2.1, use Z.RDF.getStatementsMatching(., ., undefined)
-   Zotero.RDF.newContainer
-   Zotero.RDF.newResource

The RDF functions are defined in [translator.js](https://github.com/zotero/zotero/blob/4.0/chrome/content/zotero/xpcom/translation/translate.js).

#### XML objects

-   DOMParser
-   XML
