# Zotero Connector

[Zotero Connector](/download/connectors) is a browser extension that helps you create a bibliographic library with items rich in metadata. It adds a button to your browser which allows to save items with a single click. Zotero Connector is available for Firefox, Chrome and Safari.

## Adding Items

After [installing](/download/connectors) the Connector a Zotero button will be added to your browser. Clicking the button will save the currently open website into your Zotero library. The saving workflow has three steps:

##### Select a collection in Zotero

![](/_media/connector/select_collection.png){ width=200 }

##### Click the Connector button

![](https://www.zotero.org/static/images/blog/chrome_toolbar_button.png){ width=500 }

##### The item is saved into your library

![](/_media/connector/progress_window.png){ width=330 }

For more detailed instructions read the [Adding Items to your Zotero Library](adding_items_to_zotero) guide.

## Other Features

Aside from item saving, the Connector has other features that may help your workflow.

### Institutional Proxy Detection

Many institutions provide a way to access electronic resources while you are off-campus by signing in to a web-based proxy system. The Connector makes this more convenient by automatically detecting your institutional proxy. Once you’ve accessed a site through the proxy, the connector will automatically redirect future requests to that site through the proxy (e.g., if you open a link to jstor.org, you’ll be automatically redirected to jstor.org.proxy.my-university.edu).

![](https://www.zotero.org/static/images/blog/new-features-for-chrome-and-safari-connectors/proxy-register.png){ width=600 }

Proxy detection does not require manual configuration. You can disable or customize it from the [connector preferences](connector/preferences/proxies).

### Bibliographic File Importing

Many online databases offer users the option to export citation data directly to RIS or Refer format. Zotero Connector will automatically prompt you to add the references directly into your library. If you choose ‘Cancel’, you can download the file normally.

![](/_media/connector/automatic_file_import.png){ width=500 }

### Citation Style Installation

The Connector makes it easy to install [citation styles](styles) from [Zotero Style Repository](styles). Clicking on a style will prompt you to install it into Zotero. If you choose ‘Cancel’, you can download the style normally.

![](https://www.zotero.org/static/images/blog/new-features-for-chrome-and-safari-connectors/style-install.png){ width=500 }

### Saving to Online Library

Zotero Connector allow saving items directly to your zotero.org online library without Zotero open. The preferred way to manage and save to your library should still be by running the Zotero client, but saving to online library can be used as an alternative, if the client is not available.

When using the Connector to save a page without Zotero running, you will be prompted to authorize with your zotero.org account. After successful authorization the Connector will save items directly to your online library.

![](/_media/progress_window_zotero_org.png){ width=330 }

You can see your online library by clicking My Library at the top of this page. To access the saved items from Zotero, you should set up [Syncing](sync).

## Preferences

### Locating the preferences page

##### Chrome

You can find the Connector Preferences by either right-clicking on Zotero Connector extension icon and selecting Options or by navigating to //<about:extensions//> and clicking the Options link under Zotero Connector extension.

##### Firefox

Connector Preferences page is found by right-clicking on a page, under Zotero Connector submenu or by navigating to //<about:addons//> and clicking the Preferences button under Zotero Connector extension.

##### Safari

You can locate the Connector Preferences page by long-pressing on the Connector extension button and selecting Zotero Preferences or by right-clicking on a page and selecting Zotero Preferences.

### Sections

The preference page has the following sections:

-   [General](connector/preferences/general): check Zotero client status and authorize saving to zotero.org
-   [Proxies](connector/preferences/proxies) (not available on Safari): set up and change institutional proxy settings
-   [Advanced](connector/preferences/advanced): options for troubleshooting, reporting errors and debugging

![](/_media/connector/connector_preferences.png){ width=400 }
