# Full-Text Content Requests

This page documents the methods to access full-text content of Zotero items via the [Zotero Server API](dev/web_api/v2/start). See the [Read Requests](dev/web_api/v2/read_requests) page for basic information on accessing the API, including possible HTTP status codes not listed here.

### Getting new full-text content

    GET <userOrGroupPrefix>/fulltext?newer=<version>

    Content-Type: application/json
    Last-Modified-Version: <library version>

``` javascript
{
    "<itemKey>": <version>,
    "<itemKey>": <version>,
    "<itemKey>": <version>
}
```

For each item with a full-text content version greater than stored locally, get the item's full-text content, as described below.

<table>
  <thead>
    <tr><th colspan="2">Common responses</th></tr>
  </thead>
  <tbody>
    <tr><td><code>200 OK</code></td><td>Full-text content was successfully retrieved.</td></tr>
    <tr><td><code>400 Bad Request</code></td><td>The 'newer' parameter was not provided.</td></tr>
  </tbody>
</table>

### Getting an item's full-text content

    GET <userOrGroupPrefix>/items/<itemKey>/fulltext

`<itemKey>` should correspond to an existing attachment item.

    Content-Type: application/json
    Last-Modified-Version: <version of item's full-text content>

``` javascript
{
    "content": "This is full-text content.",
    "indexedPages": 50,
    "totalPages": 50
}
```

`indexedChars` and `totalChars` may be provided instead of `indexedPages` and `totalPages`.

<table>
  <thead>
    <tr><th colspan="2">Common responses</th></tr>
  </thead>
  <tbody>
    <tr><td><code>200 OK</code></td><td>Full-text content was found for the given item.</td></tr>
    <tr><td><code>404 Not Found</code></td><td>The item wasn't found, or no full-text content was found for the given item.</td></tr>
  </tbody>
</table>

### Setting an item's full-text content

    PUT <userOrGroupPrefix>/items/<itemKey>/fulltext
    Content-Type: application/json

``` javascript
{
    "content": "This is full-text content.",
    "indexedChars": 26,
    "totalChars": 26
}
```

`<itemKey>` should correspond to an existing attachment item.

`indexedPages` and `totalPages` can be provided instead of `indexedChars` and `totalChars`.

<table>
  <thead>
    <tr><th colspan="2">Common responses</th></tr>
  </thead>
  <tbody>
    <tr><td><code>204 No Content</code></td><td>The item's full-text content was updated.</td></tr>
    <tr><td><code>400 Bad Request</code></td><td>Invalid JSON was provided.</td></tr>
    <tr><td><code>404 Not Found</code></td><td>The item wasn't found or was not an attachment.</td></tr>
  </tbody>
</table>

### Searching for items by full-text content

See the `q` and `qmode` [search parameters](dev/web_api/v2/read_requests#search_parameters).
