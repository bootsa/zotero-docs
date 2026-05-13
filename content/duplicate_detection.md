# Duplicate Detection

As you build your Zotero library, you might introduce a few duplicated items. For example, you could have saved the same item twice from a webpage, or imported items already in your library. Fortunately, Zotero can help you identify possible duplicates and allow you to merge them.

## Finding Duplicates

Clicking on the "Duplicate Items" collection in your library or right-clicking the library in the left pane and selecting "Show Duplicates" will show the items Zotero thinks are duplicates in the center pane.

![](/_media/duplicate_detection.png){ .align-right width=706 }

Zotero currently uses the the title, DOI, and ISBN fields to determine duplicates. If these fields match (or are absent), Zotero also compares the years of publication (if they are within a year of each other) and author/creator lists (if at least one author last name plus first initial matches) to determine duplicates. The algorithm will be improved in the future to incorporate other fields.

At this time, it is not possible to mark false positive matches as non-duplicates. This functionality will be added in the future.

Note that duplicate detection only works *within a library*. Items in different group libraries are [separate items](groups#interact_with_groups_through_the_zotero_client). They won't show up in the "Duplicate Items" collection of any one of the libraries.

## Merging Duplicates

You should always resolve duplicate items by merging them, rather than deleting one of the duplicates. Merges will retain all of the collections and tags of the merged items; deleting one item will lose these data. Merges are also automatically recognized by the [word processor plugins](word_processor_integration) and don't affect your automatically generated citations and bibliographies.

To merge items in the "Duplicate Items" collection, select an item in the center pane. Zotero will automatically co-select the other items that it thinks are duplicates. Click the "Merge &lt;number&gt; Items" button in the right pane to merge the items. If the item fields don't match completely, you can select one item to be the "master" from the list at the top of the right pane, then select alternative versions of mismatched fields using the icons to the right of each field.

![](/_media/duplicate_detection_select.png){ .align-right width=706 }

It may be easier to see which items are selected if you [sort the items by Title](sorting). You can select a single item in the "Duplicate Items" view by holding down Alt/Option while clicking. You can de-select an item from a set of duplicates by holding down Ctrl (Windows/Linux) or Cmd (Mac) while clicking.

You can also select a group of two or more items *of the same item type* anywhere in your Zotero library, right-click, and select "Merge Items…" from the context menu.
