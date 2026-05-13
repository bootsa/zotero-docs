# Changes in Zotero 2.1

## Changes to citation API

With the introduction of citeproc-js, all Zotero.CSL APIs have been removed. Styles can be loaded in the usual way by accessing Zotero.Styles, but
developers should use Zotero.Style.csl to acquire a citeproc-js engine instance for citation formatting. `Zotero.Cite.makeFormattedBibliography(engine, format)` can be used to generate a fully-formatted bibliography.

## Changes to interface-related code

Zotero as a tab and Zotero Standalone have required us to further abstract the interface layer. While the code for the interface has changed little, and most overlays should continue to work, as of the present Zotero trunk, plug-ins and add-ons should now overlay zoteroPane.xul instead of browser.xul or overlay.xul in chrome.manifest, e.g., using:

    overlay   chrome://zotero/content/zoteroPane.xul  chrome://zotero-addon/content/overlay.xul

## Changes to translators

### Deprecated functions eliminated

Several functions in Zotero.Utilities have been eliminated, as they were essential duplications of built-in JavaScript methods. References to these functions were removed from all translators in the repository

### Zotero.configure() and Zotero.displayOptions() replaced by configOptions and displayOptions

Zotero.configure() and Zotero.displayOptions() no longer exist. Instead, translators should specify config and display options in the metadata block at the top of the translator, e.g. `{
    "translatorID":"32d59d2d-b65a-4da4-b0a3-bdd3cfb979e7",
    [...]
    "configOptions":{"dataMode":"rdf/xml"},
    "displayOptions":{"exportNotes":true},
    "lastUpdated":"2011-01-11 04:31:00"
}`

### "dataMode":"block" and "dataMode":"line" are deprecated

It is no longer necessary to specify "dataMode":"block" or "dataMode":"line". If Zotero.read() is passed a numeric value, it reads a specified number of bytes; otherwise, it reads a full line.

### Indicating translation progress

Import and export translators now show determinate progress bars. By default, Zotero computes progress by the percentage of the file read for import, or the percentage of items retrieved using Zotero.nextItem() for export. Translators can override this by calling Zotero.setProgress(percentage) to set the percentage the progress bar displays, or Zotero.setProgress(null) to show an indeterminate indicator.

## Changes to translate interface

New code should create new instances of the translate interface using type-specific constructors, e.g., to create a web translator:

    new Zotero.Translate.Web();

## Locate Engines

Zotero 2.1b6 and later support extensible locate engines. For further details, see [Creating Locate Engines using OpenSearch](dev/creating_locate_engines_using_opensearch).

## Shorthand syntax

Z is now a shortcut for Zotero in translators, and ZU is a shortcut for Zotero.Utilities.

## XPath utility functions

-   `Zotero.Utilities.xpath(element, xpath[, namespaces])` Accepts a DOM element, document, or array of elements or documents and evaluates an XPath, optionally interpreting namespace prefixes using a object whose keys correspond to namespace prefixes and whose values correspond to namespace URIs. The result is an array of nodes matching the XPath.
-   `Zotero.Utilities.xpathText(element, xpath[, namespaces[, delimiter]])` Behaves similarly to Zotero.Utilities.xpath, but the result is the textContent of all matching nodes, joined by a delimiter if more than one node matched. If no delimiter is specified, ", " is used.
