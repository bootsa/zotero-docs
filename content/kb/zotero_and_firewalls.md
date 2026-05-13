---
tags:
  - kb
---

# What connections do I need to allow through a firewall for Zotero to work properly?

While Zotero is a local program that can be used without internet access, it should generally be given the same access that browsers on the system have. Without such access, much of its functionality will be broken.

Zotero connects over HTTPS to various zotero.org subdomains for syncing, translator/style updating, retraction notifications, error reporting, version updates, and more, as documented in the [Zotero privacy policy](privacy) (which also explains how to disable each type of access). All Zotero domains are behind AWS load balancers, so resolved IP addresses are transient and cannot be used for allowlisting.

Beyond zotero.org domains, various core functionality depends on internet access that is unrestricted beyond standard content blocking: file saving (from any site a user saves from), Add Item by Identifier, PDF retrieval, PDF metadata retrieval, metadata updating, etc. Because of these required connections, it's not possible to limit Zotero's internet access to specific domains without breaking many features.

If you're having trouble allowing Zotero to connect through a firewall or proxy, see [Connection Error](kb/connection_error).


