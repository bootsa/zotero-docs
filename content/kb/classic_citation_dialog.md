---
tags:
  - kb
  - word_processors
---

# What happened to the "classic" citation dialog?

The "classic" citation dialog was the original citation dialog in Zotero, introduced in 2006. It was replaced as the default dialog in 2011 by the "red bar" citation dialog, which allowed for faster searching and citing via the keyboard. The "classic" dialog remained an option for people who preferred to choose citations by browsing their collections rather than searching.

In 2026, Zotero 8 introduced a new unified citation dialog, replacing the "red bar" dialog, the "classic" dialog, and the Add Note dialog (the "yellow bar"). The new dialog includes a Library mode that directly replaces the classic dialog, bringing all the efficiency-enhancing features of the previous default dialog to people who want to browse by collection.

We know that switching to a new interface after many years can be a little jarring, but we believe that most people who give the new dialog a chance and spend a few days with it will quickly find that it's worth the change.

## Frequently Asked Questions

### Can I switch back to the classic dialog?

No. The classic dialog has been removed and won't be returning. Many features have been added to Zotero's word processor integration over the years, and the classic dialog wasn't able to take advantage of any of them. Maintaining a separate, parallel dialog also diverts development time from improvements to the parts of Zotero that everyone uses. The new dialog was designed to combine the library browser that classic-dialog users want with all the modern features.

If you're having trouble adjusting to the new dialog, let us know in the [Zotero Forums](https://forums.zotero.org). We're actively improving both the documentation and the dialog itself in response to feedback.

### How do I browse my collections like before?

Select "Library" mode in the bottom right of the window. Library mode shows the same collections and items lists you had in the classic dialog.

List mode, by comparison, works similarly to the previous ("red-bar") default dialog. It's the fastest mode when you generally know exactly what you're searching for and don't need to limit your search to a given collection.

By default, Zotero will open in the last mode you used. If you prefer to always open in one or the other, set Citation Dialog Mode in the Cite tab of the settings.

### How do I add a page number to a citation?

After choosing an item, you can type a page number directly into the main input field, rather than clicking around the window:

![](https://www.zotero.org/static/images/support/kb/citation-dialog-page-number-pre.png){ width=229 } ![](https://www.zotero.org/static/images/support/kb/citation-dialog-page-number-post.png){ width=234 }

You can also add other locator types by typing the short or full name (e.g., "chap4" or "chapter 4").

### Why does it take more steps to do everything in the new dialog?

It doesn't! The new dialog requires fewer steps to perform most common actions, greatly improves keyboard usage, and provides new features to speed up citing.

Bear in mind that the classic dialog hasn't been the default citation dialog in Zotero for 15 years. Citing hasn't been slower for all the people using the default dialog that entire time — it's been faster.

See [Comparing Common Actions](#comparing_common_actions) for a detailed comparison between the classic and new dialogs.

### How do I cite multiple items at once?

Use Ctrl/Cmd or Shift to select multiple items in the items list, and then press Enter/Return to add all of them to your citation.

### How do I reorder items?

Instead of clicking up/down arrows to move items into the right order, you can simply drag them to where you want them. To move with the keyboard, use left/right-arrow to select an item and Shift-left/right to move it.

### What are these random items appearing at the top of the dialog?

The new dialog lets you quickly add citations for selected items and open documents.

When you open the dialog, the selected item in your library, or the selected document tab in the reader, will be shown in a section at the top of the window. To select the first item, you can simply press Enter/Return on your keyboard or click it with your mouse. You can also choose among other open documents.

This means that, if you just want to insert a citation for the PDF you’re reading in Zotero, you can just click Add/Edit Citation and press Enter/Return twice to insert it into your document.

### What does "Cited Items" mean?

If you've already cited an item in your library, you can type its author or title, and it will show up in a Cited Items section at the top of the dialog. This also helps you avoid accidentally creating duplicate references for items that are duplicated in your library.

### What happened to the citation editor?

In the new dialog, there's no text field to make manual edits to citations. It's been possible to edit citations directly in the document since the introduction of the red-bar dialog in 2011, which is why the red bar never included such a text field.

More importantly, though, such manual edits should be avoided in almost all cases, since they prevent Zotero from updating the citation as you edit metadata, add other citations, or change citation styles. Instead, [customize the citation](word_processor_plugin_usage#customizing_citations) via the citation dialog, which will allow Zotero to continue to update the citation as necessary. If you're finding yourself regularly wanting to edit citations, post to the Zotero Forums with examples, and we may be able to suggest a better approach that avoids breaking citation updates.

## Comparing Common Actions

Below, we've detailed the steps necessary to perform some common actions in the classic and new dialogs.

### Adding a single item with a page number

`(Smith, 2026, p. 123)`

**Classic dialog:**

  1. Type "smith"
  2. Click item
  3. Click locator field
  4. Type "123"
  5. Press Enter/Return or click Done

**New dialog:**

  1. Type "smith"
  2. Click "+" next to item or double-click row
  3. Type "123"
  4. Press Enter/Return or click Accept (checkmark)

**Classic dialog, keyboard-only:**

  1. Type "smith"
  2. Tab twice to items list and ↓ to item
  3. Tab four (!) times to locator field
  4. Type "123"
  5. Press Enter/Return

**New dialog, keyboard-only:**

  1. Type "smith"
  2. ↓ to item + Enter/Return, or just Enter/Return if only result
  3. Type "123"
  4. Press Enter/Return

<p style="color: green"><strong>Winner:</strong> New dialog, for both speed and much easier keyboard use</p>

### Adding a single item with a unique search, with a chapter number 

`(Fitzgerald, 2004, ch. 3)`

**Classic dialog:**

  1. Type "gatsby"
  2. Click item
  3. Click the locator dropdown and select Chapter
  4. Click in the locator field
  5. Type "3"
  6. Press Enter/Return or click Done

**Classic dialog, keyboard-only:**

  1. Type "gatsby"
  2. Tab five (!) times to locator menu
  3. Navigate dropdown with keyboard and choose Chapter
  4. Tab once to locator field
  5. Type "3"
  6. Press Enter/Return

**New dialog:**

  1. Type "gatsby chap3"
  2. Press Enter/Return twice

<p style="color: green"><strong>Winner:</strong> New dialog</p>

### Adding a multi-item citation with page numbers and a prefix

`(Smith, 2024, p. 123; see also Jones, 2025, p. 234)`

**Classic dialog:**

  1. Type "smith"
  2. Click item
  3. Click in locator field
  4. Type "123"
  5. Click Multiple Sources…
  6. Double-click search box to select all text
  7. Type "jones"
  8. Click item
  9. Click right-arrow button
  10. Click in Prefix field
  11. Type "see also"
  12. Click in locator field
  13. Type "234"
  14. Click OK

**Classic dialog, keyboard only:**

_Not possible — right-arrow button isn't keyboard accessible_

**New dialog:**

  1. Type "smith"
  2. Click "+" next to item or double-click row
  3. Type "123"
  4. Type "jones"
  5. Click "+" next to item or double-click row
  6. Click citation bubble
  7. Type "234"
  8. Click in Prefix field or press Tab
  9. Type "see also"
  10. Press Enter/Return twice

**New dialog, keyboard only:**

  1. Type "smith"
  2. Press ↓ and Enter/Return, or press Enter/Return if only result
  3. Type "123"
  4. Type "jones"
  5. Press ↓ and Enter/Return, or press Enter/Return if only result
  6. Press ← + ↓ to open citation bubble
  7. Type "234"
  8. Tab once to Prefix field
  9. Type "see also"
  10. Press Enter/Return twice


<p style="color: green"><strong>Winner:</strong> New dialog, for both speed and keyboard accessibility</p>

### Adding a citation for the current PDF tab in Zotero

**Classic dialog:**

  1. Remember the details of the PDF you have open
  2. Type search term
  3. Click item
  4. Click Done

**New dialog:**

  1. Press Enter/Return twice

<p style="color: green"><strong>Winner:</strong> New dialog!</p>
