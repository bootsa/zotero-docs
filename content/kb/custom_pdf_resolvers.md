# Custom PDF Resolvers

Custom resolvers for [PDF retrieval](/blog/improved-pdf-retrieval-with-unpaywall-integration/) currently can be configured via the `extensions.zotero.findPDFs.resolvers` hidden pref (Advanced preferences → Config Editor). The value should be a JSON string containing an array of configuration objects. HTML and JSON sources are supported.

You may wish to distribute a custom resolver using a Zotero plugin that adds or updates the pref at startup.

## Example: Extract a PDF link from a webpage

    {
        "name": "My Paper Source",
        "method": "GET",
        "url": "https://example.com/{doi}",
        "mode": "html",
        "selector": "#pdf-link",
        "attribute": "href",
        "automatic": false
    }

`selector` is a CSS-style selector. If `attribute` is omitted, the element's `textContent` is used. `index` can be passed to select a specific element of a set.

If `automatic` is `false` or unspecified, the resolver will be used only for manual actions — Add Item by Identifier and Find Available PDFs — and not when saving from the browser.

## Example: Extract PDF URLs from a JSON API

**Note:** The Unpaywall API is used here for demonstration purposes, but Zotero
already uses its own mirror of Unpaywall data, so configuring it with a
custom resolver isn't necessary.

    {
        "name": "Unpaywall",
        "method": "GET",
        "url": "https://api.unpaywall.org/v2/{doi}?email=me@example.com",
        "mode": "json",
        "selector": ".oa_locations.url_for_pdf",
        "automatic": true
    }

`selector` uses [JSPath](https://github.com/dfilatov/jspath) syntax.

In this case, `.oa_locations.url_for_pdf` matches zero or more URL strings
in the `url_for_pdf` property in objects in the `oa_locations` array.

However, Unpaywall can return either direct PDF URLs or landing page
URLs, so matching on `url_for_pdf` alone isn't sufficient. For advanced
cases like this, a `mappings` object can be provided to pull out
specific values:

    {
        "name": "Unpaywall",
        "method": "GET",
        "url": "https://api.unpaywall.org/v2/{doi}?email=me@example.com",
        "mode": "json",
        "selector": ".oa_locations",
        "mappings": {
            "url": "url_for_pdf",
            "pageURL": "url_for_landing_page"
        },
        "automatic": true
    }

Here, the `oa_locations` array is matched directly, and `mappings` is
used to assign the `url_for_pdf` and `url_for_landing_page` properties
from the array objects to `url` (for a direct PDF link) and `pageURL`
(for a page where a PDF can be translated).
