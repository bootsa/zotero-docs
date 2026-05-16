<p id="zotero-5-update-warning" style="color: red; font-weight: bold">We’re
in the process of updating the documentation for
<a href="https://www.zotero.org/blog/zotero-5-0">Zotero 5.0</a>. Some documentation
may be outdated in the meantime. Thanks for your understanding.</p>

# Zotero Web API Global Search

The [Zotero Web API](dev/web_api/v3/) provides an interface to search aggregated metadata from the full corpus of public items stored on zotero.org.

*Global search is currently in beta, with restricted public access. If you would like to test global search, you can email [support@zotero.org](mailto:/mailto/support@zotero.org) to request access.*

## Performing a Search

    GET /global

### Search Parameters

| Parameter | Values | Default | Description                                      |
|-----------|--------|---------|--------------------------------------------------|
| `q`       | string | null    | Quick search. Searches all fields.               |
| `doi`     | string | null    | A document object identifier (DOI)               |
| `isbn`    | string | null    | An international standard book identifier (ISBN) |

### Search Syntax

Examples:

-   `/global?q=virtual`
-   `/global?doi=10.1016/j.rser.2011.07.104`
-   `/global?isbn=1421402831`

## Getting Public Library Items for a Global Item

    GET /global/items?id=<global item id>

Examples:

-   `/global/items?id=doi:10.1016/j.rser.2011.07.104`
-   `/global/items?id=isbn:1421402831`
