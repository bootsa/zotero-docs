---
tags:
  - kb-obsolete
  - zotero_for_firefox
---

**This article applies to the deprecated Zotero for Firefox (pre-Zotero 5.0) plugin. It no longer applies to the current versions of Zotero.**

#### How can I use the Chrome or Safari Connectors with Zotero for Firefox?

[Zotero Connectors](3.0#zotero_connectors) allow you to save items to Zotero from within browsers other than Firefox, using Zotero's site translators. Currently Zotero has to be open in order to save items through Zotero Connectors from most websites.

To use the Chrome and Safari connectors without switching to Zotero Standalone, you can actually use the Zotero instance in Firefox as your central repository, and the Safari and Chrome connectors can send citations to it.

Type `about:config` in the address bar of Firefox and search for "zotero.httpServer". You'll want to double-click on the entry `extensions.zotero.httpServer.enabled` and restart Firefox.

Then install the connector in the other browser (Chrome or Safari) and also restart this browser. Now the Save to Zotero icon should show up in that browser too, and clicking it will result in the item being saved in the Zotero library in Firefox.

**Note: This configuration is not supported in conjunction with Zotero Standalone.** Opening Zotero Standalone while Firefox is open may result in unexpected errors.


