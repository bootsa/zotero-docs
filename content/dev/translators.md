# Zotero Translators

Translators are at the core of one of Zotero’s most popular features: its ability to add items from across the web using the Connector, and to import and export item metadata in a variety of formats. Below we describe how translators work, and how you can write your own.

This page describes the function and structure of translators. For in-depth documentation on how to write translator code, see [Coding](dev/translators/coding).

**Note:** Before writing a translator for a site, look at the [documentation on exposing metadata](dev/exposing_metadata); website authors should try embedding the necessary metadata before attempting to write a translator.

If you're looking for a broken translator to fix, see the [recent translator errors](https://zotero-translator-tests.s3.amazonaws.com/index.html) and check on one of the top reported errors. You can also check the status of many translators by reviewing the [translator test overview](dev/translators/testing#running_tests).

## Translator Types - Web, Import, Export and Search

Zotero supports four different types of translators:

-   **[Web translators](dev/translators/coding#web_translators)**: used to save items from websites. The Zotero Connector primarily uses web translators to detect and save items from sites across the web.
-   **[Import translators](dev/translators/coding#import_translators)**: can import item metadata from one of the standard storage formats, such as BibTeX or RIS, into your Zotero library. An import translator may be run directly by Zotero using data from a file or the operating system clipboard. It may also be called by another translator. For example, a web translator that targets a library's website might download the MARCXML representation of a book, call the MARCXML translator to parse it into an item, then apply some custom site-specific tweaks before returning it to Zotero.
-   **[Export translators](dev/translators/coding#export_translators)**: can export item metadata from items in your Zotero library to a file in one of the standard storage formats (like BibTeX or RIS).
-   **[Search translators](dev/translators/coding#search_translators)**: can look up and retrieve item metadata when supplied with a standard identifier, like a PubMed ID (PMID) or DOI.

A single translator can have multiple types. For example, many import translators are also export translators (like RIS). Most web translators should just be web translators, but some translators for sites with widely-used identifier formats, like arXiv, are also search translators.

## Translator Structure

During development, you should fork the [Zotero Translators GitHub repository](https://github.com/zotero/translators) and clone it to disk (see [Contributing Translators](#contributing_translators)). [Scaffold](dev/translators/scaffold) will prompt you for the folder you cloned it into.

* Zotero automatically keeps the “translators” subdirectory of the [Zotero data directory](zotero_data#locating_your_zotero_library) up to date with the central repository. You generally should not touch the files in that directory. *

Zotero translators are stored as individual JavaScript files. On disk, they have three sections:

-   A JSON object containing metadata
-   A JavaScript body, which must include certain top-level functions, as determined by the translator type(s)
-   `var testCases =`, followed by a JSON array containing test cases

[Scaffold](dev/translators/scaffold) manages the metadata object and test case array for you, and provides a template for a web translator body. Even if you don't use Scaffold all the time when editing, you should still use it whenever you want to create a new translator, edit metadata, or add/run/update test cases.

### Metadata

![](/_media/dev/wapo.png){ width=600 }

The roles of the different metadata fields are:

-   **Translator ID** (`translatorID`)  
    The unique internal ID by which Zotero identifies the translator. You must use a stable [GUID](http://en.wikipedia.org/wiki/Globally_Unique_Identifier), as the translator ID is used for automatic updating of translators, and for calling translators within other translators. Click "Generate" to create a new GUID (for instance, when making a copy of an existing translator).
-   **Label** (`label`)  
    The name of the translator.
-   **Creator** (`creator`)  
    The author(s) of the translator.
-   **Target** (`target`)
    -   For [web translators](dev/translators/coding#web_translators), the target should specify a [JavaScript regular expression](https://www.zotero.org/support/dev/translators), e.g. `^https?://(www\.)?example.com/`.  
        When only matching a domain, the translator should terminate in a forward slash, so it only matches a non-proxied domain. Zotero will take care of de-proxifying the URL and pass the de-proxified URL to the translator.  
        Whenever a webpage is loaded, Zotero tests the target regular expressions of all web translators on the webpage URL. If there is a translator with a matching target, this translator’s `detectWeb` function is run. If this function finds item metadata, the Zotero translator icon appears or becomes active in the browser. When multiple translators have a matching target, the translator with the lowest priority number is selected. Web translators with an empty `target` string (e.g. the DOI translator) match every webpage, but normally have a high priority number and are only used when no other translator matches.
    -   For import translators, the target is set to the expected extension (e.g. the BibTeX import/export translator has its target set to "bib"; selecting BibTex in Zotero’s import window filters for files with a ".bib" extension).
    -   For export translators, the target is set to the extension that should be given to generated files (e.g. the BibTeX translator produces "filename.bib" files).
-   **Config Options** (`configOptions`)  
    An optional JSON object. Most translators will leave this blank. Certain import/export translators use this to customize the behavior of the Zotero translation framework — see `RIS.js` and `Note HTML.js`. Supported options include:
    -   **dataMode**  
        For [import translators](dev/translators/coding#import_translators), this sets the form in which the input data is presented to the translator. If set to "rdf/xml", Zotero will parse the input as XML and expose the data through the `Zotero.RDF` object. If "xml/dom", Zotero will expose the data through the function `Zotero.getXML()`. Zotero does not natively support importing N3 representations of RDF.
    -   **getCollections**  
        For [export translators](dev/translators/coding#export_translators), set to `true` or `false`. If `true`, an export translator will have access to the collection names and can recreate them in the exported file.
-   **Display Options** (`displayOptions`)  
    An optional JSON object. Most translators will leave this blank. Certain export translators use this to allow the user to set options when exporting — see `RIS.js` and `BibTeX.js`. Supported options include:
    -   **exportCharset**  
        The default character set to use for export, defaults to "UTF-8"
    -   **exportFileData**, **exportNotes** and **exportTags**  
        For each property that is set, a checkbox (respectively "Export Files", "Export Notes" and "Export Tags") is added to Zotero's export window, allowing files, notes and/or tags to be exported. A checkbox is checked by default if the corresponding property is set to `true`, and unchecked if the property is set to `false`.
-   **Min. Version** (`minVersion`)  
    The minimum Zotero version that the translator supports. This usually does not need to be changed.
-   **Priority** (`priority`)  
    An integer indicating translator priority. When multiple translators can translate a source, the translator with the lowest priority number is selected. Site-specific web translators normally have a priority of 100. Web translators that match multiple sites must have a priority higher than 100. For guidelines on picking an appropriate priority for web translators, see [this page](dev/translators/priority).
-   **Translator Type** (`translatorType`)  
    In the JSON object, this is represented as as integer. The value is the sum of the values assigned to each type: import (1), export (2), web (4) and search (8). E.g. the value of `translatorType` is 2 for an export translator, and 13 for a search/web/import translator, because 13=8+4+1.
-   **`lastUpdated`**  
    This field is updated automatically when you save a translator in Scaffold. If you're working on a translator manually in a text editor, you'll need to update this to the current UTC datetime before submitting a pull request.

### Top-level Functions

Depending on the translator type, each Zotero translator must include certain top-level JavaScript functions:

-   **[Web translators](dev/translators/coding#web_translators)**
    -   *detectWeb*  
        After a web translator has been selected based by its matching target and its priority ranking, `detectWeb` is run to determine whether item metadata can indeed be retrieved from the webpage. Should return the detected item type (e.g. "journalArticle", see the [overview of Zotero item types](https://aurimasv.github.io/z2csl/typeMap.xml)), or, if multiple items are found, "multiple". If `detectWeb` returns false, the translator with the next-highest priority is selected, until all translators with a matching target have been exhausted.
    -   *doWeb*  
        Performs the actual item metadata retrieval.
-   **[Import translators](dev/translators/coding#import_translators)**
    -   *detectImport*  
        Determines whether the translator can import item metadata. Should return `true` if it can, and `false` if it cannot.
    -   *doImport*  
        Performs the actual import.
-   **[Export translators](dev/translators/coding#export_translators)**
    -   *doExport*  
        Performs the export.
-   **[Search translators](dev/translators/coding#search_translators)**
    -   *detectSearch*  
        Determines whether the translator can look up item metadata. Should return `true` if it can, and `false` if it cannot.
    -   *doSearch*  
        Performs the actual lookup.

See [Translator Coding](dev/translators/coding) for a detailed description on how these functions can be coded.

## Tools

The following tools can make coding Zotero translators easier:

-   [Scaffold](dev/translators/scaffold) - Scaffold is an IDE for translators built into Zotero (Tools -> Developer -> Translator Editor). Translators can be quickly [tested](dev/translators/testing) and debugged, and item saving is simulated, so no changes are made to your Zotero library.
-   Browser inspector - Web translators generally use [querySelector](https://developer.mozilla.org/en-US/docs/Web/API/Document/querySelector) and [querySelectorAll](https://developer.mozilla.org/en-US/docs/Web/API/Document/querySelectorAll) (as well as Zotero's wrapper functions, `attr`, `text`, and `innerText`) to extract content from web pages. Your browser likely provides an inspector tool to help you understand pages' structure. You can access it by right-clicking and selecting Inspect (Firefox) or Inspect Element (Chrome).
-   XPath Tools - Many older web translators rely on XPath to extract information from HTML or XML. Various tools can assist with generating and checking XPath expressions, including the DevTools built into browsers. For example, in Firefox, you can get the XPath for any element by finding it in the browser's Inspector tool, right-clicking on the element, and choosing Copy -> XPath. New/revamped translators should avoid XPaths.

## Running Translators

It's generally easiest to develop and test-run your translators within Scaffold, using the Browser tab (web translators), Test Input tab (import/search translators), or selecting an item in Zotero's main window (export translators) to provide input. You can also add automated tests for web, import, and search translators in the corresponding input tabs. Adding tests is highly recommended: real-world translator input is highly complex, and it's easy to break one thing in the process of trying to fix another.

If you want to run your translator outside of Scaffold using real items, click ![](/_media/dev/save_to_zotero.png){ width=20 } Save to Zotero in the Scaffold toolbar. For web translator development, you'll also need to sync your changes to the Connector: open Connector settings, go to Advanced, and click "Reset Translators."

## Contributing Translators

If you created or modified a translator and wish to have it added to Zotero, or are looking for support on writing translators, please submit a pull request to the [Zotero Translators GitHub repo](https://github.com/zotero/translators/). You can also ask questions about translator development on [Zotero development mailing list](http://groups.google.com/group/zotero-dev).

To submit a pull request, fork the repo, commit your changes (i.e., adding or modifying translator files), and create a [pull request](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-pull-requests). You can use your Git client of choice. Most editors should have some built-in support for making Git commits and pushing branches.

If you have the [GitHub CLI](https://cli.github.com/) installed, simply run `gh repo fork zotero/translators --clone` to fork and clone the repository in a single step.

When you submit a pull request on GitHub, your translator code will be reviewed, and you will receive comments from the Zotero developers or experienced volunteers. Once you've made any necessary changes, your translator will be added to the Zotero translator repository.

### Licensing

Please note that contributed translators need to be licensed in a way that allows the Zotero project to distribute them and modify them. We encourage you to license new translators under the [GNU Affero General Public License version 3](http://www.gnu.org/licenses/agpl.html) (or later), which is the license used for Zotero. To do so, just add a license statement to the top of the file. Take a look a recently committed translator, like "Die Zeit.js", for an example of such a statement. (Scaffold handles this automatically when you add the web translator template.)

## Recommendations for Translator Authors

While there are no strict coding guidelines for translators, there are some general recommendations:

1.  Web translator detect targets should be selective, to minimize the number of `detectWeb` functions that are run for each page.
2.  `detectWeb`, `detectImport` and `detectSearch` should be coded to minimize the likelihood of the corresponding `doWeb`, etc. function failing. Do your minimum required input checking the detect functions -- a failing `do` function will cause user-visible errors.
3.  Make detect functions lightweight-- they may be run on pages that a user is not even considering saving. Detect functions should not need to make additional HTTP requests. This obviously runs counter to the preceding point-- find a happy medium.
4.  When translating the web page in the browser, do not modify any part of its DOM. DOM modification is no longer possible in Chrome and may be removed in other browser in the future. There's almost always a better way: If you want to emulate the effect of clicking a Download Citation button, for example, use your browser's network inspector to see what HTTP requests the page makes after you click on it. You should be able to build the same requests using the `request` utility.
5.  Minimize HTTP requests. More HTTP requests slow down the user, cause undue load on servers, risk getting the user rate-limited or blocked, and in general are bad.
6.  Don't leak user data. HTTP requests should in general not be directed to 3rd-party hosts.
7.  Document your code. If there are input data deficiencies and the translator is working around them, document the deficiencies. If there are specific types of pages that a web translator is for, add [test cases](dev/translators/testing) that cover the different types.
8.  Run ESLint on your code before submitting it. To make sure ESLint is installed, run`npm ci` within your clone of the `zotero/translators` repository. Scaffold runs ESLint continuously. To manually lint a translator, run `npm run lint -- "Translator Filename.js"`.

## Further Reading

**Continue to [Coding](dev/translators/coding)** for more information on translator development.
