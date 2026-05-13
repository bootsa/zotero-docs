---
tags:
  - kb
---

# How can I open multiple instances of Zotero and save to or cite from a specific instance?

You can start multiple instances of Zotero at the same time as long as they're pointing to [different profile and data directories](kb/multiple_profiles). On Windows and Linux, the [-no-remote command-line flag](http://kb.mozillazine.org/Opening_a_new_instance_of_Firefox_with_another_profile) may also be required.

Additional configuration may be required for browser and word processor integration, as described below.

Note that using multiple instances of Zotero will use more memory, so depending on how much RAM you have in your computer, using multiple instances at the same time may be slower than using a single instance with more data.

## Zotero Connector

By default, when running multiple copies of Zotero (either by using multiple profiles or running Zotero in separate OS accounts), the Zotero Connector will save items to the first opened instance. To point a specific Zotero Connector installation to a specific Zotero profile, you can set the `extensions.zotero.httpServer.port` [hidden pref](preferences/hidden_preferences) in Zotero and the `connector.url` pref in the connector. Incrementing the port number by 1 for one pair (Zotero profile + connector installation) is sufficient.

## Word Processor Integration

### Word

#### Word for Mac (Zotero 6) / Word for Windows

The Word plugin should automatically connect to the correct Zotero instance on a multi-user system. It's not possible to point the Word plugin at a specific instance of Zotero within the same OS user account.

#### Word for Mac (Zotero 7)

Open the user's [Word Startup folder](https://www.zotero.org/support/word_processor_plugin_manual_installation#locating_your_word_startup_folder) and create a `ZoteroPort.txt` file containing the port number you've configured in `extensions.zotero.httpServer.port`.

### Google Docs

Google Docs integration relies on the Zotero Connector being configured to connect to a specific Zotero instance, as described above.

### LibreOffice

The LibreOffice plugin uses a fixed HTTP port to connect to Zotero and cannot currently be configured, so it will connect to the first opened instance.


