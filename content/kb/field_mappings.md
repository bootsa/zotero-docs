## Import/Export Field Mappings

Zotero can import and export data in various bibliographic standards. This page links to mappings between Zotero fields and various standards.

**Please note:** Import/export is not recommended for [transferring entire Zotero libraries](kb/transferring_a_library) between systems, and, if you use Zotero's word processor plugins, links to Zotero items from existing word processor documents will be lost after an export/import.

Also note that Zotero and most of the formats listed on this page are in active development, which may mean that linked information becomes outdated from time to time. You can always test current field mappings by exporting the sample items from the [devTesting Group Library](https://www.zotero.org/groups/183462/devtesting/items/collectionKey/97FH6RRU). You can also see the relevant translator files at the [Zotero Translators GitHub repo](https://github.com/zotero/translators/).

#### Data loss during import/export

Different standards vary in the degree to which they are compatible with Zotero. Zotero RDF is in general the least lossy export format. (books, articles, journals, etc.). It is the only format that preserves information about item collections, attachment files, and notes. RIS or MODS will import/export notes (but not attachment files or collections). Other colelctions will only include data about Zoterotem metadata fields (not collections, attachment files, or notes).

#### Export format field mappings and documentation

Field mappings for most Zotero export types are listed [here](https://github.com/aurimasv/zotero-import-export-formats).

Mappings between Zotero types/fields and Citation Style Language (CSL) types/fields are also listed [here](https://aurimasv.github.io/z2csl/typeMap.xml).

Documentation is available for the [RIS](https://en.wikipedia.org/wiki/RIS_(file_format)), [MODS](http://www.loc.gov/standards/mods//mods-outline.html), [ReferBibIX](http://sti15.com/bib/formats/refer.html), [Unqualified Dublic Core RDF](http://dublincore.org/documents/dcmi-terms/), [BibTeX](http://www.bibtex.org/Format/), [BibLaTeX](http://ctan.math.washington.edu/tex-archive/macros/latex/contrib/biblatex/doc/biblatex.pdf), [Bibliontology RDF](http://bibliontology.com/), [COinS](https://www.google.be/url?sa=t&rct=j&q=&esrc=s&source=web&cd=4&cad=rja&uact=8&ved=0ahUKEwjxoc68vNLXAhUMthoKHai3BusQFgg_MAM&url=https%3A%2F%2Farchive.is%2FdGBd&usg=AOvVaw06rReD7TcTdcTFIoPsiGUu), [RefWorks](https://www.refworks.com/refworks/help/refworks_tagged_format.htm), and [Wikipedia Citation](http://en.wikipedia.org/wiki/Citation_templates) formats.
