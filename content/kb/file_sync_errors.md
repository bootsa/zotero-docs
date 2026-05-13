---
tags:
  - kb
  - sync
---

#### Why do I keep getting file sync errors while syncing?

When attempting to sync many files to or from the Zotero servers — for example, when syncing a library on a computer for the first time — it's not uncommon to get intermittent file sync errors. A file sync can involve thousands of network requests, and network glitches or server load can result in a small percentage of those failing. While Zotero retries many such failures automatically, Zotero may occasionally stop trying to sync a file and ask for user input.

For intermittent file sync errors, the solution is simply to press the Sync button again or, if you're using auto-sync, to simply use Zotero normally and let it auto-sync in the background. You can hover over the sync icon to view file sync progress and see how many files are syncing each time.

The one exception is if you're getting a file sync error at the very beginning of every sync attempt and don't see additional progress being made each time when you hover over the sync icon. In that case, security software or a proxy server on your network may be interfering with Zotero. If you're running security software, try temporarily disabling it. Check your system proxy settings to make sure they're either disabled (if you're not using a proxy) or correct (if you are). Then restart Zotero and try again.

If you're getting immediate file sync errors and haven't been able to fix them using the above steps, generate a [Debug ID](debug_output#debug_output_logging) for a sync attempt that produces the error and post it to the [Zotero forums](/forum).


