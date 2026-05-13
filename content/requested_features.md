# Frequently Requested Features

This page serves as an overview of the status of some commonly requested features for Zotero. **This list is unofficial and maintained by community members, not by Zotero's developers.** Do not make new feature requests here. Instead, post them to the [Zotero forum](/forum).

# Zotero Interface

#### Rich text formatting in the UI

Titles and abstracts in certain fields (e.g. biology) often contain text in superscript, subscript, italics, small-caps and bold-face. Zotero should allow in-field markup to be applied, and render marked up text with the proper formatting. This affects both the client and zotero.org.

**Status:** Supported by the Zotero team, no immediate plans to implement

**Discussion:** <http://forums.zotero.org/discussion/23785/parse-markup-tags-in-titles/> (refers to formatting on the website)
<http://forums.zotero.org/discussion/3875/rich-text-in-titles/?Focus=110229#Comment_110229> (refers to client UI)

#### Mark non-duplicates

Provide a way to indicate that two items are not duplicates of each other when Zotero thinks they are.

**Status:** Planned for a future release

**Discussion:** <http://forums.zotero.org/discussion/23682/marking-nonduplicates/>

#### Switch users

Provide a way to switch between multiple user accounts via logging on/off.

**Status:** No elegant way to accomplish this has been discussed. No plans to implement in the near future. This is partially possible using Firefox profiles.

**Discussion:** <http://forums.zotero.org/discussion/11093/using-zotero-in-a-public-library/>

#### Specify sync preferences per collection

Indicate whether attachments/items will be synced for individual collections

**Status:** Not possible with current sync architecture

**Discussion:** <http://forums.zotero.org/discussion/23977/request-choose-attachment-sync-per-collection-andor-allow-multiple-personal-libraries/>

#### Custom Fields/Item Types

Create custom item types and custom metadata fields

**Status:** No immediate plans to implement. Possible future feature.

**Comments:** Zotero item types represent different ways that items are cited in bibliographies. Adding custom item types and fields makes it nearly impossible to support them in automatic bibliography generation, which is one of the major purposes of Zotero. Other issues include synchronization with the Zotero server and data exchange with other users.

**Discussion:** <http://forums.zotero.org/discussion/15636/1/changes-to-fields-and-item-types-for-zotero-31-/>

#### Batch Editing

Editing of metadata fields and tags for multiple items at once

**Ticket:** <https://www.zotero.org/trac/ticket/364>

**Discussion:**

**Status:** Tentatively scheduled for version 5.2

#### Re-fetch metadata for an item

Provide a way to update/re-retrieve metadata for an item already in the library.

**Status:** Planned in conjunction with improved retrieve metadata feature. No specific timeline, faster implementation depends on community help.

**Discussion:** <http://forums.zotero.org/discussion/23748/automating-massimport-from-pdfs/>

#### Hierarchical Item Types (e.g. Edited Volumes and Chapters)

Allow for items to have a hierarchical relationship, e.g. have chapters as sub-items of an edited volume.

**Status:** Planned in the medium to long run, but implementation poses significant challenge & requires change in data layer.

**Ticket:** <https://www.zotero.org/trac/ticket/210>

#### Spinner for advanced search

Provide an indicator showing whether an advanced search is in process or completed.

**Status:** Open ticket exists, but no plans announced.

**Discussion:** <https://forums.zotero.org/discussion/72280/impossible-to-tell-whether-advanced-search-is-over-or-still-ongoing/>

**Ticket:** <https://github.com/zotero/zotero/issues/1370#issue-274845271>

# Group Libraries

#### See who added an item

Provide a field that indicates which user within a group added an item to the group library.

**Status:** Planned for a future release

**Ticket:** <https://www.zotero.org/trac/ticket/1639>

**Discussion:** <http://forums.zotero.org/discussion/23718/improving-group-libraries-see-who-added-what-and-whether-items-exists-in-my-local-library/>

#### Check if group item exists in local library

Provide a way to check if an item in the group library is present in the local/personal library.

**Status:** Planned for a future release

**Ticket:**

**Discussion:** <http://forums.zotero.org/discussion/23718/improving-group-libraries-see-who-added-what-and-whether-items-exists-in-my-local-library/>

#### Merge identical items inserted from different libraries

With multiple uers working on a single document, multiple citations referring to the same item can be inserted from different *personal* libraries. There should be a way to merge these citations into one.

**Status:** Planned for a future release

**Discussion:** http://forums.zotero.org/discussion/23719/word-plugin-and-groups-make-it-still-more-difficult-to-cite-from-the-wrong-libraries/  
<http://forums.zotero.org/discussion/23292/replacing-citations-with-a-copy-from-different-library/>

#### Finer control of user permissions

Create more user roles in group libraries that would allow finer control over who can add, edit, delete items/attachments.

**Status:** ?????????

**Discussion:** <http://forums.zotero.org/discussion/22731/roles-for-group-libraries-a-proposal/>

# Import/Export

#### Retrieve metadata from PDF based on file name

Use file name to improve retrieval of metadata for a PDF document.

**Status:** Planned as part of general improvements of retrieve metadata. Details still unclear. Help appreciated.

**Ticket:** <https://github.com/zotero/zotero/issues/99>

**Discussion:** <http://forums.zotero.org/discussion/23748/automating-massimport-from-pdfs/> , <http://forums.zotero.org/discussion/22882/> ,
