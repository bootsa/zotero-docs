# Locate Menu

![](/_media/locate/locate-menu.png){ .align-right }

The Locate menu offers several ways to access files in your library and to look up items online. The menu can be opened by clicking the straight arrow button (![](/_media/locate/toolbar-go-arrow.png)) at the top-left of the right-hand column of the Zotero pane.

Which menu entries are available depends on the type of items you have selected in the middle column. The possible options are:

-   **View File/PDF/Snapshot** - open the files/PDFs/snapshots of the items
-   **View Online** - look up the items online, using its URL, DOI, or child link's URL
-   **Show File** - locates the files/PDFs of the items on your computer
-   **Library Lookup** - looks up the items in your library of choice using OpenURL
-   **CrossRef Lookup** - looks up and resolves the DOI of the items
-   **Manage Lookup Engines…** -- See [#Managing Lookup Engines](#Managing Lookup Engines)

## Library Lookup

The Library Lookup option lets you locate items in an online library catalog so you can track down a physical or online full-text copy of the resource. You'll need to select your library's OpenURL resolver from the [Advanced tab](preferences/advanced#openurl) of the Zotero [preferences](preferences) (or the General tab in Zotero 7).

If your library's resolver isn't in [Zotero's OpenURL resolver directory](locate/openurl_resolvers), you can enter the address manually. Most university libraries provide their OpenURL resolver address on their websites.

## Managing Lookup Engines

The "Manage Lookup Engines…" option opens the Article Lookup Engine Manager window, where you can enable/disable lookup engines, remove installed lookup engines, or reset your installed lookup engines to the defaults.

It is not currently possible to add new lookup engines using through either the Zotero desktop client or the browser Connector extensions. To add new lookup engines, you must edit the `engines.json` file located in the `locate` folder in your [Zotero data directory](zotero_data). Lookup engines can be added to this file using JSON syntax specifying an [OpenSearch lookup engine](dev/creating_locate_engines_using_opensearch). A more user-friendly way to add lookup engines will be added in a future version.

An `engines.json` file with a variety of useful lookup engines is available from <https://github.com/bwiernik/zotero-tools>. To use this file, download it and place it in the `locate` folder in your [Zotero data directory](zotero_data) (replacing the version of `engines.json` that is already present). You can remove unwanted engines from the "Manage Lookup Engines…" in the Zotero Locate menu.

## Public Library Lookup Engines

A repository of thousands of local public library Lookup Engines (as well as engines for some universities and commercial databases) is available from <http://egh.github.io/zotero-lookup-engines>.
