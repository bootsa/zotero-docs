<p id="zotero-5-update-warning" style="color: red; font-weight: bold">We’re
in the process of updating the documentation for
<a href="https://www.zotero.org/blog/zotero-5-0">Zotero 5.0</a>. Some documentation
may be outdated in the meantime. Thanks for your understanding.</p>

# Zotero Translators - The Missing Manual

## Tools of the Trade

Writing Zotero translators can be made much easier by using the right tools. Here are some suggested downloads:

-   [Zotero](/) - writers of Zotero translators naturally can't do without a copy of Zotero.
-   [Scaffold](dev/scaffold) - this tool offers an easy and quick way to modify and test translators.
-   XPath tools - most translators rely on XPath to extract information from HTML web pages or from XML data files. To quickly construct robust XPaths, consider using one of the following tools:
    -   [Firebug](http://getfirebug.com/) - a popular and very powerful tool. Very useful in inspecting the HTML structure of web pages, and finding XPaths to the elements of interest.
    -   [XPather](http://xpath.alephzarro.com/)/[DOM Inspector](https://addons.mozilla.org/en-US/firefox/addon/6622) - XPather, which requires the DOM Inspector extension to be installed, is mostly useful for testing XPaths. Recommended in combination with Firebug.

## Zotero.Utilities

To do: include details on all the useful (but hidden) functions in Zotero.Utilities

When writing translator code, you can make use of a number of functions in [Zotero.Utilities](https://www.zotero.org/trac/browser/extension/branches/1.0/chrome/content/zotero/xpcom/utilities.js). Below each function is described, and an example of its use is given.

### String manipulation

#### cleanAuthor

**Function description**  
<https://www.zotero.org/trac/browser/extension/branches/1.0/chrome/content/zotero/xpcom/utilities.js#L40>
Zotero.Utilities.prototype.cleanAuthor = function(author, type, useComma)  
@param {String} author Creator string  
@param {String} type Creator type string (e.g., "author" or "editor")  
@param {Boolean} useComma Whether the creator string is in inverted (Last, First) format  
@return {Object} firstName, lastName, and creatorType

Sometimes it is difficult to extract clean author names from webpages. `cleanAuthor` removes white-space and punctuation (.,/[]:) that precedes or follows the author name, and performs some additional clean-up as well (e.g. removal of double spaces). If the author name is inverted (last name first, separated from the first name by a comma or comma-space), set `useComma` to true and `cleanAuthor` will correctly isolate the last and first name (see example).

**Example code**

``` javascript
var name = " :Doe, John";
Zotero.debug(Zotero.Utilities.cleanAuthor(name, "author",true));
```

**Example code debug output**  
`'firstName' => "John"
'lastName' => "Doe"
'creatorType' => "author"
`

#### trim

**Function description**  
<https://www.zotero.org/trac/browser/extension/branches/1.0/chrome/content/zotero/xpcom/utilities.js#L85>
Zotero.Utilities.prototype.trim = function(s)  
@type String

Removes leading and trailing whitespace from a string

#### trimInternal

**Function description**  
<https://www.zotero.org/trac/browser/extension/branches/1.0/chrome/content/zotero/xpcom/utilities.js#L98>
Zotero.Utilities.prototype.trimInternal = function(s)
@type String

Cleans whitespace off a string and replaces multiple spaces with one

#### cleanString

Deprecated function, use trimInternal instead.

#### superCleanString

**Function description**  
<https://www.zotero.org/trac/browser/extension/branches/1.0/chrome/content/zotero/xpcom/utilities.js#L123>
Zotero.Utilities.prototype.superCleanString = function(x)
@type String

Cleans any non-word non-parenthesis characters off the ends of a string

#### cleanTags

**Function description**  
<https://www.zotero.org/trac/browser/extension/branches/1.0/chrome/content/zotero/xpcom/utilities.js#L136>
Zotero.Utilities.prototype.cleanTags = function(x)
@type String

Eliminates HTML tags, replacing each instance of <br> with a newline

#### htmlSpecialChars

**Function description**  
<https://www.zotero.org/trac/browser/extension/branches/1.0/chrome/content/zotero/xpcom/utilities.js#L153>
Zotero.Utilities.prototype.htmlSpecialChars = function(str)
@type String

Escapes several predefined characters:

-   & (ampersand) becomes &
-   " (double quote) becomes "
-   ' (single quote) becomes '
-   < (less than) becomes <
-   > (greater than) becomes >

and

-   &lt;ZOTEROBREAK/&gt; becomes <br/>
-   &lt;ZOTEROHELLIP&gt; becomes …

#### unescapeHTML

**Function description**  
<https://www.zotero.org/trac/browser/extension/branches/1.0/chrome/content/zotero/xpcom/utilities.js#L189>
Zotero.Utilities.prototype.unescapeHTML = function(str)
@type String

Converts all HTML entities in a string into Unicode characters.

#### parseMarkup

**Function description**  
<https://www.zotero.org/trac/browser/extension/branches/1.0/chrome/content/zotero/xpcom/utilities.js#L206>
Zotero.Utilities.prototype.parseMarkup = function(str)
@return {Array} An array of objects with the following form:
{
type: 'text'|'link',
text: "text content",
[ attributes: { key1: val [ , key2: val, ...] }
}</pre>

Parses a text string for HTML/XUL markup and returns an array of parts. Currently only finds HTML links (<a> tags)

#### isInt

**Function description**  
<https://www.zotero.org/trac/browser/extension/branches/1.0/chrome/content/zotero/xpcom/utilities.js#L247>
Zotero.Utilities.prototype.isInt = function(x)
@deprecated Use isNaN(parseInt(x))
@type Boolean

Tests if a string is an integer

#### getPageRange

**Function description**  
<https://www.zotero.org/trac/browser/extension/branches/1.0/chrome/content/zotero/xpcom/utilities.js#L260>
Zotero.Utilities.prototype.getPageRange = function(pages)
@param {String} Page range to parse
@return {Integer[]} Start and end pages

Parses a page range

#### lpad

**Function description**  
<https://www.zotero.org/trac/browser/extension/branches/1.0/chrome/content/zotero/xpcom/utilities.js#L283>
Zotero.Utilities.prototype.lpad = function(string, pad, length)
@param {String} string String to pad
@param {String} pad String to use as padding
@length {Integer} length Length of new padded string
@type String

Pads a number or other string with a given string on the left

#### getLocalizedCreatorType

**Function description**  
<https://www.zotero.org/trac/browser/extension/branches/1.0/chrome/content/zotero/xpcom/utilities.js#L342>
Zotero.Utilities.prototype.capitalizeTitle = function(string, force)
@param {String} string
@param {Boolean} force Forces title case conversion, even if the capitalizeTitles pref is off
@type String

Cleans a title, converting it to title case and replacing " :" with ":"

### Other functions

#### itemTypeExists

**Function description**  
<https://www.zotero.org/trac/browser/extension/branches/1.0/chrome/content/zotero/xpcom/utilities.js#L297>
Zotero.Utilities.prototype.itemTypeExists = function(type)
@param {String} type Item type
@type Boolean

Tests if an item type exists (FIXME: what is the use case for this?)

#### getCreatorsForType

**Function description**  
<https://www.zotero.org/trac/browser/extension/branches/1.0/chrome/content/zotero/xpcom/utilities.js#L311>
Zotero.Utilities.prototype.getCreatorsForType = function(type)
@param {String} type Item type
@return {String[]} Creator types

Find valid creator types for a given item type (FIXME: what is the use case for this?)

#### getLocalizedCreatorType

**Function description**  
<https://www.zotero.org/trac/browser/extension/branches/1.0/chrome/content/zotero/xpcom/utilities.js#L327>
Zotero.Utilities.prototype.getLocalizedCreatorType = function(type)
@param {String} type Creator type
@param {String} Localized creator type
@type Boolean

Gets a creator type name, localized to the current locale (FIXME: what is the use case for this?)

Zotero.Utilities.processAsync
<https://www.zotero.org/trac/browser/extension/branches/1.0/chrome/content/zotero/xpcom/utilities.js#L361>

To Do:

processDocuments, HTTP.doGet, HTTP.doPost, getItemArray

## Item properties

Especially for screen scraper translators, knowing which item types (`book`, `journalArticle`, etc) and item fields (`title`, `url`, etc) exist in Zotero can be very helpful. Fortunately, the possible item properties can be found in the following source code file (types are listed as "itemTypes" entries, fields as "itemFields"):

<http://aurimasv.github.io/z2csl/typeMap.xml>

Note that the different item types make use of different combinations of item fields (e.g. the `book` item type has the field `ISBN`, while the `journalArticle` item type lacks this field).

## Translator delegation

To do: describe how translators can call other translators (annotate existing RIS-translator with a bunch of comments?)

## Useful translator examples

To do: pick some examples of the different types of translators:

-   XML based: NCBI Pubmed, Google Books
-   RIS translators
-   Pure screen scrapers
