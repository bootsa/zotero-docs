# Writing Translator Code

Below we will describe how the `detect*` and `do*` functions of Zotero [translators](dev/translators) can and should be coded. If you are unfamiliar with JavaScript, make sure to check out a [JavaScript tutorial](https://developer.mozilla.org/en/JavaScript/A_re-introduction_to_JavaScript) to get familiar with the syntax. In addition to the information on this page, it can often be very informative to look at existing translators to see how things are done. A [particularly helpful guide](https://www.mediawiki.org/wiki/Citoid/Creating_Zotero_translators) with up-to-date recommendation on best coding practices is provided by the Wikimedia Foundation, whose tool Citoid uses Zotero translators.

While translators can be written with any text editor, the built-in translator editor, [Scaffold](dev/translators/scaffold), can make writing them much easier, as it provides the option to test and troubleshoot translators relatively quickly.

New web translators should use Scaffold's web translator template as a starting point. The template can be inserted in the Code tab: click the green plus dropdown and choose "Web Translator".

# Web Translators

## detectWeb

`detectWeb` is run to determine whether item metadata can indeed be retrieved from the webpage. The return value of this function should be the detected item type (e.g. "journalArticle", see the [overview of Zotero item types](https://aurimasv.github.io/z2csl/typeMap.xml)), or, if multiple items are found, "multiple". If no item(s) can be detected on the current page, return false.

`detectWeb` receives two arguments: the webpage document object and URL (typically named `doc` and `url`). In some cases, the URL provides all the information needed to determine whether item metadata is available, allowing for a simple `detectWeb` function, e.g. (example from `Cell Press.js`):

``` javascript
function detectWeb(doc, url) {
  if (url.includes("search/results")) {
    return "multiple";
  }
  else if (url.includes("content/article")) {
    return "journalArticle";
  }
  return false;
}
```

## doWeb

`doWeb` is run when a user, wishing to save one or more items, activates the selected translator. It can be seen as the entry point of the translation process.

The signature of `doWeb` should be

``` javascript
function doWeb(doc, url)
```

or

``` javascript
async function doWeb(doc, url = doc.location.href)
```

Here `doc` refers to the DOM object of the web page that the user wants to save as a Zotero item, and `url` is the page's URL as a string.

In this section, we will describe the common tasks in the translation workflow started by `doWeb()`.

### Saving Single Items

#### Scraping for metadata

"Scraping" refers to the act of collecting information that can be used to populate Zotero item fields from the web page. Such information typically include the title, creators, permanent URL, and source of the work being saved (for example, the title/volume/pages of a journal).

Having identified what information to look for, you need to know where to look. The best way to do this is to use the web inspections tools that come with the browser ([Firefox](https://firefox-source-docs.mozilla.org/devtools-user/page_inspector/), [Chromium-based](https://developer.chrome.com/docs/devtools/dom/), and [Webkit/Safari](https://webkit.org/web-inspector/elements-tab/)). In most browsers, you can open the web inspector by right-clicking an element and choosing Inspect. That will take you right to the element you clicked in the tree.

To actually retrieve information from the nodes in your translator code, you should be familiar with the use of [selectors](https://developer.mozilla.org/en-US/docs/Web/API/Document_object_model/Locating_DOM_elements_using_selectors), in the way they are used with the JavaScript API function `querySelectorAll()`.

Most often, you will do the scraping using the helper functions `text()` and `attr()`, for retrieving text content and attribute value, respectively. In fact, these two actions are performed so often, that `text()` and `attr()` are available to the translator script as top-level functions.

``` javascript
function text(parentNode, selector[, index])
function attr(parentNode, selector, attributeName[, index])
```

-   `text()` finds the descendant of `parentNode` (which can also be a document) that matches `selector`, and returns the text content (i.e. the value of the `textContent` property) of the selected node, with leading and trailing whitespace trimmed. If the selector doesn't match, the empty string is returned.
-   `attr()` similarly uses the selector to locate a descendant node. However, it returns the value of the HTML attribute `attributeName` on that element. If the selector doesn't match, or if the there's no specified attribute on that element, the empty string is returned.

Optionally, a number `index` (zero-based) can be used to select a specific node when the selector matches multiple nodes. If the index is out of range, the return value of both functions will be the empty string.

Another less-used helper function, `innerText()`, has the same signature as `text()`, but it differs from the latter by returning the selected node's `innerText` value, which is affected by how the node's content would have been rendered.

In addition, you can always use the API functions `querySelector` and `querySelectorAll` directly, but the helper functions should be preferred when they are adequate for the job.

In some older translator code, you are likely to encounter node-selection expressed by XPath. Although XPath has its uses, for the most common types of scraping the selector-based functions should be preferred because of the simpler syntax of selectors.

#### Metadata

The first step towards saving an item is to create an item object of the desired [item type](https://aurimasv.github.io/z2csl/typeMap.xml) (examples from "NCBI PubMed.js"):

``` javascript
let item = new Zotero.Item('journalArticle');
```

Metadata can then be stored in the properties of the object. Of the different fields available for the chosen item type (see the [Field Index](https://aurimasv.github.io/z2csl/typeMap.xml)), only the title is required. E.g.:

``` javascript
let title = text(doc, 'h1.title');
item.title = title;
let pmid = text(doc, '#pmid');
item.url = 'https://www.ncbi.nlm.nih.gov/pubmed/' + pmid;
```

After all metadata has been stored in the item object, the item can be saved:

``` javascript
item.complete();
```

This process can be repeated (e.g. using a loop) to save multiple items.

#### HTTP requests

Often, the metadata on the page isn't enough to generate a full item. Maybe you need to request a BibTeX citation to pass to the BibTeX translator, or a JSON representation of the item that you'll parse manually. To handle these cases, Zotero provides a modern, promise-based HTTP request system, `request` (and its type-specific siblings: `requestText`, `requestJSON`, and `requestDocument`).

The `request` methods take two parameters:

-   The URL to request, as a string
-   An optional options object with these fields:
    -   `method`: `GET`, `POST`, etc.
    -   `headers`: An key-value object, like `{ 'Content-Type': 'application/json' }`
    -   `body`: The request body, as a string. You might build this using `JSON.stringify()` or `URLSearchParams#toString`.
    -   `responseCharset`: The charset with which to parse the response. `'UTF-8`' by default.
    -   `responseType`: `'text`', `'json`', or `'document`'. Set automatically when using the type-specific request methods.

`request` returns a promise that resolves to an object with `status` (number), `headers` (object), and `body` fields. The type-specific request methods resolve directly to the body. `'text`' bodies are strings, `'json`' bodies are objects, and `'document`' bodies are DOM Documents.

As an example, a translator might fetch BibTeX and pass it to the BibTeX translator like this:

``` javascript
async function scrape(doc, url = doc.location.href) {
  let bibtexURL = attr(doc, '.bibtex-link', 'href');
  let bibtex = await requestText(bibtexURL, {
    headers: { Referer: url }
  });

  let translator = Zotero.loadTranslator('web');
  translator.setTranslator('9cb70025-a888-4a29-a210-93ec52da40d4'); // BibTeX
  translator.setString(bibtex);
  translator.setHandler('itemDone', (_, item) => {
    item.url = url;
    item.complete();
  });
  await translator.translate();
}
```

Or it could parse JSON like this:

``` javascript
async function scrape(doc, url = doc.location.href) {
  let jsonURL = url.replace('/view/', '/export/json/');
  let json = await requestJSON(jsonURL, {
    method: 'POST'
  });

  let item = new Zotero.Item('journalArticle');
  item.title = json.entry.title;
  // And so on...
  item.complete();
}
```

*Note*: You'll see calls to an older callback-based HTTP request system (`doGet`, `doPost`, and `processDocuments`) in some translators. New translator code should not use these methods.

#### Attachments

Attachments may be saved alongside item metadata via the item object's `attachments` property. Common attachment types are full-text PDFs, links and snapshots. An example:

``` javascript
var linkURL = "http://www.ncbi.nlm.nih.gov/pmc/articles/PMC" + ids[i] + "/";
item.attachments = [{
  url: linkURL,
  title: "PubMed Central Link",
  mimeType: "text/html",
  snapshot: false
}];

var pdfURL = "http://www.ncbi.nlm.nih.gov/pmc/articles/PMC" + ids[i] + "/pdf/" + pdfFileName;
item.attachments.push({
  title: "Full Text PDF",
  mimeType: "application/pdf",
  url: pdfURL
});
```

An attachment can only be saved if the source is indicated. The source is often a URL (set on the `url` property), but a document object (set on `document`) or a file path (set on `path`; only for import translators). Other properties that can be set are `mimeType` ("text/html" for webpages, "application/pdf" for PDFs), `title`, and `snapshot` (if the latter is set to `false`, an attached webpage is always saved as a link).

In the very common case of saving the current page as an attachment, set `document` to the current document, so that Zotero doesn't have to make an additional request:

``` javascript
item.attachments.push({
  title: "Snapshot",
  document: doc
});
```

When `document` is set, the MIME type will be set automatically.

Zotero will automatically use proxied versions of attachment URLs returned from translators when the original page was proxied, which allows translators to construct and return attachment URLs without needing to know whether proxying is in use. However, some sites expect unproxied PDF URLs at all times, causing PDF downloads to potentially fail if requested via a proxy. If a PDF URL is extracted directly from the page, it's already a functioning link that's proxied or not as appropriate, and a translator should include `proxy: false` in the attachment metadata to indicate that further proxying should not be performed:

``` javascript
item.attachments.push({
  url: realPDF,
  title: "Full Text PDF",
  mimeType: "application/pdf",
  proxy: false
});
```

Avoid putting the name of the website into attachment titles. In most cases, a generic name ("Full Text PDF", "Preprint PDF", "Snapshot") is best. Add extra details to disambiguate, like when an item has multiple attachments for different languages.

#### Notes

Notes are saved similarly to attachments. The content of the note, which should consist of a string, should be stored in the `note` property of an entry in the item's `notes` array. E.g.:

``` javascript
let bbCite = "Bluebook citation: " + bbCite + ".";
item.notes.push({ note: bbCite });
```

### Saving Multiple Items

Some webpages, such as those showing search results or the index of a journal issue, list multiple items. For these pages, web translators can be written to a) allow the user to select one or more items and b) batch save the selected items to the user's Zotero library.

#### Item Selection

To present the user with a selection window that shows all the items that have been found on the webpage, a JavaScript object should be created. Then, for each item, an item ID and label should be stored in the object as a property/value pair. The item ID is used internally by the translator, and can be a URL, DOI, or any other identifier, whereas the label is shown to the user (this will usually be the item's title). Passing the object to the `Zotero.selectItems` function will trigger the selection window, and the function passed as the second argument will receive an object with the selected items (or `false` if the user canceled the operation), as in the default implementation of `doWeb`:

``` javascript
async function doWeb(doc, url) {
  if (detectWeb(doc, url) == 'multiple') {
    let items = await Zotero.selectItems(getSearchResults(doc, false));
    if (!items) return;
    for (let url of Object.keys(items)) {
      await scrape(await requestDocument(url));
    }
  }
  else {
    await scrape(doc, url);
  }
}

async function scrape(doc, url = doc.location.href) {
  ...
}
```

# Import Translators

To read in the input text, call `Zotero.read()`:

``` javascript
let line;
while ((line = Zotero.read()) !== false)) {
      // Do something
}
```

If given an integer argument, the function will provide up to the specific number of bytes. `Zotero.read()` returns false when it reaches the end of the file.

If `dataMode` in [the translator metadata](dev/translators#metadata) is set to `rdf/xml` or `xml/dom`, the input will be parsed accordingly, and the data will be made available through `Zotero.RDF` and `Zotero.getXML()`, respectively. Documentation for these input modes is not available, but consult the RDF translators ("RDF.js", "Bibliontology RDF.js", "Embedded RDF.js") and XML-based translators ("MODS.js", "CTX.js") to see how these modes can be used.

### Creating Collections

To create collections, make a collection object and append objects to its `children` attribute. Just like ordinary Zotero items, you must call `collection.complete()` to save a collection-- otherwise it will be silently discarded.

``` javascript
var item = new Zotero.Item("book");
item.itemID = "my-item-id"; // any string or number
item.complete();

var collection = new Zotero.Collection();
collection.name = "Test Collection";
collection.type = "collection";
collection.children = [{type: "item", id: "my-item-id"}];
collection.complete();
```

The children of a collection can include other collections. In this case, `collection.complete()` should be called only on the top-level collection.

# Export Translators

Export translators use `Zotero.nextItem()` and optionally `Zotero.nextCollection()` to iterate through the items selected for export, and generally write their output using `Zotero.write(text)`. A minimal translator might be:

``` javascript
function doExport() {
    let item;
    while (item = Zotero.nextItem()) {
        Zotero.write(item.title);
    }
}
```

As with import translators, it is also possible to produce XML and RDF/XML using `Zotero.RDF`. See for example [Zotero RDF](https://github.com/zotero/translators/blob/master/Zotero%20RDF.js) which is a RDF export translator, which also deals with collections.

### Exporting Collections

If `configOptions` in [the translator metadata](dev/translators#metadata) has the `getCollections` attribute set to `true`, the `Zotero.nextCollection()` call will be available. It provides collection objects like those created on import.

``` javascript
while ((collection = Zotero.nextCollection())) {
        // Do something
}
```

The function `Zotero.nextCollection()` returns a collection object:

``` javascript
{
        id: "ABCD1234", // Eight-character hexadecimal key
        children: [item, item, .., item], // Array of Zotero item objects
        name: "Test Collection"
}
```

The collection ID here is the same thing as the collection key used in [API calls](dev/web_api/v3/basics#user_and_group_library_urls).

# Search Translators

The `detectSearch` and `doSearch` functions of search translators are passed item objects. On any given input `detectSearch` should return `true` or `false`, as in "COinS.js":

``` javascript
function detectSearch(item) {
        if (item.itemType === "journalArticle" || item.DOI) {
                return true;
        }
        return false;
}
```

`doSearch` should augment the provided item with additional information and call `item.complete()` when done. Since search translators are never called directly, but only by other translators or by the [Add Item by Identifier](adding_items_to_zotero#add_item_by_identifier) (magic wand) function, it is common for the information to be further processed an [`itemDone` handler](#calling_other_translators) specified in the calling translator.

# Further Reference

## Utility Functions

Zotero provides several [utility functions](https://github.com/zotero/utilities/blob/master/utilities.js) for translators to use. Some of them are used for asynchronous and synchronous HTTP requests; those are [discussed above](#batch_saving). In addition to those HTTP functions and the many standard functions provided by JavaScript, Zotero provides:

-   `Zotero.Utilities.capitalizeTitle(title, ignorePreference)`  
    Applies English-style title case to the string, if the capitalizeTitles [hidden preference](preferences/hidden_preferences) is set. If `ignorePreference` is true, title case will be applied even if the preference is set to false. This function is often useful for fixing capitalization of personal names, in conjunction with the built-in string method `text.toLowerCase()`.
-   `Zotero.Utilities.cleanAuthor(author, creatorType, hasComma)`  
    Attempts to split the given string into firstName and lastName components, splitting on a comma if desired, and performs some clean-up (e.g. removes unnecessary white-spaces and punctuation). The creatorType (see the [list of valid creator types](http://gimranov.com/research/zotero/creator-types) for each item type) will be just passed trough. Returns a creator object of the form: `{ lastName: , firstName: , creatorType: }`, which can for example be used as the argument to `item.creators.push()`.
-   `Zotero.Utilities.trimInternal(text)`  
    Removes extra internal whitespace from the text and returns it. This is frequently useful for post-processing text extracted from HTML, which can have odd internal whitespace.
-   `Zotero.Utilities.xpath(elements, xpath, [namespaces])`  
    Evaluates the specified XPath on the DOM element or array of DOM elements given, with the optionally specified namespaces. If present, the third argument should be object whose keys represent namespace prefixes, and whose values represent their URIs. Returns an array of matching DOM elements, or null if no match.
-   `Zotero.Utilities.xpathText(elements, xpath, [namespaces], [delimiter])`  
    Generates a string from the content of nodes matching a given XPath, as in `Zotero.Utilities.xpath(..)`. By default, the nodes' content is delimited by commas; a different delimiter symbol or string may be specified. (Added in Zotero 2.1.9)
-   `Zotero.Utilities.removeDiacritics(str, lowercaseOnly)`  
    Removes diacritics from a string, returning the result. The second argument is an optimization that specifies that only lowercase diacritics should be replaced.
-   `Zotero.debug(text)`  
    Prints the specified message to the debug log.

`Zotero.Utilities` can optionally be replaced with the shorthand `ZU` and `Zotero` with `Z`, as in `ZU.capitalizeTitle(..)` and `Z.debug(..)`.

## Other Available APIs

See the [zotero/translators type declarations](https://github.com/zotero/translators/blob/master/index.d.ts), which contain a full index of the methods available to translator code.

## Calling other translators

Web translators can call other translators to parse metadata provided in a standard format with the help of existing import translators, or to augment incomplete data with the help of search translators. There are several ways of invoking other translators.

#### Calling a translator by UUID

This is the most common way to use another translator-- simply specify the translator type and the UUID of the desired translator. In this case, the RIS translator is being called.

``` javascript
var translator = Zotero.loadTranslator("import");
translator.setTranslator("32d59d2d-b65a-4da4-b0a3-bdd3cfb979e7"); // RIS
translator.setString(text);
translator.translate();
```

#### Calling a translator using `getTranslators`

This code, based on the "COinS.js" code, calls `getTranslators()` to identify which search translators can make a complete item out of the basic template information already present. Note that `translate()` is called from within the event handler. Analogous logic could be used to get the right import translator for incoming metadata in an unknown format.

``` javascript
let search = Zotero.loadTranslator("search");
search.setSearch(item);

// look for translators for given item
let translators = await search.getTranslators();
search.setTranslators(translators);
await search.translate();
```

#### Using `getTranslatorObject`

The MARC translator is one of several translators that provide an interface to their internal logic by exposing several objects, listed in their `exports` array. Here, it provides an object that encapsulates the MARC logic. The translator can also take input specified via `setString` that can take binary MARC, but this provides a way for library catalog translators to feed human-readable MARC into the translator.

``` javascript
// Load MARC
let translator = Zotero.loadTranslator("import");
translator.setTranslator("a6ee60df-1ddc-4aae-bb25-45e0537be973"); // MARC
let marc = await translator.getTranslatorObject();

let record = new marc.record();
record.leader = "leader goes here";
record.addField(code, indicator, content);

let item = new Zotero.Item();
record.translate(item);
item.libraryCatalog = "Zotero.org Library Catalog";
item.complete();
```

#### Method overview

-   `Zotero.loadTranslator(type)`  
    Type should be one of `web`, `import` or `search`. Returns an object with the methods below.
-   `translator.setSearch(item)`  
    For search translators. Sets the skeleton item object the translator will use for its search.
-   `translator.setString(string)`  
    For import translators. Sets the string that the translator will import from.
-   `translator.setDocument(document)`  
    For web translators. Sets the document that the translator will use.
-   `translator.setTranslator(translator)`  
    Takes a translator object, an array of translator objects (returned by `getTranslators(..)`), or the UUID of a translator (constants; usually hardcoded in your translator script).
-   `translator.setHandler(event, callback)`  
    Valid events are `itemDone`, `done`, `translators`, `error`. The `itemDone` handler is called on each invocation of `item.complete()` in the translator, and the specified callback is passed two arguments: the translator object and the item in question. **Note:** The `itemDone` callback is responsible for calling `item.complete()` on the item it receives, otherwise the item will not be saved to the database.
-   `translator.getTranslators()`  
    Fetches translators that match the input you set earlier. Returns a promise that resolves to an array of translators that return a non-false value for `detectImport`, `detectSearch` or `detectWeb` when passed the input. The `translators` handler, if set, will also be called with the array as its second argument.
-   `translator.getTranslatorObject()`  
    Returns a promise resolving to the translator's top-level `exports` variable, if it has one. (If a callback is passed, the callback will be invoked instead of returning a promise.)  
    This is typically used when calling import translators that define utility functions, like the MARC and RDF translators. Despite the unfortunate nomenclature, this object is not the same thing as the object returned by `getTranslators(..)` or by `Zotero.loadTranslator()`.
-   `translator.translate()`  
    Runs the translator on the input you set.
