<p id="zotero-5-update-warning" style="color: red; font-weight: bold">We’re
in the process of updating the documentation for
<a href="https://www.zotero.org/blog/zotero-5-0">Zotero 5.0</a>. Some documentation
may be outdated in the meantime. Thanks for your understanding.</p>

## Overview

In Zotero >= 2.0, translators are just [javascript](dev/wpjavascript) files. While [Scaffold 2.0](http://bitbucket.org/rmzelle/scaffold/downloads) can [ease translator development](dev/how_to_write_a_zotero_translator_plusplus), some prefer to work directly on the filesystem. To do this, one should

1.  find or create a Zotero development environment
2.  find or create a translator development environment
3.  create or modify a translator file
4.  edit, run, test, debug
5.  contribute your translator

## Find or create a Zotero development environment

One develops a translator to run on/against a given version of Zotero, which runs on/against a given version of Firefox. The easiest way to do this is just to use the current version of Zotero that is running in your current [Firefox profile](http://support.mozilla.com/en-US/kb/profiles). One can identify the path to one's current Zotero directory using the Zotero UI: select the gear icon to dropdown its menu, and choose Preferences>Advanced>Show Data Directory.

While convenient, using one's current Zotero

-   runs the risk of corrupting one's current Zotero data, i.e. one's saved citations.
-   does not allow one to develop against another version of Firefox or Zotero.

To create a separate Zotero development environment,

1.  Use Firefox's [Profile Manager](http://kb.mozillazine.org/Profile_Manager) to [create a Firefox profile](http://support.mozilla.com/en-US/kb/managing+profiles). (Remember below to [start Firefox using that profile](http://kb.mozillazine.org/Starting_Firefox_or_Thunderbird_with_a_specified_profile).) (Note that, by default, only one Firefox profile can run at any given time.)
2.  install the desired version of Zotero into your Firefox profile. One can install either
    -   [the latest Zotero release](installation)
    -   [a development XPI](dev_builds)
    -   [from the Zotero code repository](dev/source_code#running_svngit_builds)

## Find or create a translator development environment

When developing directly against the filesystem, one's translator development environment is

-   one's collection of one or more translator files
-   the tools one uses to work on them

### Translator files

#### Translator file location

Zotero installs its translators and related code as files in the subdirectory `translators`. I.e.

-   if the path to your Firefox profile=`${FIREFOX_PROFILE}` then the path to your Zotero is `${FIREFOX_PROFILE}/zotero`
-   if the path to your Zotero=`${FIREFOX_PROFILE}/zotero` then the path to your translators, and hence to your translator development environment, is `${FIREFOX_PROFILE}/zotero/translators` (See above regarding using Zotero UI to identify the path to your current Zotero.)

TODO: how to get alternate/uplevel versions of translators?

#### Translator file structure

At the highest level, a Zotero translator (for versions >= 2.0) consists of

-   a single [metadata block](dev/translators_reference_guide#translator_metadata), usually at the beginning of the file. The most important of its fields is the `translatorID`, which is the global identifier for the translator.
-   non-metadata code, consisting of
    -   a `detectWeb` function. This must return a string corresponding to a defined Zotero type. For a list of Zotero type names, see the values of the `itemTypes.`\* properties in [this Zotero property list](https://www.zotero.org/trac/browser/extension/branches/2.0/chrome/locale/en-US/zotero/zotero.properties#L240) (or a newer one).
    -   a `doWeb` function. This actually writes an item corresponding to your web resource to your Zotero repository.

### Translator development tools

TODO:

-   Zotero-enabled tools
-   Zotero API guides
-   Javascript-enabled tools
-   XPath tools

## Create or modify a translator file

One can generate a completely new translator file using Scaffold 2.0.

1.  Start Scaffold.
2.  In tab=Metadata, take the generated `translatorID`, but give some values for the `label`, `creator`, and `target` fields. (Note your filename will be based on the value of the `label` field: e.g. if you set that to `foo`, your file will be named `foo.js`)
3.  In tab=Code, enter a `detectWeb` stub, e.g. `function detectWeb () {
    return "book";
    }
    `
4.  Click on icon=Save (second from upper left).
5.  Check your translator filespace: you should have a new file with name based on field=`label`.
6.  Close Scaffold. You may do all subsequent work directly on the new file.

However it is usually easier to create a new translator by copy/modify-ing an existing one. This can be done in one of several ways, including

1.  working directly on an existing translator file (e.g. to fix a bug or add an feature) without modifying the `translatorID`. Note that any Zotero update to the profile containing that file will overwrite your work.
2.  "clearing out" your copy/modified file. Open it in your editor, and
    1.  in the metadata block,
        -   create a new `translatorID` for your copy/modified file. Edit the old field randomly, or (better) generate a new value using Scaffold 2.0.
        -   make the value of the `label` field match your new filename.
    2.  in the code section, clear out any undesired contents from the `detectWeb` and `doWeb` functions.
3.  somewhat "between" the previous two:
    1.  Find an existing translator with functionality that resembles what you want.
    2.  Copy that to a new file in your translator filespace.
    3.  Open the new file and
        1.  change the metadata field=`label` to match your filename (minus the `.js` extension)
        2.  assign a new value to field=`translatorID`, preferably after generating a new value using Scaffold 2.0.
        3.  change the `detectWeb` and `doWeb` functions as needed.

## Edit, run, test, debug

### Enable debugging output

One must

-   configure Firefox to write Zotero debugging output to a [terminal emulator](dev/wpterminal_emulator) (e.g. `xterm`, `terminal`, `cmd`)
-   start Firefox via command-line from a terminal emulator (i.e. not via an icon)

before one can see output from, e.g., Zotero.debug() calls. See detailed instructions for [linux](http://www.zotero.org/support/debug_output#linux), [mac](http://www.zotero.org/support/debug_output#mac_os_x), and [windows](http://www.zotero.org/support/debug_output#windows_xp).

### Running a modified translator

Zotero does not currently sense changes to a translator file after it has been loaded. The actions required to reload a modified translator depend on what has been modified: metadata or other code.

#### Running a translator after modifying metadata

If you have made changes to the metadata block of your translator, you must restart the Firefox profile containing your modified translator.

#### Running a translator after modifying non-metadata code

If you have made changes to code outside the metadata block of your translator, you need only restart the page on which you want to run the translator.

## Contribute your translator

Once your translator works on a subset of the sites on which you believe it should work, please [contribute your translator](dev/translator_overview#step_5contribute_your_translator) to the community.
