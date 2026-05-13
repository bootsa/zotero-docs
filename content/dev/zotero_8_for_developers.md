# Zotero 8 for Developers

Zotero 8 includes an internal upgrade of the Mozilla platform on which Zotero is based, incorporating changes from Firefox 115 through Firefox 140.

Most of the guidance from [Zotero 7 for Developers](dev/zotero_7_for_developers) is still relevant.

## Feedback

If you have questions about anything on this page or encounter other problems while updating your plugin, let us know on the [dev list](https://groups.google.com/g/zotero-dev). Please don't post to the Zotero Forums about Zotero 8 at this time.

## Dev Builds

<!-- <span style="color: red; font-weight: bold">WARNING:</span>--><!--  These are test builds based on Firefox 140 intended solely for use by Zotero plugin developers and **should not be used in production**. We strongly recommend using a [[https://www.zotero.org/support/kb/multiple_profiles|separate profile and data directory]] for development. -->

The `dev` channel has been paused. Use [Zotero 8 beta builds](beta_builds) for development.

<!-- These `dev` channel builds will stop updating once a beta is available with these changes.

  * [[https://www.zotero.org/download/client/dl?channel=dev&platform=mac|Mac]]
  * [[https://www.zotero.org/download/client/dl?channel=dev&platform=linux-x86_64|Linux x86_64]]
  * [[https://www.zotero.org/download/client/dl?channel=dev&platform=linux-arm64|Linux ARM64]]
  * [[https://www.zotero.org/download/client/dl?channel=dev&platform=linux-i686|Linux i686]]
  * [[https://www.zotero.org/download/client/dl?channel=dev&platform=win-x64-zip|Windows 64-bit ZIP]]
  * [[https://www.zotero.org/download/client/dl?channel=dev&platform=win-x64|Windows 64-bit Installer]]
  * [[https://www.zotero.org/download/client/dl?channel=dev&platform=win-arm64-zip|Windows ARM64 ZIP]]
  * [[https://www.zotero.org/download/client/dl?channel=dev&platform=win-arm64|Windows ARM64 Installer]]
  * [[https://www.zotero.org/download/client/dl?channel=dev&platform=win32-zip|Windows 32-bit ZIP]]
  * [[https://www.zotero.org/download/client/dl?channel=dev&platform=win32|Windows 32-bit Installer]]

 -->

## Platform Changes

### Mozilla Platform

The following list includes nearly all Mozilla changes that affected Zotero code. You may encounter other breaking changes if you use APIs not used in Zotero. [Searchfox](https://searchfox.org/) is the best resource for identifying current correct usage in Mozilla code and changes between Firefox 115 and Firefox 140.

Earlier Zotero 8.0 (formerly 7.1) beta releases were based on Firefox 128, so we've listed changes for Firefox 128 and 140 separately.

#### Firefox 115 → Firefox 128 ("Zotero 7.1" beta)

-   Manual `Services.jsm` imports must be removed ([example](https://github.com/zotero/zotero/commit/97329752a1839210d636b7b8d37deae854d42410))
-   `nsIScriptableUnicodeConverter` was removed; replace `convertToByteArray()` and `convertToInputStream()` ([example](https://github.com/zotero/zotero/commit/24bf583b787d21117000336e4f67ddc9ac7b1deb))
-   `nsIOSFileConstantsService` was removed ([example](https://github.com/zotero/zotero/commit/7f619e3fe3044ea968a9bd0fb31d98f45d5cb75b))
-   `XPCOMUtils.defineLazyGetter` → `ChromeUtils.defineLazyGetter` ([example](https://github.com/zotero/zotero/commit/9606fca3ad39a52d29d0c74ae96fb680c14ad4e3))
-   `nsIDOMChromeWindow` was removed ([example](https://github.com/zotero/zotero/commit/45e681431bfd6b77bfaf8f55ce87f04fedb4a475))
-   Login manager: `addLogin` → `addLoginAsync` ([example](https://github.com/zotero/zotero/commit/fa2073335342f5f8f067b0e2cad12611012bcab5))
-   `BrowsingContext` should be passed to `nsIFilePicker` init ([example](https://github.com/zotero/zotero/commit/72b56e7a592a6793817e2a7479b08b6f2e334252), but we recommend using Zotero's `FilePicker` module instead)
-   `DataTransfer#types`: `contains()` → `includes()` — now a standard array ([example](https://github.com/zotero/zotero/commit/f28fa763ccfc5aac4575c1a2b28f532d84c89bf2))
-   `-moz-nativehyperlinktext` → `LinkText` ([example](https://github.com/zotero/zotero/commit/b85864595754fe54ae841902df2e4f3276a7574f))

#### Firefox 128 → Firefox 140 (Zotero 8)

-   All JSMs (`.jsm` files) in Firefox and Zotero were converted to ESMs (`.mjs` files, or `.sys.mjs` files for Firefox code) ([example](https://github.com/zotero/zotero/commit/6f96fa9da8368080001143898f6c3ece60939359))
    -   Zotero now uses [standard JavaScript modules](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Modules) and `import` statements ([example](https://github.com/zotero/zotero/commit/09fc93f9772a267f581198d5ce6a768744ed9d9c))
    -   See Mozilla's [primer on ESMification](https://groups.google.com/a/mozilla.org/g/firefox-dev/c/od7Bd1QpCuU) — in particular, the "Renamed New API" section
    -   **Zotero includes a script that can update most JSM-based code automatically.** Copy the `migrate-fx140` directory into your plugin's Git repo and run `migrate-fx140/migrate.py esmify path/to/Module.jsm`. To update the imports in a non-JSM file, run `migrate-fx140/migrate.py esmify --imports path/to/file.js`. Both commands also accept a directory for batch conversion.
    -   Global imports are no longer supported. Imported modules need to be assigned to a variable. ([example](https://github.com/zotero/zotero/commit/5e64365ce1ad07bd8f9308c76c4c39658883d0a7))
    -   All ESMs run in [strict mode](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Strict_mode)
-   Bluebird was removed — Zotero now uses standard JavaScript promises everywhere ([example](https://github.com/zotero/zotero/commit/b090f5d4eb10108052f95b6afb7599301a81f125))
    -   **Zotero provides a script that can update most Bluebird-based code automatically.** Copy the `migrate-fx140` directory into your plugin's Git repo and run `migrate-fx140/migrate.py asyncify path/to/file.js`. This command also accepts a directory for batch conversion.
    -   For compatibility, `Zotero.Promise.delay()` and `Zotero.Promise.defer()` are still supported. `defer()` can no longer be called as a constructor ([example](https://github.com/zotero/zotero/commit/8d6a853a3fe11d4ad560dde8aa270f8aecee35ba)).
    -   Bluebird Promise instance methods like `map()`, `filter()`, `each()`, `isResolved()`, `isPending()`, and `cancel()` are no longer available. Collection methods can usually be replaced with iteration ([example](https://github.com/zotero/zotero/commit/692312b419dfb7f0aaa8759230a9aafe62bbdc60), [example](https://github.com/zotero/zotero/commit/d734d78812c841f7adffdbb35b20b80606b67331)) or awaits ([example](https://github.com/zotero/zotero/commit/cf18fe69a9ffef4945841d62d4031c9137f2c5f2)). Complicated `isPending()` logic will need to be rewritten ([example](https://github.com/zotero/zotero/commit/8ffdb8bca2585408334c7dad7b1dce366fd6cd1a)).
    -   `ZoteroProtocolHandler` extensions: `new AsyncChannel()` now takes an async function, not a generator ([example](https://github.com/zotero/zotero/commit/ccc5dba03220b20722e94a1936a709ffc7a6c025))
    -   `Zotero.spawn()` was removed.
-   `Services.appShell.hiddenDOMWindow` was removed outside macOS — use only as a fallback ([example](https://github.com/zotero/zotero/commit/cd813171e7d29b164d3760698274790e888c8fbb))
-   `ZOTERO_CONFIG` needs to be imported ([example](https://github.com/zotero/zotero/commit/5e64365ce1ad07bd8f9308c76c4c39658883d0a7))
-   Preference panes now run in their own global scope, so a `var` defined in one preference pane's script won't automatically be accessible to other preference panes. Set variables on `window` explicitly if you need to share them between preference panes.
-   Update button labels using the `label` property, not attribute ([example](https://github.com/zotero/zotero/commit/b828cd5281e8a3ef5c86349b13d0796d8b08caf0))
-   The first segment of a zotero: URI is now parsed as its host, not as part of its path ([example](https://github.com/zotero/zotero/commit/9cad92b817e56beb108a57b00929ce756dda4125))

## Plugin Changes

### Custom Menu Items

A new API allows plugins to create custom menu items in Zotero's menu popups. Plugins should use this official API if possible rather than manually injecting content.

The example below shows registering a custom menu item and a submenu in Zotero's items list context menu.

``` javascript
let registeredID = Zotero.MenuManager.registerMenu({
    menuID: "test",
    pluginID: "example@example.com",
    target: "main/library/item",
    menus: [
        {
            menuType: "menuitem",
            l10nID: "menu-print",
            onShowing: (event, context) => {
                Zotero.debug("onShowing");
                Zotero.debug(Object.keys(context));
            },
            onCommand: (event, context) => {
                Zotero.debug("onCommand");
                Zotero.debug(Object.keys(context));
            },
        },
        {
            menuType: "submenu",
            l10nID: "menu-print",
            menus: [
                {
                    menuType: "menuitem",
                    l10nID: "menu-print",
                    onShowing: (event, context) => {
                        Zotero.debug("onShowing submenu");
                        Zotero.debug(Object.keys(context));
                        // Only for regular items
                        context.setVisible(context.items?.every((item) => item.isRegularItem()));
                    },
                    onCommand: (event, context) => {
                        Zotero.debug("onCommand submenu");
                        Zotero.debug(Object.keys(context));
                    },
                },
            ],
        },
    ],
});
```

Available targets:

-   **Main window menubar menus**
    -   main/menubar/file — File menu in the main window menubar
    -   main/menubar/edit — Edit menu in the main window menubar
    -   main/menubar/view — View menu in the main window menubar
    -   main/menubar/go — Go menu in the main window menubar
    -   main/menubar/tools — Tools menu in the main window menubar
    -   main/menubar/help — Help menu in the main window menubar
-   **Main window library context menus**
    -   main/library/item — Context menu for library items
    -   main/library/collection — Context menu for library collections
-   **Main window toolbar & file menu submenus**
    -   main/library/addAttachment — “Add attachment” button/menu
    -   main/library/addNote — “New note” button/menu
-   **Main window tab context menus**
    -   main/tab — Context menu for main window tabs
-   **Reader window menubar menus**
    -   reader/menubar/file — File menu in reader window
    -   reader/menubar/edit — Edit menu in reader window
    -   reader/menubar/view — View menu in reader window
    -   reader/menubar/go — Go menu in reader window
    -   reader/menubar/window — Window menu in reader window
-   **Item pane context menus**
    -   itemPane/info/row — Context menu for item pane info rows
-   **Notes pane add note buttons**
    -   notesPane/addItemNote — Add item note button
    -   notesPane/addStandaloneNote — Add standalone note button
-   **Sidenav buttons**
    -   sidenav/locate — Locate button in side navigation

More advanced options are documented in the [source code](https://github.com/zotero/zotero/blob/main/chrome/content/zotero/xpcom/pluginAPI/menuManager.js).

Note that the ftl string should set the attribute `label`:

``` fluent
menu-key =
    .label = Custom Menu Item
```

When the plugin is disabled or uninstalled, custom menus with the corresponding `pluginID` will be automatically removed. If you want to unregister a custom menu manually, you can use `unregisterMenu()`:

``` javascript
Zotero.MenuManager.unregisterMenu(registeredID);
```

If you encounter any problem with this API, please let us know on the [dev list](https://groups.google.com/g/zotero-dev).
