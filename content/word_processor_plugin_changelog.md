**More recent changes to the Zotero Word Proccessor plugins are described in the [main Zotero changelog](5.0_changelog).**

# Zotero Word for Windows Integration

### Changes in 3.5.2 (September 25, 2015)

-   Eliminate dynamic toolbar functionality for Word 2007 and later introduced in 3.5.1. The Insert Citation button has been replaced with an Add/Edit Citation button.
-   Clicking Add/Edit Citation when immediately adjacent to a citation now edits that citation instead of creating a new one.

### Changes in 3.5.1 (September 20, 2015)

-   Add Zotero tab to ribbon and improve appearance in Word 2007 and later.
-   Word 2016 compatibility.
-   Remove XPCOM binary components.
-   Fix a bug that interfered with selection highlighting.
-   Signed by Mozilla.

### Changes in 3.5.0

Zotero Word for Windows Integration 3.5.0 was not publicly released.

### Changes in 3.1.20 (June 30, 2015)

-   Rewrite of Word for Windows plugin to use js-ctypes. This is enabled only for Firefox 40 and later, which no longer support XPCOM binary components. Previous versions of Firefox continue to use the old XPCOM-based plugin.
-   Localized installation preference pane.
-   Fixed an issue where error dialogs may not appear during installation.
-   Firefox 39 (and later) compatibility.

### Changes in 3.1.19 (March 6, 2015)

-   Fix Windows XP compatibility when running under Firefox 36 and 37.
-   Firefox 38 compatibility.

### Changes in 3.1.18 (January 14, 2015)

-   Firefox 35, 36, and 37 compatibility.

### Changes in 3.1.17 (September 2, 2014)

-   Firefox 32, 33, and 34 compatibility.

### Changes in 3.1.16 (April 29, 2014)

-   Fixed a bug editing the first footnote citation in a document when there are also in-text citations present.
-   Firefox 29, 30, and 31 compatibility.

### Changes in 3.1.15 (December 8, 2013)

-   Firefox 26, 27, and 28 compatibility.

### Changes in 3.1.14 (October 29, 2013)

-   Firefox 25 compatibility.

### Changes in 3.1.13 (June 23, 2013)

-   Firefox 22, 23, and 24 compatibility.

### Changes in 3.1.12 (March 23, 2013)

-   Firefox 20 and 21 compatibility.
-   Zotero 4.0 compatibility.

### Changes in 3.1.11 (February 19, 2013)

-   Fixed Firefox 19 compatibility.

### Changes in 3.1.10 (January 26, 2013)

-   Fixed "Could not find a running Word instance" or "This command is not available because no document is open" error when editing a document residing on a network share with multiple Word instances running.
-   Word 2013 compatibility.

### Changes in 3.1.9 (November 16, 2012)

-   Firefox 17 and 18 compatibility.

### Changes in 3.1.8 (July 21, 2012)

-   Firefox 15 and 16 compatibility.

### Changes in 3.1.7 (May 9, 2012)

-   Fixed restoration of "Final" view in Word 2010.
-   Use locale-specific bibliography style name in Word 2007+.
-   Move insertion point past footnote references upon insert.
-   Firefox 13 and 14 compatibility.

### Changes in 3.1.6 (March 17, 2012)

-   Fixed issues inserting bookmarks in Firefox 10+.
-   Firefox 12 compatibility.

### Changes in 3.1.5 (January 30, 2012)

-   Firefox 10 and 11 compatibility.

### Changes in 3.1.4 (November 10, 2011)

-   Fixed editing citations in footnotes with Word 2010.
-   Fixed compatibility with Word 2000.

### Changes in 3.1.3 (November 8, 2011)

-   Firefox 7, 8, and 9 compatibility.
-   Zotero 3.0b3 compatibility.
-   Compatibility with track changes.
-   Fixed an issue editing the first footnote in a document.

### Changes in 3.1.2 (August 14, 2011)

-   Firefox 6 compatibility.
-   Zotero 3.0b1 compatibility.

### Changes in 3.1.1 (June 20, 2011)

-   Firefox 5 compatibility.

### Changes in 3.1 (April 1, 2011)

-   Fixed crashes when running with Firefox 3.6 on some systems.

### Changes in 3.1b1 (January 14, 2011)

-   Added support for Zotero 2.1.

### Changes in 3.0b1 (October 29, 2010)

-   Fixed "Call was rejected by callee" error.
-   Fixed "That property is not available on that object" error.
-   Fixed "The command is not available because no document is open" error.

### Changes in 3.0a4 (June 14, 2010)

-   Added compatibility with both 64-bit and 32-bit versions of Word 2010.

### Changes in 3.0a3 (November 14, 2009)

-   Fixed communication error under certain conditions.
-   Properly restore font of surrounding text when inserting citations and bibliographies.

### Changes in 3.0a2 (September 23, 2009)

-   Added compatibility with Namoroka, Flock, and Minefield.
-   Improved error handling.
-   Fixed compatibility with very old versions of Windows.
-   Fixed installation when Word Startup folder has been moved.
-   Don't show conversion dialog when inserting citations and bibliography.

### Changes in 3.0a1 (September 15, 2009)

-   Initial release of third generation Word for Windows plugin.

# Zotero Word for Mac Integration

### Changes in 3.5.12 (August 31, 2015)

-   Signed by Mozilla.

### Changes in 3.5.11 (July 15, 2015)

-   Fix communication with Zotero under Word 2016 on some systems.

### Changes in 3.5.10 (July 14, 2015)

-   Fix compatibility with 32-bit Macs.

### Changes in 3.5.9 (July 13, 2015)

-   Stop a harmless error message from being logged to the error console when Word 2016 is not installed.

### Changes in 3.5.8 (July 13, 2015)

-   Word 2016 compatibility.
-   Localized installation preference pane.
-   Fixed an issue where error dialogs may not appear during installation.

### Changes in 3.5.7 (March 23, 2013)

-   Fixed an issue where citations could remain superscripted when switching from a superscript citation style to another citation style.
-   Fixed an installation error if the Word Startup folder is not readable by the current user.
-   Throw a more explicit error if Word is missing AppleScript support due to an unfortunate interaction between Migration Assistant and Office 2008.
-   Zotero 4.0 compatibility.

### Changes in 3.5.6 (November 16, 2012)

-   Improved error message when Visual Basic for Applications is not installed in Word 2011.
-   Fixed errors when the user switched documents while a citation was being inserted.
-   Fixed a small memory leak.
-   Now throws an error if the user deletes fields from the document while an update is in progress instead of shifting field codes.

### Changes in 3.5.5 (July 7, 2012)

-   Fixed several issues converting among in-text citations, footnotes, and endnotes.
-   Fixed several issues using bookmarks.
-   Fixed an issue inserting a second citation into a table cell.

### Changes in 3.5.4 (May 1, 2012)

-   Fixed a bug in the installation process that would cause Firefox to crash if Word was not installed.
-   Fixed a bug in the installation process that could cause Firefox to create a separate process that would hang while consuming system resources.
-   Fixed inserting an in-text citation into a note in Word 2004.
-   Fixed inserting rich text citations and bibliographies when using bookmarks.

### Changes in 3.5.3 (April 15, 2012)

-   Adjust installer for changes in the location of the Word Script Menu Items folder introduced in Office 2011 SP2.
-   Properly restore full screen mode after inserting a citation.
-   Improved error handling.

### Changes in 3.5.2 (March 19, 2012)

-   Fixed an issue editing citations in footnotes in Word 2008.
-   Fixed an issue adding a second citation to a footnote in Word 2008.
-   Fixed removing field codes.
-   Workaround for Word scripts not updated since Zotero Word for Mac Integration 3.0b3.

### Changes in 3.5.1 (March 16, 2012)

-   Fixed an issue inserting in-text citations into footnotes.
-   Fixed an issue inserting footnote citations in Word 2008.
-   Fixed an installation issue on systems with case-sensitive file systems.

### Changes in 3.5 (March 12, 2012)

-   Complete rewrite in Objective-C.
-   Firefox 11+ compatibility.

### Changes in 3.1.10 (January 30, 2012)

-   Firefox 10 compatibility.
-   Fixed an issue that could cause errors when using Track Changes.
-   Fixed an issue that could cause errors when switching citation styles.

### Changes in 3.1.9 (November 9, 2011)

-   Fixed editing citations, broken since 3.1.8.

### Changes in 3.1.8 (November 9, 2011)

-   Fixed "Unknown property, element or command: 'show_insertions_and_deletions'" error with Word 2004
-   Fixed an error converting between in-text styles and footnote styles

### Changes in 3.1.7 (November 8, 2011)

-   Firefox 9 compatibility.
-   Zotero 3.0b3 compatibility.
-   Compatibility with track changes.
-   Ask the user to authenticate if permissions for Word Startup folder are inadequate.

### Changes in 3.1.6 (August 14, 2011)

-   Firefox 6 compatibility.
-   Zotero 3.0b1 compatibility.

### Changes in 3.1.5 (July 21, 2011)

-   Fixed installation issue with Mac OS X 10.5, caused by the changes in 3.1.4 in conjunction with an operating system bug.

### Changes in 3.1.4 (July 20, 2011)

-   Firefox 6 compatibility.
-   Fixed installation issue with Mac OS X 10.7.

### Changes in 3.1.3 (June 20, 2011)

-   Firefox 5 compatibility.
-   Fixed a [rare error](http://forums.zotero.org/discussion/17539/command-appu-error-after-inserting-a-citation) in Word 2004.

### Changes in 3.1.2 (April 1, 2011)

-   Fixed crashes when running with Firefox 3.6.

### Changes in 3.1.1 (March 22, 2011)

-   Fixed compatibility with Mac OS X 10.4.
-   Update to appscript-1.0.0.

### Changes in 3.1 (March 18, 2011)

-   Show incompatibility warning when run with Firefox 4 under Mac OS X 10.5.
-   Automatically install in French, Spanish, Italian, and German versions of Word.
-   Fixed incorrect text coloring when text is not black.
-   Fixed component loading error on some systems when running Firefox 4.
-   Always use included appscript module.

### Changes in 3.1b2 (January 19, 2011)

-   Fixed crashes on Mac OS X 10.5.

### Changes in 3.1b1 (January 14, 2011)

-   Added support for Zotero 2.1.

### Changes in 3.0b7 (December 2, 2010)

-   Fixed a potential hang during Firefox startup when FlashGot is installed.

### Changes in 3.0b6 (December 1, 2010)

-   Fixed a bug that could cause the Zotero toolbar not to appear in Word 2004.

### Changes in 3.0b5 (October 30, 2010)

-   Fixed an error that could result in failed installation when 32-bit OSAX were installed on Snow Leopard.

### Changes in 3.0b4 (October 29, 2010)

-   Direct AppleScript calls to running Word instance.
-   Fixed installation errors.
-   Fixed an error when inserting text containing entities specified in the editor that cannot be expressed as MacRoman.

### Changes in 3.0b3 (June 26, 2010)

-   Fixed an issue that could cause error messages not to appear when they contain accented characters.
-   Work around an obscure AppleScript bug that could prevent Zotero Mac Word Integration from installing without a restart.

### Changes in 3.0b2 (March 28, 2010)

-   Permit manual installation.
-   Fixed rare installation issues.

### Changes in 3.0b1 (March 20, 2010)

-   Fixed an issue with short usernames containing spaces.

### Changes in 3.0a9 (March 11, 2010)

-   Use integration pipe in /Users/Shared on Mac OS X to fix issues with networked home directories.

### Changes in 3.0a8 (February 3, 2010)

-   Fixed an extension initialization that could produce a component loading error.

### Changes in 3.0a7 (November 14, 2009)

-   Fixed minor installation issues.
-   Fixed issues with Snow Leopard.

### Changes in 3.0a6 (November 6, 2009)

-   Fixed an issue with missing field codes.
-   Fixed an issue with non-English disk names.
-   Don't show conversion dialog when inserting citations and bibliography.

### Changes in 3.0a5 (September 21, 2009)

-   Upgrade bundled appscript to 0.20.
-   Fixed installation issues on non-English language systems
-   Fixed "Application could not handle this command" error.

### Changes in 3.0a4 (September 17, 2009)

-   Fixed a compatibility issue between Word for Windows and Mac Word plugins.

### Changes in 3.0a3 (September 17, 2009)

-   Offer to delete corrupted pythonext installations.
-   Fixed a communication error caused by a corrupted LaunchServices database.

### Changes in 3.0a2 (September 16, 2009)

-   Fixed component loading error.

### Changes in 3.0a1 (September 15, 2009)

-   Initial release of third generation MacWord plugin.

# Zotero LibreOffice Integration

### Changes in 3.5.10 (August 31, 2015)

-   Signed by Mozilla.

### Changes in 3.5.9 (March 11, 2014)

-   Fix message box display under LibreOffice 4.2+.

### Changes in 3.5.8 (August 17, 2013)

-   OpenOffice 4 compatibility.
-   Improved detection of LibreOffice/OpenOffice paths when multiple versions are installed.

### Changes in 3.5.7 (July 22, 2013)

3.5.7 was released for Zotero Standalone only

-   Improved detection of LibreOffice 4.1 paths.
-   Removed unnecessary files.

### Changes in 3.5.6 (March 23, 2013)

-   Zotero 4.0 compatibility.

### Changes in 3.5.5 (February 19, 2013)

-   Fixed superscripted styles in LibreOffice versions before 4.0 (broken since 3.5.4).
-   Fixed extraneous whitespace around footnote and superscripted citations under Windows (since 3.5.4).
-   Fixed handling of empty ReferenceMarks.

### Changes in 3.5.4 (February 7, 2013)

-   LibreOffice 4 compatibility.

### Changes in 3.5.3 (July 4, 2012)

-   Improved performance.
-   Fixed bustage if a Java error occurs.
-   Added common LibreOffice 3.6 paths.
-   Warn if "Unstable Features" is enabled in LibreOffice preferences.
-   Prompt to install Java on Windows if it is not installed.

### Changes in 3.5.2 (February 8, 2012)

-   Fixed compatibility with LibreOffice 3.5 (requires LibreOffice 3.5.0rc3 or later).

### Changes in 3.5.1 (February 2, 2012)

-   Fixed a bug that could cause heavy CPU utilization in Firefox.

### Changes in 3.5 (January 30, 2012)

-   Better handling of citations in text frames.

### Changes in 3.5b3 (December 22, 2011)

-   Fixed a bug that could cause Firefox to hang when adding or updating citations.

### Changes in 3.5b2 (November 8, 2011)

-   Firefox 9 compatibility.
-   Zotero 3.0b3 compatibility.

### Changes in 3.5b1 (August 14, 2011)

-   Firefox 6 compatibility.
-   Zotero 3.0b1 compatibility.
-   Improved installer's ability to find unopkg on Windows.
-   Fixed manual selection of unopkg location.

### Changes in 3.5a2 (June 20, 2011)

-   Firefox 5 compatibility.
-   Performance improvements.
-   Prompt to install libreoffice-java-common package and JRE on Ubuntu and similar systems.

### Changes in 3.5a1 (March 14, 2011)

-   Java component now loads in OpenOffice.org instead of in browser.
-   Fixed all known Java-related errors.
-   Improve installation process.

### Changes in 3.1b1 (January 14, 2011)

-   Added support for Zotero 2.1.

### Changes in 3.0b3 (February 10, 2011)

-   Added compatibility with OpenOffice.org/LibreOffice 3.3.

### Changes in 3.0b2 (October 29, 2010)

-   Fixed repeated install attempts.

### Changes in 3.0b1 (October 29, 2010)

-   Implement footnote indexing for numbered citations. Zotero references will no longer use "Ibid." when the preceding footnote is user-generated.
-   Added support for citations within tables.
-   Fixed a bug that could cause all text following a bibliography to be erased when the bibliography was updated.

### Changes in 3.0a8 (June 14, 2010)

-   Ignore unanchored citations. Unanchored citations appear to be duplicates of existing citations caused by an obscure bug in OpenOffice.org, and would previously produce a "NullPointerException" error.

### Changes in 3.0a7 (March 11, 2010)

-   Use integration pipe in /Users/Shared on Mac OS X to fix issues with networked home directories.

### Changes in 3.0a6 (January 23, 2010)

-   Update OpenOffice.org installation script to support Firefox 3.6.

### Changes in 3.0a5 (October 14, 2009)

-   Fixed "Invalid Field Code" error message when copy and pasting citations using Bookmarks.
-   Fixed compatibility with OpenOffice.org 2.4.

### Changes in 3.0a4 (September 30, 2009)

-   Fixed installation and re-installation errors.

### Changes in 3.0a3 (September 23, 2009)

-   Improve automatic recognition of OpenOffice.org paths.
-   Added compatibility with Namoroka, Flock, and Minefield.
-   Added compatibility with the IcedTea/OpenJDK OJI Java plugin on Linux.

### Changes in 3.0a2 (September 16, 2009)

-   Fixed errors when non-Zotero Bookmarks or ReferenceMarks were used within a document.

### Changes in 3.0a1 (September 15, 2009)

-   Initial release of third generation OpenOffice.org plugin.
