The Zotero 5.0 Report Viewer does not include an address bar, so it is not currently possible to change item sorting in Reports. The Search function is also currently not working (but see [a workaround](reports/reports#working_with_and_searching_reports)).

The Sort syntax that was previously available in Zotero for Firefox is described below.

### Sort Order

By default reports sort items alphabetically by title in ascending order. You can change the sort order by appending "?sort=" to the report's URL, followed by the item field(s) you would like to sort by. Use a comma to separate the different fields. To use a descending sort order, add "/d" after the field name. For example, a URL of a report that is first sorted by title in ascending order, and then by date in descending order looks like:

    zotero://report/items/0_KKZSDPI2/html/report.html?sort=title,date/d

You can sort by the following fields:

<table>
  <tbody>
    <tr><td>?sort=title</td><td>?sort=firstCreator</td></tr>
    <tr><td>?sort=date</td><td>?sort=accessed</td></tr>
    <tr><td>?sort=dateAdded</td><td>?sort=dateModified</td></tr>
    <tr><td>?sort=publicationTitle</td><td>?sort=publisher</td></tr>
    <tr><td>?sort=itemType</td><td>?sort=series</td></tr>
    <tr><td>?sort=type</td><td>?sort=medium</td></tr>
    <tr><td>?sort=callNumber</td><td>?sort=pages</td></tr>
    <tr><td>?sort=archiveLocation</td><td>?sort=DOI</td></tr>
    <tr><td>?sort=ISBN</td><td>?sort=ISSN</td></tr>
    <tr><td>?sort=edition</td><td>?sort=url</td></tr>
    <tr><td colspan="2">?sort=rights</td></tr>
  </tbody>
</table>

When a report is generated from a collection rather than from items selected in the center column, Zotero by default uses the order in which the items are shown in the center column.
