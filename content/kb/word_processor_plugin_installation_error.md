# Troubleshooting Errors with Word Processor Plugin Installation

Follow the steps below for [Word for Windows](#word_for_windows), [Word for Mac](#word_for_mac), or [LibreOffice](#libreoffice) if you receive an error trying to install the word processor plugin.

For general troubleshooting see [Word Processor Plugin Troubleshooting](word_processor_plugin_troubleshooting).

## Word for Windows

Zotero will automatically try to install the Word plugin and keep it up to date. You can force automatic installation at any time by going to the Zotero settings → Cite → Word Processors and pressing "(Re)install Word Add-in". If the automatic installation procedure fails, follow the steps below.

**Try to install the plugin via the Zotero settings after each step.**

1.  Close Word before attempting to install the plugin. The plugin will fail to install if Word is open.
2.  Temporarily disable any proprietary security software.
3.  Reset your Word Startup folder. In Word go to File → Options → Advanced. At the bottom of the dialog under the "General" section, press "File Locations…". In the dialog under "Startup", the "Location" field should either be empty or end with `Roaming\Microsoft\Word\STARTUP`. If it does not, select the Startup entry and click "Modify". In the file dialog, click in the address bar, paste `%AppData%\Microsoft\Word\STARTUP`, press Enter/Return, and then click OK to confirm the new location.
4.  Make sure your user account has permissions to write to the Word Startup folder.
    1.  Open the Word Startup folder in Explorer `%AppData%\Microsoft\Word\STARTUP`
        -   Windows 11: press the three dots (...) menu button and select Properties.
        -   Windows 10: Select the Home tab and press Properties.
    2.  Open the Security tab.
    3.  In the top list, click on your Windows Account username, and confirm in the bottom list that for the entry "Full control" there is a checkmark under Allow.
    4.  Click the Advanced button and confirm that under "Owner" your username is listed.
5.  If you are working on a computer provided by your institution, contact your IT department.
6.  [Install the plugin manually](word_processor_plugin_manual_installation#word_for_windows).

If the plugin doesn't appear in Word after a manual installation, see [Zotero toolbar doesn't appear](word_processor_plugin_troubleshooting#zotero_toolbar_doesn_t_appear).

Note that you'll need to repeat a manual installation every time the plugin is updated, so it's much better to fix automatic installation. To troubleshoot the automatic installation, please create a new thread in the [Zotero Forums](/forum) so we can try to help. Be sure to include a [Report ID](reporting_problems#provide_a_report_id) from Zotero, your operating system and Word versions (open a Word document, choose File from the top-left corner, click Account in the left navigation bar, and see the section under About Word, on the right side of the window), and the steps you've taken to try to fix the problem.

## Word for Mac

Zotero will automatically try to install the Word plugin and keep it up to date. You can force automatic installation at any time by going to the Zotero menu → Settings → Cite → Word Processors and pressing "(Re)install Word Add-in". If the automatic installation procedure fails, follow the steps below.

**Try to install the plugin via the Zotero settings after each step.**

1.  Close Word before attempting to install the plugin.
2.  If you're running macOS 15 Sequoia, when Zotero attempts to install the Word plugin, you'll be prompted to allow Zotero to "access data from other apps". You must click **"Allow"** to give Zotero permission to copy the plugin to the Word Startup folder. If you clicked "Don’t Allow", restart Zotero and reinstall the plugin from the Cite pane of the Zotero settings, and choose "Allow" when prompted. Zotero uses this permission solely to install the plugin, and the permission lasts only until Zotero is next closed. You won't be prompted again until the next time Zotero needs to update the plugin.
3.  Temporarily disable any proprietary security software.
4.  Reset your Word Startup folder. In the Word menu, select "Settings…". Under "Personal Settings", select "File Locations". Select the entry for "Start-up" and click Reset.
5.  Make sure your user account has permissions to write to the Word Startup folder. Open Finder and select Go -> "Go to Folder…" from the menu bar. Paste `~/Library/Group Containers/UBF8T346G9.Office/User Content.localized/Startup.localized/Word/` into the dialog and press Return. In the menu bar, select File → Get Info. At the bottom of the dialog, expand the "Sharing & Permissions" section and make sure that your user has the "Read & Write" privilege on the folder.
6.  If you are working on a Mac provided by your institution, contact your IT department.
7.  [Install the plugin manually](word_processor_plugin_manual_installation#word_for_mac).

If the plugin doesn't appear in Word after a manual installation, see [Zotero toolbar doesn't appear](word_processor_plugin_troubleshooting#zotero_toolbar_doesn_t_appear).

Note that you'll need to repeat a manual installation every time the plugin is updated, so it's much better to fix automatic installation. To troubleshoot the automatic installation, please create a new thread in the [Zotero Forums](/forum) so we can try to help. Be sure to include a [Report ID](reporting_problems#provide_a_report_id) from Zotero, your operating system and Word versions (in Word, go to the Word menu → About Microsoft Word to find the full version number), and the steps you've taken to try to fix the problem.

## LibreOffice

Zotero will automatically try to install the LibreOffice plugin and keep it up to date. You can force automatic installation at any time by going to the Zotero settings → Cite → Word Processors and pressing "(Re)install LibreOffice Add-in". If the automatic installation procedure fails, follow the steps below.

**Try to install the plugin via the Zotero settings after each step.**

1.  Check that LibreOffice is up to date.
2.  Open the LibreOffice preferences by going to Tools → Options (Windows/Linux) or LibreOffice → Settings… (Mac). In the dialog, click LibreOffice → Advanced. Ensure that "Use a Java runtime environment" is checked and that a JRE is selected in the list below.
    -   If no JRE appears in the list, install the current [Java JDK](https://www.oracle.com/java/technologies/downloads/). (On macOS and Windows, choose the "Installer" for the easiest installation. On an Apple Silicon Mac, choose the ARM64 installer, and make sure you're running the Apple Silicon version of LibreOffice.)
3.  If you believe your Java configuration is correct and you're still getting an error for a manual installation attempt, you can try deleting some or all of your [LibreOffice profile folder](https://wiki.documentfoundation.org/UserProfile#Default_locations).
4.  If you are working on a computer provided by your institution, contact your IT department.
5.  [Install the plugin manually](word_processor_plugin_manual_installation#libreoffice).

If the plugin doesn't appear in Word after a manual installation, see [Zotero toolbar doesn't appear](word_processor_plugin_troubleshooting#zotero_toolbar_doesn_t_appear).

Note that you'll need to repeat a manual installation every time the plugin is updated, so it's much better to fix automatic installation. To troubleshoot the automatic installation, please create a new thread in the [Zotero Forums](/forum) so we can try to help. Be sure to include a [Report ID](reporting_problems#provide_a_report_id) from Zotero, your operating system and LibreOffice version, and the steps you've taken to try to fix the problem.
