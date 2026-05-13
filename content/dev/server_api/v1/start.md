<p id="zotero-5-update-warning" style="color: red; font-weight: bold">We’re
in the process of updating the documentation for
<a href="https://www.zotero.org/blog/zotero-5-0">Zotero 5.0</a>. Some documentation
may be outdated in the meantime. Thanks for your understanding.</p>

# Zotero Server API (Version 1)

This is the current default version of the Zotero Server API. This version will be discontinued in the near future. For new development, use [API version 2](dev/server_api/v2/start).

## API Documentation

-   [Read API](dev/server_api/v1/read_api)
-   [Write API](dev/server_api/v1/write_api)
-   [File Uploads](dev/server_api/v1/file_upload)
-   [OAuth Authentication](dev/server_api/v1/oauth)

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
