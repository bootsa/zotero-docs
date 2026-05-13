---
tags:
  - kb
  - basics
---

#### Why am I getting a database version error?

After reinstalling or downgrading Zotero, you may see the following error message when you you try to open Zotero:

*This version of Zotero is older than the version last used with your database. Please upgrade to the latest version from zotero.org.*

This message results from trying to use a Zotero database from a later version of Zotero in an earlier version of the software. For example, if you installed Zotero 5.0 but then reinstalled Zotero 4.0.29.15, you would get this error. Most Zotero versions preserve backward database compatibility, but occasionally it's necessary for Zotero developers to make changes to the database that prevent it from working with previous versions.

The best solution is generally to reinstall the latest version of Zotero from [zotero.org](/). (If you were using the Zotero Beta, you may need to reinstall the [latest beta build](beta_builds).)

If for some reason you don't want to or are not able to install the latest version, you can restore the pre-upgrade database backup that Zotero stored in your [Zotero data directory](zotero_data). Look for the zotero.sqlite.\*.bak file with the highest number (e.g., zotero.sqlite.77.bak). Close Zotero, move your existing zotero.sqlite file out of the way, and then copy the numbered backup file into place as zotero.sqlite. Then restart Zotero.

If you don't have data you care about, or if you've fully synced your data and files with your online account, you can keep your current Zotero version by closing Zotero/Firefox, deleting your [Zotero data directory](zotero_data) completely, and, optionally, syncing to restore your previous data.

**Previously, the most common cause of this error was having used Juris-M (formerly known as MLZ)**. The current version of that software no longer causes this. See [this post](https://forums.zotero.org/discussion/50443/multilinguale-version-von-zotero-mlz/?Focus=228336#Comment_228336) by Juris-M's developer on how to securely return to using regular Zotero.


