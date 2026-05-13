---
tags:
  - kb
---

#### "[domain] uses an invalid security certificate."

The above or a similar message generally indicates that something on your computer or network is intercepting and possibly monitoring your connection to the internet.

(If you're getting a certificate error for a proxy or WebDAV URL, that's likely [a different issue](kb/incomplete_cert_chain).)

Try the following steps to debug the problem:

1.  Restart Zotero and/or your computer and try again. This error can be caused by intermittent network issues.
2.  Make sure your system clock and time zone are set correctly.
3.  If you get the same error after restarting, Zotero's network connection is likely getting intercepted, possibly due to a proxy server on your network or security software or malware on your computer. View the [certificate information](kb/site_certificate_info) for the affected domain in your browser, which may show you what is intercepting your connections.
    1.  If your browser shows the affected domain as validated by an expected entity (e.g., "Amazon" for zotero.org), Zotero's network connection may be [configured differently](kb/connection_error) from your browser's.
    2.  If your browser shows the affected domain as verified by something else and you recognize the listed entity (e.g., the name of security software or your institution), take appropriate action:
        -   If you see security software listed, disable it, or disable its SSL/TLS/HTTPS-scanning feature.
        -   If you see your institution listed, your IT department is likely intercepting your traffic and has installed a certificate for a "custom certificate authority" in your browser to avoid security errors resulting from the interception. Depending on how your system is configured, Zotero may not trust the same custom certificate by default, in which case it will properly warning you of the intercepted connection. You can try following the [certificate override](kb/cert_override) instructions for Zotero, but be aware that your connection to Zotero servers is being monitored by your institution.
    3.  If you don't recognize the listed entity:
        -   Check your system for malware.
        -   If you're using any security software, try temporarily disabling it.
        -   If you're in an institutional environment, ask your IT department if they have installed a "custom certificate authority" in your browser. If so, you can try following the [certificate override](kb/cert_override) instructions for Zotero, but be aware that your connection to Zotero servers is being monitored by your institution.
        -   If you're using a laptop, try from a different network.
        -   In rare circumstances, reinstalling Zotero may help.


