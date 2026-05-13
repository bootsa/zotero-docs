# “Could not find a running Word instance”

This page only applies to the error "Could not find a running Word instance" when using the Zotero plugin in Word on Windows.

For general word processor troubleshooting, see [Word Processor Plugin Troubleshooting](word_processor_plugin_troubleshooting).

Perform the following steps:

1.  Make sure you're running **at least Zotero 7.0.3**, which includes a change that can avoid this issue.
2.  Make sure neither Zotero nor Word are running as administrator (right-click → Properties → Compatibility → "Run this program as an administrator" is unchecked) and that you're not running Windows using the hidden Administrator account. ![](/_media/kb/no_admin.png){ .align-right width=300 }
3.  If using OneDrive, save the copy of the document to your local hard drive, or try renaming the file to remove any spaces in the filename. OneDrive is known to interfere with the plugin for some people.
4.  Make sure you have [User Account Control](https://support.microsoft.com/en-us/windows/user-account-control-settings-d5b2046b-dcb8-54eb-f732-059f321afe18) enabled. You can change the UAC behavior by opening the Control Panel → System and Security → Change User Account Control settings. Make sure your level is at least "Notify me only when programs try to make changes to my computer (do not dim my desktop)" or higher, and **then restart your computer**.![](/_media/kb/uac.png){ .align-right width=500 }
5.  If re-enabling UAC and restarting doesn't resolve the problem, you can try temporarily changing Zotero to run in Windows 8 compatibility mode. We've received several reports that this fixes the problem, and that compatibility mode can then be disabled without the problem recurring. To test, right-click on the Zotero shortcut, go to Properties → Compatibility, and set "Run this program in compatibility mode for" to "Windows 8". Then restart Zotero and test the Word plugin. You should then disable compatibility mode, as permanently running a program under compatibility mode can result in lower performance, security vulnerabilities, and other unexpected problems.
6.  Temporarily disable any security software you're running, which could interfere with the connection between Word and Zotero.

#### Post on the Zotero Forums

If none of these steps help resolve the issue, please create a new thread in the [Zotero Forums](/forum) for further troubleshooting. Be sure to include a [Report ID](reporting_problems#provide_a_report_id) from Zotero, your operating system and Word versions, and the steps you've taken to try to fix the error.
