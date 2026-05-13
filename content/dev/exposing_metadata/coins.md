---
tags:
  - kb
---

# Using Zotero to create COinS metadata

## Introduction

Although the [Google/Highwire key-value system](http://scholar.google.com/intl/en/scholar/inclusion.html) is generally preferred for embedding bibliographic metadata into a webpage, another possible format is COinS. Zotero can [automatically import COinS metadata from a website](https://www.zotero.org/support/adding_items_to_zotero#via_your_web_browser).

COinS is an abbreviation for "[ContextObjects in Spans](http://ocoins.info/)". Spans in this context refers to the html tag <span></span>. Spans allow you to add the bibliographic metadata to your webpage without it being visible to people browsing the page.

The format of COinS is relatively simple, but creating them by hand is difficult because certain characters need to be converted to URL format. For example, a space character needs to be represented by '%20'.

Example COinS code is shown below:

``` html
<span class='Z3988' title='url_ver=Z39.88-2004&amp;ctx_ver=Z39.88-2004&amp;rfr_id=info%3Asid%2Fzotero.org%3A2&amp;rft_val_fmt=info%3Aofi%2Ffmt%3Akev%3Amtx%3Ajournal&amp;rft.genre=article&amp;rft.atitle=Thelymitra%20epipactoides%20F.%20Muell.%20(Orchidaceae)%3A%20The%20morphology%2C%20biology%20and%20conservation%20of%20an%20endangered%20species&amp;rft.jtitle=Proceedings%20of%20the%20Royal%20Society%20of%20Victoria&amp;rft.volume=101&amp;rft.aufirst=S.%20C.&amp;rft.aulast=Cropper&amp;rft.au=S.%20C.%20Cropper&amp;rft.au=D.%20M.%20Calder&amp;rft.au=D.%20Tonkinson&amp;rft.date=1989&amp;rft.pages=89-101&amp;rft.spage=89&amp;rft.epage=101'></span>
<span class='Z3988' title='url_ver=Z39.88-2004&amp;ctx_ver=Z39.88-2004&amp;rfr_id=info%3Asid%2Fzotero.org%3A2&amp;rft_id=urn%3Aisbn%3A0%207306%202243%206&amp;rft_val_fmt=info%3Aofi%2Ffmt%3Akev%3Amtx%3Abook&amp;rft.genre=book&amp;rft.btitle=A%20census%20of%20Victorian%20bryophytes&amp;rft.place=East%20Melbourne&amp;rft.publisher=The%20Department%20of%20Conservation%20and%20Environment&amp;rft.aufirst=S.%20C.&amp;rft.aulast=Cropper&amp;rft.au=S.%20C.%20Cropper&amp;rft.au=D.%20A.%20Tonkinson&amp;rft.au=G.%20A.%20M.%20Scott&amp;rft.date=1991&amp;rft.tpages=56&amp;rft.isbn=0%207306%202243%206'></span>
<span class='Z3988' title='url_ver=Z39.88-2004&amp;ctx_ver=Z39.88-2004&amp;rfr_id=info%3Asid%2Fzotero.org%3A2&amp;rft_id=urn%3Aisbn%3A0%20643%2005533%209&amp;rft_val_fmt=info%3Aofi%2Ffmt%3Akev%3Amtx%3Abook&amp;rft.genre=book&amp;rft.btitle=Management%20of%20endangered%20plants&amp;rft.place=East%20Melbourne&amp;rft.publisher=CSIRO%20Publishing&amp;rft.aufirst=S.%20C.&amp;rft.aulast=Cropper&amp;rft.au=S.%20C.%20Cropper&amp;rft.date=1993&amp;rft.tpages=182&amp;rft.isbn=0%20643%2005533%209'></span>
```

Zotero can automatically create COinS from items in your library. Select the items in Zotero, right click, and choose "Export Items…". Then choose COinS from the dropdown menu. Open the exported file to see the COinS metadata. Copy and paste this code into your web page editor.

You can also set Zotero to use COinS as your default "Quick Copy" export format. Open the [Export](preferences/export) pane of Zotero preferences and select "COinS" as the Default Format. Then, you can drag and drop items from your library to your web page editor to insert COinS code. You can also copy COinS to your clipboad by pressing Ctrl/Cmd-Shift-C.


