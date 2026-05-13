---
tags:
  - kb
  - sync
---

# Why can't I connect to a WebDAV server via HTTP on iOS or Android?

In current versions of both iOS and Android, non-HTTPS connections are blocked by default. Apps that want to allow unencrypted connections have to specifically do so and list which domains to allow them for, and the apps may face increased review scrutiny. Since anyone can get a free certificate through [Let's Encrypt](https://letsencrypt.org/) these days, we've chosen to stick to the defaults and not jeopardize the security of connections from the app, which can involve various upstream services for metadata retrieval that would pose a privacy hazard if accidentally made over HTTP. (We've also seen some egregious things like HTTPS WebDAV hosts redirecting to HTTP, and the default configuration blocks that, as it very much should.)

iOS does allow unencrypted connections to private IP address ranges (e.g., 192.168.\*). Android doesn't seem to do the same, but we've added `.local` and `.home.arpa` as exceptions.


