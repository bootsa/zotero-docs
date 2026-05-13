# Bibliographic Data Formats

This is a guide to bibliographic data formats that Zotero can work with. Most of these formats can be imported directly by Zotero, and some can be exported as well. Others are used only in conjunction with site translators and cannot be imported or exported directly.

For information on getting records into your library by using these import formats, see [Importing from Other Tools](adding_items_to_zotero#importing_from_other_tools).

For troubleshooting import and export issues, you can consult the information below, but first try the relevant steps in the [translator troubleshooting procedure](troubleshooting_translator_issues) and direct questions to the [support forums](/forum).

The format descriptions here are very cursory. See the linked documentation and specifications for more details.

There is also [a very outdated description](kb/field_mappings) of the mappings between Zotero fields and the fields in some of these formats.

## BibLaTeX

Export

## BibTeX

Import and export

## Browser bookmarks

Import and export

## CSL JSON

Import and export. JSON format designed for the interaction between reference managers and citeproc-js. Supported by many products using citeproc-js.

## CrossRef unixref

Import (only when called by other translators)

## Evernote

Export only. Basic transfer of info to Evernote/

## ISI Web of Knowledge

Import only. Tagged data format used by all WoK databases.

## MARC

Import
UNIMARC, MARC21, MARCXML

## MEDLINE (.nbib)

Import only (Pubmed XML should be preferred when both options are available)

## MODS XML

Import and export

-   [Introduction to MODS version 3](http://bibutils.refbase.org/mods_intro.html) -- an introduction to the format, written by the Chris Putman, author of [Bibutils](#tools).

## OpenURL ContextObjects

Import and export.
As COinS, as CTX.
Implemented not as a translator.

## OVID Tagged

Import only. Data format used across all OVID(R) databases. Import quality may vary as data is inconsistent.

## PubMed XML

Import

To generate file from a list of citations in PubMed:

1.  Select "Send to"
2.  Select "File"
3.  Under Format, select "XML"
4.  Click "Create File" button

## RIS

Import and export

RIS is a simple plain-text reference format. It is nearly universally supported by reference management software and journal databases. The official specification was last updated in 2001, so reading the format is complicated by the frequent divergences from the specification. Zotero accounts for some of the more frequent non-standard uses in its import, but exports fairly strict RIS.

Translators that build off of RIS will frequently have to pre-process the RIS to account for non-standard use of tags.

-   [RIS Specification](http://www.refman.com/support/risformat_intro.asp), provided by Reference Manager.

## Refer/BibIX

Import and export

## RefWorks(R) Tagged Format

Import and Export. Does not include collection and attachment info from RefWorks.

## RDF

Complex!

### Zotero RDF

### Vocabularies

## Non-Supported Formats

### EndNote(R) XML

### Microsoft Word Bibliography

## Tools

-   [Bibutils](https://sourceforge.net/p/bibutils/home/Bibutils/) is a utility that can convert several of the formats above into and out of MODS XML, which serves as a very expressive intermediate format. This will often be more faithful than importing into Zotero and exporting in another format.
