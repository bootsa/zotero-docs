<p id="zotero-5-update-warning" style="color: red; font-weight: bold">We’re
in the process of updating the documentation for
<a href="https://www.zotero.org/blog/zotero-5-0">Zotero 5.0</a>. Some documentation
may be outdated in the meantime. Thanks for your understanding.</p>

# Zotero Server Read Requests

**This is not currently the default [version](dev/server_api/v2/read_requests#api_versioning) of the Zotero API. Include the HTTP header `Zotero-API-Version: 2` to access this version.**

The page documents read requests available in the [Zotero Server API](dev/server_api/v2/start), providing read-only access to online Zotero libraries.

## Base URL

The base URL for all API requests is

    https://api.zotero.org

All requests must use HTTPS rather than HTTP.

## API Versioning

**To use this version of the API, include the HTTP header `Zotero-API-Version: 2` with all requests.** The current default version is [version 1](dev/server_api/v1), which will be discontinued in the near future.

At most times, there is only one active API version, and changes are made in a backwards-compatible manner. On rare occasions, however, backwards-incompatible changes may need to be made. When this occurs, the new API version will first be made available via an HTTP header, `Zotero-API-Version: <version>`, while all other clients continue to receive the old version. After a transition period, the new API version will become the default. At that point, the previous API version may be discontinued, with the new API version being returned even to clients requesting the previous version. Announcements regarding API version transitions will always be made ahead of time on [zotero-dev](https://groups.google.com/group/zotero-dev).

The API version of a response will be returned in the `Zotero-API-Version` response header.

## Authentication

Accessing non-public data via the API requires use of an API key. Third-party developers should [use OAuth to establish credentials](dev/server_api/v2/oauth) or instruct their users to create dedicated keys for use with their services. End users can create API keys via [their Zotero account settings](/settings/keys/new).

## GET Requests

Requests for data in a specific library begin with `/users/<userID>` or `/groups/<groupID>`. User IDs are different from usernames and can be found on the [API Keys](/settings/keys) page and in OAuth responses.

### Requests for "/users/&lt;userID&gt;" or "/groups/&lt;groupID&gt;"

| URI                                                           | Description                                                            |
|---------------------------------------------------------------|------------------------------------------------------------------------|
| &lt;userOrGroupPrefix&gt;/items                                    | The set of all items in the library                                    |
| &lt;userOrGroupPrefix&gt;/items/top                                | The set of all top-level items in the library                          |
| &lt;userOrGroupPrefix&gt;/items/trash                              | The set of items in the trash                                          |
| &lt;userOrGroupPrefix&gt;/items/&lt;itemKey&gt;                         | A specific item in the library                                         |
| &lt;userOrGroupPrefix&gt;/items/&lt;itemKey&gt;/children                | The set of all child items under a specific item                       |
| &lt;userOrGroupPrefix&gt;/items/&lt;itemKey&gt;/tags                    | The set of all tags associated with a specific item                    |
| &lt;userOrGroupPrefix&gt;/tags                                     | The set of all tags in the library                                     |
| &lt;userOrGroupPrefix&gt;/tags/<url+encoded+tag>                  | The set of tags (i.e., of all types) matching a specific name          |
| &lt;userOrGroupPrefix&gt;/collections                              | The set of collections in the library                                  |
| &lt;userOrGroupPrefix&gt;/collections/top                          | The set of all top-level collections in the library                    |
| &lt;userOrGroupPrefix&gt;/collections/&lt;collectionKey&gt;             | A specific collection in the library                                   |
| &lt;userOrGroupPrefix&gt;/collections/&lt;collectionKey&gt;/collections | The set of subcollections within a specific collection in the library  |
| &lt;userOrGroupPrefix&gt;/collections/&lt;collectionKey&gt;/items       | The set of all items within a specific collection in the library       |
| &lt;userOrGroupPrefix&gt;/collections/&lt;collectionKey&gt;/items/top   | The set of top-level items within a specific collection in the library |
| &lt;userOrGroupPrefix&gt;/collections/&lt;collectionKey&gt;/tags        | The set of tags within a specific collection in the library            |
| &lt;userOrGroupPrefix&gt;/searches                                 | The set of all saved searches in the library                           |
| &lt;userOrGroupPrefix&gt;/searches/&lt;searchKey&gt;                    | A specific saved search in the library                                 |

### Requests Specific to "/users/&lt;userID&gt;"

| URI                          | Description                                                                                                                                                     |
|------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| /users/&lt;userID&gt;/groups      | The set of groups the current API key has access to, including public groups the key owner belongs to even if the key doesn't have explicit permissions for it. |
| /users/&lt;userID&gt;/keys/&lt;key&gt; | The privileges of the given API key.                                                                                                                            |

## URL Parameters

All parameters are optional.

### Parameters for All Requests

<table>
<thead>
<tr class="header">
<th>Parameter</th>
<th>Values</th>
<th>Default</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>format</td>
<td>"atom", "bib", "keys", "versions", <a href="#export_formats">export formats</a></td>
<td>"atom"</td>
<td>"atom" will return an Atom feed.<br />
"bib", valid only for item requests, will return a formatted bibliography as XHTML. "bib" mode is currently limited to a maximum of 150 items.<br />
"keys", valid for multi-object requests, will return a newline-separated list of object keys. "keys" mode has no default or maximum limit.<br />
"versions", valid for multi-object collection, item, search, and tag requests, will return a JSON object with Zotero object keys as keys and object versions as values. Like "keys", "versions" mode has no default or maximum limit.<br />
Export formats, valid only for item requests, produce output in the specified format. The 'limit' parameter is required for multi-item export format requests.</td>
</tr>
<tr class="even">
<td>newer</td>
<td>integer</td>
<td>0</td>
<td>Return only objects modified after the specified library verson.</td>
</tr>
<tr class="odd">
<td>key</td>
<td>string</td>
<td>null</td>
<td>If a valid API key is provided, the request will be processed with the identity of the key's owner and the authority granted to the key.</td>
</tr>
</tbody>
</table>

### Search Parameters

| Parameter | Values                           | Default            | Description                                                                                                                                                     |
|-----------|----------------------------------|--------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| itemKey   | string                           | null               | A comma-separated list of item keys. Valid only for item requests. Up to 50 items can be specified in a single request.                                         |
| q         | string                           | null               | Quick search. Searches titles and individual creator fields by default. Use the `qmode` parameter to change the mode. Currently supports phrase searching only. |
| qmode     | "titleCreatorYear", "everything" | "titleCreatorYear" | Quick search mode. To include full-text content in the search, use "everything". Searching of other fields will be possible in the future.                      |
| itemType  | [search syntax](#search_syntax)  | null               | Item type search                                                                                                                                                |
| tag       | [search syntax](#search_syntax)  | search syntax      | Tag search                                                                                                                                                      |

### Search Syntax

`itemType` and `tag` parameters support Boolean searches:

Examples:

-   "itemType=book"
-   "itemType=book `||` journalArticle" (OR)
-   "itemType=-attachment" (NOT)
-   "tag=foo"
-   "tag=foo bar" (tag with space)
-   "tag=foo&tag=bar" (AND)
-   "tag=foo bar `||` bar" (OR)
-   "tag=-foo" (NOT)
-   "tag=\\-foo" (literal first-character hyphen)

### Parameters for "format=atom", "format=keys", and "format={export_format}"

The following parameters are valid only when accessing a resource that represents a set of objects. For example, `/users/123/items` represents a set of items, while `/users/123/items/ABCD2345` represents a single item.

| Parameter | Values                                                                                                                                                                                                                    | Default           | Description                                                                                                 |
|-----------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------|-------------------------------------------------------------------------------------------------------------|
| order     | "dateAdded", "dateModified", "title", "creator", "type", "date", "publisher", "publicationTitle", "journalAbbreviation", "language", "accessDate", "libraryCatalog", "callNumber", "rights", "addedBy", "numItems" (tags) | dateAdded         | The name of the field by which entries are ordered                                                          |
| sort      | "asc", "desc"                                                                                                                                                                                                             | varies by "order" | The sorting direction of the field specified in the `order` parameter                                       |
| limit     | integer 1-99\*                                                                                                                                                                                                            | 50\*              | The maximum number of results to return with a single request. Required for export formats.                 |
| start     | integer                                                                                                                                                                                                                   | 0                 | The index of the first result. Combine with the limit parameter to select a slice of the available results. |

\* Applies to `format=atom` and `format={export_format}` only. `format=keys` and `format=versions` have no default or maximum limit.

### Parameters for "format=atom" and "format={export_format}"

<table>
<thead>
<tr class="header">
<th>Parameter</th>
<th>Values</th>
<th>Default</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>pprint</td>
<td>boolean</td>
<td>false</td>
<td>Pretty print the response:<br />
<code>format=atom</code>: Outputs the response with content type <code>text/xml</code> instead of <code>application/atom+xml</code> and adds a long comment before to disable Firefox's feed auto-detection.<br />
<code>format={export_format}</code>: Outputs the response with content type <code>text/plain</code> for easier display in browsers.</td>
</tr>
</tbody>
</table>

### Parameters for "format=atom"

<table>
<thead>
<tr class="header">
<th>Parameter</th>
<th>Values</th>
<th>Default</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>content</td>
<td>"html", "json", "bib", <a href="#export_formats">export formats</a>, "none"<br />
Multiple formats can be specified by using a comma as the delimiter ("content=json,bib").</td>
<td>"html"</td>
<td>The format of the Atom response's &lt;content&gt; node:<br />
"html" (the default) will return an XHTML representation of each object, useful for display in feed readers and for parsing by XML tools.<br />
"json", currently valid only for item and collection requests, will return a JSON representation of all the item's fields.<br />
"bib", valid only for item requests, will return a formatted reference for each item.<br />
Export formats, valid only for item requests, will return data in the specified format for each item.<br />
If additional data is not required, use "none" to decrease the response size.<br />
If multiple formats are requested, &lt;content&gt; will contain multiple &lt;zapi:subcontent&gt; elements (in the http://zotero.org/ns/api namespace), each with a zapi:type attribute matching one of the specified content parameters.</td>
</tr>
</tbody>
</table>

### Parameters for "format=bib" and "content=bib"

| Parameter | Values | Default                     | Description                                                                                                                                                                                                                                                       |
|-----------|--------|-----------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| style     | string | "chicago-note-bibliography" | Citation style to use for formatted references. Should be the file name (without the ".csl" extension) of one of the default styles in the Zotero Style Repository (e.g., "apa" for <http://www.zotero.org/styles/apa>). Support for other styles is forthcoming. |

Note the difference between `format=bib` and `content=bib`. `format=bib` returns a formatted bibliography as XHTML, sorted according to the rules of the selected style. `content=bib` (valid only for `format=atom`, the default format mode) returns an individual formatted reference within the Atom &lt;content&gt; block for each item, with the Atom feed sorted according to the query parameters. `format=bib` processes the entire feed you are requesting without regard for any limit arguments, so it is generally a good idea to use it only with collections or tags.

### Export Formats

The following bibliographic data formats can be used as 'format' and 'content' parameters:

| Parameter         | Description                                                                                                        |
|-------------------|--------------------------------------------------------------------------------------------------------------------|
| bibtex            | BibTeX                                                                                                             |
| bookmarks         | Netscape Bookmark File Format                                                                                      |
| coins             | COinS                                                                                                              |
| csljson           | [Citation Style Language data format](https://github.com/citation-style-language/schema/blob/master/csl-data.json) |
| mods              | MODS                                                                                                               |
| refer             | Refer/BibIX                                                                                                        |
| rdf_bibliontology | [Bibliographic Ontology](http://bibliontology.com/) RDF                                                            |
| rdf_dc            | Unqualified Dublin Core RDF                                                                                        |
| rdf_zotero        | Zotero RDF                                                                                                         |
| ris               | RIS                                                                                                                |
| tei               | Text Encoding Initiative (TEI)                                                                                     |
| wikipedia         | Wikipedia Citation Templates                                                                                       |

## Caching

For efficient usage of the API, clients should make conditional GET requests whenever possible. If `If-Modified-Since-Version: <libraryVersion>` is passed with a multi-object read request (e.g., `<userOrGroupPrefix>/items`) and data has not changed in the library since the specified version, the API will return `304 Not Modified`. If `If-Modified-Since-Version: <objectVersion>` is passed with a single-object read request (e.g., `<userOrGroupPrefix>/items/<itemKey>`), a `304 Not Modified` will be returned if the individual object has not changed.

While a conditional GET request that returns a 304 should be fast, some clients may wish to perform additional caching on their own, using stored data for a period of time before making subsequent conditional requests to the Zotero API. This makes particular sense when the underlying Zotero data is known not to change frequently. For example, a web page that displayed a bibliography from a Zotero collection might cache the returned bibliography for an hour, after which time it would make another conditional request to the Zotero API. If the API returned a `304`, the web page would continue to display the cached bibliography for another hour before retrying.

## Rate Limiting

Clients accessing the Zotero API should be prepared to handle two forms of rate limiting: backoff requests and hard limiting.

If the API servers are overloaded, the API may include a `Backoff: <seconds>` HTTP header in responses, indicating that the client should perform the minimum number of requests necessary to maintain data consistency and then refrain from making further requests for the number of seconds indicated. `Backoff` can be included in any response, including successful ones.

If a client has made too many requests within a given time period, the API may return `429 Too Many Requests` with a `Retry-After: <seconds>` header. Clients receiving a `429` should wait the number of seconds indicated in the header before retrying the request.

`Retry-After` can also be included with `503 Service Unavailable` responses when the server is undergoing maintenance.

## Example Requests and Responses

Several examples of read request URLs and their responses:

<table>
  <thead>
    <tr><th colspan="2">Atom feed - List of items in collection</th></tr>
  </thead>
  <tbody>
    <tr><td>Request</td><td><https://api.zotero.org/users/475425/collections/9KH9TNSJ/items?format=atom></td></tr>
    <tr><td>Response</td><td><https://gist.github.com/923206> (Not updated for API v2)</td></tr>
  </tbody>
</table>

<table>
  <thead>
    <tr><th colspan="2">Atom feed - Single item</th></tr>
  </thead>
  <tbody>
    <tr><td>Request</td><td><https://api.zotero.org/users/475425/items/X42A7DEE?format=atom></td></tr>
    <tr><td>Response</td><td><https://gist.github.com/mronkko/5077731></td></tr>
  </tbody>
</table>

<table>
  <thead>
    <tr><th colspan="2">Atom feed - Single item with all possible content</th></tr>
  </thead>
  <tbody>
    <tr><td>Request</td><td><https://api.zotero.org/users/475425/items/X42A7DEE?format=atom&content=json,bib,html></td></tr>
    <tr><td>Response</td><td><https://gist.github.com/mronkko/5077751></td></tr>
  </tbody>
</table>

<table>
  <thead>
    <tr><th colspan="2">Atom feed - List of collections for a user</th></tr>
  </thead>
  <tbody>
    <tr><td>Request</td><td><https://api.zotero.org/users/475425/collections?format=atom></td></tr>
    <tr><td>Response</td><td><https://gist.github.com/1492705> (Not updated for API v2)</td></tr>
  </tbody>
</table>

<table>
  <thead>
    <tr><th colspan="2">Formatted bibliography</th></tr>
  </thead>
  <tbody>
    <tr><td>Request</td><td><https://api.zotero.org/users/475425/collections/9KH9TNSJ/items?format=bib></td></tr>
    <tr><td>Response</td><td><https://gist.github.com/mronkko/77bc2413cce4c219f862></td></tr>
  </tbody>
</table>

These requests can be performed from the command line:

``` bash
curl -H 'Zotero-API-Version: 2' 'https://api.zotero.org/users/475425/collections/9KH9TNSJ/items?format=atom'
curl -H 'Zotero-API-Version: 2' 'https://api.zotero.org/users/475425/items/X42A7DEE?format=atom'
curl -H 'Zotero-API-Version: 2' 'https://api.zotero.org/users/475425/items/X42A7DEE?format=atom&content=json,bib,html'
curl -H 'Zotero-API-Version: 2' 'https://api.zotero.org/users/475425/collections?format=atom'
curl -H 'Zotero-API-Version: 2' 'https://api.zotero.org/users/475425/collections/9KH9TNSJ/items?format=bib'
```

## Write Requests

The API also supports [write requests](dev/server_api/v2/write_requests) that allow the creation, modification, and deletion of data in online Zotero libraries.

## HTTP Status Codes

Successful GET requests will return a `200 OK` status code.

[Conditional GET requests](#caching) may return `304 Not Modified`.

For any read or write request, the server may return a `400 Bad Request`, `404 Not Found`, or `405 Method Not Allowed` for an invalid request and `500 Internal Server Error` or `503 Service Unavailable` for a server-related issue. [Authentication](#authentication) errors (e.g., invalid API key or insufficient privileges) will return a `403 Forbidden`.

Passing an `Expect` header, which is unsupported, will result in a `417 Expectation Failed` response.

[Library/object versioning](dev/server_api/v2/syncing#version_numbers) or [Zotero-Write-Token](dev/server_api/v2/write_requests#zotero_write_token) errors will result in `412 Precondition Failed` or `428 Precondition Required`.

`429 Too Many Requests` indicates that the client has been [rate-limited](#rate_limiting).
