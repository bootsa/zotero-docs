# Zotero Web API Syncing

This document outlines the recommended steps for synchronizing a [Zotero Web API](dev/web_api/v3/start) client with the Zotero server. Be sure you've read the [write request](dev/web_api/v3/write_requests) documentation for basic information on modifying data via the API.

TODO:

-   Incorporate [WebSocket handling](dev/web_api/v3/streaming_api)

## Sync Properties

In addition to standard object metadata (item field values, group names, etc.), clients should store the following properties:

-   A version number for metadata for each group
-   A version number for each library
-   A version number and a boolean `synced` flag for each syncable object
-   A list of downloaded objects that could not be processed and should be requested explicitly regardless of their remote version number (optional; see [Handling save errors](#Handling save errors) for details)

## Version Numbers

Every Zotero library and object (collection, item, etc.) on the server has an associated version number. The version number can be used to determine whether a client has up-to-date data for a library or object, allowing for efficient and safe syncing.

The API supports three custom HTTP headers that expose the versions: the `Last-Modified-Version` response header and the `If-Unmodified-Since-Version` and `If-Modified-Since-Version` request headers. The version number that the headers apply to depends on the request being made: for multiple-object requests such as `<userOrGroupPrefix>/items`, the headers apply to the entire library, whereas for single-object requests such as `<userOrGroupPrefix>/items/<itemKey>`, the headers apply to the individual object.

The version numbers are also accessible in several other ways, discussed below.

The version number is guaranteed to be monotonically increasing but is not guaranteed to increase sequentially, and clients should treat it as an opaque integer value.

#### Last-Modified-Version

The `Last-Modified-Version` response header indicates the current version of either a library (for multi-object requests) or an individual object (for single-object requests). If changes are made to a library in a write request, the library's version number will be increased, any objects modified in the same request will be set to the new version number, and the new version number will be returned in the `Last-Modified-Version` header.

#### If-Modified-Since-Version

The `If-Modified-Since-Version` request header can be used to efficiently check for new data. If `If-Modified-Since-Version: <libraryVersion>` is passed with a multi-object read request and data has not changed in the library since the specified version, the API will return `304 Not Modified`. If `If-Modified-Since-Version: <objectVersion>` is passed with a single-object read request, a `304 Not Modified` will be returned if the individual object has not changed.

#### If-Unmodified-Since-Version

The `If-Unmodified-Since-Version` request header is used to ensure that existing data won't be overwritten by a client with out-of-date data. All write requests that modify existing objects must include either the `If-Unmodified-Since-Version: <version>` header or a [#JSON version property](#JSON version property) for each object. If both are omitted, the API will return a `428 Precondition Required`.

For write requests to multi-object endpoints such as `<userOrGroupPrefix>/items`, the API will return `412 Precondition Failed` if the library has been modified since the passed version. For write requests to single-object endpoints such as `<userOrGroupPrefix>/items/<itemKey>`, the API will return a `412` if the object has been modified since the passed version.

Clients should generally use `If-Unmodified-Since-Version` for multi-object requests only if they have downloaded all server data for the object type being written. Otherwise, a client creating a new object could assign an object key that already exists on the server and accidentally overwrite the existing object.

`If-Unmodified-Since-Version` also enables more efficient syncs. Rather than first polling for remote updates, clients that have changes to upload should start by simply trying to perform the necessary [write requests](#iv_upload_modified_data), passing the current local library version in the `If-Unmodified-Since-Version` header. If updated data is available, the API will return `412 Precondition Failed`, indicating that the client must first retrieve the updated data. In the absence of a `412` for a write request, clients with local modifications do not need to check for remote changes explicitly.

`If-Unmodified-Since-Version: <version>` replaces the `If-Match: <etag>` header previously required for single-object writes.

#### JSON version property

`format=json` responses will include a `version` property in each object's editable JSON (the `data` property) indicating the current version of that object. This value will be identical to the `version` property supplied at the top level of the JSON object. For single-object requests, this will also be identical to the value of the `Last-Modified-Version` response header.

If included in JSON submitted back to the API, the JSON version property will behave equivalently to a single-object `If-Unmodified-Since-Version`: if the object has been modified since the specified version, the API will return a `412 Precondition Failed`. When writing objects that include object keys, either the request must include `If-Unmodified-Since-Version` or each object must include the JSON version property. When writing new objects with an object key in a request without `If-Unmodified-Since-Version`, use the special version 0 to indicate that the objects should not yet exist on the server.

While `If-Unmodified-Since-Version` and the JSON version property are not mutually exclusive for write requests, they are redundant, and generally clients should use one or the other depending on their interaction mechanism. See [#Partial-Library Syncing](#Partial-Library Syncing) for a discussion of possible syncing methods.

#### ?since=&lt;version&gt;

The `since` query parameter can be used to retrieve only objects modified since a specific version.

#### ?format=versions

`format=versions` is similar to `format=keys`, but instead of returning a newline-delimited list of object keys, it returns a JSON object with object versions keyed by object keys:

    {
      "<itemKey>": <version>,
      "<itemKey>": <version>,
      "<itemKey>": <version>
    }

Like `format=keys`, `format=versions` is not limited by a maximum number of results and returns all matching objects by default.

#### Local object versions

The use of local object versions during syncing, and the process for updating them, is described below.

When objects are created or modified locally by the user during regular usage, set `synced = false` to indicate that the object needs to be uploaded on the next sync. Give new objects version 0. Do not change the version when objects are modified outside of the sync process.

## Full-Library Syncing

The following steps are for complete syncing of Zotero libraries, such as to enable full offline usage. For tips on alternative syncing methods, see [Partial-Library Syncing](#partial_library_syncing).

### 1) Verify key access

    GET /keys/current

`200` Response:

    {
      {
        "userID": 12345
        "username": "Z User"
        "access": {
            "user": {
                "library": true
                "files": true
                "notes": true
                "write": true
            }
            "groups": {
                "all": {
                    "library": true
                    "write": true
                }
            }
        }
    }
    }

`/keys/current` returns information on the API key provided in the `Zotero-API-Key` header. Use this response to verify that the key has the expected access to the library you're trying to access. If necessary, show a warning that the user no longer has sufficient access and offer to remove a local library or reset local changes.

### 2) Get updated group metadata

Group metadata includes group titles and descriptions as well as member/role/permissions information. It is separate from group library data.

First, retrieve a list of the user's groups, with a version indicating the current state of each group's metadata:

    GET /users/<userID>/groups?format=versions

`200` Response:

    {
      "<groupID>": "<version>",
      "<groupID>": "<version>",
      "<groupID>": "<version>"
    }

Delete any local groups not in the list, which either were deleted or are currently inaccessible. (The user may have been removed from a group, or the current API key may no longer have access.) If data has been modified locally in any groups that are no longer available, offer the user the ability to cancel and transfer modified data elsewhere before continuing.

For each group that doesn't exist locally or that has a different version number, retrieve the group metadata:

    GET /groups/<groupID>

    Last-Modified-Version: <version>
    JSON response with metadata

Update the local group metadata and version number.

### 3) Sync library data

Perform the following steps for each library:

#### i. Get updated data

**Note:** Clients with changes to upload should attempt to [upload data](#iv_upload_modified_data) first and retrieve updated data only if they receive a `412 Precondition Failed`. See [If-Unmodified-Since-Version](#if-unmodified-since-version) for more information.

Retrieve the versions of all objects changed since the last check for that object type, using the appropriate request for each object type:

    GET <userOrGroupPrefix>/collections?since=<version>&format=versions
    GET <userOrGroupPrefix>/searches?since=<version>&format=versions
    GET <userOrGroupPrefix>/items/top?since=<version>&format=versions&includeTrashed=1
    GET <userOrGroupPrefix>/items?since=<version>&format=versions&includeTrashed=1

`<version>` is the final `Last-Modified-Version` returned from the API for the last successfully completed sync process, or `0` when syncing a library for the first time.

(The `since` parameter can also be used on `.../tags` requests (without `format=versions`) by clients that don't download all items and wish to keep a list of all tags in a library up-to-date. It isn't necessary for clients that download all items to request updated tags directly, as item objects contain all associated tags.)

The first request — e.g., for collection versions — can also include an `If-Modified-Since-Version: <last saved library version>` header. If the API returns `304 Not Modified`, no library data of any object type has changed since the version specified and no further requests need to be made to retrieve data unless there are [previously failed objects](#Handling save errors) that should be retried.

`200` response:

    Last-Modified-Version: <version>

    [
        "<objectKey>": <version>,
        "<objectKey>": <version>
        "<objectKey>": <version>,
    ]

For each returned object, compare the version to the local version of the object. If the remote version doesn't match, queue the object for download. Generally all returned objects should have newer version numbers, but there are some situations, such as full syncs (i.e., `since=0`) or interrupted syncs, where clients may retrieve versions for objects that are already up-to-date locally. The version will also match for top-level items on the second, non-`/top` `items` request, since top-level items will have already been processed.

Retrieve the queued objects, as well as any [flagged](#Handling save errors) as having previously failed to save, by key, up to 50 at a time, using the appropriate request for each object type:

    GET <userOrGroupPrefix>/collections?collectionKey=<key>,<key>,<key>,<key>
    GET <userOrGroupPrefix>/searches?searchKey=<key>,<key>,<key>,<key>
    GET <userOrGroupPrefix>/items?itemKey=<key>,<key>,<key>,<key>&includeTrashed=1

Item responses include creators, tags, collection associations, and relations.

Process the remote changes:

    for each updated object:
      if object doesn't exist locally:
         create local object with version = Last-Modified-Version and set synced = true
         continue
      
      if object hasn't been modified locally (synced == true):
          overwrite with synced = true and version = Last-Modified-Version
      
      else:
        perform conflict resolution
          if object hasn't changed:
            set synced = true and version = Last-Modified-Version
          
          else if changes can be automatically merged:
            apply changes from each side and set synced = true and version = Last-Modified-Version
          
          else:
            prompt user to choose a side or merge conflicts
              if user chooses remote copy:
                overwrite with synced = true and version = Last-Modified-Version
          
              else if user chooses local copy:
                synced = false and set a flag to restart the sync when finished
        

##### Conflict resolution

Conflict resolution is a complex process not fully described here, but see the Zotero client code for examples.

A few notable features:

1.  When an object is successfully downloaded or upload, the Zotero client saves the `data` block from the API response as pristine JSON tied to the object version. When a conflict occurs during a sync, it can then compare both the local and remote versions of the object to the pristine JSON to determine which changes were made on each side and automatically merge changes that aren't in conflict. Users are prompted to manually resolve only conflicting changes to the same field.
2.  The Zotero client automatically resolves conflicts for objects other than items without prompting the user, erring on the side of restoring deleted data.
3.  Restoring locally deleted collections is a special case. Item membership is a property of items, so no local items will still be a member of the collection after it's restored, and the local items also may have been deleted along with the collection. When restoring a locally deleted collection, the Zotero client fetches the collection's items from the API and either adds them back to the collection and marks them as unsynced (if they still exist locally) or removes them from the local delete log and flags them for manual download (if they don't).

##### Handling save errors

If an error occurs while processing an object (e.g., due to a foreign-key constraint in the local database), it can be handled one of two ways:

1.  Treat the error as fatal and stop the sync without updating the local library version
2.  Add the object key to a list of objects needing to be downloaded later and continue with the sync, updating the local library version at the end as if the sync had succeeded. In a future sync, add objects on this list to the set of objects returned from the `versions` request so that their data is requested again even if the remote version is lower than the library version specified in `?since=`. Retry these objects on a backoff schedule, since they may require either a server-side fix or a client update to save successfully. Skip objects in this list when uploading locally changed objects, since they are known to be out of date and would result in `412` errors. If these objects later appear as remotely deleted, remove them from the list of objects.

When processing a set of objects, it may be helpful to maintain a process queue for the sync run and move failing objects to the end of the queue in case they depend on other objects being retrieved. (In many cases, it's possible to sort objects beforehand to avoid such errors, such as by sorting parent collections before subcollections.) If a loop of the process queue completes without any objects being successfully processed, stop the sync.

#### ii. Get deleted data

    GET <userOrGroupPrefix>/deleted?since=<version>

`<version>` is, as above, the `Last-Modified-Version` returned from the API during the last successful sync run.

Response:

    Content-Type: application/json
    Last-Modified-Version: <version>

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

Process the remote deletions:

    for each deleted object in ['collections', 'searches', 'items']:
      if local object doesn't exist:
        continue
      
      if object hasn't been modified locally (synced == true):
        delete local object, skipping delete log
      
      else:
        perform conflict resolution
          if user chooses deletion, delete local object, skipping delete log
        
          if user chooses local modification, keep object and set synced = true and version = Last-Modified-Version

The Zotero client automatically resolves conflicts for objects other than items without prompting the user, erring on the side of restoring deleted data.

#### iii. Check for concurrent remote updates

For each response from the API, check the `Last-Modified-Version` to see if it has changed since the `Last-Modified-Version` returned from the first request (e.g., `collections?since=`). If it has, restart the process of retrieving updated and deleted data, waiting increasing amounts of time between restarts to give the other client the opportunity to finish.

After saving all remote changes without the remote version changing during the process, save `Last-Modified-Version` from the last run as the new local library version.

#### iv. Upload modified data

Upload objects which have `synced` set to `false`. Follow the instructions in [Updating Multiple Objects](dev/web_api/v3/write_requests#updating_multiple_objects), passing the current library version as `If-Unmodified-Since-Version`.

Creators, tags, and relations are included in item objects and are not synced separately.

On a `200` response, set `synced = true` and `version = Last-Modified-Version` for each successfully uploaded Zotero object and store `Last-Modified-Version` as the current library version to be passed with the next write request. Do not update the version of Zotero objects in the `unchanged` object. Retry non-fatal failures.

On a `412 Precondition Failed` response, return to the beginning of the sync process for that library, waiting increasing amounts of time between restarts.

#### v. Upload local deletions

When an object is deleted locally during regular usage, add its library and key to a delete log. When syncing, send delete requests for objects in the log and clear them from the log on successful deletion. When resolving a conflict between a locally deleted object and a remotely modified object in favor of the remote object, remove it from the delete log.

See [Deleting Multiple Collections](dev/web_api/v3/write_requests#deleting_multiple_collections), [Deleting Multiple Searches](dev/web_api/v3/write_requests#deleting_multiple_searches), and [Deleting Multiple Items](dev/web_api/v3/write_requests#deleting_multiple_items) for the specific requests. Pass the current library version as `If-Unmodified-Since-Version`.

Example request:

    DELETE <userOrGroupPrefix>/collections?collectionKey=<key>,<key>,<key>
    If-Unmodified-Since-Version: <version>

Response:

    204 No Content
    Last-Modified-Version: <version>

On a `204` response, store the returned `Last-Modified-Version` as the current library version to be passed with the next write request.

On a `412 Precondition Failed` response, return to the beginning of the sync process for that library.

## Partial-Library Syncing

The steps above are designed for clients that, after syncing, should always contain a complete local copy of a user's Zotero data. While this may make sense for permanently installed clients, it is less ideal for other use cases, such as for clients that provide temporary access to a library or that will often be connected via mobile connections where downloading all data in a library would be prohibitively slow or expensive. Selective syncing requires some modifications to the above steps. Three possible approaches are outlined below:

### Fixed Collection List

This approach would work for a client that allowed users to choose a subset of collections to sync but otherwise behaved like a full offline client.

The client would still need to track only a single library version, but instead of downloading a list of all items from `<userOrGroupPrefix>/items?format=versions&since=<version>`, it would retrieve the list of items from each selected collection individually with requests such as `<userOrGroupPrefix>/collections/<collectionKey/items?format=versions&since=<version>`. The local library version would be updated only once the items in all collections had been downloaded (or queued for download in a persistent fashion).

### Per-Collection Versions

This approach would work for a client that loaded data only in response to user interaction — such as clicking on a collection — rather than loading a predefined set of collections.

The client would need to track separate library versions for each view that represented the state of all objects within that view. If an upload to a multi-object endpoint such as `<userOrGroupPrefix>/items` resulted in a `412`, indicating that something in the library — though not necessarily in the view — had changed, the client would need to fetch only the new data (or the list of objects containing new data) in the view and update the version number associated with the view. Note that such a version number would be separate from the version number of the view object — for example, the collection — itself.

Clients would also need to keep track of a version number that represented the state of the collection/search list. (While they could simply reload the entire collections list, doing so would be slow for users with many collections.)

### Single-Object Versions

A final approach would be to eschew library-wide version numbers altogether and use only single-object versions to upload data. This could be done via the single-object endpoints using the `If-Unmodified-Since-Version` header or via multi-object endpoints using the JSON version properties. As an object's editable JSON includes the object version, clients that pass the received JSON back to the server will get safe updates automatically. This can be thought of as the default API usage mode.

Note that multi-object endpoints should always be used for large operations. Using single-object endpoints excessively could result in throttling by the server.
