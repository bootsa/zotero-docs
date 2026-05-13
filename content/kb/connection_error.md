---
tags:
  - kb
  - sync
---

## "Error connecting to server. Check your Internet connection."

When Zotero can't access the network, it's usually caused by proxy settings or security software on your computer.

By default, Zotero uses any manually entered proxy servers or a proxy auto-config (PAC) URL in your system proxy settings. It does not automatically use Web Proxy Auto-Discovery (WPAD), or "Auto Proxy Discovery" on macOS, even when enabled in the system settings.

If you don't use a proxy to connect to the internet, you should disable all proxies in your system proxy settings. If you do need to connect via a proxy, you should verify that the system settings are correct. Note that other software on your computer may not be using the system proxy settings, which is why other programs may still be able to connect to the internet when Zotero cannot.

If you need to configure the Zotero proxy settings differently from the system settings, you can access the Config Editor from the Advanced pane of the Zotero preferences, apply the [same settings that you would in Firefox](http://kb.mozillazine.org/Network.proxy.type) (on which Zotero is based), and restart Zotero, but the default setting (network.proxy.type = 5, to use the system proxy settings) is recommended.

If using a PAC file, either automatically or with network.proxy.type = 2, and your proxy requires HTTP authentication, ensure that most or all of the hosts in `extensions.zotero.proxyAuthenticationURLs` are being handled by your PAC file. Zotero will test a random subset on each startup to trigger a proxy authentication prompt if necessary.

To use WPAD, you must set network.proxy.type to 4.

If changing proxy settings doesn't help, try temporarily disabling any security/firewall software on your system.

Some connection errors can also be caused by [certificate issues](kb/ssl_certificate_error) on your network.

See also [Zotero and Firewalls](kb/zotero_and_firewalls).


