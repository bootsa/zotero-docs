<p id="zotero-5-update-warning" style="color: red; font-weight: bold">We’re
in the process of updating the documentation for
<a href="https://www.zotero.org/blog/zotero-5-0">Zotero 5.0</a>. Some documentation
may be outdated in the meantime. Thanks for your understanding.</p>

Site translators allow you to save items in Zotero with just a single click. Here you'll find the tools and documentation to get started with translator development.

[Introduction to Zotero translators](dev/translators)

**Note** Much of the translator documentation below is outdated and/or incomplete.

[Translator Tutorial](dev/translators/tutorial)

[Scaffold: an IDE for Zotero translators](dev/translators/scaffold)  
Scaffold is a Firefox add-on to help you write translators.

[How to Write a Zotero Translator](http://niche-canada.org/member-projects/zotero-guide/chapter1.html)  
Adam Crymble's guide to writing a simple screenscraping translator for Zotero (aka *HWZT*) is a comprehensive guide to writing a translator using [Scaffold 1.0](http://dev.zotero.org/scaffold) and [Solvent](http://simile.mit.edu/wiki/Solvent), not to mention the DOM, JavaScript, and XPath. Unfortunately

-   much has changed since HWZT was written, limiting its current usability.
-   HWZT is not wikified, limiting its maintainability.

[How to Write a Zotero Translator++](dev/how_to_write_a_zotero_translator_plusplus)  
*HWZT++* wikifies HWZT, and updates it by using uplevel tools. Currently (Jul 2010) HWZT++ is useful, though further work is planned, since it currently

-   is merely a list of deltas to HWZT, so one will unfortunately need to work with both resources open.
-   does only the same thing that HWZT does, i.e. it uses Scaffold (2.0) to write a screenscaper.

[Translator Development Outside Scaffold](dev/translator_development_outside_scaffold) In Zotero >= 2.0, translators are just [JavaScript](http://en.wikipedia.org/wiki/JavaScript) files. While Scaffold can ease translator development, some prefer to work directly on the filesystem. Here's how.

[Zotero Translators - The Missing Manual](dev/translators_reference_guide) This missing manual aims to expand on Adam Crymble's introductory tutorial, discussing the functions in Zotero.Utilities, describing how translators can call other translators, and more.

[Translator Overview](dev/translator_overview)

[Translator Tips & Tricks](dev/translator_tips__tricks)

A more technical (but fairly outdated) guide additionally covering the creation of import and export translators can be found [here](http://deskbox.gmu.edu/translators.html)
