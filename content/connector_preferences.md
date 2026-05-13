---
tags:
  - pref
---

# Zotero Connector Preferences

The Zotero Connector browser extensions allow you to add items to your Zotero library with the [click of a button](adding_items_to_zotero#web_translators) in Firefox, Chrome, or Safari. This page describes the preferences for the Zotero Connectors.

## Accessing the Zotero Connector Preferences

-   **Firefox:** Right-click on the Zotero save button and choose Preferences
-   **Chrome:** Right-click on the Zotero save button and choose Options
-   **Safari:** Right-click on the page background and choose "Zotero Preferences"

## General

![connector_preferences_general.png](/_media/connector_preferences_general.png){ .align-center width=700 }

-   **Zotero Status:**
    -   Whether the Zotero Connector can connect to the Zotero desktop client. If the Connector reports that Zotero is unavailable, see [Zotero Unavailable](kb/connector_zotero_unavailable).
-   **Save to Zotero.org:**
    -   When the Zotero desktop client is closed, the Zotero Connector will save directly to the [zotero.org](/) servers. These settings let you reauthorize your broswer to save to your zotero.org account or clear your account credentials. You can also control whether PDF attachments and [web page snapshots](attaching_files#web_snapshots) are automatically saved when importing to zotero.org.
-   **Automatic File Importing:**
    -   By default, the Zotero Connector will offer to import RIS, BibTeX, and Refer/BibIX bibliographic files when you open them in your browser. You can disable this feature or manage the sites from which data is imported here.

## Proxies

![connector_preferences_proxies.png](/_media/connector_preferences_proxies.png){ .align-center width=700 }

Many institutions require you to sign-in to a proxy system to access electronic resources while you are off-campus. The Zotero Connector can make this more convenient. When it detects that you are using an institutional proxy to access a particular site, it will ask if you want to remember it in the future. If you agree, Zotero will automatically use the proxy for matching URLs in the future. You should be routed through the proxy login site if you're not already logged in, then you can access the database as you normally would.

Zotero users can use the proxies feature without ever looking at this preference tab. By default, Zotero will prompt you to store the proxy and then route you through the proxy automatically and without further input.

Zotero proxy redirection is not available in Safari.

The Proxies preferences allow you to adjust the following options:

-   **Enable proxy redirection**
    -   Zotero's proxy redirection is enabled by default. Uncheck this option to disable proxy redirection. You can do this temporarily and your proxy settings will remain saved. *Do not* use this option if you no longer have access to the saved proxies. In that case, delete those settings by selecting them in the "Configured Proxies" box and pressing the minus (-) button below it.
-   **Show a notification when redirecting through a proxy**
    -   By default, Zotero will show a temporary banner at the top of your browser when it redirects through a saved proxy. Uncheck this box to disable this notification.
-   **Automatically detect new proxies**
    -   By default, Zotero will automatically detect when you visit a page through an institutional proxy and offer to remember the proxy the next time you visit the website. Uncheck this box to prevent Zotero from prompting you to store proxies it detects.
-   **Disable proxy redirection when domain name contains**
    -   Typically you won't need to use a proxy when you are connected to the internet through your institution’s network. This option automatically disables Zotero's proxy re-direction when the domain of your internet provider contains the given string. In the United States, ".edu" (the default setting) will usually work. In other countries you will have to find out your institution's domain name.
    -   This option is disabled by default. This option is only available when the Zotero desktop client is open.

##### Configured Proxies

When Zotero automatically detects and saves institutional proxies, they will be stored here. You can remove stored proxies by clicking the minus (-) button below the list. If you are having issues with a proxy, try to remove it from the list and re-add it by visiting the site and letting Zotero automatically detect the proxy settings again.

You can manually add proxies by by clicking on the plus (+) button. From there, you can specify the URL of the database being accessed under hostname and the URL scheme of the proxy. You can add/remove additional URLs to redirect through a single proxy by clicking on the plus (+) and minus (-) buttons below the Hostnames list. You can also enable/disable automatic association of new hostname URLs with a proxy server.

Some proxy servers require hyphens in proxied hostname URLs to be converted to dots. Check the box for this option if this is the case for your proxy server.

If you are having trouble accessing a site due to Zotero proxy redirection functionality, see [Proxy Troubleshooting](kb/proxy_troubleshooting).

## Advanced

![connector_preferences_advanced.png](/_media/connector_preferences_advanced.png){ .align-center width=700 }

These preferences are used for reporting errors and troubleshooting information to the Zotero developers.

-   **Report Errors:** If you are having a problem using the Zotero Connector, use this button to submit an Error Report ID to Zotero, then post to the [Zotero forums](/forum). See [Reporting Problems](reporting_problems) for instructions on how to submit helpful error reports.
-   **Debug Output Logging:** To help diagnose a problem, the Zotero developers may ask you to submit a Debug Log ID. This is different from an Error Report ID above. To submit a debug log, check "Enable Logging", then complete the sequence of steps neeeded to produce your error. Then, click "Submit Debug Report" and post the Debug ID number to the [Zotero forums](/forum). Try to avoid performing unrelated actions when making a debug log.
-   **Translators:** Zotero will automatically check for and install updated translators. You can manually check for updates here. By default, the Zotero Connector will report broken site translators to zotero.org. This helps Zotero to keep the Zotero import process working smoothly on sites across the Web.
-   **Advanced Configuration:** The Config Editor options are not useful for general troubleshooting and should only be used if instructed by the Zotero developers.


