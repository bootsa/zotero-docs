# Changes in Zotero Web API v3

Version 3 of the [Zotero Web API](dev/web_api/v3/) introduces a new all-JSON response format and various other changes. While API v3 is mostly backwards compatible, existing clients may need to make [a few small adjustments](#tldr_for_existing_atom_consumers) for full compatibility, depending on usage.

-   New default all-JSON response format, `format=json`
    -   Contains a single JSON object for single-object requests and an array of objects for multi-object requests
    -   All individual objects contain top-level `key` and `version` properties and top-level `library`, `links`, and `meta` objects.
    -   `meta` contains non-editable system-generated properties like `createdByUser`/ `lastModifiedByUser` (for group items), `creatorSummary`, and `numChildren`.
    -   Other Atom-specific feed properties (`title`, `author`, `published`, `updated`) have been removed.
    -   Clients sending `application/atom+xml` in the `Accept` header will continue to receive Atom responses if no other format is requested
-   For `format=json`, `include=data` has replaced Atom's `content=json` and is now the default mode, with a top-level `data` object containing the editable fields. As with `content`, additional comma-separated types can be requested (e.g., `include=data,bib`). The requested types are provided as top-level properties. `content=html` remains the default in Atom.
-   Multi-object writes now take an array of JSON objects directly, rather than an object with an `items`/`collections`/`searches` property containing an array.
-   For write requests, the API now accepts either the editable JSON (`data`) or the full parent JSON object, with the server extracting the `data` object automatically. The latter allows for some editing tasks to be performed without any programming.
-   The `parsedDate` property in the `format=json` `meta` object gives the full parsed date in YYYY-MM-DD form, so that clients don't need to replicate Zotero's date-parsing logic to get exact dates. In v3 Atom, `zapi:parsedDate` replaces `zapi:year`.
-   `zapi:numTags` is removed in v3 Atom, since it's unnecessary with the `tags` array in the editable json.
-   The API now returns 25 results per request instead of 50 if `limit` isn't provided.
-   The total result count for multi-object responses is available in a new custom HTTP header, `Total-Results`. `zapi:totalResults` is removed in v3 Atom.
-   `rel=first`/`prev`/`next`/`last`/`alternate` links for multi-object responses are now provided in the `Link` HTTP header.
-   The API key can be provided in the `Authorization` request header instead of the `key` query parameter. Since API keys have never been included in the URLs provided in responses, previously all provided URLs had to be modified for key-based access.
-   The API version can be provided as a query parameter (`v=3`) instead of the `Zotero-API-Version` header for easier debugging and sharing of requests, though both will remain supported.
-   For formats other than Atom, `dateModified` descending is the default sort instead of `dateAdded` descending.
-   `itemKey`/`itemVersion` (and similar properties on collections and searches) in the editable JSON are now just `key` and `version` for easier handling by clients. Clients that simply pass back the edited JSON without touching those properties shouldn't be affected. Clients that store the JSON will need to modify it before sending in v3.
-   The `version` metadata field in the `computerProgram` item type is now `versionNumber` to avoid a conflict with the renamed object version property.
-   dateAdded/dateModified are included in the 'data' object in ISO 8601 form. Previously these timestamps were provided only in the Atom `published`/`updated` elements, though in v2 they can be sent back in the JSON as `dateAdded`/`dateModified` in YYYY-MM-DD hh-mm-dd format, interpreted as UTC. In v3 write requests, either is accepted, though the previous form is deprecated.
-   The `accessDate` field, which was also previously YYYY-MM-DD[ hh-mm-dd], is ISO 8601 in v3 (including in Atom) for both reading and writing. The previous form is accepted but deprecated.
-   The pagination links (`rel=self`/`first`/`prev`/`next`/`last`) on multi-object responses can be used without modification by clients using the `Authorization` header. The `rel=self` links in individual objects are meant as base URIs and do not include any query parameters (e.g., `include=data,bib`). This is a change from the previous behavior, where the Atom entry `rel="self"` links include all non-default provided parameters. But with the `Authorization` header and `include=data` as the new default, the base URI may be sufficient for most individual-object requests.
-   The `newer` parameter is now `since` for clarity. `newer` is deprecated.
-   The `order` parameter is now `sort` and `sort` is now `direction`. `order=<field>` and `sort=<asc/desc>` are deprecated.
-   Requests for updated group metadata can now use `format=versions` instead of `format=etags`. `format=etags` is deprecated.
-   `pprint=1` has been removed, and all responses are now pretty-printed.
-   '<', '>', and '&' are no longer unnecessarily escaped to \\u.... in returned JSON data. In Atom, these characters are instead turned into XML numeric character references. Proper XML and JSON parsers shouldn't be affected by these changes.
-   The HTTP Warning header may be used to send clients non-fatal warnings — such as deprecation warnings — that can be logged.

### tl;dr for existing Atom consumers

-   Request `format=atom` explicitly, or send `application/atom+xml` in the `Accept` header
-   Use `zapi:parsedDate` instead of `zapi:year`
-   Use `Total-Results` HTTP header instead of `zapi:totalResults`
-   Count the `tags` array in editable JSON instead of using `zapi:numTags`
-   Use `key`/`version` instead of `itemKey`/`itemVersion` (and `collection*`/`search*`) in editable JSON
-   Use `versionNumber` instead of `version` metadata field in `computerProgram` item type
-   Use ISO 8601 dates for `accessDate`, `dateAdded`, and `dateModified`
-   Use `since` parameter instead of `newer`
-   Use `sort` parameter instead of `order` and `direction` instead of `sort`
-   For writes, upload an array of JSON objects directly instead of an object containing an `items`/`collections`/`searches` array
-   Optionally, use `Authorization: Bearer <apiKey>` instead of `key` parameter
-   Optionally, use `v` parameter instead of `Zotero-API-Version` for debugging
