## Reports

Reports are simple HTML pages that give an overview of the item metadata, notes, and attachments of the selected items. You can print them, post them to the web, and email them.

![](/_media/report.png){ width=600 }

### Generating Reports

To create a report, right-click (ctrl-click on macOS) an item or a selection of items in the center pane and select "Generate Report from Selected Item(s)…". You can also right-click a collection in the left column and select "Generate Report from Collection".

![](https://www.zotero.org/static/images/support/report_from_items.png)

### Sharing and Printing Reports

Reports can be saved by selecting "File -> Save…" in the File menu, and printed by selecting File -> "Print…".

### Working with and Searching Reports

To copy text from a report, highlight the text and type Ctr/Cmd-C or select "Copy" from the "Edit" menu. Searching currently does not work in the Zotero Report Viewer. However, if you save a Report to your computer ("File -> Save…"), you can open it in your browser and search there.

### Sort Order

By default reports sort items alphabetically by title in ascending order. Sorting within the Zotero report window is not currently possible. You can, however, customize the sort order for reports by generating them from a [Collection](collections_and_tags#collections) or [Saved Search](searching#saved_searches).

If you right-click on a collection or Saved Search in Zotero's left pane, then choose "Generate Report from Collection/Saved Search", Zotero will use the current sort order of the columns in the Zotero center pane for the report. To generate a report for an entire library, first make a Saved Search with the parameters: `Title` `contains` `%`, then right-click on this Saved Search.

### Customizing Reports

It's not currently possible to customize which fields are included in Reports within Zotero itself, but there are [third-party options](plugins#zotero_reports) for doing so.

### Uses For Reports

#### Reviewing Abstracts

If you need to review a large number of papers' titles, authors, and abstracts (e.g., if you are conducting a systematic review using Zotero), reports can provide a convenient layout for reading the abstracts and writing notes in the margins.

#### Teaching

Reports can also be used in teaching to track and assess students during the process of collecting information and writing. Reports show when items were collected, how students associate their items with notes and tags, and how students are interpreting their research items. Reports can also be a useful tool for discussing sources with students and guiding the research, organization, and writing process.

#### Organizing Notes into Outlines

While Zotero has not been designed to be an outlining tool, you can create outlines from notes. By default, reports list child notes together with their parent items. To include child notes in your outline and separate them from their parent items, change the "extensions.zotero.report.combineChildItems" [hidden preference](preferences/hidden_preferences) to "false".

Then, to build your outline, add an outline number at the beginning of each note you want to include, e.g. 1.1, 1.2, 2.1. Select the notes in Zotero, then right-click and generate a report from them.

If you are working with a large number of notes and you do not want to manually select each one, Tags and Advanced Searches can make life easier. First, tag each note with a description, such as "chapter one" or "methods". Then create an Advanced Search for "Item Type" "is" "Note" and "Tag" "is" "chapter one". Save the Advanced Search, then right-click the Saved Search and choose "Generate Report from Saved Search…". This will create a report including only the notes tagged "chapter one".

### Disabled Features

Zotero 5.0 opens reports in a window without an address bar or a right-click menu. As a result, several features that were previously available in Zotero for Firefox are [currently disabled](reports/disabled_features).

-   Sorting (but see the workaround [above](#sort_order))
-   Searching (but see the workaround [above](#working_with_and_searching_reports))
-   Copying from right-click menu (but see available methods [above](#working_with_and_searching_reports))
