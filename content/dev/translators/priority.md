Translator priority determines which order the translators are called for detect\* and do\* stages of translation. The lower the priority value the earlier the translator is called.

### Web Translators

The priority for a [web translator](https://www.zotero.org/support/dev/translators/coding#web_translators) should be chosen according to the following guidelines:

-   100 = specific journal/website (target should be a specific domain)
-   150 = multi-journal sites with different subdomains, but all journals would look practically the same
-   200 = multi-journal sites with different subdomains and some journals may have somewhat different layout
-   250 = CMS/Library Catalog with no specific domain, but either a very unique URL or unique checks in detectWeb (for all possible detection options). i.e. unlikely to be a false-positive
-   260 = CMS/Library Catalog with no specific domain, but somewhat unique detectWeb checks (mostly URL-based checks).
-   270 = CMS/Library Catalog with no specific domain and rather generic URL checks (conceivably, could be a false-positive)
-   300+ = Translators to be run on every page. Priority numbers should be in order of metadata quality.

(see <https://github.com/aurimasv/translators/commit/5b4ef451a9c3c14fa9b2b8d5bce37a8bf7c1a3f2> for more information)

Higher priority (lower value) translators will override translators for detectWeb even in other frames of the web page window and will become the translator invoked by the URL bar icon.

### Import Translators

The priority for import translators is mostly important for automatic detection of translators when importing metadata from files. The first translator that matches in detectImport stage will be used for import. Generally, different metadata formats will not match against different translators, but where this is a possibility, the translator priority may be important.

### Search Translators

Priority is important to consider for search translators, where several translators may match against given metadata. In this case, lower priority value should be assigned to translators that have more broadly applicable databases (e.g. Library of Congress vs Lulu for ISBN, or CrossRef vs mEDRA for DOI) and preferably to APIs with fast response times.

### Export Translators

Priorities are not relevant to export translators.
