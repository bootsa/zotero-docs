<p id="zotero-5-update-warning" style="color: red; font-weight: bold">We’re
in the process of updating the documentation for
<a href="https://www.zotero.org/blog/zotero-5-0">Zotero 5.0</a>. Some documentation
may be outdated in the meantime. Thanks for your understanding.</p>

# Proxies

*This feature is not available in Safari.*

This page describes the Proxies tab of [Zotero Connector preferences](connector#preferences). Zotero users should be able to make complete use of the [proxies feature](connector#institutional_proxy_detection) without ever looking at this tab. By default, Zotero will prompt you to store the proxy and then route you through the proxy automatically and without further input.

![](/_media/connector/preferences/connector_proxy_preferences.png){ width=600 }

The Proxies preferences allow you to adjust the following options:

#### Enable proxy redirection

Default: checked - unchecking this will disable Zotero's proxy redirection feature. You can do this temporarily and your proxy settings will remain saved. Do not use this option if you no longer have access to the proxies saved in Zotero. In that case, delete those settings by selecting them in the “Configured Proxies” box and pressing the minus (-) button below it.

#### Automatically detect new proxies

Default: checked - unchecking this will prevent Zotero from automatically detecting and storing proxies it detects.

#### Disable proxy redirection when domain name contains...

Default: unchecked - typically you won't need to use a proxy when you are connected to the internet through your institution’s network. This option automatically disables Zotero's proxy redirection when the domain of your internet provider contains the given string. In the United States, “.edu” (the default setting) will usually work, in other countries you will have to find out your institution's domain name.

#### Configured Proxies

Proxies can be added manually by clicking on the “+” button. This section allows to specify the URL of the database being accessed under hostname and the URL scheme of the proxy. Existing proxies can be edited by selecting them in the configured proxies box. You can remove proxies by clicking the “-” button.

#### Troubleshooting

Having trouble accessing a site due to Zotero's proxying functionality? See [Proxy Troubleshooting](kb/proxy_troubleshooting).
