# Zotero Web API (Version 2)

This is an old version of the Zotero Web API. **For new development, use [API version 3](dev/web_api/v3/).**

## API Documentation

-   [Read Requests](dev/web_api/v2/read_requests)
-   [Write Requests](dev/web_api/v2/write_requests)
-   [File Uploads](dev/web_api/v2/file_upload)
-   [Syncing](dev/web_api/v2/syncing)
-   [OAuth Authentication](dev/web_api/v2/oauth)
-   [Changes from API Version 1](dev/web_api/v2/changes_from_v1)

## API Support

Please post questions regarding the Zotero API to the [zotero-dev](http://groups.google.com/group/zotero-dev) mailing list.

## API Implementations

Known implementations of the Zotero Web API include:

-   <https://github.com/fcheslack/libZotero> (PHP and Python)
-   <https://github.com/shazino/SZNZotero> (Objective-C)
-   <https://github.com/urschrei/pyzotero> (Python)
-   <https://github.com/clioweb/phpZotero> (PHP, no longer maintained)
-   <https://github.com/scholarpress/scholarpress-workshop>

The API‌ forms a fundamental part of several projects, including:

-   The online library view at zotero.org, which is built using the same API‌
-   [Zotpress](http://wordpress.org/extend/plugins/zotpress/), a WordPress plugin for including citations to items in your Zotero library in blog posts. The plugin makes extensive use of the read API and implements both key-based and OAuth for access control.
-   [Biblio Bouts](http://www.bibliobouts.org/), an game where participants compete to collect high quality sources online. The game uses the API‌ to see what items participants have saved.
-   [phpZoteroWebDAV](https://github.com/krueschan/phpZoteroWebDAV), a WebDAV implementation in PHP which allows users to sync their attachments to their own webservers, including an online library and attachment view building off the read API. (AGPL)
-   [Scanner for Zotero](https://github.com/jmschanck/Scanner-For-Zotero), Android app which saves items to Zotero libraries using the write API (Java, GPL-licensed)
-   [Zandy](https://github.com/ajlyon/zandy) Android app using the read and write APIs to provide full access to Zotero libraries (Java, AGPL-licensed)
-   [ZotPad](http://www.zotpad.com) iPad/iPhone app using the read and file upload APIs to provide read access to Zotero libraries and read/write access to attachment files. Write access is planned. (Objective C, GPL-licensed)
-   [Zotero Reader](http://www.zoteroreader.com) Browser app that provides read access to Zotero library and read/write access to PDF attachments. (Javascript/PHP)
-   [ZotSpip](http://plugins.spip.net/zotspip.html), a SPIP plugin to synchronise a Zotero library with SPIP (a content management system). References can be presented in web pages and searched through a dedicated webpage. A complementary plugin (BiblioCheck) allows a research unit to manage corrections to apply to the unit bibliography. (PHP)
