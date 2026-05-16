<p id="zotero-5-update-warning" style="color: red; font-weight: bold">We’re
in the process of updating the documentation for
<a href="https://www.zotero.org/blog/zotero-5-0">Zotero 5.0</a>. Some documentation
may be outdated in the meantime. Thanks for your understanding.</p>

# Zotero Server Write API

**This is version 1 of the Zotero Server API. For new development, use [API version 2](dev/server_api/v2/).**

This page documents the write methods of the [Zotero Server API](dev/server_api/v1/). See the [Read API](dev/server_api/v1/read_api) page for basic information on accessing the API, including possible HTTP status codes not listed here.

An API key with write access to a given library is necessary to use write methods.

To-do:

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
  "notes" : []
}
```

    GET /items/new?itemType=note
    If-Modified-Since: Mon, 14 Mar 2011 22:30:17 GMT

``` javascript
{
  "itemType" : "note",
  "note" : "",
  "tags" : []
}
```

Adding attachments is not yet supported.

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

## Write Requests

### Creating an Item

    POST /users/1/items
    Content-Type: application/json
    X-Zotero-Write-Token: 19a4f01ad623aa7214f82347e3711f56

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
      "notes" : [
        {
          "itemType" : "note",
          "note" : "<p>What a <strong>great</strong> book!</p>"
        }
      ]
    }
  ]
}
```

All fields other than `itemType` are optional.

Note content will be treated as HTML and sanitized automatically.

<table>
  <thead>
    <tr><th colspan="2">Common responses</th></tr>
  </thead>
  <tbody>
    <tr><td><code>201 Created</code></td><td>Item(s) successfully created --- see example Atom response below</td></tr>
    <tr><td><code>400 Bad Request</code></td><td>Invalid type/field; unparseable JSON</td></tr>
    <tr><td><code>409 Conflict</code></td><td>The target library is locked.</td></tr>
    <tr><td><code>412 Precondition Failed</code></td><td>The provided <code>X-Zotero-Write-Token</code> has already been submitted.</td></tr>
    <tr><td><code>413 Request Entity Too Large</code></td><td>Too many items submitted</td></tr>
  </tbody>
</table>

Example `201 Created` response:

``` xml
<?xml version="1.0"?>
<feed xmlns="http://www.w3.org/2005/Atom" xmlns:zapi="http://zotero.org/ns/api">
  <title>Zotero / Zotero User / Items</title>
  <id>http://zotero.org/users/1/items?itemKey=ABCD2345</id>
  <link rel="self" type="application/atom+xml" href="https://api.zotero.org/users/1/items?itemKey=ABCD2345"/>
  <link rel="first" type="application/atom+xml" href="https://api.zotero.org/users/1/items?itemKey=ABCD2345"/>
  <link rel="last" type="application/atom+xml" href="https://api.zotero.org/users/1/items?itemKey=ABCD2345"/>
  <zapi:totalResults>1</zapi:totalResults>
  <zapi:apiVersion>1</zapi:apiVersion>
  <updated>2010-12-17T00:18:51Z</updated>
    <entry>
      <title>My Book</title>
      <author>
          <name>Zotero User</name>
          <uri>http://zotero.org/zuser</uri>
      </author>
      <id>http://zotero.org/users/zuser/items/ABCD2345</id>
      <published>2010-12-17T00:18:51Z</published>
      <updated>2010-12-17T00:18:51Z</updated>
      <link rel="self" type="application/atom+xml" href="https://api.zotero.org/users/1/items/ABCD2345?content=json"/>
      <link rel="alternate" type="text/html" href="http://zotero.org/users/zuser/items/ABCD2345"/>
      <zapi:key>ABCD2345</zapi:key>
      <zapi:itemType>book</zapi:itemType>
      <zapi:creatorSummary>McAuthor</zapi:creatorSummary>
      <zapi:numChildren>1</zapi:numChildren>
      <zapi:numTags>2</zapi:numTags>
      <content type="application/json" etag="8e984e9b2a8fb560b0085b40f6c2c2b7">
        {
          "itemType" : "book",
          "title" : "My Book",
          "creators" : [
            {
              "creatorType" : "author",
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
          ]
        }
      </content>
    </entry>
</feed>
```

### Creating Multiple Items

JSON for multiple items can be passed in the `items` array. A maximum of 50 items can be added in a single request.

### Updating an Existing Item

First, retrieve the current version of the item, specifying JSON as the format for the Atom `<content>` node:

    GET /users/1/items/ABCD2345?content=json

See [Creating an Item](#creating_an_item) above for an example response.

Next, modify the JSON and resubmit to the server. Include the value of the `<content>` node's `etag` attribute in the `If-Match` HTTP header:

    PUT /users/1/items/ABCD2345
    Content-Type: application/json
    If-Match: "8e984e9b2a8fb560b0085b40f6c2c2b7"

``` javascript
{
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
      "name" : "John T. Singlefield"
    }
  ],
  "tags" : [
    { "tag" : "awesome" },
    { "tag" : "rad", "type" : 1 }
  ]
}
```

All fields other than `itemType`, `creators`, and `tags` are optional. If `creators` and/or `tags` are empty, any associated creators and/or tags will be removed from the item.

Child notes can be added only with new items. To add child notes to an existing item, POST an `items` array containing note items to `/users/<userID>/items/<itemKey>/children`.

PUT requests must include an `If-Match` header with an ETag provided by a previous request for the item. If the item has been changed on the server since the item was retrieved, the PUT request will be rejected with a `412 Precondition Failed` error, and the most recent version of the item will have to be retrieved from the server before changes can be made.

<table>
  <thead>
    <tr><th colspan="2">Common responses</th></tr>
  </thead>
  <tbody>
    <tr><td><code>200 OK</code></td><td>Same as Atom response above, but with updated data.</td></tr>
    <tr><td><code>400 Bad Request</code></td><td>Invalid type/field; unparseable JSON; client did not include ETag.</td></tr>
    <tr><td><code>409 Conflict</code></td><td>The target library is locked.</td></tr>
    <tr><td><code>412 Precondition Failed</code></td><td>The item has changed since retrieval (i.e., the provided ETag no longer matches).</td></tr>
  </tbody>
</table>

### Deleting an Item

    GET /users/1/items/ABCD2345?content=json

    DELETE /users/1/items/ABCD2345
    If-Match: "8e984e9b2a8fb560b0085b40f6c2c2b7"

<table>
  <thead>
    <tr><th colspan="2">Common responses</th></tr>
  </thead>
  <tbody>
    <tr><td><code>204 No Content</code></td><td>The item was deleted.</td></tr>
    <tr><td><code>409 Conflict</code></td><td>The target library is locked.</td></tr>
    <tr><td><code>412 Precondition Failed</code></td><td>The item has changed since retrieval (i.e., the provided ETag no longer matches).</td></tr>
  </tbody>
</table>

### Adding Items to a Collection

    POST /users/1/collections/QRST9876/items

    ABCD2345 BCDE3456 CDEF4567 DEFG5678

The POST body is a space-delimited list of item keys from the same library as the collection. Existing items not specified will not be removed from the collection.

Child items cannot be added directly to collections.

<table>
  <thead>
    <tr><th colspan="2">Common responses</th></tr>
  </thead>
  <tbody>
    <tr><td><code>204 No Content</code></td><td>Items were added to collection.</td></tr>
    <tr><td><code>400 Bad Request</code></td><td>Item not found in library; attempt to add child item to collection.</td></tr>
    <tr><td><code>409 Conflict</code></td><td>The target library is locked.</td></tr>
  </tbody>
</table>

### Removing an Item from a Collection

    DELETE /users/1/collections/QRST9876/items/ABCD2345

<table>
  <thead>
    <tr><th colspan="2">Common responses</th></tr>
  </thead>
  <tbody>
    <tr><td><code>204 No Content</code></td><td>Item was removed from the collection.</td></tr>
    <tr><td><code>409 Conflict</code></td><td>The target library is locked.</td></tr>
  </tbody>
</table>

### Creating a Collection

    POST /users/1/collections
    Content-Type: application/json
    X-Zotero-Write-Token: 19a4f01ad623aa7214f82347e3711f56

``` javascript
{
  "name" : "My Collection",
  "parent" : "QRST9876"
}
```

<table>
  <thead>
    <tr><th colspan="2">Common responses</th></tr>
  </thead>
  <tbody>
    <tr><td><code>201 Created</code></td><td>The collection was created.</td></tr>
    <tr><td><code>409 Conflict</code></td><td>The target library is locked.</td></tr>
    <tr><td><code>412 Precondition Failed</code></td><td>The provided X-Zotero-Write-Token has already been submitted.</td></tr>
  </tbody>
</table>

### Updating an Existing Collection

    GET /users/1/collections/RSTU8765?content=json

    PUT /users/1/collections/RSTU8765
    Content-Type: application/json
    If-Match: "f0ebb2240a57f4115b3ce841d5218fa2"

``` javascript
{
  "name" : "My Collection",
  "parent" : false
}
```

<table>
  <thead>
    <tr><th colspan="2">Common responses</th></tr>
  </thead>
  <tbody>
    <tr><td><code>200 OK</code></td><td>The collection was updated.</td></tr>
    <tr><td><code>409 Conflict</code></td><td>The target library is locked.</td></tr>
    <tr><td><code>412 Precondition Failed</code></td><td>The collection has changed since retrieval (i.e., the provided ETag no longer matches).</td></tr>
  </tbody>
</table>

### Deleting a Collection

    GET /users/1/collections/RSTU8765?content=json

    DELETE /users/1/collections/RSTU8765
    If-Match: "f0ebb2240a57f4115b3ce841d5218fa2"

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

### X-Zotero-Write-Token

    X-Zotero-Write-Token: 19a4f01ad623aa7214f82347e3711f56

`X-Zotero-Write-Token` is an optional HTTP header, containing a client-generated identifier string between 8 and 32 characters in length, that can be included with item and collection creation requests to prevent them from being processed more than once (e.g., if a user clicks a form submit button twice). The Zotero server caches write tokens for successful requests for 12 hours, and subsequent requests from the same API key using the same write token will be rejected with a `412 Precondition Failed` status code. If a request fails, the write token will not be stored.
