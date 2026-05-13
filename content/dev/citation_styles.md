# Citation Styles

Zotero uses [Citation Style Language](http://citationstyles.org/) (CSL) styles and the [citeproc-js](https://bitbucket.org/fbennett/citeproc-js/wiki/Home) CSL processor for [creating citations and bibliographies](creating_bibliographies).

For information on how to use existing CSL styles with Zotero, see [Citation Styles](styles).

## Editing CSL Styles

For basic instructions on how to edit CSL styles for Zotero, see the [Step-by-step guide](dev/citation_styles/style_editing_step-by-step). More documentation can be found at <http://citationstyles.org/citation-style-language/documentation/>.

## Mapping of Zotero Variables and Item Types to CSL

A mapping of Zotero item types and variables to CSL is available [here](https://aurimasv.github.io/z2csl/typeMap.xml). A Zotero extension to create and export the current mapping from a local Zotero installation can be found [here](https://github.com/aurimasv/z2csl).

## Submitting Styles to the Citation Style Repository

Citation styles can be hosted on the [Citation Style Language Repository](https://github.com/citation-style-language/styles). Follow [these instructions](https://github.com/citation-style-language/styles/blob/master/CONTRIBUTING.md) to have your style added to the repository.

## Self-hosting CSL Styles

If you decide to host CSL styles online yourself, serving them with the “vnd.citationstyles.style+xml” MIME type allows programs such as Zotero to automatically recognize and install your styles.

## citeproc-node

[citeproc-node](dev/citation_styles/citeproc-node) is a wrapper for [citeproc-js](https://bitbucket.org/fbennett/citeproc-js/wiki/Home) for server-side rendering of citations and bibliographies.
