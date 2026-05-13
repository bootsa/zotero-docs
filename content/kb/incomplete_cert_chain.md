---
tags:
  - kb
  - sync
---

## "[domain] uses an invalid security certificate. The certificate is not trusted because […]"

If a Zotero error report shows an error similar to the above for your institution's **proxy** or **WebDAV server** or a site you're trying to save from, there are two possibilities:

1.  You're connecting to a server with a "self-signed certificate". For a proxy or WebDAV server, you would need to [whitelist the certificate](kb/cert_override) in Zotero. This is uncommon for public servers.
2.  The server is misconfigured and will need to be fixed by your IT department or the IT department of the site operator. See the technical details below for more information.

If you're using an institutional proxy or WebDAV server and are unsure which is the case, point your IT department to this page along with the URL from the error report.

If you're getting a certificate error for a zotero.org or s3.amazonaws.com URL — for example, while syncing — that's [a different issue](kb/ssl_certificate_error).

### Technical Details: Missing Intermediate Certificate

If the server isn't using a self-signed certificate (i.e., if it's chained to a root certificate that's trusted in browser stores), this error generally occurs because the server isn't serving the necessary "intermediate certificate" for secure connections, and Zotero (like Firefox, on which it is based) won't download it on its own. Without an intermediate certificate, it's impossible to determine whether the connection is secure, and the connection fails.

To verify that this is the case, submit the URL from the error report to the [SSL Labs server test](https://www.ssllabs.com/ssltest/) and view the results. If you see "Chain issues: Incomplete" in orange under "Additional Certificates (if supplied)", you're experiencing this issue. The report will then also say "Extra download" (instead of "Sent by server" or "In trust store") for one or more certificates listed under "Certification Paths". Alternatively, one or more bundled intermediate certificates may be listed as expired. The missing intermediate certificate(s) should be provided along with the site's primary certificate when HTTPS clients connect.

Note that loading the same HTTPS URL in a browser may still work. In that case, either the browser is downloading intermediate certificates automatically (as Chrome does) or you previously loaded another site (perhaps even another from your institution) that included the intermediate certificate, which the browser cached and is using even on sites that don't serve it properly. Sites should always serve their intermediate certificates, however, and are misconfigured if they don't. If you create a new profile in Firefox, you should get a certificate error trying to load the same URL, which is essentially the situation Zotero is in.


