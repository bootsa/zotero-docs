# Zotero Security

*If you believe you've found a security issue in Zotero software, please contact [security@zotero.org](mailto:security@zotero.org).*

Zotero was created with the philosophy that your research data belongs to you and should be kept secure and private by default.

All Zotero software is [open source](https://github.com/zotero) and can be audited for security and privacy practices. Zotero builds for macOS and Windows are code-signed, and all builds are distributed with transport encryption, ensuring that the version you run is the version we released.

Unlike many cloud-based tools, the Zotero desktop application is a local program that runs on your computer and saves all research data locally by default. Unless you explicitly set up syncing, your research data never leaves your computer.

If institutional policies prevent uploading of data to third-party servers, Zotero can always be used locally without syncing any data, but syncing is required to use group functionality.

If you choose to sync your data with the Zotero servers, all data is encrypted in transit with current best practices ([Zotero's API endpoint receives an A+ score](https://www.ssllabs.com/ssltest/analyze.html?d=api.zotero.org&hideResults=on) on the well-respected SSL Labs test) and stored within the Amazon cloud, where access is tightly restricted to the small number of Zotero staff members who need access to maintain the service. Data in newly created accounts is also encrypted at rest using AES-256. All data is currently stored in the us-east-1 AWS region in the United States.

While library data and group files can be synced only with Zotero servers, for syncing of files in personal libraries you can choose between Zotero servers and a WebDAV server under your control, or you can use linked files that are stored in a location of your choosing and aren't synced by Zotero.

The Zotero data server is open-source and can be run locally, which some organizations choose to do, but this can be technically challenging, and we don't currently provide support for such installations.

See our [privacy policy](privacy) for further details on Zotero's collection and use of data you choose to share.
