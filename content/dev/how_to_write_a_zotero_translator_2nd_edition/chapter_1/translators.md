<p id="zotero-5-update-warning" style="color: red; font-weight: bold">We’re
in the process of updating the documentation for
<a href="https://www.zotero.org/blog/zotero-5-0">Zotero 5.0</a>. Some documentation
may be outdated in the meantime. Thanks for your understanding.</p>

## The Three Major Types of Translators

-   Scrapers
-   Metadata Converters
-   Exporters

### Scrapers

This guide will teach you how to create a "Scraper."

The advantage of a Scraper is that it is the only kind of translator that can be used on any website. What a scraper does is take (scrape) words off the webpage and tells Zotero which words correlate to which part of the citation. It's sort of like cutting and pasting in a text document, but by using code rather than keystrokes.

Another advantage of a scraper is that you can tailor it to your exact needs by choosing to gather all, some, or very little of the information available. Scrapers are easy to learn and to make.

The disadvantage of a scraper is that it relies heavily on format and the consistency of the webpage's creator. If a Webmaster decides to change the structure of a web page even slightly, you will have to alter your scraper to reflect this. However, these changes happen infrequently and once released to all Zotero users, you may find that others take an interest in your translator and help to keep it up to date when needed.

The other two types of translators are powerful and accurate, but are only possible to use under certain conditions that are almost always out of your control unless you are the website's administrator. We will look at how these work, but our focus will be on scrapers.

### Metadata Converters

These translators take information that a Webmaster has voluntarily embedded in a webpage, known as metadata, and organizes it into the correct Zotero fields. You can think of metadata as invisible ink that only appears if you know how to find it. Obviously the catch here is that the Webmaster must have included this information in the first place.

The practice of including metadata is becoming more common, especially in databases. In the past couple of years, how people display metadata has become more standardized. Because of this standardization, Zotero already supports most sites that have it. Some of the most commonly used metadata standards are:

-   [Dublin Core Metadata Initiative](http://dublincore.org/)
-   [unAPI](http://unapi.info/)
-   [COinS](http://ocoins.info/)
-   [Embedded RDF](http://research.talis.com/2005/erdf/wiki/Main/RdfInHtml)

If you are a website administrator and want your site to automatically be Zotero compliant, it is best to use one of these systems rather than writing a translator; they are standardized and reliable. Let me repeat that. If you are an administrator and can include standardized metadata, stop reading this guide and add the data! If you are not a website administrator, you might make this recommendation to the site in question.

### Exporters

Exporters also rely on a website providing certain information. In this case, we need a link that allows us to download a citation. For the most part, there are very few export formats. You may have come across them before, labeled as "MARC display" buttons, or a "RefWorks" button. These options are most common in library catalogs and on academic journal databases. This type of translator actually uses two translators, one embedded in the other. This can get quite complicated so we will not cover it in detail in this guide. However, if you do need to write one of these and need a few hints to get started, here are a few (rather technical) pointers. If you do not need to write an exporter please feel free to ignore this section.

1.  Use an XPath to grab the link URL of the citation download.
2.  Use HTTP get to download the page found at that URL.
3.  Call the translator for that type of citation (ie, MARC, Bibtex, etc) to interpret the citation.
4.  Save results into Zotero.
5.  If you are lost, check one of the many Library Catalogue translators by launching Scaffold and loading the translator code.

You do not need to understand the latter two types of translators or the contents of the paragraph above to be successful at writing scrapers.

**Note**: from this point forward, we will be using the word "Translator" exclusively when referring to "scrapers." Most of the terminology used to explain how to write a scraper is the same as would be used to explain how to write any other translator. The other types of translators will be referenced explicitly if used.

## A few notes before we begin

As with anything new and computer-related, it is important that you backup your entire computer before you start. Coding is generally a safe practice but you never know when something could go wrong and your hard work gets wiped out! Best to backup now than be sorry later.

There are many short cuts available when writing JavaScript and experienced programmers may tell you to use these. You are free to learn the short cuts if you wish; however, this guide will not use them, for simplicity's sake.

This is **NOT** a guide detailing how to use Zotero. It is a guide detailing how to write code to extend the usefulness of Zotero.

**Next**: [Chapter 2: General Troubleshooting Guidelines](dev/how_to_write_a_zotero_translator_2nd_edition/chapter_2)
