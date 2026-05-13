# CSL 0.8.1 Syntax Overview

This page describes the syntax of version 0.8.1 of the [Citation Style Language](http://citationstyles.org/) (CSL), including information specific to Zotero. An additional source of documentation is the [CSL 0.8.1 schema](http://bitbucket.org/bdarcus/csl-schema/src/83f9cf9b53bd/csl.rnc), which is written in [RELAX NG Compact](http://www.relaxng.org/compact-tutorial-20030326.html) and can be used for [style validation](dev/creating_citation_styles#validation).

Pointers on how CSL styles can be created, modified, validated, shared and installed in Zotero can be found [here](dev/citation_styles), together with more background information about CSL.

# CSL Style Structure

All CSL styles share the same basic structure: only five different XML elements can be nested directly in the `style` root element: `info`, `citation`, `bibliography`, `macro` and `terms`. The roles of each of these elements (described in more detail below) are:

-   `info`: contains metadata describing the style (name of the style, authors of the style, etc)
-   `citation`: describes how in-text citations should be formatted
-   `bibliography`: describes how bibliographies should be formatted
-   `macro`: allows for reuse of formatting instructions, allowing for more compact styles
-   `terms`: allows for the modification of locale-specific strings (e.g. "edited by" can be changed in "ed. by")

## Independent and Dependent Styles

Two main types of CSL styles exist: independent and dependent styles. An independent style contains a full style description, and includes at least the `info` and `citation` element. Unless it is a note-based style that lacks a bibliography, it also includes the `bibliography` element. The `terms` element and one or more `macro` elements are optional in independent styles. A dependent style, on the other hand, merely refers to an independent style, like an alias or shortcut. It only includes the info element. Dependent styles are used if multiple publications share a single style format. Each publication can thus have its own dependent style (with the info section describing the journal's metadata, e.g. the journal's name or ISSNs) with a corresponding entry in (for instance) the Zotero Style Repository, while only a single independent master style has to be maintained.

Note that dependent styles cannot be used to indicate changes compared to the master style. If there is any difference in formatting between two styles, however small, two separate CSL styles have to be created.

## Preamble

Before the style element, each CSL style should include the XML declaration element, specifying the version of XML used as well as the character encoding. The `style` element itself carries a number of arguments:

-   `xmlns`: the namespace declaration that binds the elements in the style to the given namespace URI
-   `class`: with two possible values, "in-text" or "note", this specifies whether the style is note-based or uses in-text citations coupled to a bibliography
-   `xml:lang` (optional): specifies the locale used for argument values within the style
-   `default-locale` (optional): sets the localization of the style output. The effect is currently limited to localization of preset strings (e.g. "edited by"), but plans exist to extend this to punctuation (French quotes, different punctuation around quotation marks in American and British English). N.B. Support for the default-locale argument has not yet been implemented in Zotero. Currently styles are solely localized according to the locale set in Firefox, which can be overruled with the [export.bibliographyLocale](preferences/hidden_preferences#export_and_citation_settings) user preference.

An example of a preamble is shown below. For most styles only the value of `class` and `default-locale` will differ.

``` xml
<?xml version="1.0" encoding="UTF-8"?>
<style xmlns="http://purl.org/net/xbiblio/csl" class="in-text" xml:lang="en" default-locale="fr-FR">
```

## Info

The `info` section of a CSL style contains the style metadata, which does not affect the formatting of citations. Instead, the metadata makes it possible to host styles in style repositories, to allow users to subscribe to field-specific style collections, and to automatically update styles. An example of a filled-in `info` section is shown below, and is followed by a description of all possible elements.

``` xml
<info>
 <title>My first style</title>
 <id>http://www.zotero.org/styles/my-style-name</id>
 <link href="http://www.zotero.org/styles/my-style-name"/>
 <author>
  <name>My name</name>
  <email>my-address@wherever.com</email>
  <uri>http://wherever.com/</uri>
 </author>
 <category term="author-date"/>
 <category term="zoology"/>
 <updated>2008-10-29T21:01:24+00:00</updated>
 <summary>My great new style format.</summary>
 <rights>This work is licensed under a Creative Commons
         Attribution-Share Alike 3.0 Unported License
         http://creativecommons.org/licenses/by-sa/3.0/</rights>
</info>
```

Many elements available in the info section are borrowed from the [Atom Syndication Format](http://tools.ietf.org/html/rfc4287):

-   `id`: this required field should preferably be a valid, stable, and unique URL if the style is to be made publicly available. Make sure you choose the id carefully, as it will be used to identify the style (if a style is installed in Zotero, it will overwrite an already present style with the same id). For styles uploaded to the [Zotero Style Repository](http://www.zotero.org/styles) this can be the link to your schema (e.g. <http://www.zotero.org/styles/your-style-filename>).
-   `title`: name of the style (required). The title is shown in the Zotero Style Repository.
-   `author`/`contributor`/`translator`(:!:): people who write a new style, or make significant changes can claim authorship (see example above). For smaller changes the contributor role can be used. In both cases one should supply a name. An email-address and URI are optional.
-   `updated`: the contents of this required element is used to assess whether the style has changed since the last time it has been accessed or cached. If uploading to the Zotero Style Repository, the timestamp will be generated automatically. The syntax of the timestamp is described [here](http://books.xmlschemata.org/relaxng/ch19-77049.html).
-   `published`: similar to updated, this element contains a timestamp, in this case the timepoint when the style was initially created or first made available.
-   `category`: styles can be divided in a number of categories. This information can be used to ease browsing of large style repositories and could allow users to subscribe to styles within particular content areas. The different types of categories are:
    -   the style's class, which describes how in-text citations are rendered:
        -   `author-date`: e.g. "... (Doe, 1999)"
        -   `numeric`: e.g. "... [1]"
        -   `label`: " ... [doe99]."
        -   `note`: the citation appears as a footnote or endnote
        -   `in-text`: the full citation appears in-line
    -   the field(s) the style applies to (the `generic-base` category is meant for generic styles like Harvard and APA): `anthropology`, `astronomy`, `biology`, `botany`, `chemistry`, `communications`, `engineering`, `generic-base`, `geography`, `geology`, `history`, `humanities`, `law`, `literature`, `math`, `medicine`, `philosophy`, `physics`, `psychology`, `sociology`, `science`, `political_science`, `social_science`, `theology`, `zoology`
-   `rights`: a license dictating how the style file may be modified and distributed by others. See, e.g. <http://creativecommons.org/license/>
-   `issn`: a style written for a specific journal can include the journal's ISSN (International Standard Serial Number). N.B. currently Zotero only supports a single ISSN. There are plans to add a `issnl` element to allow for inclusion of the ISSN-L, and also to allow for multiple ISSNs (as many journals have both a print and online ISSN).

## Citation

The `citation` construct is a key part of the style, and describes how in-line citations should be formatted. Sometimes a citation will only be a simple number, in other cases a more elaborate citation is desired, as is the case for author-date styles. The basic structure of the `citation` construct is as follows:

``` xml
<citation>
  <option />
  <layout>
    some layout
  </layout>
</citation>
```

The `layout` specifies what information should be included in the citation. Additional control is possible with a range of options, which will be discussed later. Already for the `layout` element itself some optional parameters can be set, the most common being a prefix, suffix and delimiter. The delimiter functions in distinguishing multiple items in a single citation. For instance

``` xml
<layout prefix="(" suffix=")" delimiter="; ">
```

would result in a citation like "(item1;item2)", where the contents of the `layout` element would describe how item1 and item2 should be formatted (e.g. as "(Doe 1999; Johnson 2002)").

## Bibliography

This is the second of the key parts, where the bibliography is formatted. It is very similar to the citations section.

``` xml
<bibliography>
  <option .../>
  <layout>
    ...
  </layout>
</bibliography>
```

Again, a set of options to control some of the layout, then the layout itself.

## Macros

A list of macro definitions is usually included between the `info` and `citation` sections. These are sort of like subroutines that can be called later in the description to make similar styles for parts.
**Effective use of macros is a key to making good styles**. Ideally, in fact, the main layout sections for the citation and bibliography should be quite simple, and simply call a series of macros.

An example macro is

``` xml
<macro name="editor-translator">
  <names variable="editor translator" prefix="(" suffix=")" delimiter=", ">
    <name and="symbol" initialize-with=". " delimiter=", "/>
    <label form="short" prefix=", " text-transform="capitalize" suffix="."/>
  </names>
</macro>
```

It is particularly crucial in author-date styles that rely on author names for sorting that one create a macro that can handle a wide variety of cases, including resources that do no include listed authors. Example:

``` xml
<macro name="author">
  <names variable="author">
    <name name-as-sort-order="all" 
          and="symbol" 
          sort-separator=", " 
          initialize-with=". "
          delimiter=", " 
          delimiter-precedes-last="always"/>
    <label form="short" prefix=" (" suffix=".)" text-transform="capitalize"/>
    <substitute>
      <names variable="editor"/>
      <names variable="translator"/>
      <text macro="title"/>
    </substitute>
  </names>
</macro>
```

This example includes the logic that allows the formatter to gracefully adapt to a wide-range of resource types. Likewise, one could create a macro for titles like so:

``` xml
  <macro name="title">
    <choose>
      <if type="book">
        <text variable="title" text-case="sentence" font-style="italic"/>
      </if>
      <else>
        <text variable="title" text-case="sentence"/>
      </else>
    </choose>
  </macro>
```

Note here that CSL reserves three types as generic fallbacks. In this case, for example, "book" is a generic fallback for all resources that have the characteristic that they are essentially self-contained items. So, for example, a music album will use this rule in the absence of any rules specific to its type.

Because of the value of macros and the potential to reuse them in different styles and automated software tools, it is recommended that you try to adapt common macro names, such as:

-   title
-   author
-   author-short
-   editor-translator
-   publisher
-   access (for URLs and archival locations)
-   event (for conference, hearings, etc.)
-   issued
-   issued-year
-   pages
-   citation-locator (for cited pages and such)
-   locators (volume and issue, for example)
-   container-prefix (for the "In" and such that often preceded container info)
-   edition (for edition or version info)

## Terms

CSL provides a number of localized strings like "et al.", "vol.", and "edited by". However, in some cases you might want to change these preset strings. Specifying terms via the `terms` element allows you to do just that. Usually this element is included just below the `info` element. An example is shown below:

``` xml
<terms>
  <locale xml:lang="en">
    <term name="editor" form="verb-short">ed. by</term>
    <term name="editor" form="short">
      <single>edtr</single>
      <multiple>edtrs</multiple>
    </term>
  </locale>
</terms>
```

A complete list of localized terms, together with their translations, can be found in the [Zotero SVN repository](https://www.zotero.org/trac/browser/extension/branches/2.0/chrome/content/zotero/locale/csl).

# Citation-Bibliography-Macro Syntax

Most of following syntax applies to the `macro`, `citation` and `bibliography` sections.

## Options

Styles are partially configured by setting a number of options. Some of these options are available in both the `citation` and `bibliography` sections, while others are specific to one of the two sections. Below a description and example is given for each option.

### Common options

These apply to both `citation` and `bibliography` sections.

-   et-al-min - the minimum length of contributor lists (e.g. of authors or editors) for et-al abbreviation to kick in.

``` xml
<option name="et-al-min" value="6"/>
```

-   et-al-use-first - if et-al abbreviation is used, the number of contributors to be included before the et-al part.

``` xml
<option name="et-al-use-first" value="6"/>
```

### Citation only options

-   et-al-subsequent-min - the minimum authors for et-al in subsequent references.

``` xml
<option name="et-al-subsequent-min" value="6"/>
```

-   et-al-subsequent-use-first - the minimum authors for et-al in subsequent references.

``` xml
<option name="et-al-subsequent-use-first" value="1"/>
```

-   disambiguate-add-year-suffix a true/false to indicate how to disambiguate two references that are otherwise the same. This adds a suffix to the year, so you'll get 2007a, 2007b etc.

``` xml
<option name="disambiguate-add-year-suffix" value="true"/>
```

-   disambiguate-add-names - add additional names, disregarding the "et-al" setting, to disambiguate the citations.

``` xml
<option name="disambiguate-add-names" value="true"/>
```

-   disambiguate-add-givenname - add a given name to a citation to disambiguate authors with the same last name, so J. Doe, 2005 compared to M. Doe, 2005.

``` xml
<option name="disambiguate-add-givenname" value="true"/>
```

-   collapse - this allows citations to be collapsed into an abbreviated style. The value is one of the following:
    -   citation-number - collapses numeric citations from [1, 2, 3] to [1-3]
    -   year - collapses multiple references to the same author to just the years. So (Doe 2000, Doe 2001) collapses to (Doe 2000, 2001).
    -   year-suffix - collapses like in the year option, but also collapses (Doe 2000a, Doe 2000b) to (Doe 2000a, b). This is ignored if the disambiguate-add-year-suffix is not in use.

### Bibliography only options

-   hanging-indent - formats the bibliography with a hanging indent.

``` xml
<option name="hanging-indent" value="true"/>
```

-   second-field-align - values of true or margin. It is most useful with numbered items and allows the number to be placed in the margin.

``` xml
<option name="second-field-align" value="margin"/>
```

-   subsequent-author-substitute - substitutes subsequent recurrences of an author for a given string, such as "--- --- ---". Help wanted here!

``` xml
<option subsequent-author-substitute="some text"/>
```

-   Spacing in the Bibliography is controlled by the "entry-spacing" and "line-spacing" options

``` xml
<option name="entry-spacing" value="0"/>
<option name="line-spacing" value="2"/>
```

## Sorting

The sorting order for in-text citation groups [e.g. (Doe 2001; Johnson 2003)], and for the bibliography can be set with the `sort` element, in which one or multiple sort keys can be specified. Sort keys can consist of either variables or macros, e.g.:

``` xml
<citation>
  <sort>
    <key macro="author"/>
    <key variable="issued" sort="descending"/>
  </sort>
</citation>
```

In this example, citations are first sorted by the output of the author macro. Multiple entries that share the same author macro output are further sorted in reverse order by date of issue (if not specified, the value of the `sort` attribute is assumed to be "ascending"). Using macros instead of variables as sort keys is especially useful in case of substitutions (e.g., if no authors are specified, sort according to the translators/editors), or when sorting should be according to year instead of date of issue.

## Variables

These are the variables that can be used in the layout. They can also be tested in the `<if>` syntax, and displayed with the `<text variable="title">` syntax. They map to various things in the zotero entries. Some of them are available in both short and long form.

-   title - maps to the **Title** field in the long form, and the **Short Title** in the short form.
-   container-title - maps to **Publication**, **Website Title**, **reporter**, **code**
-   collection-title - maps to **Series**, **Series Title**
-   collection-number - maps to **Series Number**
-   original-title - no mapping.
-   publisher - maps to **Publisher**, **Distributor**, **University**
-   publisher-place - maps to **Place**.
-   event - maps to **Meeting Name**, **Conference Name**
-   event-place - maps to **Place**
-   page - maps to **Pages**
-   number-of-pages - maps to **# of Pages**.
-   references - maps to **History** (Bill)
-   locator - maps to the location in the cite dialog.
-   version - maps to **Version**
-   volume - maps to **Volume**.
-   number-of-volumes - maps to **# of Volumes**.
-   issue - maps to **Issue**.
-   medium - maps to **Medium** (Interview), **Format** (Film, Videorecording, Audiorecording)
-   status - no mapping
-   section - maps to **Section** (Bill)
-   edition - maps to **Edition**.
-   genre - maps to **Type**, **Artwork Size**.
-   note - maps to **Extra**
-   annote - no mapping.
-   authority - maps to **Court** (Case)
-   abstract - maps to **Abstract**.
-   keyword - no mapping.
-   number - maps to **Bill Number**, **Docket Number**
-   archive - maps to **Repository**.
-   archive_location - maps to **Loc. in Archive**.
-   archive-place - no mapping.
-   URL - maps to **URL**.
-   DOI - maps to **DOI**.
-   ISBN - maps to **ISBN**.
-   citation-number - maps to the number of the citation.
-   citation-label - no mapping.

## Authors

These are the types of author that can be used in the layout. They can be displayed with the `<names>` syntax. They map to various things in the zotero entries. Some of them are available in both short and long form.

-   author - maps to the **Author** field.
-   editor - maps to the **Editor**.
-   translator - maps to the **Translator**.
-   publisher - no mapping.
-   original-author - no mapping.
-   original-publisher - no mapping.
-   recipient - no mapping
-   interviewer - no mapping
-   collection-editor - maps to the **Series Editor** field.
-   composer - no mapping

Author markup is done using the `<names>` and `<name>` directives.
The names wraps the whole thing, and the name how to format an individual.
The names also allows a &lt;substitute&gt; block to fill in with other syntax.
For the &lt;name&gt; block, there are a number of options that can be specified, besides the generic formatting:

-   form - long or short.
-   and - set to either *symbol* to use & or *text* to use the word "and" to combine authors.
-   delimiter - set to something like "," to separate names.
-   delimiter-precedes-last - *always* uses the delimiter even for the last author, *never* doesn't.
-   name-as-sort-order - determines the order of *last name* and *first name*(initials). No entry has all authors as *firstname-lastname*, "first" displays only the first author as *lastname-firstname*, "all" displays all authors as *lastname-firstname*.
-   sort-separator - some text to separate the first and last names.
-   initialize-with - the text to follow each initial and a directive to use initials.

e.g.,

``` xml
<names variable="author">
 <name form="short" and="symbol" delimiter=", " initialize-with=". "/>
</names>
```

The &lt;substitute&gt; comes into play if the named author variable is missing. It allows other things to be substituted. For instance

``` xml
<names variable="author">
 <name name-as-sort-order="all" and="symbol" sort-separator=", " initialize-with=". "
    delimiter=", " delimiter-precedes-last="always"/>
 <label form="short" prefix=" (" suffix=".)" text-transform="capitalize"/>
 <substitute>
   <names variable="editor"/>
   <names variable="translator"/>
   <text macro="title"/>
 </substitute>
</names>
```

would fill in with the editor, translator or the title in that order.

## Dates

There are various date fields that can be used. These are typically displayed with the `<date>` markup.

-   issued - maps to the **Date**.
-   event - no mapping
-   accessed - maps to **Accessed**.
-   container - no mapping.

Dates are processed with the `<date>` and `<date-part>` markup.
The `<date>` part is a wrapper around the block, and specifies the date you are working with. This usually encapsulates a sequence of `<date-part>` directives. The date as a whole can have the usual formatting directives.
The &lt;date-part&gt; lets you format individual parts of the date. The parameters, apart from the usual formatting constructs, are

-   month - which can also have the form attributes
    -   short (e.g. Jan)
    -   long (e.g. January)
    -   numeric (e.g. 1)
    -   numeric-leading-zeros (e.g. 01)
-   day - which can also have the form attributes
    -   numeric (e.g. 1)
    -   numeric-leading-zeros (e.g. 01)
    -   ordinal (e.g. 1st)
-   year - which can be with form short or long. (e.g. 05 or 2005)
-   other - other bits of the date (time maybe) also in short/long form.

For example:

``` xml
<date variable="issued" suffix=";">
   <date-part name="year" suffix=" "/>
   <date-part name="month" form="short" suffix=" "/>
   <date-part name="day"/>
</date>
```

Although a delimiter can be specified in the date part, it is used to separate multiple dates and not to separate parts of the date. Therefore prefix and suffix are important in the date-part.

## Text

The &lt;text&gt; directive is the way to include text in the output from a variety of sources. For example:

``` xml
<text variable="title" prefix=" Title: " form="short"/>
```

The first parameter can be one of:

-   variable - include the contents of a variable.
-   macro - output the results of evaluating a macro.
-   term - output a specific term which is subject to localisation
-   value - output a given bit of verbatim text.

Other parameters you can include are

-   form - either short or long, only makes sense with certain variables (otherwise defaults to long).
-   include-period - true/false term that adds a '.' if parameter is of type "term" and the term used is an abbreviation, not a long form or symbol

You can also include any of the Formatting directives.

## Formatting

The following formatting parameters for most elements specifying output.

-   **`prefix`**: text to insert before the main output
-   **`suffix`**: text to insert after the main output
-   **`font-family`**: which font family to use.
-   **`font-style`**: `normal`, `italic` or `oblique` (slanted).
-   **`font-variant`**: `normal` or `small-caps`.
-   **`font-weight`**: `normal`, `bold` or `light`.
-   **`text-decoration`**: `none` or `underline`.
-   **`text-case`** (modifies the capitalization of the text): `lowercase`, `uppercase`, `capitalize-first`, `capitalize-all`, `title`, `sentence`.
-   **`vertical-align`**: `baseline`, `sup` or `sub`.
-   **`display`**: if set to `block` makes this a block of separate text.
-   **`quotes`**: true/false to include quotes around it.

For instance

``` xml
<text variable="edition" prefix=" " suffix=" ed. "/>
<text term="retrieved" text-transform="capitalize" suffix=" "/>
```

## Labels

Labels are used to add common text that may be dependent on the item. An example is
the label for pages, which can be p. or pp. depending on the number of pages referenced.
For instance

``` xml
<group prefix=" (" suffix=")">
  <label variable="page" form="short" suffix=". "/>
  <text variable="page"/>
</group>
```

`locator` is the other variable commonly used.
Label elements allow for the usual text formatting, the choice between different forms (short, long, etc.) and an option to include a trailing '.'.
Labels can also be applied without a variable inside a `<names>` element. In this case, the label is the role label (e.g., "edited by")

## Groups

The group construct allows you to group together elements with a format applied to the whole group.

``` xml
<group delimiter=": ">
 <text variable="publisher-place"/>
 <text variable="publisher"/>
</group>
```

The group is ignored if it contains no variables that exist in the document, even if it contains locale terms. A group can also represent semantic document components, as in:

``` xml
<group class="container" prefix=". ">
```

## Conditionals

Conditional information is tested with the `<if>` construct, which must be embedded in a &lt;choose&gt; block. There is an &lt;else-if&gt; and an `<else>` to allow multi-way choices.
It is common in bibliographies to do different arrangements based on the type, as in

``` xml
<choose>
  <if type="book">
    ...
  </if>
  <else-if type="chapter">
    ...
  </else-if>
  <else>
    ...
  </else>
</choose>
```

Things that can be tested are type's as above, variables (which includes authors and dates). Also are a few meta variables which include

-   `position` which can be tested against `first`, `subsequent`, `ibid`, `ibid-with-locator`. The first time a citation is made to a certain item, the position will be `first`. If the next citation again references that item, the position becomes `ibid`, or, if a locator is added in the Insert Citation window, `ibid-with-locator`. Finally, if the same item is again referenced after some other items have been cited, the position becomes `subsequent`.
-   `disambiguate` which can be tested against true/false. This allows two citations to see if they are the same still.
-   `locator` which can be compared against locator types such as `page`, `chapter`, `verse` etc.
-   `match` - this allows and/or/not like behaviour by setting against `all`/`any`/`none`. This is required if you test multiple types or variables too.

Multiple variables can be tested as in

``` xml
<if type="chapter book" match="any">
```

## Item Types

Here is a list of Zotero item types which have a specific mapping ([a complete table of item types and associated field mappings is available here](http://aurimasv.github.io/z2csl/typeMap.xml)). For example your CSL code must use "paper-conference" if you want to refer to the "Conference Paper" type. Note that some item types are not, at the moment, mapped (e.g.: encyclopediaArticle).
These types can be tested in the `<if>` syntax.

-   article-journal - maps to **journalArticle** Type
-   article-magazine - maps to **magazineArticle**
-   article-newspaper - maps to **newspaperArticle**
-   thesis - maps to **thesis**
-   paper-conference - maps to **conferencePaper**
-   personal_communication - maps to **letter**, **email** and **instantMessage**
-   manuscript - maps to **manuscript**
-   interview - maps to **interview**
-   motion_picture - maps to **film**
-   graphic - maps to **artwork**
-   webpage - maps to **webpage**
-   report - maps to **report**
-   bill - maps to **bill**, **hearing** (?) and **statute** (?)
-   legal_case - maps to **case**
-   patent - maps to **patent**
-   map - maps to **map**
-   book - maps to **computerProgram** (?)
-   webpage - maps to **blogPost** and **forumPost**
-   song - maps to **audioRecording** (?) and **podcast** (?)
-   speech - maps to **presentation**
-   motion_picture - maps to **videoRecording**
-   broadcast - maps to **tvBroadcast** and **radioBroadcast**

However CSL reserves some types as generic fallbacks. Thus, for example, a film will use the rule which has been defined for book in the absence of any rules specific to its type.

You must test a specific type before its generic fallback. For instance, as "book" is the fallback for "film", you need to test for "film" *before* testing for "book" if you want it to work correctly.

-   "book" is a generic fallback for **book**, **film**, **artwork**, **report**, **bill**, **case**, **hearing**, **statute**, **audioRecording**, **videoRecording** and **computerProgram**.
-   "article" is a generic fallback for **journalArticle**, **magazineArticle**, **newspaperArticle**, **thesis**, **letter**, **manuscript**, **interview**, **webpage**, **patent**, **email**, **map**, **blogPost**, **instantMessage**, **forumPost**, **tvBroadcast**, **radiobroadcast**, **podcast** and **presentation**.
-   "chapter" is a generic fallback for **bookSection**, **encyclopediaArticle**, **dictionaryEntry**, **conferencePaper**.
