---
tags:
  - kb
  - basics
---

# How Do I Install Zotero on a Chromebook?

#### Step 1: Set up Linux on Chrome OS

Following the steps from Google to [Set up Linux on your Chromebook](https://support.google.com/chromebook/answer/9145439?hl=en).

#### Step 2: Open Terminal

1.  After Linux is installed, you will notice a new app in your overflow menu (where all your app icons live) called Terminal.
2.  Wait for the Terminal app to open. This might take a few minutes the first time.

#### Step 3: Install Zotero

Enter these commands in Terminal to install a packaged version of Zotero [maintained by a community member](https://github.com/retorquere/zotero-deb):

    curl -sL https://raw.githubusercontent.com/retorquere/zotero-deb/master/install.sh | sudo bash
    sudo apt update
    sudo apt install zotero

(If you prefer, you can install the [official tarball](/download), but you will have to perform some [setup steps](installation#linux) manually.)

Once these finish, you can close the Terminal and go back to your overflow (apps) menus. You will now see an icon for Zotero, and clicking on it will open the app. You can then pin the app to your Chrome Launcher.

#### Step 4: Set up the Zotero Connector

*This step may no longer be required on current versions of ChromeOS. If you can save to the Zotero app from the Zotero Connector, you can skip this step.*

To use the Zotero Connector, which allows you to save from Chrome to Zotero and use Zotero in Google Docs, you may need to install a port-forwarding app such as Connection Forwarder.

To set up forwarding using Connection Forwarder, close Zotero and any other Linux apps, and then set a forwarding rule as follows:

-   Protocol: TCP
-   Source: 127.0.0.1 (Localhost) port 23119 (Source Port, i.e., the connection port from Chrome)
-   Destination: 127.0.0.1 (Localhost) port 8080 (Destination Port, i.e., the target port in Linux)

Within the Zotero app, go to Edit → Preferences → Advanced → Config Editor, set `extensions.zotero.httpServer.port` to `8080`, and then restart Zotero.

Once you have done all these things, you should be good to go.


