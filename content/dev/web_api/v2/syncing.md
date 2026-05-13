# API-Based Syncing

**This is version 2 of the Zotero Web API. For new development, use [API version 3](dev/web_api/v3/start).**

This document outlines the recommended steps for synchronizing a Zotero API client with the Zotero server.

TODO:

-   Full-text content ([see separate documentation](dev/web_api/v2/fulltext_content))
-   Backoff instruction ([see read request documentation](dev/web_api/v2/read_requests#rate_limiting))
-   WebSocket notifications (planned feature)

## Sync Properties

In addition to standard object metadata (item field values, group names, etc.), clients should store the following properties:

-   An ETag for metadata for each group
-   A version number for each library
-   A version number and a boolean `synced` flag for each syncable object

## Version Numbers

Every Zotero library and object (collection, item, etc.) on the server has an associated version number. The version number can be used to determine whether a client has up-to-date data for a library or object, allowing for efficient and safe syncing.

The API supports three custom HTTP headers that expose the versions: the `Last-Modified-Version` response header and the `If-Unmodified-Since-Version` and `If-Modified-Since-Version` request headers. The version number that the headers apply to depends on the request being made: for multiple-object requests such as `<userOrGroupPrefix>/items`, the headers apply to the entire library, whereas for single-object requests such as `<userOrGroupPrefix>/items/<itemKey>`, the headers apply to the individual object.

The version numbers are also accessible in several other ways, discussed below.

The version number is guaranteed to be monotonically increasing but is not guaranteed to increase sequentially, and clients should treat it as an opaque integer value.

#### Last-Modified-Version

The `Last-Modified-Version` response header indicates the current version of either a library (for multi-object requests) or an individual object (for single-object requests). If changes are made to a library in a write request, the library's version number will be increased, any objects modified in the same request will be set to the new version number, and the new version number will be returned in the `Last-Modified-Version` header. Since modified objects always receive the newly increased library version, the returned `Last-Modified-Version` will be the same whether an item is modified as part of a multi-object or single-object request.

#### If-Modified-Since-Version

The `If-Modified-Since-Version` request header can be used to efficiently check for new data. If `If-Modified-Since-Version: <libraryVersion>` is passed with a multi-object read request and data has not changed in the library since the specified version, the API will return `304 Not Modified`. If `If-Modified-Since-Version: <objectVersion>` is passed with a single-object read request, a `304 Not Modified` will be returned if the individual object has not changed.

#### If-Unmodified-Since-Version

The `If-Unmodified-Since-Version` request header is used to ensure that existing data won't be overwritten by a client with out-of-date data. All write requests that modify existing objects must include either the `If-Unmodified-Since-Version: <version>` header or a [#JSON version property](#JSON version property) for each object. If both are omitted, the API will return a `428 Precondition Required`.

For write requests to multi-object endpoints such as `<userOrGroupPrefix>/items`, the API will return `412 Precondition Failed` if the library has been modified since the passed version. For write requests to single-object endpoints such as `<userOrGroupPrefix>/items/<itemKey>`, the API will return a `412` if the object has been modified since the passed version.

Clients should generally use `If-Unmodified-Since-Version` for multi-object requests only if they have downloaded all server data for the object type being written. Otherwise, a client creating a new object could assign an object key that already exists on the server and accidentally overwrite the existing object.

`If-Unmodified-Since-Version` also enables more efficient syncs. Rather than first polling for remote updates, clients that have changes to upload should start by trying to perform the necessary [write requests](#iv_upload_modified_data), passing the current local library version in the `If-Unmodified-Since-Version` header. If updated data is available, the API will return `412 Precondition Failed`, indicating that the client must first retrieve the updated data. In the absence of a `412` for a write request, clients with local modifications do not need to check for remote changes explicitly.

`If-Unmodified-Since-Version: <version>` replaces the `If-Match: <etag>` header previously required for single-object writes.

#### JSON version property

`content=json` responses will include a `collectionVersion`, `itemVersion`, or `searchVersion` property in each object's JSON indicating the current version of that object. This value will be identical to the value given in the Atom entry's `zapi:version` element. For single-object requests, this will also be identical to the value of `Last-Modified-Version`.

If included in JSON submitted back to the API, the JSON version property will behave equivalently to a single-object `If-Unmodified-Since-Version`: if the object has been modified since the specified version, the API will return a `412 Precondition Failed`. When writing objects that include objects keys, either the request must include `If-Unmodified-Since-Version` or each object must include the JSON version property. When writing new objects with an object key in a request without `If-Unmodified-Since-Version`, use the special version 0 to indicate that the objects should not yet exist on the server.

While `If-Unmodified-Since-Version` and the JSON version property are not mutually exclusive for write requests, they are redundant, and generally clients should use one or the other depending on their interaction mechanism. See [#Partial-Library Syncing](#Partial-Library Syncing) for a discussion of possible syncing methods.

#### zapi:version Atom entry element

Each object's Atom entry will include a `zapi:version` element indicating the object's current version number. For `content=json` responses, this value will be identical to the version given in the JSON version property. For single-object requests, this will also be identical to the value of `Last-Modified-Version`.

Unlike the JSON version property, the name of this element is consistent across all object types and is present for all Atom content modes.

#### ?newer=&lt;version&gt;

The `newer` query parameter can be used to retrieve only objects modified since a specific version.

#### ?format=versions

`format=versions` is similar to `format=keys`, but instead of returning a newline-delimited list of object keys, it returns a JSON object with object versions keyed by object keys:

``` javascript
{
  "<itemKey>": <version>,
  "<itemKey>": <version>,
  "<itemKey>": <version>
}
```

Like `format=keys`, `format=versions` is not limited by a maximum number of results and returns all matching objects by default.

## Full-Library Syncing

The following steps are for complete syncing of Zotero libraries, such as to enable full offline usage. For tips on alternative syncing methods, see [Partial-Library Syncing](#partial_library_syncing).

### 1) Get updated group metadata

Group metadata includes group titles and descriptions as well as member/role/permissions information. It is separate from group library data.

First, retrieve a list of the user's groups, with an ETag indicating the current state of each group's metadata:

    GET /users/<userID>/groups?format=etags

`200 ` Response:

``` javascript
{
  "<groupID>": "<etag>",
  "<groupID>": "<etag>",
  "<groupID>": "<etag>"
}
```

Delete any local groups not in the list. Optionally, if data has been modified locally in any remotely deleted groups, offer the user the ability to cancel and transfer modified data elsewhere before continuing.

For each group that doesn't exist locally or that has a different ETag, retrieve the group metadata:

    GET /groups/<groupID>?content=json

    ETag: <etag>
    Atom response with JSON group metadata

Update the local group metadata and ETag.

### 2) Sync library data

Perform the following steps for each library:

#### i. Get updated data

**Note:** Clients with changes to upload should attempt to [upload data](#iv_upload_modified_data) first and retrieve updated data only if they receive a `412 Precondition Failed`. See [If-Unmodified-Since-Version](#if-unmodified-since-version) for more information.

Retrieve the versions of all objects changed since the last check for that object type, using the appropriate request for each object type:

    GET <userOrGroupPrefix>/collections?newer=<last collections version>&format=versions
    GET <userOrGroupPrefix>/searches?newer=<last searches version>&format=versions
    GET <userOrGroupPrefix>/items?newer=<last items version>&format=versions

    If-Modified-Since-Version: <current local library version>

(The `newer` parameter can also be used on `.../tags` requests (without `format=versions`) by clients that don't download all items and wish to keep a list of all tags in a library up-to-date. It isn't necessary for clients that download all items to request updated tags directly, as item objects contain all associated tags.)

If the API returns `304 Not Modified`, no library data of any object type has changed since the version specified. If you are tracking a single library version for all object types, skip ahead to [uploading modified data](#iv_upload_modified_data); otherwise, skip to the next object type with a lower stored library version.

200 response:

    Last-Modified-Version: <version>

``` javascript
[
    "<objectKey>": <version>,
    "<objectKey>": <version>
    "<objectKey>": <version>,
]
```

For each returned object, compare the version to the local version of the object. If the remote version doesn't match, queue the object for download. Generally all returned objects should have newer version numbers, but there are some situations, such as full syncs (i.e., newer=0) or interrupted syncs, where clients may retrieve versions for objects that are already up-to-date locally.

Retrieve the queued objects by key, up to 50 at a time, using the appropriate request for each object type:

    GET <userOrGroupPrefix>/collections?content=json&collectionKey=<key>,<key>,<key>,<key>
    GET <userOrGroupPrefix>/searches?content=json&searchKey=<key>,<key>,<key>,<key>
    GET <userOrGroupPrefix>/items?content=json&itemKey=<key>,<key>,<key>,<key>

Item responses include creators, tags, collection associations, and relations.

Process the remote changes:

    for each updated object:
      if object doesn't exist locally:
         create local object with version and set synced = true
         continue
      
      if object hasn't been modified locally (synced == true):
        if version number matches:
          continue
        
        else:
          overwrite with synced = true and new version number
      
      else:
        if different:
          perform conflict resolution
          
          if user chooses remote copy:
            overwrite with synced = true and new version number
          
          if user chooses local copy:
            synced = false
        
        else:
          Update version and set synced = true
        

When modifying objects locally, set `synced = false` unless the write is a result of syncing.

#### ii. Get deleted data

    GET <userOrGroupPrefix>/deleted?newer=<last deleted version>

Response:

    Content-Type: application/json
    Last-Modified-Version: <version>

``` javascript
{
  "collections": [
    "<collectionKey>"
  ],
  "searches": [
    "<searchKey>"
  ],
  "items": [
    "<itemKey>",
    "<itemKey>"
  ],
  "tags": [
    "<tagName>",
    "<tagName>"
  ]
}
```

Process the remote deletions:

    for each deleted object in ['collections', 'searches', 'items', 'tags']:
      if local object doesn't exist:
        continue
      
      if object hasn't been modified locally (synced == true):
        delete local object, skipping delete log
      
      else:
        perform conflict resolution
        
        if user chooses deletion, delete local object, skipping delete log
        
        if user chooses local modification, keep object and set synced = true

Tags removed from all items are not necessarily deleted, hence the separate tag deletion mechanism.

TODO: tag-deletion complications

#### iii. Check for concurrent remote updates

When done updating local data, compare the `Last-Modified-Version` returned from the `collections?newer` request (i.e., the first request for changed data) to `Last-Modified-Version` from the `/deleted` request (i.e., the last request for changed data). If the version hasn't changed, server data hasn't changed in that library while downloading changes and the version can be stored locally as the current version for that library. If the version has changed, repeat the above steps to retrieve updated and deleted data. The `Last-Modified-Version` from each `?newer` request can optionally be stored in memory to avoid having to download and compare the same keys if the requests need to be repeated.

#### iv. Upload modified data

Upload objects which have `synced` set to `false`. Follow the instructions in [Updating Multiple Objects](dev/web_api/v2/write_requests#updating_multiple_objects), passing the current library version as `If-Unmodified-Since-Version`.

Creators, tags, and relations are included in item objects and are not synced separately.

On a `200` response, set `synced = true` and `version = Last-Modified-Version` for each successfully uploaded Zotero object and store `Last-Modified-Version` as the current library version to be passed with the next write request. Do not update the version of Zotero objects in the `unchanged` object. Retry non-fatal failures.

On a `412 Precondition Failed` response, return to the beginning of the sync process for that library.

#### v. Upload local deletions

See [Deleting Multiple Collections](dev/web_api/v2/write_requests#deleting_multiple_collections), [Deleting Multiple Searches](dev/web_api/v2/write_requests#deleting_multiple_searches), [Deleting Multiple Items](dev/web_api/v2/write_requests#deleting_multiple_items), and [Deleting Multiple Tags](dev/web_api/v2/write_requests#deleting_multiple_tags). Pass the current library version as `If-Unmodified-Since-Version`.

Example request:

    DELETE <userOrGroupPrefix>/collections?collectionKey=<key>,<key>,<key>
    If-Unmodified-Since-Version: <version>

Response:

    204 No Content
    Last-Modified-Version: <version>

On a 204 response, store the returned `Last-Modified-Version` as the current library version to be passed with the next write request.

On a `412 Precondition Failed` response, return to the beginning of the sync process for that library.

## Partial-Library Syncing

The steps above are designed for clients that, after syncing, should always contain a complete local copy of a user's Zotero data. While this may make sense for permanently installed clients, it is less ideal for other use cases, such as for clients that provide temporary access to a library or that will often be connected via mobile connections where downloading all data in a library would be prohibitively slow or expensive. Selective syncing requires some modifications to the above steps. Three possible approaches are outlined below:

### Fixed Collection List

This approach would work for a client that allowed users to choose a subset of collections to sync but otherwise behaved like a full offline client.

The client would still need to track only a single library version, but instead of downloading a list of all items from `<userOrGroupPrefix>/items?format=versions&newer=<version>`, it would retrieve the list of items from each selected collection individually with requests such as `<userOrGroupPrefix>/collections/<collectionKey/items?format=versions&newer=<version>`. The local library version would be updated only once the items in all collections had been downloaded (or queued for download in a persistent fashion).

### Per-Collection Versions

This approach would work for a client that loaded data only in response to user interaction—such as clicking on a collection—rather than loading a predefined set of collections.

The client would need to track separate library versions for each view that represented the state of all objects within that view. If an upload to a multi-object endpoint such as `<userOrGroupPrefix>/items` resulted in a `412`, indicating that something in the library—though not necessarily in the view—had changed, the client would need to fetch only the new data (or the list of objects containing new data) in the view and update the version number associated with the view. Note that such a version number would be separate from the version number of the view object—for example, the collection—itself.

Clients would also need to keep track of a version number that represented the state of the collection/search list. (While they could simply reload the entire collections list, doing so would be slow for users with many collections.)

### Single-Object Versions

A final approach would be to eschew library-wide version numbers altogether and use only single-object versions to upload data. This could be done via the single-object endpoints using the `If-Unmodified-Since-Version` header or via multi-object endpoints using the JSON version properties. As `content=json` responses include object versions, clients that pass the received JSON back to the server will get safe updates automatically. This can be thought of as the default API usage mode.

Note that multi-object endpoints should always be used for large operations. Using single-object endpoints excessively could result in throttling by the server.

## Collection/Tag Deletions and Syncing

A collection or tag deletion will cause all associated items to be updated on the server, and the updated items will be set to the library version returned by the deletion request. This interaction between object types can result in sync conflicts if clients don't take special precautions when performing these actions.

Clients have two options for performing collection and tag deletions:

### Re-upload Items and Delete Collection/Tag

This method is appropriate for clients that sync the entire library.

When deleting a collection/tag locally, mark previously associated items as changed. Before sending the collection/tag DELETE request, upload the modified items to the server. Once those changes have been uploaded, the DELETE for the collection/tag can be sent. Since the collection/tag on the server will have no associated items, there is no potential for a conflict between local and remote items.

### Delete Collection/Tag and Redownload Items

This method is appropriate for clients that will not necessarily have all items associated with the collection/tag locally or that expect to have significantly more limited upload bandwidth.

When deleting a collection/tag locally, the client should not mark previously associated items as changed to avoid triggering conflicts when the items updated on the server are redownloaded.

However, a conflict can still occur if an associated item is modified locally in other ways and not synced to the server before the collection/tag deletion is uploaded. When the client tries to pull down the updated remote item after the collection/tag deletion, the local version will be marked as changed, and since the data won't match, the client will need to perform conflict resolution.

To avoid this, clients can store a pristine copy of the item data (not counting collections and tags) before modifying an item locally. This will allow the client to determine what local and remote changes have been made since the item was last downloaded.

Then, when a conflict occurs, if the server's item data matches the pristine copy and the server collections/tags match the current local collections/tags, clients can just upload the local item data changes.

If the server item data doesn't match the pristine copy, the client can attempt to apply both local and remote changes and perform a conflict resolution only if the same field has been modified.

If the server collections/tags don't match the current local collections/tags, the client will need to either perform conflict resolution or automatically merge the collections and tags, restoring any deleted ones.
