# Changes from API Version 1

As [announced on zotero-dev](https://groups.google.com/d/msg/zotero-dev/egIdfVmWEeo/dkOfupK7EXoJ), version 2 of the [Zotero Web API](dev/web_api/v2/start) brings many changes to enable [API-based syncing](dev/web_api/v2/syncing). While read-only clients may continue to work properly, clients that write to the API are likely to need updating.

This page provides a brief summary of changes and may not be comprehensive. See the appropriate documentation sections for full details on all changes.

-   New: [API versioning](dev/web_api/v2/read_requests#api_versioning)
-   New: [Conditional read support](dev/web_api/v2/read_requests#caching)
-   New: [Multi-object modification](dev/web_api/v2/write_requests#updating_multiple_objects) and [multi-object deletion](dev/web_api/v2/write_requests#deleting_multiple_items)
-   New: [Delta writes](dev/web_api/v2/write_requests#partial_item_updating_patch)
-   Saved search metadata is now available via the API. It is not currently possible to retrieve the results of saved searches via the API.
-   Related items and relations are now available in the `relations` property of item JSON. Currently, only the RDF predicates used by Zotero itself are available.
-   Object ETags have been replaced by [library/object versions](dev/web_api/v2/syncing#version_numbers). `If-Match` has been replaced by `If-Unmodified-Since-Version` and JSON version properties.
-   Object writes no longer return Atom feeds with the newly created objects. Single-object writes return `204 No Content`, while [multi-object writes](dev/web_api/v2/write_requests#creating_multiple_objects) return `200 OK` with a JSON document indicating the status of each write.
-   `X-Zotero-Write-Token` has changed to `Zotero-Write-Token`.
-   Child items can no longer be created by including `note` or `attachment` properties when creating top-level items or by POSTing to `<userOrGroupPrefix>/items/<itemKey>/children`. Instead, child items can be created or moved by including a `parentItem` property in the item's JSON.
-   New collection JSON objects can no longer be POSTed directly. Instead, collections must be within a top-level `collections` object, similar to the `items` object used for items.
-   The `parent` property for collections has been changed to `parentCollection`.
-   The collections an item belongs to can be read and modified via the item's `collections` property. The previous POST and DELETE requests have been removed.
