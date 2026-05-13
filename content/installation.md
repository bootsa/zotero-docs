## Installation Instructions

### Where do I download Zotero?

You can download Zotero on the [Zotero download page](/download/). Be sure to also install the Zotero Connector for your browser.

### How do I install Zotero?

#### Mac

Open the .dmg you downloaded and drag Zotero to the Applications folder. You can then run Zotero from Spotlight, Launchpad, or the Applications folder and add it to your Dock like any other program.

After installing Zotero, you can eject and delete the .dmg file.

#### Windows

Run the setup program you downloaded.

#### Linux

##### Official Tarball

Download the tarball, extract the contents, and run `zotero` from that directory to start Zotero.

For Ubuntu and other distros that support .desktop files, the tarball includes a .desktop file that can be used to add Zotero to the launcher:

1.  Move the extracted directory to a location of your choice (e.g., `/opt/zotero`).
2.  Run the `set_launcher_icon` script from a terminal to update the .desktop file for that location. .desktop files require absolute paths for icons, so `set_launcher_icon` replaces the icon path with the current location of the icon based on where you've placed the directory.
3.  Symlink `zotero.desktop` into `~/.local/share/applications/` (e.g., `ln -s /opt/zotero/zotero.desktop ~/.local/share/applications/zotero.desktop`)

Zotero should then appear either in your launcher or in the applications list when you click the grid icon ("Show Applications"), from which you can drag it to the launcher.

You may need to re-run `set_launcher_icon` after certain Zotero updates. If something isn't working, it may help to remove the current symlink (`~/.local/share/applications/zotero.desktop`), wait a few seconds for Zotero to disappear from the launcher, and recreate it.

##### Debian/Ubuntu-based Distros

A longtime community member maintains [zotero-deb](https://github.com/retorquere/zotero-deb), a lightweight wrapper for the official tarball that uses `apt` for installation and updates. If you're not comfortable installing tarballs or are having trouble following the above instructions, this is what we recommend using.

##### Other Packages

Unofficial packages are also available for various distros, but note that such packages are built by third parties, and we can only provide support for the official tarball and zotero-deb. In particular, third-party packages may be sandboxed, breaking various functionality.

##### Chromebook

To set up Zotero on a Chromebook, see [Installing on a Chromebook](kb/installing_on_a_chromebook).

### How do I upgrade to a new version?

Zotero should update itself automatically by default, or you can go to the Help menu and select "Check for Updates…" to check for updates manually. You can also always manually install a new version of Zotero over your existing version without losing any data.

### Troubleshooting

If you're running older software, check the [system requirements](system_requirements) to be sure Zotero is compatible with your system.

If something still isn't working, [let us know in the Zotero Forums](getting_help#step_3_post_to_the_zotero_forums_really_it_works).
