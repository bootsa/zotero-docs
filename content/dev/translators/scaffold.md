# Scaffold - an IDE for Zotero translators

[Translators](dev/translators) are stored as individual JavaScript files with additional metadata at the top and tests at the bottom in the "translators" subdirectory of the [Zotero data directory](zotero_data). While translators can be edited with any tool, Scaffold is dedicated to writing Zotero translators, offering advantages such as real-time testing and debugging.

Scaffold supports editing and testing web translators and import translators. Search and export translators can not yet be tested using the IDE.

## Interface

Scaffold is available via Tools → Developer → Translator Editor in Zotero.

When you first open Scaffold, you'll need to select your translator development directory. In most cases, this should be a git clone of the [Zotero translators repository](https://github.com/zotero/translators) on GitHub.

After selecting your translator directory, the main Scaffold window will open:

![](/_media/dev/translators/scaffold_new_small.png){ width=750 }

### Top buttons

![](/_media/dev/load.png) **Open**  
Opens the "Load Translator" window. Select one of the currently installed translators, and load the translator metadata and code into Scaffold.

![](/_media/dev/save.png) **Save**  
Saves the translator you are currently working on. Provide a unique label and translator ID for your translator if you don't want to overwrite an existing translator. New translator IDs can be automatically generated via the "Generate" button.

![](/_media/dev/translators/savetozotero.png){ width=16 } **Save to Zotero**  
Saves the translator you are currently working on and writes it to the "translators" subdirectory of the Zotero data directory, making it available to the client and Zotero Connector. (To use it in the Connector, open the Connector preferences to the Advanced tab and click Reset Translators.)

![](/_media/dev/translators/detectweb.png){ width=16 } **Run detect**\*  
Saves and runs the appropriate `detect` function:

-   If it's a web translator and a page is loaded in the Browser tab: `detectWeb`
-   If it's an import translator and data has been entered in the Test Data tab: `detectImport`
-   If it's a search translator and a JSON search object has been entered in the Test Data tab: `detectSearch`

![](/_media/dev/translators/doweb.png){ width=16 } **Run do**\*  
Saves and runs the appropriate `do` function of the translator code. Runs the corresponding `do` functions for the above situations, plus:

-   If it's an export translator and an item is selected in the main Zotero window: `doExport`

### Tabs

**Metadata**  
Shows the translator metadata. Translator IDs can be generated via the "Generate" button. The target regular expression can be tested with the "Test Regex" button.

**Code**  
The text box in this tab contains the translator's JavaScript code. The editor supports syntax highlighting, folding of code parts, search and replace, basic type inference, code suggestions, Zotero-specific hints when hovering over an item type or translator UUID string, and more. The editor also integrates ESLint, and you'll be prompted to set it up when you begin using Scaffold.

**Tests**  
This tab contains the list of tests saved in the translator, as well as the raw JSON and expected output for each one. You can run or update tests from here. Create tests from the corresponding tab for the type of test you want to create (Browser or Test Data).

**Test Data**  
Input data for import and search translators.

**Browser**  
View sites and test detection and data extraction.

### Debug Output

The main strength of Scaffold is its ability to provide you with immediate feedback, which can dramatically speed up translator development. After a code change, a single click suffices to run the modified translator and generate debug output. The following types of debug output can be generated:

#### Metadata

When the "Test Regex" button in the "Metadata" tab is clicked, the regular expression in the target field is applied to the site loaded in the Browser tab. The debug window at the right of the Scaffold window will show whether the regular expression matches (`true` for a match, `false` for no match), e.g.:

    09:54:11 ===>true<===(boolean)

#### detectWeb and doWeb

When the "Run detectWeb" button is clicked, the `detectWeb` function of the translator will be executed. Similarly, clicking the "Run doWeb" button executes the translator's `doWeb` function.

Debug output for the `detectWeb` function shows what type of item is found on the loaded webpage, e.g.:

    19:19:43 detectWeb returned type "book"

Debug output for the `doWeb` function shows all the item data that would be saved if the translator would be run by Zotero (when testing translators with Scaffold, no items are actually saved to your Zotero library), e.g.:

    19:24:21 Returned item:
                 'itemType' => "book"
                 'creators' ...
                     '0' ...
                         'firstName' => "Herman"
                         'lastName' => "Melville"
                         'creatorType' => "author"
                 'notes' ...
                 'tags' ...
                 'seeAlso' ...
                 'attachments' ...
                     '0' ...
                         'title' => "Google Books Link"
                         'snapshot' => "false"
                         'mimeType' => "text/html"
                         'url' => "http://books.google.com/books?id=cYKYYypj8UAC"
                         'document' => "[object]"
                 'date' => "1851"
                 'pages' => "504"
                 'ISBN' => "1603033742, 9781603033749"
                 'publisher' => "Plain Label Books"
                 'title' => "Moby Dick"
                 'repository' => "Google Books"
                 'complete' => function(...){...} 
             
    19:24:21 Translation successful

If running `detectWeb` or `doWeb` results in an error, the debug window will show an error message. For debugging, additional debug output can be added to the code by adding `Zotero.debug(string);` statements.

## Import, Export, and Search Translators

Starting with version 6.0, Scaffold can be used to test import, export, and search translators. To test an import or search translator, enter the test data in the "Test Data" tab and use the "Run detect\*" and "Run \*" buttons to test the translator against the data. The output will be displayed in the right-hand pane as with web translators. For export translators, select an item in the main Zotero window to use it for testing.

In the translator load window, import translators are arranged in alphabetical order at the bottom of the list.

## Scaffold Troubleshooting

**Why does my translator work in Scaffold but not when I click the Save to Zotero button in my browser?**
Scaffold runs the functions `detectWeb` and `doWeb` against the document in the Browser tab. In your browser, clicking the toolbar button runs the first web translator with a matching `target` regular expression that returns a non-false value from the `detectWeb` function when run on that document and URL.

These results can differ when the `target` expression or `detectWeb` conditions are too lax, which can allow embedded documents, such as `iframe`s used for advertising or sharing panes, to be detected as content pages by the Zotero Connector. To see if this is what is happening, look at the Zotero Connector's debug output for a save attempt in your browser and check the URL that is being processed.

**Why won't my attachments save?**

The output pane in Scaffold shows the item object as Zotero is about to save it. It does not in fact save the object.

**Why do some fields show in the output pane but not in the created item?**

As an item is saved, the contents of some fields may change.

The attachment information in the output pane of Scaffold merely says what Zotero is going to try to save; as the attachments are saved, they may be discarded if their actual content type differs from the one specified, as can happen when PDFs or other attachments are hidden by providers behind an interstitial terms or copyright notice page.

Fields that are not allowed for the specified item type will be added to the Extra field, even if they show up in the output pane of Scaffold.

# Further Reading

More detailed instructions are available at [MediaWiki](https://www.mediawiki.org/wiki/Citoid/Creating_Zotero_translators). These instructions may be slightly out of date.
