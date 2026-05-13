# Zotero Web API (Version 1)

This is an old version of the Zotero Web API. **For new development, use [API version 3](dev/web_api/v3/start).**

## API Documentation

-   [Read API](dev/web_api/v1/read_api)
-   [Write API](dev/web_api/v1/write_api)
-   [File Uploads](dev/web_api/v1/file_upload)
-   [OAuth Authentication](dev/web_api/v1/oauth)

## API Implementations

Known implementations of the Zotero Web API include:

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
