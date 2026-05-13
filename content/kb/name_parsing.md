---
tags:
  - kb
  - styles
---

#### How does Zotero parse things in the name fields?

There are actually three parts to the story of names in Zotero ("creators", in techie lingo):

1.  Creator types;
2.  Field mode; and
3.  Name-part parsing.

Each of these topics is covered below. The first two are very simple.

##### Creator types

Each name field has a label to its left, which is actually a button. Clicking on it will open a list of possible \*creator types\* for the current item type. You can change the type of an individual creator by clicking on its label and selecting from the list.

##### Field mode

There is a small square icon to the right of each name (just before the **(+)** and **(-)** buttons used to add and remove creators). Clicking on the square icon will toggle the name between *single-field mode* and *two-field mode*.

-   In single-field mode, the field content is not parsed when generating citations. [1] This mode is ordinarily used for institutional names.
-   In two-field mode, the field is parsed to (even) smaller parts when generating citations. Two-field mode should ordinarily be used for personal names. *This includes Asian names!* The CSL processor in Zotero can correctly format names in a variety of languages, [2] and across all citation styles; but this flexibility requires correctly entered data. It is not a good practice to "force" a particular form by selecting single-field mode unnecessarily.

##### Name-part parsing

In two-field mode only, personal names are parsed into five separate parts for formatting purposes. Here they are, with a brief explanation of each:

-   *Family name:* The family or clan name of an individual is the primary "family name" in Zotero: [3]
    -   The family name of "Sam Spade" is "Spade".
    -   The family name of "Jeremy Atticus Finch" is "Finch".
    -   The family name of "Kuruma Torajirō" is "Kuruma" (note that the family name part of this Japanese character's name is written first).
-   *Given name:* This refers to an individual's "own" name, or names:
    -   The given name of "Sam Spade" is "Sam".
    -   The given names of "Jeremy Atticus Finch" are "Jeremy Atticus".
    -   The given name of "Kuruma Torajirō" is "Torajirō" (the lead protagonist of the Japanese "Tora-san" series).
-   *Dropping particle:* Dropping particles, a feature of some European names, are descriptive elements that are placed between the given and the family name when written in "normal" order. A dropping particle is never placed with the family name when written in "sort order".
    -   In "Ludwig van Beethoven", "van" is a dropping particle.
    -   In "Jean de La Fontaine", "de" is a dropping particle.
-   *Non-dropping particle:*
-   Articular



[1] In the Juris-M (formerly Multilingual Zotero/MLZ) variant of official Zotero, single-field names are parsed into subunits by splitting the field on pipe ("**|**") characters. In official Zotero, the field is printed exactly as written.

[2] Chinese and Japanese names will render correctly in official Zotero. Names in some languages (Khmer and Myanmar being two examples) are not yet handled correctly by official Zotero; users with special requirements may wish to explore Juris-M, which is able to apply precise name formatting rules across all language domains.

[3] In some other countries, individuals have no family or clan name, but only given names. Formatting conventions in such countries vary. In Myanmar and Cambodia, the entire set of names is always written in formal contexts (including citations). In Mongolia, it is customary to handle the bare patronymic in the same way as a "family" name. Where names with special requirements must be handled frequently, Juris-M may be worth a look.
