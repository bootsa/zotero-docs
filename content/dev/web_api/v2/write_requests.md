# Zotero Server Write Requests

**This is version 2 of the Zotero Web API. For new development, use [API version 3](dev/web_api/v3/).**

This page documents the write methods of the [Zotero Web API](dev/web_api/v2/). See the [Read Requests](dev/web_api/v2/read_requests) page for basic information on accessing the API, including possible HTTP status codes not listed here.

An API key with write access to a given library is necessary to use write methods.

Not yet implemented:

-   Mappings caching (If-Modified-Since)
-   Non-English type/field locales

## Item Type/Field Requests

For an API client to present an editing UI to its users, it must know what combinations of Zotero item types, fields, and creator types are valid. Clients can request this data from the Zotero API.

As schema changes are currently rare, clients should cache type/field data for a period of time (e.g., one hour) without making further requests. Subsequent requests for new data should then include `If-Modified-Since` headers containing the contents of the `Last-Modified` header from the original response. If no changes have occurred, the server will return a `304 Not Modified` and clients should continue to use cached data for the same period of time.

User-friendly type/field names will be returned in English by default. Clients can request names in other languages by passing a `locale` parameter (e.g., `GET /itemTypes?locale=fr-FR`).

Hint: For manual viewing, add `pprint=1` to the following requests for easier-to-read output.

### Get All Item Types

    GET /itemTypes
    If-Modified-Since: Mon, 14 Mar 2011 22:30:17 GMT

``` javascript
[
  { "itemType" : "book", "localized" : "Book" },
  { "itemType" : "note", "localized" : "Note" },
  (…)
]
```

<table>
  <thead>
    <tr><th colspan="2">Common responses</th></tr>
  </thead>
  <tbody>
    <tr><td colspan="2"><code>200 OK</code></td></tr>
    <tr><td><code>304 Not Modified</code></td><td>No changes have occurred since <code>If-Modified-Since</code> time.</td></tr>
    <tr><td><code>400 Bad Request</code></td><td>Locale not supported.</td></tr>
  </tbody>
</table>

### Get All Item Fields

    GET /itemFields
    If-Modified-Since: Mon, 14 Mar 2011 22:30:17 GMT

``` javascript
[
  { "field" : "title", "localized" : "Title" },
  { "field" : "url", "localized" : "URL" },
  (…)
]
```

<table>
  <thead>
    <tr><th colspan="2">Common responses</th></tr>
  </thead>
  <tbody>
    <tr><td colspan="2"><code>200 OK</code></td></tr>
    <tr><td><code>304 Not Modified</code></td><td>No changes have occurred since <code>If-Modified-Since</code> time.</td></tr>
    <tr><td><code>400 Bad Request</code></td><td>Locale not supported.</td></tr>
  </tbody>
</table>

### Get All Valid Fields for an Item Type

Note: API consumers intending to write to the server should generally use [/items/new](#get_template_for_a_new_item) combined with [/itemTypes](#get_all_item_types) instead of this request.

    GET /itemTypeFields?itemType=book
    If-Modified-Since: Mon, 14 Mar 2011 22:30:17 GMT

``` javascript
[
  { "field" : "title", "localized" : "Title" },
  { "field" : "abstractNote", "localized" : "Abstract" },
  (…)
]
```

<table>
  <thead>
    <tr><th colspan="2">Common responses</th></tr>
  </thead>
  <tbody>
    <tr><td colspan="2"><code>200 OK</code></td></tr>
    <tr><td><code>304 Not Modified</code></td><td>No changes have occurred since <code>If-Modified-Since</code> time.</td></tr>
    <tr><td><code>400 Bad Request</code></td><td>Locale not supported.</td></tr>
  </tbody>
</table>

### Get Valid Creator Types for an Item Type

    GET /itemTypeCreatorTypes?itemType=book

``` javascript
[
  { "creatorType" : "author", "localized" : "Author" },
  { "creatorType" : "editor", "localized" : "Editor" },
  (…)
]
```

<table>
  <thead>
    <tr><th colspan="2">Common responses</th></tr>
  </thead>
  <tbody>
    <tr><td colspan="2"><code>200 OK</code></td></tr>
    <tr><td><code>304 Not Modified</code></td><td>No changes have occurred since <code>If-Modified-Since</code> time.</td></tr>
    <tr><td><code>400 Bad Request</code></td><td>'itemType' is unspecified or invalid; locale not supported.</td></tr>
  </tbody>
</table>

### Get Localized Creator Fields

    GET /creatorFields
    If-Modified-Since: Mon, 14 Mar 2011 22:30:17 GMT

``` javascript
[
  { "field" : "firstName", "localized" : "First" },
  { "field" : "lastName", "localized" : "Last" },
  { "field" : "name", "localized" : "Name" }
]
```

<table>
  <thead>
    <tr><th colspan="2">Common responses</th></tr>
  </thead>
  <tbody>
    <tr><td><code>304 Not Modified</code></td><td>No changes have occurred since <code>If-Modified-Since</code> time.</td></tr>
    <tr><td><code>400 Bad Request</code></td><td>Locale not supported.</td></tr>
  </tbody>
</table>

### Get Template for a New Item

    GET /items/new?itemType=book
    If-Modified-Since: Mon, 14 Mar 2011 22:30:17 GMT

``` javascript
{
  "itemType" : "book",
  "title" : "",
  "creators" : [
    {
      "creatorType" : "author",
      "firstName" : "",
      "lastName" : ""
    }
  ],
  "url" : "",
  (...),
  "tags" : [],
  "collections" : [],
  "relations" : {}
}
```

    GET /items/new?itemType=note
    If-Modified-Since: Mon, 14 Mar 2011 22:30:17 GMT

``` javascript
{
  "itemType" : "note",
  "note" : "",
  "tags" : [],
  "collections" : [],
  "relations" : {}
}
```

TODO: attachment creation (see [File Uploads](dev/web_api/v2/file_upload))

<table>
  <thead>
    <tr><th colspan="2">Common responses</th></tr>
  </thead>
  <tbody>
    <tr><td colspan="2"><code>200 OK</code></td></tr>
    <tr><td><code>304 Not Modified</code></td><td>No changes have occurred since <code>If-Modified-Since</code> time.</td></tr>
    <tr><td><code>400 Bad Request</code></td><td><code>itemType</code> is unspecified or invalid.</td></tr>
  </tbody>
</table>

## Item Requests

### Creating an Item

    POST <userOrGroupPrefix>/items
    Content-Type: application/json
    Zotero-Write-Token: <write token>

``` javascript
{
  "items" : [
    {
      "itemType" : "book",
      "title" : "My Book",
      "creators" : [
        {
          "creatorType":"author",
          "firstName" : "Sam",
          "lastName" : "McAuthor"
        },
        {
          "creatorType":"editor",
          "name" : "John T. Singlefield"
        }
      ],
      "tags" : [
        { "tag" : "awesome" },
        { "tag" : "rad", "type" : 1 }
      ],
      "collections" : [
        "BCDE3456", "CDEF4567"
      ],
      "relations" : {
        "owl:sameAs" : "http://zotero.org/groups/1/items/JKLM6543",
        "dc:relation" : "http://zotero.org/groups/1/items/PQRS6789",
        "dc:replaces" : "http://zotero.org/users/1/items/BCDE5432"
      }
    }
  ]
}
```

All properties other than `itemType`, `tags`, `collections`, and `relations` are optional.

<table>
  <thead>
    <tr><th colspan="2">Common responses</th></tr>
  </thead>
  <tbody>
    <tr><td><code>200 OK</code></td><td>The request completed. See the response JSON for status of individual writes.</td></tr>
    <tr><td><code>400 Bad Request</code></td><td>Invalid type/field; unparseable JSON</td></tr>
    <tr><td><code>409 Conflict</code></td><td>The target library is locked.</td></tr>
    <tr><td><code>412 Precondition Failed</code></td><td>The provided <code>Zotero-Write-Token</code> has already been submitted.</td></tr>
    <tr><td><code>413 Request Entity Too Large</code></td><td>Too many items submitted</td></tr>
  </tbody>
</table>

`200 OK` response:

``` javascript
{
  "success": {
    "0": "<itemKey>"
  },
  "unchanged": {},
  "failed": {},
  }
}
```

See [Creating Multiple Objects](#creating_multiple_objects) for more information on the response format.

### Creating Multiple Items

See [Creating Multiple Objects](#creating_multiple_objects).

### Updating an Existing Item

First, retrieve the current version of the item, specifying JSON as the format for the Atom `<content>` node:

    GET <userOrGroupPrefix>/items/<itemKey>?content=json

See [Creating an Item](#creating_an_item) above for an example response.

The API supports two ways of modifying item data: by uploading full item data (`PUT`) or by sending just the data that changed (`PATCH`).

#### Full-item updating (PUT)

With `PUT`, you submit full item JSON to the server, typically by modifying the downloaded JSON directly and resubmitting it:

    PUT <userOrGroupPrefix>/items/<itemKey>
    Content-Type: application/json

``` javascript
{
  "itemKey": "ABCD2345",
  "itemVersion": 1,
  "itemType" : "book",
  "title" : "My Amazing Book",
  "creators" : [
    {
      "creatorType":"author",
      "firstName" : "Sam",
      "lastName" : "McAuthor"
    },
    {
      "creatorType":"editor",
      "name" : "Jenny L. Singlefield"
    }
  ],
  "tags" : [
    { "tag" : "awesome" },
    { "tag" : "rad", "type" : 1 }
  ],
  "collections" : [
    "BCDE3456", "CDEF4567"
  ],
  "relations" : {
    "owl:sameAs" : "http://zotero.org/groups/1/items/JKLM6543",
    "dc:relation" : "http://zotero.org/groups/1/items/PQRS6789",
    "dc:replaces" : "http://zotero.org/users/1/items/BCDE5432"
  }
}
```

All properties other than `itemType`, `tags`, `collections`, and `relations` are optional. Any existing fields not specified will be removed from the item. If `creators`, `tags`, `collections`, or `relations` are empty, any associated creators/tags/collections/relations will be removed from the item.

#### Partial-item updating (PATCH)

With `PATCH`, you can submit just the properties that have actually changed, for a potentially much more efficient operation. Properties not included in the uploaded JSON are left untouched on the server. To clear a property, pass an empty string or an empty array as appropriate.

    PATCH <userOrGroupPrefix>/items/<itemKey>
    If-Unmodified-Since-Version: <version>

``` javascript
{
  "date" : "2013"
  "collections" : [
    "BCDE3456", "CDEF4567"
  ]
}
```

This would add a `date` field to the item and add it in the two specified collections if not already present. Array properties are interpreted as complete lists, so omitting a collection key would cause the item to be removed from that collection.

The `PATCH` behavior is also available when [modifying multiple items](dev/web_api/v2/write_requests#updating_multiple_objects) via `POST`.

#### Both PUT and PATCH

Notes and attachments can be made child items by assigning the parent item's key to the `parentItem` property. If parent and child items are created in the same request, the child items must appear after the parent item in the `items` array.

The item's current version number is included in the `itemVersion` JSON property, as well as in the `Last-Modified-Version` header of single-item requests. `PUT` and `PATCH` requests must include the item's current version number in either the `itemVersion` property or the `If-Unmodified-Since-Version` header. If the item has been changed on the server since the item was retrieved, the write request will be rejected with a `412 Precondition Failed` error, and the most recent version of the item will have to be retrieved from the server before changes can be made.

<table>
  <thead>
    <tr><th colspan="2">Common responses</th></tr>
  </thead>
  <tbody>
    <tr><td><code>204 No Content</code></td><td>The item was successfully updated.</td></tr>
    <tr><td><code>400 Bad Request</code></td><td>Invalid type/field; unparseable JSON</td></tr>
    <tr><td><code>409 Conflict</code></td><td>The target library is locked.</td></tr>
    <tr><td><code>412 Precondition Failed</code></td><td>The item has changed since retrieval (i.e., the provided item version no longer matches).</td></tr>
  </tbody>
</table>

### Updating Multiple Items

See [Updating Multiple Objects](#updating_multiple_objects).

### Deleting an Item

    GET <userOrGroupPrefix>/items/<itemKey>?content=json

Retrieve the version from the `Last-Modified-Version` response header.

    DELETE <userOrGroupPrefix>/items/<itemKey>
    If-Unmodified-Since-Version: <version>

<table>
  <thead>
    <tr><th colspan="2">Common responses</th></tr>
  </thead>
  <tbody>
    <tr><td><code>204 No Content</code></td><td>The item was deleted.</td></tr>
    <tr><td><code>409 Conflict</code></td><td>The target library is locked.</td></tr>
    <tr><td><code>412 Precondition Failed</code></td><td>The item has changed since retrieval (i.e., the provided item version no longer matches).</td></tr>
  </tbody>
</table>

### Deleting Multiple Items

Up to 50 items can be deleted in a single request.

    DELETE <userOrGroupPrefix>/items?itemKey=<key>,<key>,<key>
    If-Unmodified-Since-Version: <version>

    204 No Content
    Last-Modified-Version: <version>

<table>
  <thead>
    <tr><th colspan="2">Common responses</th></tr>
  </thead>
  <tbody>
    <tr><td><code>204 No Content</code></td><td>The items were deleted.</td></tr>
    <tr><td><code>409 Conflict</code></td><td>The target library is locked.</td></tr>
    <tr><td><code>412 Precondition Failed</code></td><td>The library has changed since the specified version.</td></tr>
  </tbody>
</table>

## Collection Requests

### Creating a Collection

    POST <userOrGroupPrefix>/collections
    Content-Type: application/json
    Zotero-Write-Token: <write token>

``` javascript
{
  "collections" : [
    {
      "name" : "My Collection",
      "parentCollection" : "QRST9876"
    }
  ]
}
```

<table>
  <thead>
    <tr><th colspan="2">Common responses</th></tr>
  </thead>
  <tbody>
    <tr><td><code>200 OK</code></td><td>The request completed without a general error. See the response JSON for status of individual writes.</td></tr>
    <tr><td><code>409 Conflict</code></td><td>The target library is locked.</td></tr>
    <tr><td><code>412 Precondition Failed</code></td><td>The provided Zotero-Write-Token has already been submitted.</td></tr>
  </tbody>
</table>

### Updating an Existing Collection

    GET <userOrGroupPrefix>/collections/<collectionKey>?content=json

    PUT <userOrGroupPrefix>/collections/<collectionKey>
    Content-Type: application/json
    If-Unmodified-Since-Version: <version>

``` javascript
{
  "name" : "My Collection",
  "parentCollection" : false
}
```

<table>
  <thead>
    <tr><th colspan="2">Common responses</th></tr>
  </thead>
  <tbody>
    <tr><td><code>200 OK</code></td><td>The collection was updated.</td></tr>
    <tr><td><code>409 Conflict</code></td><td>The target library is locked.</td></tr>
    <tr><td><code>412 Precondition Failed</code></td><td>The collection has changed since retrieval (i.e., the provided collection version no longer matches).</td></tr>
  </tbody>
</table>

### Collection-Item Membership

Items can be added to or removed from collections via the `collections` property in the item JSON.

### Deleting a Collection

    GET <userOrGroupPrefix>/collections/<collectionKey>?content=json

    DELETE <userOrGroupPrefix>/collections/<collectionKey>
    If-Unmodified-Since-Version: <version>

<table>
  <thead>
    <tr><th colspan="2">Common responses</th></tr>
  </thead>
  <tbody>
    <tr><td><code>204 No Content</code></td><td>The collection was deleted.</td></tr>
    <tr><td><code>409 Conflict</code></td><td>The target library is locked.</td></tr>
    <tr><td><code>412 Precondition Failed</code></td><td>The collection has changed since retrieval (i.e., the provided ETag no longer matches).</td></tr>
  </tbody>
</table>

### Deleting Multiple Collections

Up to 50 collections can be deleted in a single request.

    DELETE <userOrGroupPrefix>/collections?collectionKey=<collectionKey>,<collectionKey>,<collectionKey>
    If-Unmodified-Since-Version: <version>

    204 No Content
    Last-Modified-Version: <version>

<table>
  <thead>
    <tr><th colspan="2">Common responses</th></tr>
  </thead>
  <tbody>
    <tr><td><code>204 No Content</code></td><td>The collections were deleted.</td></tr>
    <tr><td><code>409 Conflict</code></td><td>The target library is locked.</td></tr>
    <tr><td><code>412 Precondition Failed</code></td><td>The library has changed since the specified version.</td></tr>
  </tbody>
</table>

## Saved Search Requests

### Creating a Search

    POST <userOrGroupPrefix>/search
    Content-Type: application/json
    Zotero-Write-Token: <write token>

``` javascript
{
  "searches": [
    {
      "name": "My Search",
      "conditions": [
        {
          "condition": "title",
          "operator": "contains",
          "value": "foo"
        },
        {
          "condition": "date",
          "operator": "isInTheLast",
          "value": "7 days"
        }
      ]
    }
  ]
}
```

<table>
  <thead>
    <tr><th colspan="2">Common responses</th></tr>
  </thead>
  <tbody>
    <tr><td><code>201 Created</code></td><td>The search was created.</td></tr>
    <tr><td><code>409 Conflict</code></td><td>The target library is locked.</td></tr>
    <tr><td><code>412 Precondition Failed</code></td><td>The provided Zotero-Write-Token has already been submitted.</td></tr>
  </tbody>
</table>

### Deleting Multiple Searches

Up to 50 searches can be deleted in a single request.

    DELETE <userOrGroupPrefix>/searches?searchKey=<searchKey>,<searchKey>,<searchKey>
    If-Unmodified-Since-Version: <version>

    204 No Content
    Last-Modified-Version: <version>

<table>
  <thead>
    <tr><th colspan="2">Common responses</th></tr>
  </thead>
  <tbody>
    <tr><td><code>204 No Content</code></td><td>The searches were deleted.</td></tr>
    <tr><td><code>409 Conflict</code></td><td>The target library is locked.</td></tr>
    <tr><td><code>412 Precondition Failed</code></td><td>The library has changed since the specified version.</td></tr>
  </tbody>
</table>

## Tag Requests

### Deleting Multiple Tags

Up to 50 tags can be deleted in a single request.

    DELETE <userOrGroupPrefix>/tags?tag=<URL-encoded tag 1> || <URL-encoded tag 2> || <URL-encoded tag 3>
    If-Unmodified-Since-Version: <version>

    204 No Content
    Last-Modified-Version: <version>

## Multi-Object Requests

### Creating Multiple Objects

Up to 50 collections, saved searches, or items can be created in a single request by including multiple objects in the `collections`, `searches`, or `items` property:

    POST <userOrGroupPrefix>/collections
    Content-Type: application/json
    Zotero-Write-Token: <write token>

``` javascript
{
  "collections": [
    {
      "name" : "My Collection",
      "parentCollection": "QRST9876"
    },
    {
      "name": "My Other Collection"
    }
  ]
}
```

For syncing objects with predetermined keys, an object key can also be provided with new objects. See the [Syncing](dev/web_api/v2/syncing) documentation for more information.

200 response:

    Content-Type: application/json
    Last-Modified-Version: <version>

``` javascript
{
  "success": {
    "0": "<objectKey>",
    "2": "<objectKey>"
  },
  "unchanged": {
    "4": "<objectKey>"
  }
  "failed": {
    "1": {
      "key": "<objectKey>",
      "code": <HTTP response code>,
      "message": "<error message>"
    },
    "3": {
      "key": "<objectKey>",
      "code": <HTTP response code>,
      "message": "<error message>"
    },
  }
}
```

The keys of the `success`, `unchanged`, and `failed` objects are the numeric indexes of the Zotero objects in the uploaded array. The `Last-Modified-Version` is the version that has been assigned to any Zotero objects in the `success` object.

<table>
  <thead>
    <tr><th colspan="2">Common responses</th></tr>
  </thead>
  <tbody>
    <tr><td><code>200 OK</code></td><td>The objects were uploaded.</td></tr>
    <tr><td><code>409 Conflict</code></td><td>The target library is locked.</td></tr>
    <tr><td><code>412 Precondition Failed</code></td><td>The provided Zotero-Write-Token has already been submitted.</td></tr>
  </tbody>
</table>

#### Updating Multiple Objects

Up to 50 collections, saved searches, or items can be updated in a single request.

Follow the instructions in [Creating Multiple Objects](#creating_multiple_objects), but add an `itemKey`, `collectionKey`, or `searchKey` property to each object. Pass the current library version as `If-Unmodified-Since-Version`, replacing `Zotero-Write-Token`, or include an `itemVersion`, `collectionVersion`, or `searchVersion` in each object.

Items can also include `dateAdded` and `dateModified` properties containing UTC timestamps in SQL DATETIME format (e.g., "2012-10-03 16:42:12"). If `dateAdded` is included with an existing item, it must match the existing `dateAdded` value or else the API will return a 400 error. If a new `dateModified` time is not included with an update to existing item, the item's `dateModified` value will be set to the current time.

Creators, tags, and relations are included in item objects and cannot be modified separately.

    POST <userOrGroupPrefix>/collections
    Content-Type: application/json
    If-Unmodified-Since-Version: <version>

``` javascript
{
  "collections": [
    {
      "collectionKey": "BD85JEM4",
      "name": "My Collection",
      "parentCollection": false
    },
    {
      "collectionKey": "MNC5SAPD",
      "name": "My Subcollection",
      "parentCollection": "BD85JEM4"
    }
  ]
}
```

The response is the same as that in [Creating Multiple Objects](#creating_multiple_objects).

Note that `POST` follows `PATCH` semantics, meaning that any properties not specified will be left untouched on the server. To erase an existing property, include it with an empty string or `false` as the value.

## Zotero-Write-Token

    Zotero-Write-Token: 19a4f01ad623aa7214f82347e3711f56

`Zotero-Write-Token` is an optional HTTP header, containing a client-generated identifier string between 8 and 32 characters in length, that can be included with item and collection creation requests to prevent them from being processed more than once (e.g., if a user clicks a form submit button twice). The Zotero server caches write tokens for successful requests for 12 hours, and subsequent requests from the same API key using the same write token will be rejected with a `412 Precondition Failed` status code. If a request fails, the write token will not be stored.
