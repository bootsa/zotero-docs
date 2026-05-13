---
tags:
  - kb
---

# Zotero and the Text Encoding Initiative (TEI)

The [Text Encoding Initiative](http://www.tei-c.org/) is a consortium that curates an international standard for the XML markup of texts. The standard enjoys broad support among libraries, museums, publishers, and scholars. Web-based TEI-compliant documents are found in increasing numbers online.

TEI provides for rich bibliographic metadata in the element `<teiHeader>` and its children, some of which are modeled after the [International Standard Bibliographic Description (ISBD)](http://en.wikipedia.org/wiki/International_Standard_Bibliographic_Description) (see TEI's [note for library cataloguers](http://www.tei-c.org/release/doc/tei-p5-doc/en/html/HD.html#HD8)). For encoding bibliographic citations that may appear in a text, the element `<biblStruct>` is commonly used for a structured bibliographic citation, in which only bibliographic sub-elements appear and in a specified order.

TEI and Zotero are in theory a perfect fit, with Zotero able to detect and import a TEI-compliant text and, in turn, able to export to a well-formed `<biblStruct>` element. At this time, such interaction is still under development:

-   Zotero records can be exported to TEI-compliant XML
-   Zotero cannot currently import TEI-compliant XML. An import translator could be written, or a stylesheet could be created to convert TEI tags to Zotero-ready RDF.

And there is a [TEI group on Zotero](http://www.zotero.org/groups/tei), in case you want to get acquainted with what has been published on TEI. As users in the Zotero and TEI communities build bridges to each other, they are encouraged to add new tools to this page.


