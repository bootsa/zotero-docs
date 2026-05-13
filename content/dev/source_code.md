# Zotero Source Code

**Note:** If you do not plan to make any code changes yourself, and only wish to run the latest prerelease versions of Zotero, you can just install a [beta build](beta_builds).

## Licensing

Zotero code is available under the [AGPLv3](http://www.gnu.org/licenses/agpl.html) license, except where the source code specifies otherwise.

## Code Repositories

### Zotero Code

Zotero source code is hosted [on GitHub](https://github.com/zotero).

### Third-Party Components

| Component                                                          | URL                                                  |
|--------------------------------------------------------------------|------------------------------------------------------|
| [citeproc-js](http://gsl-nagoya-u.net/http/pub/citeproc-doc.html)  | <https://github.com/juris-m/citeproc-js>             |
| [Citation Style Language (CSL)](http://citationstyles.org) styles  | <https://github.com/citation-style-language/styles>  |
| [Citation Style Language (CSL)](http://citationstyles.org) locales | <https://github.com/citation-style-language/locales> |

## Issue Tracking

We don't use GitHub Issues for bug reports or feature requests regarding the Zotero client or website. Please post all such requests to the [Zotero Forums](/forum), where Zotero developers and many others can help. Keeping product discussions in the Zotero Forums allows the entire Zotero community to participate, including domain experts that can address many questions better than Zotero developers. See [How Zotero Support Works](zotero_support) for more information.

For confirmed bugs or agreed-upon changes, Zotero developers will create new issues in the relevant repositories.

## Working with the Zotero Source Code

### Zotero

See [Building the Desktop App](dev/client_coding/building_the_desktop_app).

#### Zotero Connector

To run a Git build of the Google Chrome Connector, you need to:

-   `git clone --recursive https://github.com/zotero/zotero-connectors/`
-   `cd zotero-connectors`
-   `npm i`
-   `./build -d && gulp`
-   Run Zotero and Chrome
-   Load the Connector extension in Chrome
    1.  Browse to <chrome://extensions/>
    2.  Expand the "Developer mode" bar
    3.  Click the button "Load unpacked extension...", and give the path to the `build/browserExt` directory within the local repository

You should now see a Zotero icon in the address bar when visiting translatable webpages (e.g., [this article](https://agupubs.onlinelibrary.wiley.com/doi/abs/10.1029/2018JC014784) or [this book](http://www.amazon.com/gp/product/B002B3YBZO/ref=s9_pop_gw_ir03/190-5343882-9824666?pf_rd_m=ATVPDKIKX0DER&pf_rd_s=center-2&pf_rd_r=00JVFZE24KQ87CV9QJ59&pf_rd_t=101&pf_rd_p=1263340922&pf_rd_i=507846)), and clicking the icon should add the item to your Zotero library.

After making changes, click Reload for the Connector entry in the Chrome Extensions pane and reload any open pages where you want to use the Connector. (If `gulp` isn't running, you'll need to run `./build -d` after each change.)

See the [Zotero Connector GitHub repo](https://github.com/zotero/zotero-connectors) for more details.

### Contributing patches

The preferred way to contribute code is to fork the relevant Git repository, commit your changes, and submit a pull request on GitHub.

See [Client Coding](dev/client_coding) for more information on coding for Zotero.
