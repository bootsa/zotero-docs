# Editing CSL Styles - Step-by-Step Guide

## CSL Visual Editor

An open source, visual CSL editor has been developed in a collaboration of Columbia University Library and Mendeley. You can find the editor [here](http://editor.citationstyles.org/about/)
and a usage guide [here](https://github.com/citation-style-editor/csl-editor/wiki/User-guide-for-the-CSL-Editor). If you have trouble editing styles you can still ask for help on the Zotero forums. You can report bugs [here](https://github.com/citation-style-editor/csl-editor/issues) - make sure you're reporting reproducible errors. The github issue tracker is not the place for questions.

## Manually Editing CSL styles

In many cases you may still want to manually edit CSL styles. This guide provides easy to follow steps.

### 1 - Start with the Right Style

Start by checking the [Zotero Style Repository](styles). If you want to improve an existing CSL style, make sure that you start from the most recent version (the repository shows the date and time each style was last updated). If you want to create a new style, find the style that most closely matches what you need using the previews in the style repository.
Typically the best way to find a most similar style is the "[search by Example](http://editor.citationstyles.org/searchByExample/)" function of the visual style editor.

### 2 - Edit the Style

Download the style you want to edit to your computer, and open it in a (plain) text editor like Notepad on Windows, TextEdit on Mac OS X (select "Make Plain Text" under "Format"), or gedit in Linux. Other options are [Notepad++](http://notepad-plus-plus.org/) for Windows, [TextWrangler](http://www.barebones.com/products/TextWrangler/) for Mac OS X, [oXygen XML Editor](http://www.oxygenxml.com/), [Emacs in nXML mode](http://www.thaiopensource.com/nxml-mode/), and [jEdit](http://www.jedit.org/), which all support XML syntax highlighting (CSL is an XML-based language) and in some cases also real-time [validation against the CSL schema](https://github.com/citation-style-language/styles/wiki/Validation).

Paste the style code into the [Zotero CSL Editor](dev/citation_styles/reference_test_pane), so you instantly see the effect of code changes on the style output. If you make your edits directly in the test pane, save your edits often via your text editor or using the "Save" button ![dev/citation_styles/csledit-save.png](/_media/dev/citation_styles/csledit-save.png), as changes in the test pane get lost easily.

See the [documentation page](http://citationstyles.org/citation-style-language/documentation/) of the CSL project website for information on making CSL changes (in particular, make sure to take a look at the [CSL specification](http://citationstyles.org/downloads/specification.html). Below we discuss a few common and simple style edits to get you started.

#### Change the Style Title and ID

**Important:** Before installing your edited style, you must change the style title and ID at the top of the style code. If you don't change these, your modified style will be overwritten the next time the original style is updated.

The style title and ID are stored within the `<title/>` and `<id/>` elements near the top of the style. For example,

    <title>American Psychological Association 6th edition</title>
    <title-short>APA</title-short>
    <id>http://www.zotero.org/styles/apa</id>

can be changed to

    <title>American Psychological Association 6th edition Modified</title>
    <title-short>APA</title-short>
    <id>http://www.zotero.org/styles/apa-modified</id>

The URLs that you put in as an ID do not have to exist (i.e., you can use a zotero.org/style/mystyle type ID even if the style will not be posted on the Zotero repository).

#### Validation

Before installing a modified style, always make sure it is valid XML and CSL by [validating against the CSL schema](https://github.com/citation-style-language/styles/wiki/Validation).

#### Examples Edits

##### Changing Punctuation

In this example, we want to display the publisher ("CSHL Press") and the location of the publisher ("Cold Spring Harbor, NY") in a bibliographic entry. While this can be achieved with the code

    <text variable="publisher"/>
    <text variable="publisher-place"/>

this would result in "CSHL PressCold Spring Harbor, NY". Fortunately, we can add some punctuation with the `prefix`, `suffix` and `delimiter` attributes. Let's say we want to separate the `publisher` and `publisher-place` by a comma-space, and wrap the whole in parentheses, i.e. "(CSHL Press, Cold Spring Harbor, NY)". This can be done with:

    <group delimiter=", " prefix="(" suffix=")">
      <text variable="publisher"/>
      <text variable="publisher-place"/>
    </group>

The advantage of use a `group` element is that whenever you have a `publisher`, but no `publisher-place`, you don't end up with incorrect punctuation: the output would become "(CSHL Press)". If you would set the punctuation directly onto the `text` elements, e.g.

``` xml
<text variable="publisher" prefix="("/>
<text variable="publisher-place" prefix=", " suffix=")"/>
```

you would lose the closing bracket, i.e. "(CSHL Press".

##### Changing Et-al Abbreviation

There are two main settings for et-al abbreviation (e.g., rendering the names "Doe, Smith & Johnson" as "Doe et al."). The minimum number of names that activates et-al abbreviation, and the number of names shown before "et al.".

In CSL, these settings can appear on the `style`, `citation`, `bibliography` or `names` elements in the form of the `et-al-min` and `et-al-use-first` attributes (it is possible to have separate settings for items that have been cited previously by using the `et-al-subsequent-min` and `et-al-subsequent-use-first` attributes).

For example,

``` xml
<citation et-al-min="3" et-al-use-first="1">
  ...
</citation>
```

will result in name lists like "Doe", "Doe & Smith" and, if there are three or more names, "Doe et al.". Try changing these numbers and observe the effect.

##### Changing Disambiguation

CSL offers multiple methods to disambiguate cites or names. For example, a style might normally render only the family name (e.g., "(Doe 1999, Doe 2002)"). If the authors are Jane Doe and Thomas Doe, these names can be disambiguated by adding initials or the full given names (e.g., "(J. Doe 1999, T. Doe 2002)").

Disambiguation methods are selected on the `citation` element. For example, to disable [given name disambiguation](kb/given_name_disambiguation), delete the `disambiguate-add-givenname` attribute, e.g. change

``` xml
<citation disambiguate-add-givenname="true">
  ...
</citation>
```

to

``` xml
<citation>
  ...
</citation>
```

##### Separation of authors

By default several authors are separated by a delimiter `, ` and the word `and`. This settings can be changed, for example to use the symbol `&` instead:

``` xml
<names variable="author">
  <name form="short" and="symbol" delimiter=", "/>
  ...
</names>
```

or to not use `and` at all, but to use the delimiter `/`:

``` xml
<names variable="author">
  <name form="short" delimiter="/"/>
  ..
</names>
```

##### Conditional Rendering (full footnote style)

The appearance of citations in (full) footnote styles may depend on their position in the paper. If the same source is cited twice, it may be that a shortened version is used in the second (and any further) citation. To handle this distinction, one can use [conditional rendering based on the position](http://citationstyles.org/downloads/specification.html#choose) of the citation. A generic structure could then look as

``` xml
<citation>
  <layout>
    <choose>
      <if position="ibid-with-locator">
        ...
      </if>
      <else-if position="ibid">
        ...
      </else-if>
      <else-if position="subsequent">
        ...
      </else-if>
      <else>
        ...
      </else>
    </choose>
  </layout>
</citation>
```

If a case is missing in your style, you can add that and fill out what and how the information should be rendered in that case ([an example of such a full footnote style](https://www.zotero.org/styles/chicago-fullnote-bibliography?source=1)).

### 3 - Install your Edited Style with Zotero

See [Citation Styles](styles).

Save the style with a ".csl" file extension (you can generally do this by simply typing ”.csl” after the name of your file). Then, go to the [Cite pane](preferences/cite) in the Zotero [preferences](preferences). Click on the "+" sign below the list of installed styles. In the file selection dialogue that opens, navigate to the .csl file you just created and open it. This will install your new style into the Zotero data directory.

### 4 - Sharing Styles

If you think that your modified style might be useful to other people, consider [submitting](https://github.com/citation-style-language/styles/blob/master/CONTRIBUTING.md) it to the [Zotero Style Repository](styles).

### Getting Help

If you get stuck at any point, try posting a question on the [Zotero forums](/forum/).
