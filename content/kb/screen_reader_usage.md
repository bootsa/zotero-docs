### Using Zotero with Screen Readers

We regularly test Zotero for accessibility with VoiceOver on macOS and with NVDA and JAWS on Windows. There are some settings and best practices for different screen readers that will help them work well with Zotero. Based on our testing, below are settings that are likely to work for each screen reader, along with known issues with some of them.

#### macOS with VoiceOver

##### Usage

-   Ensure that the Settings > Keyboard > Keyboard navigation setting is toggled on. It is required for keyboard navigation to properly work.
-   Make sure that the Voiceover QuickNav setting is toggled off. It allows one to move focus in unwanted ways and, in addition, can move the cursor onto nodes that are not supposed to be focusable. There are cases when it can be helpful but as a general rule it is better left off.

##### Issues

-   Known Voiceover issue in Firefox and Zotero: aria-readonly/readonly properties are ignored and inputs with those props are announced as editable fields.

  

#### Windows with NVDA

NVDA is the most reliably working screen reader with Zotero and never caused any issues. No changes to the default configuration was needed.

#### Windows with JAWS

##### Usage

-   By default, JAWS will not announce description aria properties. It can be adjusted in Settings > Speech Verbosity > Verbosity Level. Click on the verbosity level setting button (“Beginner” by default), and enable “Control Description”.
-   JAWS should be started *before* opening Zotero. There is additional setup during startup to accommodate JAWS usage that only runs if JAWS is already running on the system.
-   Virtual cursor should be avoided in Zotero, except for reading the content in PDF/ePub/Snapshot reader tabs and the note editor. JAWS treats these parts of Zotero as a web browser.

##### Issues

-   JAWS may not always announce labels and descriptions of groups when the focus enters them. For example, Linked Attachment Base Directory preference comment gets skipped. One can use JAWS (by default INSERT) + Tab shortcut to have JAWS announce the currently focused element, which will force it to read out the parent group labels.
-   JAWS does not have the right configuration to handle alert windows in Zotero, which leads to poor handling of these in which JAWS won’t read text in input and text fields. This can be changed, but the JAWS configuration is not exposed to end users.
