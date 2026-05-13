---
tags:
  - kb
  - basics
---

# Zotero Connector: “Is Zotero Running?”

When you click the Save to Zotero button in your browser or try to use Zotero with Google Docs, you may receive the following message:

*"The Zotero Connector was unable to communicate with the Zotero desktop application."*

The Zotero Connector needs to connect to the Zotero desktop app in order to save data or insert citations into Google Docs. (It can also save pages directly to zotero.org, but saving to the Zotero application provides the best experience.)

First, make sure that Zotero is installed and open on your computer. If you don't yet have the Zotero application, you can install it from the [downloads page](/download).

Next, restart your browser and try again.

After restarting, if Zotero is open but the Zotero Connector still reports that Zotero is unavailable, something on your computer is preventing the Connector from talking to Zotero. You can determine whether the problem is within the browser or a system-wide problem by loading the URL `http://127.0.0.1:23119/connector/ping` in one or more browsers while Zotero is open. If Zotero is running, it should display "Zotero is running" or "Zotero Connector Server is Available".

-   If you can load that URL but the Zotero Connector still shows Zotero as unavailable, try these steps until the problem is resolved:
    1.  Make sure you've given the Zotero Connector permission to access all websites. In Chrome or Edge, right-click on the Save to Zotero button, select "This Can Read and Change Site Data", and make sure it's set to "On All Sites". In Safari, go to the Websites tab of the Safari settings, select Zotero Connector under Extensions, and make sure "For other websites" is set to "Allow". The [Zotero privacy policy](privacy#zotero_connector) explains why this is necessary.
    2.  Uninstall and reinstall the Zotero Connector.
    3.  Temporarily disable any browser extensions that may block network requests, such as AdBlock, uBlock Origin, NoScript, EFF Privacy Badger, or Request Policy. If the Connector stops saying that Zotero is offline, reenable each extension one at a time and, if the problem recurs, whitelist `127.0.0.1` port `23119` in the extension's settings.
    4.  Temporarily disable any other installed extension.
    5.  Try in another browser. If the problem occurs there as well, security software on your computer is likely blocking extension requests across multiple browsers.
    6.  If the other browser works, create a new profile in your original browser. If this fixes the problem, something is wrong with your original profile, and you'll need to either identify the problem or transfer your bookmarks, history and other data to the new profile. If the problem occurs in a new profile, security software on your computer may be interfering with extension requests only in this particular browser.
-   If you can't load the URL in one browser but you can in another browser, try these steps in the original browser until the URL works:
    1.  If your computer is connecting via a proxy server, ensure that the host `127.0.0.1` (an alias for your computer itself) is excluded from proxying in either the browser or system proxy settings.
    2.  Temporarily disable any browser extensions that may block network requests, such as AdBlock, uBlock Origin, NoScript, EFF Privacy Badger, or Request Policy. If the URL starts working, reenable each extension one at a time and, if the problem recurs, whitelist `127.0.0.1` port `23119` in the extension's settings.
    3.  Temporarily disable any other installed extension.
-   If you can't load the URL in any browser, try these steps until the URL works:
    1.  If your computer is connecting via a proxy server, ensure that the host `127.0.0.1` (an alias for your computer itself) is excluded from proxying.
    2.  Restart your computer.
    3.  Temporarily disable any security software running on your system. If the URL starts working, reenable each piece of software one at a time and, if the problem recurs, whitelist `127.0.0.1` port `23119` in the software's settings.
    4.  Restart Zotero with debug logging enabled via Help → Debug Output Logging → "Restart with Logging Enabled…", and then go to Help → Debug Output Logging → View Output. Copy the output to a text file and search for "HTTP server". You should see one of three messages:
        -   `HTTP server listening on 127.0.0.1:23119` — Zotero is listening successfully and something else is blocking the connection.
        -   `Not initializing HTTP server` — Zotero wasn't able to listen on port 23119, possibly because some other program was already doing so. This should be preceded by an error that may provide more information.
        -   `Browser is offline -- not initializing HTTP server` — Zotero couldn't detect a network connection at all.
    5.  It may help to try in a new OS account. (You don't need to set up syncing in Zotero — an empty library is fine for testing.) If the URL starts working, you'll need to figure out what in your original account is blocking the connection, based on the message you see in Zotero debug output. If it doesn't work in a new account either, some system-level software on your computer is blocking the connection, and you'll need to troubleshoot this on your own system.


