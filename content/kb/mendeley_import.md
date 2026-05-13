---
tags:
  - kb
  - entry
---

# How do I import a Mendeley library into Zotero?

Zotero can directly import all data, including the full folder structure, from an online Mendeley library.

To import your Mendeley library, follow these steps:

1.  Make sure that all data and files have been synced to Mendeley servers.
    -   If you use **Mendeley Reference Manager**, your data and files are already all online.
    -   If you use **Mendeley Desktop**, check your sync settings to make sure that data and files are being synced, and confirm that you can open PDFs in your online Mendeley library.
2.  Make sure you're running the latest version of Zotero (Help → Check for Updates…).
3.  Go to File → Import within Zotero and choose the "Mendeley Reference Manager (online import)" option.

You'll be asked to log in to Mendeley to allow Zotero to perform the import. Your Mendeley password is never seen or stored.

## Alternative Method

If for some reason you're not able to perform a direct online import, it's possible to import from a local Mendeley database by installing an old version of Mendeley Desktop from before Mendeley began [encrypting](#mendeley_database_encryption) the local database. All your data and files will still need to be synced to Mendeley servers. See the [local import instructions](kb/mendeley_local_import) for more information.

## Using Mendeley Citations

Zotero's Word and LibreOffice plugins can read citations created by Mendeley Desktop and automatically relink them to imported Mendeley items in your Zotero library, so you can continue using the same documents with Zotero.

Citations created with Mendeley Cite are not readable by Zotero.

Note: Prior to Zotero 6.0.19 (released in December 2022), Zotero could read and use Mendeley citations, but they wouldn't be linked to imported items in your Zotero library. If you imported your Mendeley library using Zotero 6.0.18 or earlier, you'll need to repeat the import process once using Zotero 6.0.19 or later — just select "Relink Mendeley Desktop citations" when starting the importer. (If you've already imported citations using 6.0.19 or later, this option will no longer appear.)

## Known Issues

There are a few issues to be aware of when importing from Mendeley.

-   If your Mendeley account requires institutional credentials to log in, you may need to create a separate Mendeley account and connect it to the institutional account, and then use the personal account to log in. See [How do I use institutional (Shibboleth) credentials with Mendeley?](https://service.elsevier.com/app/answers/detail/a_id/33535/supporthub/mendeley/p/16075/) on the Mendeley support site for more information.
-   It’s not possible to directly import group libraries. To import items in group libraries, copy the group items to a collection in your Mendeley library before importing. You can then create a Zotero group and drag imported collections or items to that group.
-   Mendeley allows any field to be added to any type. When importing into Zotero, if a field isn’t valid for a given item type, the field is placed into the Extra field. When possible, those will be used automatically in citations (e.g., Original Date), and future versions of Zotero will automatically convert those to any real fields that become available.

## Troubleshooting

Make sure you’re running the latest version of Zotero available via Help → “Check for Updates…”.

If you’re running the latest version and something doesn’t come through how you expect or you run into any trouble, let us know in the [Zotero Forums](https://forums.zotero.org/).

## Mendeley Database Encryption

The importer described above imports data directly from an online Mendeley library, which requires all data and files to be uploaded to Elsevier servers in order to be imported into Zotero.

Zotero originally announced work on a fully local importer in early 2018, but a few months later, Elsevier began encrypting the local Mendeley database, making it unreadable by Zotero and other standard database tools. This change came despite Mendeley having long touted the openness of their database format as a guarantee against lock-in and explaining in documentation that the database could be accessed using standard tools. Mendeley Desktop itself had imported data from Zotero’s own open database since 2009.

The [Mendeley 1.19 release notes](https://www.mendeley.com/release-notes/v1_19) claimed that the encryption was for “improved security” on shared machines, yet applications rarely encrypt their local data files, as file protections are generally handled by the operating system with account permissions and full-disk encryption, and someone using the same operating system account or an admin account can already install a keylogger to capture passwords. Mendeley later [switched to claiming](https://twitter.com/mendeley_com/status/1006915998841221120) that the change was required by new European privacy regulations — a bizarre claim, given that those regulations are designed to give people control over their data and guarantee data portability, not the opposite — and continued to assert, falsely, that full local export was still possible, while [repeatedly](https://twitter.com/mendeley_com/status/1006919608471818240) [dismissing](https://web.archive.org/web/20211120213432/https://twitter.com/MendeleySupport/status/1006920802120470528) reports of the change as “#fakenews”.

Direct access to the Mendeley database is the only fully local way to export the full contents of one’s own research. The export formats supported by Mendeley don’t contain folders, various metadata fields (date added, favorite, and others), or PDF annotations. While Mendeley offers a web-based API, it contains only uploaded data, so relying on it means that anyone wanting to export their own data first needs to upload all their data and files to Elsevier’s servers. The API is under Elsevier’s control and can be [changed](https://service.elsevier.com/app/answers/detail/a_id/31598/supporthub/mendeley/p/16075/) or [discontinued](https://mendeleyblog.wordpress.com/2021/03/11/mendeley-refocusing-announcement-mobile-app-retirement//) at any time.

Since making this change, Elsevier has replaced Mendeley Desktop with Mendeley Reference Manager, which is essentially a wrapper around the website and doesn’t contain a real local database at all.


