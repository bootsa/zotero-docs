---
tags:
  - kb
---

#### How can I use Zotero with a SOCKS proxy?

Zotero can be configured to use a SOCKS proxy. This is useful when you have set up a local port forwarding to your institution's servers. If you only configure your browser to use the proxy, Zotero Connector may fail to download the full-text files of references you save because it will not download them via your institution's servers.

First, open the Config Editor, which is located under the Advanced tab of the Preferences window.

![](/_media/preferences_about_config_proxy_socks.png){ width=600 }

Scroll down until you find the **network.proxy...** options or use the search box.

Type the IP of the proxy server in the **network.proxy.socks** preference. If the proxy server is on your machine, use `127.0.0.1`.

Likewise, set **network.proxy.socks_port** to be the port of the proxy server.

**network.proxy.socks_remote_dns** specifies whether to use the DNS of the proxy server. If you are not sure, it is best to change it to `true`.

Finally, set **network.proxy.type** to the value `1`. This indicates that you have manually configured the proxy settings.

Zotero will now redirect all requests to the proxy server. This means that when you ask the Zotero Connector add-on in the browser to download a file or web page, Zotero will download it using the proxy you just specified in the settings.


