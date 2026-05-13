---
tags:
  - kb
---

**These directions have not been updated in some time and may no longer be up to date.**

#### How do I get my Zotero collection to work with an Exhibit or Citeline presentation?

The [Simile Project](http://simile.mit.edu/), sponsored by MIT, has developed several JavaScript applications that help a Zotero user integrate a bibliography into a website.

[Citeline](http://citeline.mit.edu/), under Simile's purview, has a Firefox plugin called Zotz to streamline the conversion process. This plug-in, however, works only with Firefox 2.0. Further, when importing the BibTeX file, the Citeline filter incorrectly handles Unicode characters beyond the Basic Latin set. Boxes or question marks are frequently encountered. At this time Citeline is not able to provide support for non-Latin characters.

[Exhibit](http://www.simile-widgets.org/exhibit/), now supported independent of Simile, is very similar to Citeline, but is more powerful and customizable. Exhibit has a page explaining how to [generate a publications exhibit](http://www.simile-widgets.org/wiki/How_to_make_a_publications_exhibit). But a different kind of problem is encountered here: one must convert a Zotero collection to Exhibit's JSON format. And Zotero does not directly export to a JSON format.

The handiest conversion tool is Simile's [Babel converter](http://service.simile-widgets.org/babel/) ([alternate link](http://simile.mit.edu/babel/)). But in using Babel one encounters conversion problems similar to those found in the Citeline conversion. Exhibit calls for Unicode characters rendered as UTF-32, but Babel renders them UTF-8. Further, the characters < and > are converted to {\\\\textless} and {\\\\textgreater}. And if you have started with a Zotero-generated BibTeX file, you may find curled braces {} in fields where they do not belong (an [idiosyncrasy](/forum/discussion/31/bibtex-export) in Zotero's BibTeX converter). So some cleanup is necessary before the JSON file exported by Babel is ready for interaction with Exhibit.

Here is a detailed explanation of the problems in the Babel conversion process: when Babel encounters a character outside the Basic Latin table (but less than value U+0800), Babel replaces it with two new character sequences: one a multiplicand (e.g., \\u00C3 and upward, depending upon how large the target Unicode number is) and the other the Unicode value of the character point in the Basic Latin plane that is an exact multiple of 64 less than the intended Unicode value. For example, é (Unicode value U+00E9) is translated by Babel, not as \\u00E9 (as Exhibit calls for) but into \\u00C3\\u00A9, which displays as Ã©.

