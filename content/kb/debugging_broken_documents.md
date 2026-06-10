# Troubleshooting Errors in Word Processor Documents

Follow the steps below for [Microsoft Word](#microsoft_word), [Google Docs](#google_docs), or [LibreOffice](#libreoffice).

## Microsoft Word

<p style="color: red"><strong>June 10, 2026: The June 9 Windows security updates from Microsoft <a href="https://forums.zotero.org/discussion/comment/513866/#Comment_513866" style="color: red; text-decoration-color: red">broke Word integration on Windows</a>. We've fixed the issue in Zotero 9.0.5, available from the <a href="https://www.zotero.org/download/" style="color: red; text-decoration-color: red">download page</a>. You can install 9.0.5 over your existing version. Your Zotero data will not be affected. An in-app update will be available shortly.</strong></p>

If you get an error trying to use Zotero in a **new, empty document**, see [Word Processor Plugin Troubleshooting](word_processor_plugin_troubleshooting).

If you can insert citations into a new, empty Word document but get an error using Zotero in an **existing document**, follow these steps:

1.  Restart both Zotero and Word.
2.  Make sure you're using the latest versions of Zotero and Word.
3.  While troubleshooting, disable the Track Changes feature in Word, as it can have complicated effects when working with Zotero. If Track Changes is enabled when you insert or modify a Zotero citation, it may mark many or all of the Zotero citations in your document as changed or cause [field codes to be displayed](kb/word_field_codes). On rare occasions, Track Changes may cause Zotero to think a citation is corrupted. If you had Track Changes enabled previously, try accepting all changes to see if that resolves the issue.
4.  If using Windows, in Word Options → Advanced, make sure "Typing replaces selected text" is checked.
5.  If you use any clipboard enhancing software on macOS such as TextExpander, LaunchBar, Pure Paste, etc., temporarily disable it.
6.  Check for citations in image captions. Zotero won't let you insert them, but if you copied a citation to a caption, that's most likely the source of the problem. Delete it.
7.  Try copying and pasting the document content into a new document to see if the problem goes away. You may need to click the "Set Document Preferences" button before your old citations will be recognized.
8.  Make a copy of your document — by duplicating the file itself, not by copying and pasting the content — to use for debugging.
9.  If using OneDrive on Windows, save the copy of the document to your local hard drive, or try renaming the file to remove any spaces in the filename. OneDrive is known to interfere with the plugin for some people.
10. Open the copied file and check if you get the error after switching to a different bibliography style.
11. If the document has a bibliography, delete it completely and check if you still get the error.
12. While debugging, if you are using Fields mode in the Word plugin, it may help to display field codes rather than formatted text. To do this, press Alt/Option-F9 (or Alt/Option-Fn-F9) in Word.
13. **Isolate the problematic citations.** In the copy of your document, delete half of the contents at a time and see if the error still occurs. If not, use Undo to restore the deleted section and then try deleting the other half. Repeat the halving process on the section that fails, or pick one at random if both do. Continue this until you find the smallest possible section, ideally with a single citation, that must be present for the problem to occur. Remove the isolated citations from the original document and the problem should go away (unless there are multiple broken citations, in which case you'll need to repeat the process). Unless the error still occurs if you completely clear the contents of the document, **this final step will by definition identify the problem.**

If you encounter a broken document, please create a new thread in the [Zotero Forums](/forum) so we can attempt to fix the issue. Include a [Report ID](reporting_problems#provide_a_report_id) from Zotero, your operating system and Word versions, and the steps you've taken to try to fix the error. You should also send the document excerpt from the final step and a link to your forum thread to [support@zotero.org](mailto:support@zotero.org) so that we can try to reproduce the problem.

## Google Docs

If you get an error trying to use Zotero in a **new, empty document**, see [Google Docs Troubleshooting](google_docs#troubleshooting).

If you can insert citations into a new, empty Google Doc but get an error using Zotero in an **existing document**, follow these steps:

1.  Restart both Zotero and your browser.
2.  Make sure you're using the latest versions of Zotero and the Zotero Connector.
3.  Disable any other browser extensions and reload Google Docs.
4.  Try using File → "Make a copy" to see if the problem goes away in a new document. You may need to click the "Set Document Preferences" button before your old citations will be recognized.
5.  In the copy of the document, check if you get the error after switching to a different bibliography style.
6.  If the document has a bibliography, delete it and check if you still get the error.
7.  **Isolate the problematic citations.** In the copy of your document, delete half of the contents at a time and see if the error still occurs. If not, use Undo to restore the deleted section and then try deleting the other half. Repeat the halving process on the section that fails, or pick one at random if both do. Continue this until you find the smallest possible section, ideally with a single citation, that must be present for the problem to occur. Remove the isolated citations from the original document and the problem should go away (unless there are multiple broken citations, in which case you'll need to repeat the process). Unless the error still occurs if you completely clear the contents of the document, **this final step will by definition identify the problem.**

If you encounter a broken document, please create a new thread in the [Zotero Forums](/forum) so we can attempt to fix the issue. Include a [Debug ID](debug_output) from the Zotero for reproducing the problem and the steps you've taken to try to fix the error. You should also make a sharing link for the document excerpt from the final step and email it to [support@zotero.org](mailto:support@zotero.org) with a link to your forum thread so that we can try to reproduce the problem.

## LibreOffice

If you get an error trying to use Zotero in a **new, empty document**, see [Word Processor Plugin Troubleshooting](word_processor_plugin_troubleshooting).

If you can insert citations into a new, empty LibreOffice document but get an error using Zotero in an **existing document**, follow these steps:

1.  Restart both Zotero and LibreOffice.
2.  Make sure you're using the latest versions of Zotero and LibreOffice.
3.  While troubleshooting, disable the Track Changes feature in LibreOffice, as it can have complicated effects when working with Zotero. If Track Changes is enabled when you insert or modify a Zotero citation, it may mark many or all of the Zotero citations in your document as changed or cause [field codes to be displayed](kb/word_field_codes). On rare occasions, Track Changes may cause Zotero to think a citation is corrupted. If you had Track Changes enabled previously, try accepting all changes to see if that resolves the issue.
4.  Check for citations in image captions. Zotero won't let you insert them, but if you copied a citation to a caption that's most likely the source of the problem. Delete it.
5.  Make sure your LibreOffice text style uses the same text style in the "Next Style" property.
6.  Try copying and pasting the document content into a new document to see if the problem goes away. You may need to click the "Set Document Preferences" button before your old citations will be recognized.
7.  Make a copy of your document — by duplicating the file itself, not by copying and pasting the content — to use for debugging.
8.  Open the copied file and check if you get the error after switching to a different bibliography style.
9.  If the document has a bibliography, delete it and check if you still get the error.
10. While debugging, if you are using Reference Marks mode in the LibreOffice plugin, it may help to display field codes rather than formatted text by pressing Ctrl-F9.
11. **Isolate the problematic citations.** In the copy of the document, delete half of the contents at a time and see if the error still occurs. If not, use Undo to restore the deleted section and then try deleting the other half. Repeat the halving process on the section that fails, or pick one at random if both do. Continue this until you find the smallest possible section, ideally with a single citation, that must be present for the problem to occur. Remove the isolated citations from the original document and the problem should go away (unless there are multiple broken citations, in which case you'll need to repeat the process). Unless the error still occurs if you completely clear the contents of the document, **this final step will by definition identify the problem.**

If you encounter a broken document, please create a new thread in the [Zotero Forums](/forum) so we can attempt to fix the issue. Include a [Report ID](reporting_problems#provide_a_report_id) from Zotero, your operating system and LibreOffice versions, and the steps you've taken to try to fix the error. You should also send the document excerpt from the final step and a link to your forum thread to [support@zotero.org](mailto:support@zotero.org) so that we can try to reproduce the problem.
