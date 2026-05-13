# Overriding Security Certificate Errors in Zotero

**Note:** These instructions are only for use with security software that intercepts/scans HTTPS connections, a WebDAV server with a self-signed certificate, or an institutional network that monitors encrypted traffic using a custom root certificate authority (CA). You should never override certificate errors unless you [understand the consequences](kb/ssl_certificate_error). When in doubt, please contact your network administrator or ISP.

## Self-Signed Certificate

Zotero does not currently provide a graphical way to whitelist self-signed certificates, so you will need to copy files from a working Firefox installation.

If you are using a WebDAV server with a self-signed certificate, you can open the WebDAV URL in Firefox, accept the certificate, and then copy the cert_override.txt file from the [Firefox profile directory](http://support.mozilla.com/kb/Profiles) to the [Zotero profile directory](kb/profile_directory).

### Zotero 8.0

Zotero 8.0 can read a cert_override.txt file from [Firefox 140 ESR](https://ftp.mozilla.org/pub/firefox/releases/140.7.0esr/). A file from a later version of Firefox may or may not work.

### Zotero 7.0

Zotero 7.0 can read a cert_override.txt file from [Firefox 115 ESR](https://ftp.mozilla.org/pub/firefox/releases/115.29.0esr/). A file from a later version of Firefox may or may not work.

### Zotero 6

Zotero 6 expects a cert_override.txt file created by [Firefox 60 ESR](https://ftp.mozilla.org/pub/firefox/releases/60.9.0esr/), with a line in this form:

    192.168.xxx.xxx:1234    OID.2.16…    1D:E4:07:…    U    AAAA…

If you create an override file with a newer version of Firefox, your cert_override.txt file may contain a line with a trailing colon after the port number ("1234" in this example) and may be missing one or more letters before "AAAA" ("U" in the above example):

    192.168.xxx.xxx:1234:    OID.2.16…    1D:E4:07:…    AAAA…

To use such a file in Zotero 6, strip the colon from after the port number and add a "U" (untrusted cert) before "AAAA". To allow for a hostname mismatch, add "M".

## Custom Certificate Authority

If you or your organization is using a custom certificate authority, which can be the case when using security software or connecting via a proxy server, Zotero may need to be configured to accept the custom CA:

-   **Windows/Mac:** Zotero 7 will automatically use the system root certificate store, which in most cases should allow it to work automatically like other browsers on the system.
-   **Linux**: Zotero is based on Firefox and uses the same certificate mechanism, so you or your IT department will need to configure Firefox for the custom CA in a new Firefox 115 ESR profile and then copy the cert9.db, key4.db, and pkcs11.txt files from the [Firefox profile directory](http://support.mozilla.com/kb/Profiles) to the [Zotero profile directory](kb/profile_directory).

![](tag&gt;kb){ .align-left }
