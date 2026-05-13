---
tags:
  - kb-obsolete
  - zotero_for_firefox
---

**This article applies to the deprecated Zotero for Firefox (pre-Zotero 5.0) plugin. It no longer applies to the current versions of Zotero.**

#### Why am I getting an "unresponsive script warning"?

While Zotero is performing long operations, Firefox may display the message:

*"A script on this page may be busy, or it may have stopped responding. You can stop the script now, or you can continue to see if the script will complete."*

…and include a URL beginning with chrome://zotero/. Note that for all other URLs, including http://www.zotero.org/ URLs, the following advice does not apply.

**Short answer:** Click Continue until the message stops appearing. Don't click Stop Script. This message has nothing to do with Chrome the browser.

**Long answer:** Zotero automatically disables this Firefox warning before beginning most long operations and re-enables it afterwards, but there may be places where the message still shows up, particularly on slower computers. If you receive the message repeatedly, report it in the Zotero Forums, and be sure to include the file and line number from the message in your post.

To prevent the message from appearing, type "<about:config>" into the Firefox address bar and press Enter. Search for dom.max_chrome_script_run_time in the list and double-click it. To disable the warning completely, enter 0 in the dialog box that pops up. You can also set a longer timeout (in seconds) after which you should receive the message if a Firefox extension is still busy or has frozen. For example, to display the message after two minutes, enter 120. Unless you get frequent freezes afterward, there's no downside to adjusting the timeout.

Note that, if you do receive the warning, pressing Stop Script in the middle of certain operations may disable Zotero until Firefox is restarted and/or may cause the message to reappear.


