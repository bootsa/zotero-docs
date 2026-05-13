---
tags:
  - kb
  - styles
---

### Does Zotero support label/authorship trigraph styles, like [ddb98]?

Not yet fully. Zotero's citation processor, [citeproc-js](https://github.com/juris-m/citeproc-js) will automatically create values for the "citation-label" variable in CSL styles consisting of four inital letters from author names See [DIN-1505-2](styles/din-1505-2-alphanumeric) for an example style using this format.

The formatting for automatic citation labels cannot currently be customized in Zotero. You can manually enter citation labels for individual items in your Zotero library by adding them to the "Extra" field with this format:

    citation-label: Smi01

Some discussions about this topic are available [here](https://github.com/citation-style-language/schema/issues/41) and [here](https://github.com/citation-style-language/styles/issues/678).


