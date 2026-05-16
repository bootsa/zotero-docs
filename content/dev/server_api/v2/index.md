<p id="zotero-5-update-warning" style="color: red; font-weight: bold">We’re
in the process of updating the documentation for
<a href="https://www.zotero.org/blog/zotero-5-0">Zotero 5.0</a>. Some documentation
may be outdated in the meantime. Thanks for your understanding.</p>

# Zotero Server API (version 2)

This is the recommended API version for all new development. To use this version, you currently must include the [Zotero-API-Version HTTP header](dev/server_api/v2/read_requests#api_versioning) in all requests. The current default version of the API is [version 1](dev/server_api/v1/).

## API Documentation

-   [Read Requests](dev/server_api/v2/read_requests)
-   [Write Requests](dev/server_api/v2/write_requests)
-   [File Uploads](dev/server_api/v2/file_upload)
-   [Syncing](dev/server_api/v2/syncing)
-   [OAuth Authentication](dev/server_api/v2/oauth)
-   [Changes from API Version 1](dev/server_api/v2/changes_from_v1)

## API Support

Please post questions regarding the Zotero API to the [zotero-dev](http://groups.google.com/group/zotero-dev) mailing list.

## API Implementations

Known implementations of the Zotero Server API include:

-   <https://github.com/fcheslack/libZotero> (PHP and Python)
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
