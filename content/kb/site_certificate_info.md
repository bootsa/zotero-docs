## Viewing Site Certificate Information

When encountering [security certificate errors](kb/ssl_certificate_error) in Zotero, viewing the certificate information for zotero.org or another affected domain in your web browser may provide more details on what is causing the problem on your system. If you share this information in the Zotero Forums, we may be able to help identify what is interfering (or it may be self-explanatory, based on, for example, the name of your institution or security software on your system).

1.  Load any zotero.org web page (such as this one) or, if you're getting an error about another domain, an HTTPS URL for that domain. (If you're getting a certificate error for s3.amazonaws.com, use [this URL](https://s3.amazonaws.com/zoterofilestorage/test).)
2.  View the certificate information. The process to do this varies by browser:
    -   In **Firefox**, click the padlock icon, click the right-arrow next to the domain name, and look at the "Verified by:" line. For full information, click More Information -> Security -> View Certificate and look at the details under Issued To, Issued By, and Period of Validity.
    -   In **Chrome (Windows)**, click the padlock icon, click on Certificate, and look at the "Issue to:" and "Issued by:" lines.
    -   In **Chrome (Mac)**, click the padlock icon, click on Certificate, and look at the "Issued by" line. For full information, expand the Details section and look at the values for Common Name and Organization.
    -   In **Safari**, click the padlock icon -> Show Certificate and look at Expires, Common Name under Subject Name, and Organization and Common Name under Issuer Name.

Secure connections to zotero.org will show that the certificate is issued by "Amazon". If you see a different entity, something is likely intercepting your secure connections. (Something intercepting your connection could also self-identify as one of the expected entities, but this is rare.)

![](tag&gt;kb){ .align-left }
