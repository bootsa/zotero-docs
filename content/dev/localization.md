# Localization

While Zotero is primarily developed in English, most parts of the Zotero ecosystem have been translated into other languages. These include the Zotero client, the wiki documentation, and the Citation Style Language (CSL) citation styles.

## Desktop App

Translation efforts for the Zotero desktop app exist for over 40 languages, but many languages are still incomplete. To help localize Zotero in your favorite language, sign up for free at <https://www.transifex.com>, go to the [Transifex Zotero project page](https://explore.transifex.com/zotero/zotero/), and join a language translator team.

**Note** Translators should also check already translated strings, as some English strings have changed over time (predominantly to account for the move to Zotero as a standalone desktop app, rather than the Zotero for Firefox plugin).

Translations can be tested by [changing the language of the Zotero interface](kb/user_interface_language).

## CSL Styles

Zotero uses Citation Style Language (CSL) styles to format citations and bibliographies. CSL has advanced support for (automatic) localization of terms (e.g. "and" [English] and "und" [German]), date formats (e.g. mm/dd/yyyy [American English] and dd/mm/yyyy [Dutch]), and grammar rules.

CSL styles rely on a shared set of language-specific CSL locale files. Localization data can also be embedded in the styles themselves to override the data stored in these locale files.

To learn more about the localization support of CSL, read the sections of the CSL specification on [locale files](http://citationstyles.org/downloads/specification.html#locale-files-structure), [embedding localization data in styles](http://citationstyles.org/downloads/specification.html#locale), and the [default-locale attribute](http://citationstyles.org/downloads/specification.html#the-root-element-cs-style).

To learn how to contribute to the collection of CSL locale files, and to see the status of translation, see the [CSL locale repository wiki](https://github.com/citation-style-language/locales/wiki).

## Documentation

We're no longer accepting translations of the Zotero documentation.

Zotero staff and volunteers spend a lot of time making sure the official English documentation is comprehensive, accurate, up to date, and phrased carefully to avoid common misunderstandings we encounter in the forums, and there's no realistic way for non-English versions to be similarly maintained. Given that both Chrome and Safari now offer built-in machine translation of webpages, and it can be done in Firefox via extensions, we think that that will provide a better way of translating the official documentation for most users.

We'd encourage communities that want to maintain documentation in other languages to create more manageable usage guides elsewhere without trying to mirror the full breadth, detail, and up-to-dateness of the official documentation. If you've created a resource in another language that you feel would be useful for Zotero users, let us know in the Zotero Forums and we can add a link from the official documentation.
