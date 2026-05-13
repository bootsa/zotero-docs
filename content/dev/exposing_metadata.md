# Exposing Your Metadata

Do you operate a website containing resources people might want to save to their Zotero libraries?

Zotero has over 700 [translators](translators) that allow it to save high-quality bibliographic metadata from across the web, but the best translator is no translator at all: by exposing metadata on your site in a format that Zotero already understands, you can ensure that Zotero users can always save accurate bibliographic information and correctly cite the materials on your site.

When exposing metadata, it's important to identify the object of interest: this can be the webpage itself (e.g., a page on a newspaper's website showing a article) or the resources described on the webpage (e.g., a page of a library catalog showing bibliographic records).

## Zotero-Ready Web Applications

The easiest way to expose bibliographic metadata is to use a web application that comes with this feature, or offers it through a plugin or minimal configuration. Examples are the content management systems [WordPress](http://wordpress.org/) (together with a [WordPress metadata plugin](plugins#wordpress)) and [Omeka](http://www.omeka.org), and the web-based bibliographic managers [refbase](http://www.refbase.net) and [Bebop BibTeX publisher](http://people.alari.ch/derino/Software/Bebop/).

Zotero-compatible OPAC (Online Public Access Catalog) software packages for libraries, archives, and museums include:

-   [Aleph](https://exlibrisgroup.com/products/aleph-integrated-library-system/)
-   [BiblioCommons](https://www.bibliocommons.com/)
-   [Dynix](https://www.sirsidynix.com/)
-   [Innovative Encore](https://www.iii.com/products/encore/)
-   [Evergreen](https://evergreen-ils.org/)
-   [Koha](https://koha.org/)
-   [Primo](https://exlibrisgroup.com/products/primo-discovery-service/)
-   OCLC-PICA
-   [SIRSI/Symphony/eLibrary](https://www.sirsidynix.com/symphony/)
-   [TLC/YouSeeMore](https://tlcdelivers.com/)
-   [Voyager](https://exlibrisgroup.com/products/voyager-integrated-library-system/) (WebVoyage)

These OPACs are used by tens of thousands of libraries around the world; SIRSI alone is used by [almost 7000 libraries](http://www.librarytechnology.org/libraries.pl?ILS=Unicorn). If you are using one of these and Zotero doesn't work with the library's catalog interface, post to the [Zotero forums](http://forums.zotero.org) to see what changes can be made to make Zotero work with the OPAC installation.

## Using an Open Standard for Exposing Metadata

Alternatively you can directly edit your HTML code of your webpage, using one of the following open standards, to expose your metadata:

-   **Embedded Metadata** The <meta> tags in the header of many webpages will be parsed and used by Zotero. This fairly standard embedding of RDF metadata can use any RDF vocabularies; Zotero supports most major RDF vocabularies used for bibliographic metadata. For details on this approach, see the [Dublin Core description](https://www.dublincore.org/specifications/dublin-core/dc-html/2008-08-04/). The translator will also interpret metadata expressed in the [Google/Highwire key-value system](http://scholar.google.com/intl/en/scholar/inclusion.html). Zotero supports the following values for the <meta> `name` attribute from the Highwire vocabulary:
    -   Title: `citation_title`
    -   Date: `citation_date` (preferred), `citation_publication_date`, `citation_cover_date`, `citation_online_date`, `citation_year`
    -   Publication: `citation_journal_title`
    -   Journal Abbreviation: `citation_journal_abbrev`
    -   Book Title or Proceedings Title: `citation_book_title`, `citation_inbook_title`
    -   Pages: `citation_firstpage` and `citation_lastpage`
    -   Volume: `citation_volume`
    -   Issue: `citation_issue`
    -   Series: `citation_series_title`
    -   Publisher: `citation_publisher`
    -   DOI: `citation_doi`
    -   ISBN: `citation_isbn`
    -   ISSN: `citation_issn`, `citation_eIssn`
    -   PMID: `citation_pmid`
    -   URL: `citation_public_url`, `citation_abstract_html_url`, `citation_fulltext_html_url`
        -   Embedded Metadata can also find the URL in a `<link rel="canonical">` tag or use the page URL.
    -   Abstract: `citation_abstract`
    -   Language: `citation_language`
    -   Conference Name: `citation_conference_title`, `citation_conference`
    -   University (for theses and dissertations): `citation_dissertation_institution`
    -   Institution (for reports): `citation_technical_report_institution`
    -   Report Number: `citation_technical_report_number`
    -   Creators: `citation_author`, `citation_authors`, `citation_editor`, `citation_editors`
        -   Creators should be listed in repeated <meta> tags or in a single tag, separated by semicolons: `    <!-- This -->
                <meta name="citation_editor" content="Surname, Given Name">
                <meta name="citation_authors" content="Smith, Jane; Public, John Q.">
                <!-- is equivalent to -->
                <meta name="citation_editor" content="Surname, Given Name">
                <meta name="citation_author" content="Smith, Jane">
                <meta name="citation_author" content="Public, John Q.">`
    -   Full-Text PDF attachment: `citation_pdf_url`
    -   Tags: `citation_keywords` (semicolon-separated)
-   **COinS** The [COinS website](http://ocoins.info/) defines COinS (ContextObjects in Spans) as "a simple, ad hoc community specification for publishing OpenURL references in HTML." Although somewhat limited in the number of metadata categories, using COinS is a relatively easy and lightweight option for embedding reference metadata into a webpage or blog.
    -   Individual COinS can be manually generated using the [COinS Generator](http://generator.ocoins.info/) and inserted into your webpage or blog;
    -   Alternatively, [Zotero can be used to create COinS](dev/exposing_metadata/coins) from references in your library, and these can dragged-and-dropped into your website or blog;
    -   Note also, that when you right-click a selection of references in your Zotero library and choose 'Create bibliography from Selected Items', choose the 'Citation Style', check 'Save as HTML' then click on 'OK', that the webpage created contains COinS, which theoretically can be extracted or that page directly linked to from you website or blog.
-   **unAPI**. As described on the [unAPI website](http://www.unapi.info), "unAPI is a tiny HTTP API for the few basic operations necessary to copy discrete, identified content from any kind of web application." For our purposes, unAPI allows you to serve up bibliographic information in a variety of different bibliographic formats for Zotero to automatically ingest. If you use unAPI, you can use one of the following standard and documented file formats:
    -   **MODS XML**. Developed by the Library of Congress, [MODS XML](http://www.loc.gov/standards/mods/) is one of the richest standard formats available.
    -   **MARC**. An older, flat format, MARC is only recommended if your application can already generate it.
    -   **Bibliontology/Dublin-Core-like/Zotero RDF**. [Bibliontology RDF](http://bibliontology.com/) can store any information that Zotero can save. Dublin Core is standardized and extremely common, but is limited in its expressive abilities. The legacy Zotero RDF format is also supported.
    -   **[BibTeX](http://www.bibtex.org/)**, **[RIS](http://www.refman.com/support/risformat_intro.asp)**, and **[Bibix/EndNote(R)/Refer](http://auditorymodels.org/jba/bibs/NetBib/Tools/bp-0.2.97/doc/endnote.html)**. These formats are more limited in their ability to describe metadata, but have good code library support and they are simpler to generate.
    -   *Note that the unAPI website appears to be no longer maintained, but sites built using the unAPI specification will still work with Zotero. See [here](/forum/discussion/50327/is-unapi-dead-because-their-website-sure-seems-to-be) for a discussion.*

## Force Zotero to refresh metadata

Websites for which metadata changes without a page reload should fire a ZoteroItemUpdated event to tell Zotero to re-detect metadata on the page.

``` javascript
document.dispatchEvent(new Event('ZoteroItemUpdated', {
    bubbles: true,
    cancelable: true
}))
```

## Zotero Web Translators

Exposing bibliographic metadata through an open standard is very powerful (and also benefits non-Zotero users!). However, if you have little control over the way your website is built, you may have to [create a Zotero web translator](dev/translators) for Zotero-compatibility. Translators have some downsides: apart from the fact that they are a Zotero-specific solution, translators can break easily if the structure of the targeted website changes.
