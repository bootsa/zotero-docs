# Connecting to Zotero with the Firefox Developer Tools

Since Zotero is based on Firefox, it's possible to use the Firefox Developer Tools to interact with the DOM, set code breakpoints, follow network requests, and more.

Zotero 7 beta builds include the Firefox 115 devtools. To start a beta build with the Browser Toolbox open, pass the `-jsdebugger` flag on the command line:

    $ /Applications/Zotero\ Beta.app/Contents/MacOS/zotero -ZoteroDebugText -jsdebugger

When running Zotero from source, passing `-d` flag to the [build_and_run script](dev/client_coding/building_the_desktop_app#helper_script) will rebuild (`-r`) with the devtools included and pass `-jsdebugger`.
