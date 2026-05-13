---
tags:
  - kb
  - basics
---

### Why isn't Zotero detecting updates?

#### Updates require Administrator privileges

Zotero does not require Administrator privileges for any of its operations and generally does not require them to install updates. If you are asked for a password or for Administrator privileges during Zotero update, one of two things is occurring:

1.  Zotero was initially installed with Administrator privileges. This is not necessary. Uninstall Zotero and re-install it from [zotero.org/download](/download). If prompted to give Administrator privileges during the installation process, click Cancel, rather than OK.
2.  Your IT administrators have set your system to require Administrator privileges to install program updates. Inquire with your IT administrator if Zotero can be whitelisted to allow it to update itself.

#### No automatic updates are found, but manual update checks work

If you're not receiving automatic updates to Zotero or an add-on but you can find updates manually by clicking Help → Check for Updates… (for Zotero) or Tools → Add-ons → Gear → Check for Updates… (for add-ons), check that automatic updates are enabled. For Zotero, open the Config Editor from the [Advanced pane](preferences/advanced) of [Zotero preferences](preferences), and ensure that `app.update.auto` and `app.update.enabled` are both set to `true`. For add-ons, check Update Add-Ons Automatically in the Gear menu of the Zotero Add-ons window.

#### No automatic or manual updates are found

If new versions of Zotero or add-ons aren't being installed automatically and aren't being detected when you manually check for updates, something on your system or network may be intercepting secure (HTTPS) connections to zotero.org or the add-on's update server. To determine whether your connection is being intercepted, check the [site certificate info](kb/site_certificate_info).

##### Quick Fix

If the site certificate information points to security software on your system (Bitdefender, Avast), disable the SSL/TLS/HTTPS scanning feature of that software. The exact name of the feature will vary. Consult the software's documentation for help. Read on for more details.

##### More Details

To ensure the security and privacy of its users, Zotero requires all connections to be made over HTTPS, which ensures that you're connecting directly to a remote website and that your connection is encrypted. However, software installed on your system, or your network administrator, can override the security protections of HTTPS, essentially masquerading as any website. Some security software does this in an attempt to provide additional security: it intercepts HTTPS connections, scans the contents itself, and then re-encrypts the data and sends it to the original website in a new connection. While the makers of such software would argue that they're protecting you with this feature by searching for malware served over HTTPS, this behavior breaks a fundamental security feature built into web browsers. You can think of it as someone going through all your postal mail, reading every letter, and warning you if they find any junk mail. While what they're doing is potentially useful, they really have no business snooping around in your mail. (And in some cases, antivirus vendors have even [stuck their own ads and trackers into the envelopes](http://www.howtogeek.com/199829/avast-antivirus-was-spying-on-you-with-adware-until-this-week/) before resealing them.)

To receive updates automatically, you have two options:

1\) Disable the SSL/TLS/HTTPS scanning feature in the security software and try the update again. If the certificate information identifies your institution as the intercepting party, you'll need to speak to your network administrator and request that they stop intercepting your secure connections to websites, though it may be a condition of your use of the network.

2\) If you trust the software or institution that is intercepting your connection, you can force Zotero to download updates over intercepted connections. Open the Zotero Config Editor from the [Advanced pane](preferences/advanced) of [Zotero preferences](preferences). Right-click on the list of settings that appears and select New → Boolean. For Zotero, enter `app.update.cert.requireBuiltIn` for the property name and choose `true` for the value. For add-ons, enter `extensions.update.requireBuiltInCerts` and choose `true` for the value. Be aware that there will no longer be a guarantee that you are receiving legitimate versions of Zotero or add-ons unless you return to the Config Editor and disable these preferences.

#### Zotero Connector for Firefox not detecting updates

If the Zotero Connector for Firefox is not updating automatically, verify that automatic updates are enabled from the Firefox Add-ons window (Tools → Add-ons → Gear → Update Add-ons Automatically). Also check the [Zotero Connector preferences](connector_preferences) and ensure that automatic updates are enabled there.

If automatic updates are enabled, try to update the connector manually by clicking the Gear button in the Firefox Add-ons window and choosing Check for Updates. If updates aren't being detected manually, you may be encountering the secure connection interception issue described above. To determine whether your connection is being intercepted, check the [site certificate info](kb/site_certificate_info).

If the site certificate information points to security software on your system (Bitdefender, Avast), disable the SSL/TLS/HTTPS scanning feature of that software. The exact name of the feature will vary. Consult the software's documentation for help.

As a temporary fix, you can manually install the updated extension from [zotero.org/download](downlod). (Normally Firefox prevents manual installations over such connections as well, but we have implemented a workaround to allow them.) Without automatic updates, however, you may run into compatibility issues or bugs later that have already been fixed.

To receive updates automatically, you have two options:

1\) Disable the SSL/TLS/HTTPS scanning feature in the security software and try the update again. If the certificate information identifies your institution as the intercepting party, you'll need to speak to your network administrator and request that they stop intercepting your secure connections to websites, though it may be a condition of your use of the network.

2\) If you trust the software or institution that is intercepting your connection, you can force Firefox to download add-on updates over intercepted connections. Enter "<about:config>" in the Firefox address bar, right-click on the list of settings that appears, select New → Boolean, enter `extensions.update.requireBuiltInCerts` for the property name, and choose `true` for the value. Be aware that there will no longer be a guarantee that you are receiving legitimate versions of Zotero and other Firefox add-ons unless you return to <about:config> and disable that preference.


