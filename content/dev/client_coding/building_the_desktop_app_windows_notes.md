# Building the Zotero Desktop App on Windows

***Note:**
If you 1) primarily work on macOS or Linux and just want to test a build on Windows; 2) have [WSL](https://learn.microsoft.com/en-us/windows/wsl/install) installed, you don't need to follow these steps. You can simply create an unpackaged Windows build on your main system/WSL with `app/scripts/dir_build -p w` and run the application in `app/staging/` from Windows.*

Instructions for [building the Zotero desktop app](dev/client_coding/building_the_desktop_app) assume a POSIX-compliant system capable of handling symbolic links. These instructions will work out-of-the box on most Linux and macOS systems, but Windows requires a few extra steps.

1.  Install [Node.js](https://nodejs.org/en/download/) (Node 18 LTS recommended) and [Cygwin](https://www.cygwin.com/). During Cygwin setup, in the "Select Packages" step, select the following additional packages to install: "git", "p7zip", "python3", "wget", "xz", "zip", and "unzip".
2.  Run Cygwin Terminal as Administrator (right click -> Run as Administrator). Run the following commands in that Cygwin terminal, in a single session.
3.  Force Cygwin to use native windows symlinks: `export CYGWIN="winsymlinks:nativestrict"`
4.  Clone the Zotero source code without checking it out: `git clone --config core.symlinks=true --no-checkout https://github.com/zotero/zotero zotero-client`
5.  Change to the source code repo, check out required files, and install Node.js modules: `cd zotero-client
    git checkout HEAD package.json package-lock.json
    npm install
    `
6.  Check out the remaining files, creating valid symbolic links: `git checkout -f HEAD
    git submodule update --init --recursive` *Note*: If you are seeing here errors of the form "error: unable to create symlink [...]: Operation not permitted" then you are not running Cygwin as an administrator (see step 2 above).
7.  Fetch `rcedit`, which is an additional build dependency on Windows:`app/scripts/fetch_rcedit`
8.  Continue building the app with `app/scripts/build_and_run -r`, as explained on [Building the Zotero Desktop App](dev/client_coding/building_the_desktop_app)

## Troubleshooting Errors

#### line 2: $'\\r' : command not found

This error is caused by the Cygwin shell misinterpreting Windows line endings in the Node executable. Rerun the Cygwin installer, add the "dos2unix" package, then run:

``` sh
dos2unix "$(which npm)" "$(which npx)"
```
