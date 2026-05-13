# Direct Access to the Zotero SQLite Database

While it is generally preferable to access Zotero library data via either the [Web API](dev/web_api) or [JavaScript API](dev/client_coding/javascript_api), it is also possible to directly access the SQLite database of the Zotero client using an SQLite client, library, or third-party tool. All library data is stored in an SQLite database, zotero.sqlite, within the [Zotero data directory](zotero_data).

However, **access to the SQLite database should be done only in a read-only manner.** Modifying the database while Zotero is running can easily result in a corrupted database. A caching layer breaks the normal file-locking in SQLite that allows for safe concurrent file access, and even if Zotero is shut down before accessing the file, modifying the database directly bypasses the data validation and referential integrity checks performed by Zotero and the Zotero web API that are required for Zotero to function properly. Generally, the SQLite database should be viewed as an internal database that has the benefit of being externally readable for people who want to get the data out in other ways.

Also be aware that the SQLite database structure can change between Zotero releases.

# Zotero Client Data Model

Each bibliographic record in Zotero has an "item type" (book, journal article, thesis, …), a set of fields (author, title, date, …), and field values. The selection of fields depends on the item type.

Item types and fields, as well as mappings to CSL types and fields and translations into various languages, are defined in the [Zotero data schema](https://github.com/zotero/zotero-schema/tree/master). Zotero can be used in many languages, but you should always refer to item types and fields with their internal name as defined in the data schema.

In theory, you can change and add item types and fields, but this will break Zotero sync and may make break many parts of Zotero functionality, such as item import and citation formatting. If you need to add additional information to your records, you should use the "Extra" field that is available for all item types.

In addition to the basic item types and fields, each item can have associated user data, including:

-   a set of notes
-   a set of attachments
-   a set of tags
-   a set of links to related items

Attachments (PDFs, snapshots, etc.) are stored inside the [Zotero data directory](zotero_data), in separate subdirectories named after the key of the item they belong to.

For a list of the internal names of fields, their English equivalents, and their CSL mappings, see the [CSL/Zotero Metadata Field Index](https://aurimasv.github.io/z2csl/typeMap.xml).
