<p id="zotero-5-update-warning" style="color: red; font-weight: bold">We’re
in the process of updating the documentation for
<a href="https://www.zotero.org/blog/zotero-5-0">Zotero 5.0</a>. Some documentation
may be outdated in the meantime. Thanks for your understanding.</p>

Site translators are discrete pieces of code that extract web-based metadata and then insert it into a Zotero item. Writing them sometimes requires a little ingenuity, but this overview should help to simplify the process. This document will not cover the nitty gritty of GUIDs, sqlite insertion, etc. It intended instead to get developers thinking about how translators work.

Note that this document refers to a new version of our Amazon scraper that is only available to developers working with our svn build.

## Step 1: Should I Run?

The first thing that a site translator needs to know is whether it should run on a web page. Every time a Zotero user visits any web page at all, Zotero checks the page URL against its translator database to see whether it finds any matching translators. This operation is extremely quick and is meant only to find a match at the very highest level. We don't yet care whether the web page has any metadata or search results: we just want to know whether we're in the ballpark. This scanning operation uses a regular expression. For example, to determine whether we should run the Amazon.com translator, we search for: `^http://(?:www\.)amazon`

Any page with a URL beginning with `http://amazon` or `http://www.amazon` will bind to this translator. By leaving off `.com` we allow this particular translator to to run on any of Amazon's international sites: amazon.ca, amazon.co.jp, amazon.co.uk, amazon.de, and amazon.fr.

## Step 2: Have I Found Something?

Once a translator is bound to a page, it will execute a JavaScript function called detectWeb. This function is responsible for making the little icon appear in the address bar that tells users that Zotero can do something with the page at hand. The detectWeb function could, for example, parse the page URL to look for signs of a search results page. If so, we would want to have Zotero display the folder icon in the address bar. Our Amazon translator, for example, tests for the following regular expression appearing after the hostname: `//(gp/search/|exec/obidos/search-handle-url/|s/)`

In addition to the page URL, the detectWeb function also has access to the page document object. If the URL does not provide enough information about what kind of page the user is viewing, Zotero can use this document object to examine page content and structure. The detectWeb function might analyze HTML tags, or it might use an XPath to zero in on specific page content that indicates what we're viewing. In the case of the Amazon translator, use the XPath `//input[@name="ASIN"]` to find out whether the page contains a form input for an ASIN, or Amazon Standard Identification Number. Every Amazon item page contains this input (even if it's out of stock), so it is a very good test of whether we're looking at a single Amazon item that Zotero can import. From here we do a little additional logic to determine whether we have found a book or other item to fine tune what kind of icon displays in the address bar, but at this stage of the translator, these are merely cosmetic flourishes. It doesn't really matter to Zotero what kind of icon it displays in the address bar. This icon, whatever its form, merely allows us to proceed to the next step.

## Step 3: Let's Grab It

Once Zotero displays an icon in the browser's address bar, it is ready to run the piece of code that will create a new Zotero item and populate its fields with metadata. This function is called doWeb, and it is usually significantly more complicated than detectWeb. At this stage, we will need to parse out our metadata and then decide where to place it.

The doWeb function usually begins with something very much like detectWeb. Since doWeb doesn't know anything about detectWeb, it needs to determine whether it is going to pull data for a single record or whether it is going to offer the user the chance to select multiple records and then grab each of them (the drop-down selection dialog). Let's take the simpler case first: a single record.

### Single Record

Just as in detectWeb, we start by looking for evidence that the user is looking at a single record. In our Amazon example, we see whether there is an ASIN input. Now that we have a unique identifier for the record, we can try to find a way to get nicely formatted metadata for the record. In this particular case, we can take advantage of Amazon's API to formulate a URL to retrieve that item's metadata formatted as an XML response. Our Amazon request looks something like:

    http://ecs.amazonaws.com/onca/xml?Service=AWSECommerceService&Version=<version>&Operation=ItemLookup&SubscriptionId=<ID>&ItemId=<ASIN>&ResponseGroup=ItemAttributes

For a library catalog, we might instead find a way to use an ISBN or other unique identifier to return a text or binary MARC record. Many sites currently allow users to download a RIS-formatted citation, which Zotero already knows how to import. In either case, the good news is that doWeb can also call other translators, so if, for example, we find a page that includes a MARC record or RIS-formatted citation, we can pass this data to one of Zotero's existing translators.

In some situations, there will be no "clean" metadata available, and it will be necessary to pull information right off of the web page itself. In such cases we will have to "scrape" metadata from HTML source or rendered DOM. To write a scraper that works well, we'll need to know the basic structure of a record's web page in order to know where to look for the right metadata. In the case of Amazon, we know that publication information is always contained in a similarly formatted section `//td[@class="bucket"]/div[@class="content"]/ul/li` By looking for this section and parsing out its text, we could extract the record's relevant metadata. In fact, this is the approach used in Zotero's currently released Amazon scraper. Please note that for any work involving XPaths, MIT's [Solvent tool](http://simile.mit.edu/wiki/Solvent) is essential.

### Multiple Records

If, instead of a single record, the user is looking at a search results page, we're going to want the user to be able to select one or more items and have Zotero grab those items. In the Amazon translator, we examine search results pages using the XPath `//a/span[@class="srTitle"]` which happens to map to the anchor tag surrounding any Amazon search result. We then parse out each of these anchors' texts to display to the user in a drop-down search box. We could then use the associated URLs to formulate requests for each of those pages and then find their embedded ASINs. In the case of Amazon, however, we can in fact use the URLs themselves to determine a unique identifer for each item. Now we have all the information we need to ping Amazon's API to get the relevant metadata.

## Step 4: Put Everything in Its Place

Once we have our metadata, we need only to create a new Zotero item and then populate its fields. Usually translators perform this task inline with parsing the metadata, so that as each piece of metadata is retrieved, it goes into the appropriate [Zotero item field](dev/zotero_metadata_format). Sometimes we might want to add some additional information that does not appear in the metadata or that does not have an appropriate item field in the Zotero case type. Perhaps we are looking at a journal article and have pulled a clean set of metadata about the article, but we also want to include the article's associated PDF file. We can tailor the translator to download that file and add it as an attachment to the Zotero item. Alternatively, we may find a good piece of miscellaneous metadata that we want to keep. Amazon, for example, provides two release dates for DVD films: the DVD release date and the original theatrical release date. If we want to include the latter, we can simply add it to the "extra" field so that it is saved along with the rest of the item's metadata.

## Step 5: Contribute Your Translator

If your new or modified translator would be useful to others,

1.  upload your JavaScript to [section=Files of the Zotero developers googlegroup](http://groups.google.com/group/zotero-dev/files).
2.  notify the [Zotero developers mailing list](http://groups.google.com/group/zotero-dev).
