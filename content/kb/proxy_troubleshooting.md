---
tags:
  - kb
  - basics
---

#### Why can't I access a proxied site when the Zotero Connector is enabled?

When you attempt to access a site that you've previously accessed through a proxy server, the Zotero Connector can [automatically redirect you through your proxy](connector_preferences#proxies).

If a site is inaccessible through your browser when the Zotero Connector is enabled but works in other browsers or when the Connector is disabled, there may be a problem with a proxy setting that the Connector has stored.

To help ensure this doesn't happen in the future, please perform the following steps:

1.  Generate a [Debug ID](debug_output#debug_output_logging) from the Connector for an attempt to load the page.
2.  Open the Proxies pane of the Zotero Connector preferences and look for a relevant proxy entry. Copy down the Hostname and Scheme, and then click the entry and copy down the settings from the section below.

Post the Debug ID and proxy details to a new forum thread so that developers can investigate.

You can then delete the proxy entry from the Proxies pane, which should fix the problem temporarily.


