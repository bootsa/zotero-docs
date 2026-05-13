# Why isn’t Zotero detecting my existing Google Docs citations?

Google Docs integration uses a different mechanism for storing citations than is used in the Word and LibreOffice plugins, and it can be easier for citations to accidentally become unlinked. The most common reason for unlinking is collaborators editing the document without having the Zotero Connector installed. To ensure Zotero citations stay linked, everyone editing the Google Doc should install the [Zotero Connector](/download/) in their browser. (The Zotero app itself is only required for inserting and editing citations.) Citations [can also become unlinked](google_docs#limitations) if you drag them with the mouse within the Google Doc rather than cutting and pasting them.

To restore unlinked citations, you have two options:

1.  Use the Google Docs version history and restore to an earlier version of the document before the citation was unlinked. The version history can be found under Google Docs → File → Version History → "See version history". Note that the warning about unlinked citations will show up on the next operation *after* the operation that caused the problem, so restoring to a previous version that doesn't immediately show citations as unlinked isn't sufficient — you need to press Refresh in the Zotero menu and confirm that the warning doesn't reappear. If it does, revert to an earlier version.
2.  Use the Zotero plugin to reinsert the missing unlinked citations.

If all your collaborators have the Zotero Connector installed but you still see citations becoming unlinked, try to identify the actions that lead to the links breaking via the Google Docs version history and post details to the [Zotero Forums](/forum). Again, be sure to press Refresh after restoring to confirm that the citations aren't already unlinked in that version.

For information regarding other word processor plugins, see [Existing Citations Not Detected](kb/existing_citations_not_detected).
