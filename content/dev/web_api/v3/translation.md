<p id="zotero-5-update-warning" style="color: red; font-weight: bold">We’re
in the process of updating the documentation for
<a href="https://www.zotero.org/blog/zotero-5-0">Zotero 5.0</a>. Some documentation
may be outdated in the meantime. Thanks for your understanding.</p>

# Zotero Web API Translator-Based Saving

**This is not currently the default [version](dev/web_api/v3/basics#api_versioning) of the API. Include the `Zotero-API-Version: 3` HTTP header or the `v=3` query parameter to access this version.**

The [Zotero Web API](dev/web_api/v3/) allows items to be [created manually](dev/web_api/v3/write_requests), but it can also automatically create items from uploaded URLs, similar to the one-click saving from web pages offered in the Zotero client. The server takes care of downloading the page, extracting metadata using Zotero translators, and creating a new item in the library.

An [API key](dev/web_api/v3/basics#authentication) with write access to a given library is necessary to use write methods.

## Restrictions on Use

This feature is not meant as a general-purpose tool for extracting metadata from web pages. If you're only interested in extracting metadata from web pages — for example, for integration into another project — rather than saving items to a Zotero library, you should install Zotero's [translation-server](https://github.com/zotero/translation-server), a server-side version of Zotero's translation framework, on your own server. To prevent abuse, use of web translation may be [rate limited](dev/web_api/v3/basics#rate_limiting) to a greater extent than other API requests.

## Web Translation Requests

### Single item

    POST /users/1/items

    {
      "url": "http://www.amazon.com/gp/product/0838985890/"
    }

If only a single item is found for the given URL, the item will be saved to the library with a `200 OK` response:

    {
      "success": {
        "0": "C6SA6U3W"
      },
      "unchanged": {},
      "failed": {}
    }

### Multiple items

    POST /users/1/items

    {
      "url": "http://scholar.google.com/scholar?q=test"
    }

If multiple items are found for the URL, the API will return `300 Multiple Choices`:

    {
      "url": "http://scholar.google.com/scholar?q=test",
      "token": "085f1b8341ea4c221320de18d6f4e3c6",
      "items": {
        "0":"Reproductive Tradeoffs In Uncertain Environments: Explaining The Evolution Of Cultural Elaboration",
        "1":"Dynamics of clade diversification on the morphological hypercube",
        "2":"The Clustering of High Redshift Galaxies in the Cold Dark Matter Scenario",
        "3":"Recovering the Primordial Density Fluctuations: A comparison of methods",
        "4":"Reconstruction Analysis of Galaxy Redshift Surveys: A Hybrid Reconstruction Method",
        "5":"On-line determination of stellar atmospheric parameters Teff, log g, [Fe/H] from ELODIE echelle spectra. I - The method",
        "6":"Limits on the star formation rates of z>2 damped Ly-alpha systems from H-alpha spectroscopy",
        "7":"Unambiguous quasar microlensing",
        "8":"Does the AGN Continuum Shape Change with Luminosity?",
        "9":"Testing the Relation Between the Local and Cosmic Star Formation Histories",
        "10":"Supernova pencil beam survey"
      }
    }

Delete the unwanted entries from the `items` array in the returned JSON and reupload the JSON, making sure existing keys aren't changed.

    POST /users/1/items

    {
      "url": "http://scholar.google.com/scholar?q=test",
      "token": "085f1b8341ea4c221320de18d6f4e3c6",
      "items": {
        "1":"Dynamics of clade diversification on the morphological hypercube",
        "2":"The Clustering of High Redshift Galaxies in the Cold Dark Matter Scenario",
        "7":"Unambiguous quasar microlensing"
      }
    }

`200 OK` response:

    {
      "success": {
        "1": "A7NC29DW",
        "2": "NPN2K5ZA",
        "7": "CPWS7BVK"
      },
      "unchanged": {},
      "failed": {}
    }
