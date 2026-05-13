**While the Translator Framework still works, new translators using the Framework are no longer accepted, and we are migrating existing translators away from the format.**

**This page exists as legacy documentation only.**

# Translator Framework

The translator framework is a way to build web translators that lets translator authors avoid most of the boilerplate that usually is required for new translators, making it possible to write simple content scrapers in just a few lines of JavaScript.

The framework was written and contributed by Erik Hetzner and is licensed under the AGPLv3+. It currently resides at <https://gitlab.com/egh/zotero-transfw>, but there are plans to include it in Zotero itself.

To use the framework, simply insert the framework code at the beginning of your translator, after the translator information block (JSON header). If you are using [Scaffold](dev/translators/scaffold) to develop your translator, you won't see the information block, and can click "Uses translator framework" on Scaffold's Metadata tab to automatically include the code.

You'll start writing beneath the line that reads:
`/* End generic code */`

**Note:** The latest version of [Scaffold](dev/translators/scaffold), the Zotero translator IDE, can automatically include the framework code.

### Example Translator

From EurasiaNet.js:

``` javascript
function detectWeb(doc, url) { return FW.detectWeb(doc, url); }
function doWeb(doc, url) { return FW.doWeb(doc, url); }
 
/** Articles */
FW.Scraper({
itemType         : 'newspaperArticle',
detect           : FW.Url().match(/(\/node\/\d+|articles\/[a-zA-Z0-9]+\.shtml)/),
title            : FW.Xpath('//h1[@class="title"]').text().trim(),
attachments      : [{ url: FW.Url().replace(/node/,"print"),
  title:  "EurasiaNet Printable",
  type: "text/html" }],
// here, we use the replace(..) to break names on &nbsp;
creators         : FW.Xpath('//div[@class="submitted"]/span[@class="authors"]/a')
                    .text().replace(/\s/," ").cleanAuthor("author"),
date             : FW.Xpath('//div[@class="submitted"]/span[@class="timestamp"]').text(),
tags             : FW.Xpath('//div[@class="terms terms-inline"]/ul/li/a[@rel="tag"]').text(),
publicationTitle : "EurasiaNet"
});

FW.MultiScraper({
itemType         : 'multiple',
detect           : FW.Url().match(/\/search\/node/),
choices          : {
  titles :  FW.Xpath('//dl[@class="search-results node-results"]/dt[@class="title"]/a').text().trim(),
  urls    :  FW.Xpath('//dl[@class="search-results node-results"]/dt[@class="title"]/a').key("href")
}
});
```

This is the functional portion of a real, working web translator using the translator framework. It defines two scrapers, in this case one for newspaper articles and one for multiple result pages.

This is the general model for creating a translator using the framework -- define several scrapers that are triggered by different kinds of page content or URLs.

### Scrapers

As the example translator above shows, there are two kinds of scrapers in the framework, defined using the functions `FW.Scraper()` and `FW.MultiScraper()`. The first kind identifies item metadata for a single item from a single page, while the second kind identifies item page URLs on a single page and is usually used for things like search results of journal issue tables of contents.

Both kinds of scrapers are defined by passing an object with the scraper's item type (`itemType`), detect conditions (`detect`) and other keys to the corresponding function.

Each value can be either a string, in which case it is always the same, a function, or a chained series of filters. This last form is most common. In the above example we can see, for instance, the `creators` filter. It starts with an XPath expression. This expression is then turned into text only using the `.text()` function. Finally, the author is cleaned up using the `cleanAuthor` function as provided by Zotero.

#### FW.Scraper

-   Required keys: `detect`, `itemType` ([list of itemType options](http://aurimasv.github.io/z2csl/typeMap.xml))
-   Optional keys: `attachments`

#### FW.MultiScraper

-   Required keys: `detect`, `itemType`, `choices` (with two keys: `titles`, `urls`)
-   Optional keys: `beforeFilter`, `itemTrans` (`attachments`, key on `choices` object)

The key `choices` must be set to an object with keys `titles` and `urls`. The latter should be set to expressions that yield sets of corresponding titles and URLs of items to be processed by other scrapers defined in the translator. If set, the `attachments` key should be set to an expression yielding a corresponding set of attachment objects (that is, one for each title and URL).

``` javascript
choices : {
 titles    : FW.Xpath('//table[contains(@class,"searchresults")]/tbody/tr/td/a').text(),
 urls      : FW.Xpath('//table[contains(@class,"searchresults")]/tbody/tr/td/a').key('href').text()
}
```

##### Pre-processing

The `beforeFilter` key can be set to a function that returns a new URL. The framework will request this new document and run the MultiScraper in the context of the resulting document and URL. This is used in the framework translator for Google Scholar:

``` javascript
beforeFilter : function (doc, url) {
                var haveBibTeXLinks = FW.Xpath('//a[contains(@href, "scholar.bib")]')
                      .evaluate(doc);
                if(!haveBibTeXLinks) {
                      url = url.replace (/hl\=[^&]*&?/, "");
                      url = url.replace("scholar?",
                         "scholar_setprefs?hl=en&scis=yes&scisf=4&submit=Save+Preferences&");
                 }
                 return url;
} 
```

Here the option is used to guarantee that the multiple item page has links to the BibTeX files that the translator uses.

#### Attachments

To add attachments to an item, specify the `attachments` key in the scraper object. The key should be set to an array of attachment objects:‌ `{ url : ... , title : ... , type : ... }`.

The keys `url`, `title` and `type` can be set to single values (like `FW.Url()` or `"Page Snapshot"`) or to multiple values, as in the XPath constructions below.

``` javascript
 attachments : [
  { url : FW.Url(),
    title : FW.Url().match(/[0-9]+$/).prepend("Washington Monthly Snapshot pg. "),
    type : "text/html" },
  { url : FW.Xpath('//div[@class="pagination"]/a[not(@class)]').key('href').text(),
    title : FW.Xpath('//div[@class="pagination"]/a').
                        key('href').text().
                        match(/[0-9]+$/).
                        prepend("Washington Monthly Snapshot pg. "),
    type : "text/html" }
 ]
```

#### Post-Processing with Hooks

Sometimes the basic capabilities provided by the framework are not enough to get the desired output, and some additional data gathering or post-processing is needed. Arbitrary post-processing of scraped items can be done by defining hooks:

``` javascript
hooks : { "scraperDone": function  (item,doc, url) {
    item.date = item.date ? item.date : item.runningTime;
    item.runningTime = undefined;
    for (i in item.creators) {
        if (item.creators[i].lastName == item.creators[i].lastName.toUpperCase()) {
            item.creators[i].lastName = Zotero.Utilities.capitalizeTitle(
                item.creators[i].lastName.toLowerCase(),true);
        }
    }}
```

The `hooks` property should be an object with the property "scraperDone", set to a function that should be run when the scraper has finished processing a single item. The function is passed three arguments: the in-progress item, the current DOM, and the current URL. The function can run any JavaScript allowed in the Zotero translator sandbox; see [Translator Coding](dev/translators/coding) for more details.

In the example above, the scraper had been written to save two potential date fields, one as "runningTime" and one as "date". The post-processing function sets the item's "date" property to the valid one of these two choices. It also checks if the author last names are in all-caps and fixes them if they are. Both of these tasks are a little hard to do within the framework.

## Functions

To use the framework, just chain together functions from the list below until you get the desired output. Note that JavaScript functions not in this list will not work within the scrapers.

#### Main functions

-   `FW.PageText ( )` Provides the HTML source of the current document as a string.
-   `FW.Url ( )` Provides the URL of the current document as a string.
-   `FW.Xpath ( expression )` Runs the given [XPath expression](dev/technologies#xpath) on the current document. Returns the matching nodes; to get an attribute, use `key( attribute_name )`; to get the textContent of the node, use `text()`
-   `FW.Scraper ( {..} )` Sets up a scraper using the given object (usually an anonymous object in curly braces, as in the examples).
-   `FW.MultiScraper ( {..} )` Sets up a special scraper for matching multiple items using the given object (usually an anonymous object in curly braces, as in the examples). Set `itemType` to `multiple`, and provide expressions for `titles`, `urls` and optionally for `attachments`.
-   `FW.DelegateTranslator ( { translatorType : "import", translatorId : id} )` Used with MultiScraper; assign DelegateTranslator to the `itemTrans` property of the MultiScraper. Define a translator to use to handle the URLs the MultiScraper provides; the framework will pass the document source of the documents at those URLs to the specified translator.

#### String functions

-   `prepend ( text )` Add a string to the end of the result.
-   `append ( text )` Add a string to the beginning of the result.
-   `remove (regex, flags )` Removes any text that matches the [regular expression](dev/technologies#regular_expressions). Note that empty entries are dropped silently, so this can be used to filter out unwanted results.
-   `trim ()` Removes whitespace at the beginning and end of the result.
-   `trimInternal ()` Like `trim ()`, but also removes extra whitespace inside the result.
-   `match ( regex, [ group ] )` Match the [regular expression](dev/technologies#regular_expressions), and pass on the specified match group. If no group is specified, the whole match is used (match group 0).
-   `capitalizeTitle ( )` Capitalizes the string using Zotero's capitalization function
-   `unescapeHTML ( text )`
-   `unescape ( text )`
-   `split ( regex )` Split the string into multiple strings on the [regular expression](dev/technologies#regular_expressions).
-   `join ( separator )` Join all the strings into one, placing specified the separator between them.
-   `cleanAuthor ( type, [ useComma ] )` Makes creator objects of the specified type (i.e., `author`, `editor`, `translator`, `contributor`, `bookAuthor`, `director`, etc.) If the second argument is true, the input will be split into first and last names on a comma, if present, in the input. See the [list of valid creator types for each item type](http://gimranov.com/research/zotero/creator-types).

#### Putting things together

`FW.Xpath()` and `FW.Url()` are the main functions you'll call; they return an object that, when processed by the framework, results in selecting some text from a page or in the current URL.

You can also call a method on this object, e.g.:

    FW.Xpath("//xpath/expression").split(/,/)

This modifies the object to include a filter that splits the
text on /,/. You can chain these together:

    FW.Xpath("//xpath/expression").text().split(/,/).trim().cleanAuthor()

This will split the text returned by the XPath into an array and call
the filters (trim, then cleanAuthor) on each member of the array. This
way we can add multiple creators to the item.

If you want to add an arbitrary filter, this should work:

    FW.Xpath("//xpath/expression").text().addFilter(function (s) { return s + "HELLO WORLD"; })

## Templates

Just paste the following templates into your translator, fill in the appropriate fields, and delete the unnecessary fields.

### Boilerplate

Required for every framework-derived translator.

``` javascript
function detectWeb(doc, url) { return FW.detectWeb(doc, url); }
function doWeb(doc, url) { return FW.doWeb(doc, url); }
```

### FW.MultiScraper

``` javascript
FW.MultiScraper({
itemType         : 'multiple',
detect           : ,
choices          : {
  titles :  
  urls   :
  attachments :  // optional
}
});
```

### FW.Scraper

For possible values of `itemType` and the legal fields for each type, see the schema description at <http://aurimasv.github.io/z2csl/typeMap.xml> .

``` javascript
FW.Scraper({
itemType         : ,
detect           : ,
attachments      : ,
creators         : ,
hooks            : {
        "scraperDone" : function (item, doc, url) {}
}
// All possible fields
abstractNote : ,
applicationNumber : ,
archive : ,
archiveLocation : ,
artworkMedium : ,
artworkSize : ,
assignee : ,
audioFileType : ,
audioRecordingType : ,
billNumber : ,
blogTitle : ,
bookTitle : ,
callNumber : ,
caseName : ,
code : ,
codeNumber : ,
codePages : ,
codeVolume : ,
committee : ,
company : ,
conferenceName : ,
country : ,
court : ,
date : ,
dateDecided : ,
dateEnacted : ,
dictionaryTitle : ,
distributor : ,
docketNumber : ,
documentNumber : ,
DOI : ,
edition : ,
encyclopediaTitle : ,
episodeNumber : ,
extra : ,
filingDate : ,
firstPage : ,
forumTitle : ,
genre : ,
history : ,
institution : ,
interviewMedium : ,
ISBN : ,
ISSN : ,
issue : ,
issueDate : ,
issuingAuthority : ,
journalAbbreviation : ,
label : ,
language : ,
legalStatus : ,
legislativeBody : ,
letterType : ,
libraryCatalog : ,
manuscriptType : ,
mapType : ,
medium : ,
meetingName : ,
nameOfAct : ,
network : ,
number : ,
numberOfVolumes : ,
numPages : ,
pages : ,
patentNumber : ,
place : ,
postType : ,
presentationType : ,
priorityNumbers : ,
proceedingsTitle : ,
programTitle : ,
programmingLanguage : ,
publicLawNumber : ,
publicationTitle : ,
publisher : ,
references : ,
reportNumber : ,
reportType : ,
reporter : ,
reporterVolume : ,
rights : ,
runningTime : ,
scale : ,
section : ,
series : ,
seriesNumber : ,
seriesText : ,
seriesTitle : ,
session : ,
shortTitle : ,
studio : ,
subject : ,
system : ,
thesisType : ,
title : ,
type : ,
university : ,
url : ,
version : ,
videoRecordingType : ,
volume : ,
websiteTitle : ,
websiteType :
});
```
