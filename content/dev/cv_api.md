<p id="zotero-5-update-warning" style="color: red; font-weight: bold">We’re
in the process of updating the documentation for
<a href="https://www.zotero.org/blog/zotero-5-0">Zotero 5.0</a>. Some documentation
may be outdated in the meantime. Thanks for your understanding.</p>

# Zotero CV API

Though not strictly part of the Zotero server API, Zotero profile CVs can be retrieved programmatically via:

    http://www.zotero.org/api/users/<userID>/cv

Note that User IDs are different from usernames and can be found on the [API Keys](/settings/keys) page and in OAuth responses. Also note that SSL is not required.

The specified user's CV is returned as XML which can be embedded or reused in a variety of ways. For example, you could transform it into HTML ready for styling via the following XSL:

``` xml
<?xml version="1.0" encoding="utf-8"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" xmlns:zapi="http://zotero.org/ns/api" version="1.0">
  <xsl:output method="html"/>
  <xsl:template match="/">
    <div id="cv">
      <xsl:for-each select="zapi:cvsection">
        <div class="section">
          <div class="title">
            <xsl:value-of select="./@title"/>
          </div>
          <div class="content">
            <xsl:copy-of select="."/>
          </div>
        </div>
      </xsl:for-each>
    </div>
  </xsl:template>
</xsl:stylesheet>
```
