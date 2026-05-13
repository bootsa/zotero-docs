<p id="zotero-5-update-warning" style="color: red; font-weight: bold">We’re
in the process of updating the documentation for
<a href="https://www.zotero.org/blog/zotero-5-0">Zotero 5.0</a>. Some documentation
may be outdated in the meantime. Thanks for your understanding.</p>

This page describes some of the reported issues with the Word and OpenOffice/NeoOffice word processor plugins for Zotero 1.0, together with possible solutions.

If you are using Zotero 2.0, see the [main troubleshooting page](word_processor_plugin_troubleshooting).

# Error Messages

## "An error occurred communicating with Zotero"

You may receive the following message when attempting to use the word processor plugins:

*"An error occurred communicating with Zotero. Please ensure Firefox is open and try again."*

There are a number of possible causes for this error. Make sure you are running the latest version of Zotero, and then review the following steps in order:

#### If you can insert a citation into a new, empty document but receive a communication error in an existing document:

1.  Verify that you have the CSL style file used by the document installed.
2.  See [Debugging Broken Documents](word_processor_plugin_troubleshooting#debugging_broken_documents).

#### If you receive a communication error when attempting to insert a citation into a new, empty document:

1.  Make sure Firefox is running and Work Offline mode is **not** checked in the File menu. You do not need to be online to use Zotero word processor integration, but Firefox's Work Offline mode cannot be enabled.
2.  Check if you get the error using a different bibliography style.
3.  Make sure the Track Changes feature is disabled in Word/OpenOffice, as it is known to cause problems with Zotero integration.
4.  If you are using Microsoft Word on Windows, open Internet Explorer and make sure Work Offline is not enabled under the File menu. Word's connection to Zotero is dependent on the Windows/IE network settings.
5.  If you are using OpenOffice, make sure the plugin and the required Python components are correctly installed and enabled.
    -   Ensure that Zotero and all subcomponents are enabled in the Extension Manager.
    -   Linux users may need to install the openoffice.org-pyuno (or equivalent) package if their distribution doesn't install it by default.
    -   If the PYTHONPATH environment variable is set by another application, you may need to remove it.
6.  Start Zotero with [debug output](debug_output) enabled and look for a message in the first 15-20 lines that includes the phrase "integration HTTP server".
    -   If you see the message "Not initializing integration HTTP server":
        -   Make sure other copies of Firefox/Zotero aren't running on your system (including in other user accounts or in hidden processes). Restarting the computer might help. Advanced users on OS X and Linux could use the netstat tool from a terminal window to check if other applications are bound to port 50001.
    -   If you see the message "Integration HTTP server listening on 127.0.0.1:50001":
        -   Disable any firewall software running on your computer. If this fixes the problem, make sure your firewall is set to allow access to "localhost" or "127.0.0.1" (also known as the "loopback interface").
        -   If you don't have or have disabled firewall software, check your computer's proxy settings.
            -   On Windows XP, open Internet Explorer, go to Tools→Internet Options→Connections→LAN Settings, and disable “Automatically detect settings” and "Use a proxy server for your LAN". If this fixes the problem, you will need to keep "Automatically detect settings" off and make sure "Bypass proxy server for local addresses" is checked.
7.  Still having trouble? Search the Zotero forums. There are many threads on [communication errors in Word and OpenOffice](http://forums.zotero.org/discussion/1615/2/communicating-with-zotero/) and [communication errors in OpenOffice specifically](http://forums.zotero.org/discussion/1155/openoffice-extension-no-connection-with-firefox/). If posting a new message, please include the following information:
    -   Operating system
    -   Firefox version
    -   Zotero version
    -   Word processor (Word or OpenOffice) and version
    -   Zotero word processor plugin version
    -   Whether the integration server was listed as running in the debug output
        -   If the integration server was running, please also send in an error report via Report Errors (if available) in the Zotero Actions menu (![](/_media/start/gearicon2.jpg)) and include the Report ID in your message.

## Run-time error '91'

This is a generic error with many potential causes. It is often caused by problems with proxy servers or other network settings.

1.  Open Internet Explorer, go to Tools->Internet Options->Connections->LAN Settings, and disable "Automatically detect settings". This is known to fix the problem for Shaw Cable users in Canada and may help with other ISPs as well.
2.  See the [relevant forum thread](http://forums.zotero.org/discussion/2787/new-thread-on-the-ms-word-plugin-vb-runtime-error-91/) for further discussion.

One user also reported that deleting Normal.dot from Word fixed the error.

## "BASIC execution error, property or method not found"

This has been reported in OpenOffice if a citation is inserted inside a frame.

# Word Processor Freezing

Some users have experienced freezes when attempting to insert citations.

-   Make sure more than one Zotero-enabled Firefox isn't running on your computer.
    -   If you use multiple user accounts on your computer, plugin windows may appear in other user accounts. You will need to always close Firefox before switching users or [use a different integration port](http://forums.zotero.org/discussion/5072/ooo-opens-window-in-wrong-session/) on each account.

Other solutions that people have found:

-   Disable Java runtime in OpenOffice
-   Upgrade to OpenOffice 3.1 or later
