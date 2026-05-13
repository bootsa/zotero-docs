<p id="zotero-5-update-warning" style="color: red; font-weight: bold">We’re
in the process of updating the documentation for
<a href="https://www.zotero.org/blog/zotero-5-0">Zotero 5.0</a>. Some documentation
may be outdated in the meantime. Thanks for your understanding.</p>

-   When using XPaths to locate page elements, try to avoid absolute paths that might break easily. For example, instead of using`/html/body/table/tbody/tr/td[2]/table/tbody/tr/td[@class="bucket"]/div[@class="content"]/ul/li`try a more flexible XPath like`//table/tbody/tr/td[@class="bucket"]/div[@class="content"]/ul/li`
-   When writing translators, debugging via the console is essential. Unfortunately, this is slow and ugly in Windows. It is better in Windows to use the debug log accessible through the Zotero preferences pane, under "advanced". Don't forget to turn off debug logging after you are through with a translator-writing session. To debug via the console, start Firefox from the command line (Terminal.app in MacOS). Any output from the translator can be dumped to the console using `Zotero.debug("hello world!");`
-   The functions `Zotero.Utilities.HTTP.doGet` and `Zotero.Utilities.processDocuments` run asynchronously. In order to allow them to complete before moving along, follow either function with `Zotero.wait()` and include `Zotero.done()` as the onDone in order to signal the translator that it has completed its asynchronous operations.
