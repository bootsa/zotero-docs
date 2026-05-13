# Changes in Zotero 3.0

## Changes to translators

### Zotero.done() and Zotero.wait() are deprecated

Calling `Zotero.done()` and `Zotero.wait()` during translation is no longer necessary. `Zotero.done()` is still used to indicate item type in translators that implement asynchronous detection (currently only unAPI).

### Customizable attachment export

When the `exportFileData` option is specified and selected, attachments are no longer saved automatically. Instead, you should call the `attachment.saveItem(relativePath, overwriteExisting)` method to save attachments. `relativePath` is the path to the attachment relative to the folder in which the metadata file resides; if intermediate directories do not exist, they are created automatically. `overwriteExisting` determines whether existing attachments are automatically overwritten; if false, a `ERROR_FILE_EXISTS` error will be thrown.

### ZU.removeDiacritics()

`Zotero.Utilities.removeDiacritics(str, lowercaseOnly)` removes diacritics from a string, returning the result. The second argument is an optimization that specifies that only lowercase diacritics should be replaced.

### ZoteroItemUpdated event

Sites can now fire the `ZoteroItemUpdated` event to force Zotero to re-run detection after new data is loaded asynchronously ([example code](dev/exposing_metadata#using_an_open_standard_for_exposing_metadata)).

### Modifying translators to run in the Zotero Connectors

Zotero Connectors now allow translators to operate outside of Firefox/XULRunner. Legacy translators can still run inside Zotero Standalone, but will require that Zotero Standalone is running to operate. In order to run in the Zotero Connectors, translators must conform to the following rules.

#### No Firefox-specific JavaScript

Firefox-specific JavaScript, with the exception of "for each", must be avoided. This includes

-   array comprehensions
-   destructuring assignment
-   several other features

#### E4X unavailable

E4X functionality is not available. As of Zotero 2.1b6, Zotero also offers DOM XML interfaces to translators. Current trunk builds offer cross-browser utility functions for working with XPaths detailed above, which greatly simplify migration away from E4X.

#### retrieveSource() and retrieveDocument() are unavailable

Zotero.Utilities.retrieveDocument() and Zotero.Utilities.retrieveSource() should be avoided. Zotero.Utilities.retrieveDocument() will throw an error outside of Firefox, whereas Zotero.Utilities.retrieveSource() will freeze the main thread and will not work across domains. Code should be rewritten to use Zotero.Utilities.processDocuments(), Zotero.Utilities.HTTP.doGet(), or Zotero.Utilities.HTTP.doPost(), which remain available in all environments.

#### getTranslatorObject() must be called with a callback

Translate#getTranslatorObject() should now be called with a callback function as an argument, which will receive the translator object when it is available. This is backwards compatible with Zotero 2.1b6 and later.

#### Translators that export objects via getTranslatorObject() must define exported objects explicitly

In Chrome and Safari, the "exports" object is exposed to other translators, rather than the entire translator sandbox. Any variables or functions that need to be accessible to other translators should be properties or methods of this object. In Zotero 2.1.9 and later, Translate#getTranslatorObject() will always return the "exports" object if it has properties.

#### getTranslators() does not return

Translators should not expect a return value from Translate#getTranslators(). Instead, they should register a "translators" handler, which will receive the list of translators as the second argument. This is backwards compatible with Zotero 1.0 and later.

#### selectItems() should be called with a callback

Zotero.selectItems() should now be called with a callback function as an argument, which will receive the list of selected items when it is available. Translators may still use Zotero.selectItems() synchronously, but this will require that the first part of the translator be executed twice. This is backwards compatible with Zotero 2.1b6 and later.

## Translator testing framework

Zotero 3.0 contains a translator testing framework, used by Scaffold 3.0. You can also run available translator tests in batch mode by accessing the translator tester page. In Firefox, this page is available in the standard extension at:

    chrome://zotero/content/tools/testTranslators/testTranslators.html

In Chrome and Safari, the translator tester is accessible from the Advanced pane of the preferences in [connector debug builds](dev_builds#connector_debug_builds).

## Add-on support in Zotero Standalone

It is possible to create add-ons for Zotero Standalone just as one would create add-ons for Firefox. To do so, create a Firefox extension, but add the following lines to install.rdf:

``` xml
    <em:targetApplication>
        <Description>
            <em:id>zotero@chnm.gmu.edu</em:id>
            <em:minVersion>3.0b1</em:minVersion>
            <em:maxVersion>3.0.*</em:maxVersion>
        </Description>
    </em:targetApplication>
```

where minVersion is the lowest Zotero Standalone version you have tested with, and maxVersion is the maximum version you can reasonably expect your add-on to work with. For add-ons that overlay [zoteroPane.xul](dev/client_coding/changes_in_zotero_2.1#changes_to_interface_related_code), this addition should be sufficient, and the same XPI should work in both Firefox and Zotero Standalone. If your add-on overlays browser.xul, you should change it to overlay zoteroPane.xul.

Calls to `window.loadURI()` will not work in Zotero Standalone. However, you can use `ZoteroPane.loadURI()` to load a URI in the default browser, or `ZoteroStandalone.openInViewer()` to open a page in Zotero Standalone.

To install an add-on in Zotero Standalone, go to Tools->Add-ons and choose "Install Add-on From File..." from the cog menu.

## Miscellaneous changes

### Zotero.Translate itemSaving handler

Zotero.Translate now fires both `itemSaving` and `itemDone` handlers.

The `itemSaving` handler is called as soon as the translator returns an item, but before it's saved to the database. It is passed the item object returned by the translator as the second argument.

The `itemDone` handler is called after the item is saved. When not operating in connector mode, it is passed the DB item as its second argument and the item object returned by the translator as its third. When operating in connector mode, or when `false` is passed to `Zotero.Translate#translate` is passed the item object returned by the translator as both arguments.

### getNotes(), getAttachments, and getTags() return empty arrays

Zotero.Item.getNotes(), Zotero.Item.getAttachments(), and Zotero.Item.getTags() now return empty arrays rather than FALSE if no matches
