# HTTP Citing Protocol

The Google Docs plugin uses a simple HTTP protocol to communicate with Zotero. The below documentation applies to Zotero 6.0 and newer.

## Basics

Zotero operates a server on port 23119 for [Zotero Connector integration](dev/client_coding/connector_http_server). It includes endpoints for integrating with Zotero citing functionality. The integrating plugin or application only needs to be able to send HTTP JSON requests to fully implement the citing protocol.

A single [citing integration command](#word_processor_commands) is implemented as a series of requests and responses to the HTTP endpoints, constituting a transaction. The integration client begins a transaction by sending a request to <http://127.0.0.1:23119/connector/document/execCommand> which responds a command to be executed by the client, then subsequent requests with executed command results are made to <http://127.0.0.1:23119/connector/document/respond> until a transaction is complete.

### An example

In order to add a citation to a document, the implementing client sends the following to <http://127.0.0.1:23119/connector/document/execCommand>:

    {
      "command":"addEditCitation",
      "docId":"1ro9AmDxrwbys-xjazJqQG7UlSbBC76CU5xRJ71I8UjE"
    }

Zotero then responds by asking for the active document:

    {
      "command":"Application.getActiveDocument",
      "arguments":[]
    }

The client then sends a response to <http://127.0.0.1:23119/connector/document/respond> consisting of the the document ID and config options for the implementing client:

    {
      "documentID":"1ro9AmDxrwbys-xjazJqQG7UlSbBC76CU5xRJ71I8UjE",
      "outputFormat":"html",
      "supportedNotes":["footnotes"]
    }

You can observe the communication between Zotero and Google Docs in the Zotero Connector background page, which is accessed at `about:extensions` on Chrome by enabling Developer mode and clicking "background page" for Zotero Connector, or at `about:debugging` on Firefox by clicking "Debug" for Zotero connector. The requests are listed under the Network tab in the developer tools window.

## Integration Commands

These commands are sent from the word processor to Zotero, and do not receive a response. The command payload always follows this format.

    {
      "command":"<Command>",
      "docId":"<Document ID>" // an unique document identifying string
    }

| Command               | Description                                                                          |
|-----------------------|--------------------------------------------------------------------------------------|
| "addEditCitation"     | Add a new or edit an existing citation                                               |
| "addEditBibliography" | Add a new or edit an existing bibliography                                           |
| "addNote"             | Insert a Zotero note into the document                                               |
| "refresh"             | Refresh all fields in the document, verifying that they match expectations           |
| "removeCodes"         | Remove field codes from the document                                                 |
| "setDocPrefs"         | Change the citation style or other document parameters                               |
| "exportDocument"      | Export the citations in the document to a format importable in other word processors |

An up-to-date command list is always available by looking at the methods of [Zotero.Integration.Interface](https://github.com/zotero/zotero/blob/master/chrome/content/zotero/xpcom/integration.js#L619).

If Zotero responds with a 503 HTTP response, it means that another integration transaction is already in progress. If your integration client initiates an integration transaction and fails to complete it by either returning an error or responding to requests until `#Document.complete` is issued the Zotero integration layer will continuously respond with 503 until it is restarted.

## Word Processor Commands

These commands are sent from Zotero to the word processor. They must always receive a response. The command payload is always a JSON-encoded string in the form

    {
      "command":"<Command Name>",
      "arguments":[]
    }

If the request is successful, the client must send a response with a JSON-encoded payload. This response is often null if the command returns no output, but may also be an array, an integer, a string, or a boolean value depending on the command.

If the request is unsuccessful, the client must send a response with the payload:

    {
      "error": "<Error Name>",
      "message": "<Error Message>",
      "stack": "<Optional error stack Object or String>"
    }

Zotero will cancel the current operation, log this error, and present it to the user using the [Document.displayAlert](#documentdisplayalert) command if possible. If the subsequent Document.displayAlert command fails, Zotero will present the error using its own dialog box.

A full and up-to-date API of commands is available as part of [Zotero Integration tests](https://github.com/zotero/zotero/blob/master/test/tests/integrationTest.js) and [|LibreOffice plugin code](https://github.com/zotero/zotero-libreoffice-integration/blob/master/components/zoteroOpenOfficeIntegration.js#L358).

### Application.getActiveDocument

Gets information about the client and the currently active document.

#### Parameters

N/A

#### Returns

<table>
  <tbody>
    <tr><td>documentID</td><td>Integer</td><td>String</td><td>An ID corresponding to the document that is currently active</td></tr>
    <tr><td>outputFormat</td><td>String</td><td>Either "html" or "rdt". Defaults to "html"</td></tr>
    <tr><td>supportedNotes</td><td>Array</td><td>Supported options are an empty array if no Note support, "footnotes" and/or "endnotes". Note styles will not be available if this option is an empty array. Default to ["footnotes"]</td></tr>
  </tbody>
</table>

### Document.displayAlert

Shows an alert.

#### Parameters

<table>
  <tbody>
    <tr><td>dialogText</td><td>String</td><td>The text to display inside the dialog.</td></tr>
    <tr><td>icon</td><td>Integer</td><td>One of: <code class="multiline">DIALOG_ICON_STOP = 0&#10;DIALOG_ICON_NOTICE = 1&#10;DIALOG_ICON_CAUTION = 2</code></td></tr>
    <tr><td>buttons</td><td>Integer</td><td>One of: <code class="multiline">DIALOG_BUTTONS_OK = 0&#10;DIALOG_BUTTONS_OK_CANCEL = 1&#10;DIALOG_BUTTONS_YES_NO = 2&#10;DIALOG_BUTTONS_YES_NO_CANCEL = 3</code></td></tr>
  </tbody>
</table>

#### Returns

(Integer) The index of the button pressed, according to the value of buttons sent as a parameter.

<table>
  <tbody>
    <tr><td>DIALOG_BUTTONS_OK</td><td><code>OK = 1</code></td></tr>
    <tr><td>DIALOG_BUTTONS_OK_CANCEL</td><td><code class="multiline">CANCEL = 0&#10;OK = 1</code></td></tr>
    <tr><td>DIALOG_BUTTONS_YES_NO</td><td><code class="multiline">NO = 0&#10;YES = 1</code></td></tr>
    <tr><td>DIALOG_BUTTONS_YES_NO_CANCEL</td><td><code class="multiline">CANCEL = 0&#10;NO = 1&#10;YES = 2</code></td></tr>
  </tbody>
</table>

### Document.activate

Brings the document to the foreground.

#### Parameters

N/A

#### Returns

null

### Document.canInsertField

Indicates whether a field can be inserted at the current cursor position.

#### Parameters

N/A

#### Returns

(Boolean) Whether a field can be inserted.

### Document.setDocumentData

Stores a document-specific persistent data string. This data contains the style ID and other user preferences.

#### Parameters

<table>
  <tbody>
    <tr><td>dataString</td><td>String</td><td>The data string</td></tr>
  </tbody>
</table>

#### Returns

null

### Document.getDocumentData

Retrieves data string set by [setDocumentData](#setdocumentdata).

#### Parameters

N/A

#### Returns

(String) The document data string.

### Document.cursorInField

Indicates whether the cursor is in a given field. If it is, returns information about that field.

#### Parameters

<table>
  <tbody>
    <tr><td>fieldType</td><td>String</td><td>The type of field used by the document, always "Http" for HTTP integration and can be ignored</td></tr>
  </tbody>
</table>

#### Returns

Either null, indicating that the cursor isn't in a field, or (Array)

<table>
  <tbody>
    <tr><td>0</td><td>fieldID</td><td>Integer</td><td>String</td><td>A unique identifier corresponding to this field</td></tr>
    <tr><td>1</td><td>fieldCode</td><td>Integer</td><td>String</td><td>The code stored within this field</td></tr>
    <tr><td>2</td><td>noteIndex</td><td>Integer</td><td>The number of the footnote in which this field resides, or 0 if the field is not in a footnote.</td></tr>
  </tbody>
</table>

### Document.insertField

Inserts a new field at the current cursor position.

#### Parameters

<table>
  <tbody>
    <tr><td>fieldType</td><td>String</td><td>The type of field used by the document, either ReferenceMark or Bookmark</td></tr>
    <tr><td>noteType</td><td>Integer</td><td>The type of note specified by the style: <code class="multiline">NOTE_IN_TEXT = 0&#10;NOTE_FOOTNOTE = 1&#10;NOTE_ENDNOTE = 2</code>If noteType is not NOTE_IN_TEXT, the implementation should create a new note before inserting the field</td></tr>
  </tbody>
</table>

#### Returns

(Array)

<table>
  <tbody>
    <tr><td>0</td><td>fieldID</td><td>Integer</td><td>String</td><td>A unique identifier corresponding to this field</td></tr>
    <tr><td>1</td><td>fieldCode</td><td>Integer</td><td>String</td><td>The code stored within this field. Since no data has been set, this should be empty.</td></tr>
    <tr><td>2</td><td>noteIndex</td><td>Integer</td><td>The number of the footnote in which this field resides, or 0 if the field is not in a footnote.</td></tr>
  </tbody>
</table>

### Document.insertText

Inserts rich text (HTML) at cursor position. The rich text may contain citation placeholder hyperlinks (to <https://www.zotero.org/>?[placeholderID]) which are later converted to citations via [Document.convertPlaceholdersToFields](#documentconvertplaceholderstofields).

#### Parameters

<table>
  <tbody>
    <tr><td>text</td><td>String</td><td>The text</td></tr>
  </tbody>
</table>

#### Returns

null

### Document.getFields

Get all fields present in the document, in document order.

#### Parameters

<table>
  <tbody>
    <tr><td>fieldType</td><td>String</td><td>The type of field used by the document, always "Http" for HTTP integration and can be ignored</td></tr>
  </tbody>
</table>

#### Returns

(Array)

<table>
  <tbody>
    <tr><td>0</td><td>fieldID</td><td>Array(Integer</td><td>String)</td><td>Unique identifiers for each field</td></tr>
    <tr><td>1</td><td>fieldCode</td><td>Array(Integer</td><td>String)</td><td>The code stored in each field</td></tr>
    <tr><td>2</td><td>noteIndex</td><td>Array(Integer)</td><td>The number of the footnote in which each field resides, or 0 if the field is not in a footnote</td></tr>
  </tbody>
</table>

### Document.convert

Converts all fields in a document to a different fieldType or noteType. Called upon style change from a an in-text to note type or vice-versa

#### Parameters

<table>
  <tbody>
    <tr><td>fields</td><td>Array(String)</td><td>Array of field IDs to be converted</td></tr>
    <tr><td>toFieldType</td><td>Array(String)</td><td>Should be ignored</td></tr>
    <tr><td>toNoteType</td><td>Array(Number)</td><td>Array of note types to be converted to. Each array entry corresponds to a field in the <code>fields</code> parameter and is one of <code class="multiline">NOTE_IN_TEXT = 0&#10;NOTE_FOOTNOTE = 1&#10;NOTE_ENDNOTE = 2</code></td></tr>
    <tr><td>count</td><td>Number</td><td>Size of the above arrays</td></tr>
  </tbody>
</table>

#### Returns

null

### Document.convertPlaceholdersToFields

Converts placeholders (which are text with links to <https://www.zotero.org/>?[placeholderID]) to fields and sets their field codes to strings in \`codes\` in the reverse order of their appearance

#### Parameters

<table>
  <tbody>
    <tr><td>0</td><td>placeholderIDs</td><td>Array(String)</td><td>An array of placeholderID strings which are to be converted to citation fields in the document.</td></tr>
    <tr><td>1</td><td>noteType</td><td>Number</td><td>Note type to convert citation placeholders to. Is one of <code class="multiline">NOTE_IN_TEXT = 0&#10;NOTE_FOOTNOTE = 1&#10;NOTE_ENDNOTE = 2</code></td></tr>
    <tr><td>2</td><td>fieldType</td><td>Number</td><td>To be ignored</td></tr>
  </tbody>
</table>

#### Returns

Array of fields after conversion

(Array)

<table>
  <tbody>
    <tr><td>0</td><td>fieldID</td><td>Array(Integer</td><td>String)</td><td>Unique identifiers for each field</td></tr>
    <tr><td>1</td><td>fieldCode</td><td>Array(Integer</td><td>String)</td><td>The code stored in each field</td></tr>
    <tr><td>2</td><td>noteIndex</td><td>Array(Integer)</td><td>The number of the footnote in which each field resides, or 0 if the field is not in a footnote</td></tr>
  </tbody>
</table>

### Document.setBibliographyStyle

Sets parameters to be used to style the bibliography. Numbers are in [twips](https://en.wikipedia.org/wiki/Twip)

#### Parameters

<table>
  <tbody>
    <tr><td>firstLineIndent</td><td>Number</td><td>First line indent of each bibliography paragraph</td></tr>
    <tr><td>indent</td><td>Number</td><td>The indent of each bibliography paragraph</td></tr>
    <tr><td>lineSpacing</td><td>Number</td><td>Paragraph line spacing</td></tr>
    <tr><td>entrySpacing</td><td>Number</td><td>Line spacing between paragraphs</td></tr>
    <tr><td>tabStops</td><td>Array(Number)</td><td>An array of tab stops</td></tr>
    <tr><td>tabStopsCount</td><td>Number</td><td>Size of the <code>tabStops</code> array</td></tr>
  </tbody>
</table>

#### Returns

null

### Document.complete

Indicates that the given documentID will no longer be used and associated resources may be freed. **NOTE: No further requests to <http://127.0.0.1:23119/connector/document/respond> should be made after this point**

#### Parameters

N/A

#### Returns

null

### Field.delete

Deletes a field from the document (both its code and its contents).

#### Parameters

<table>
  <tbody>
    <tr><td>fieldID</td><td>Integer</td><td>String</td><td>The fieldID, as originally returned by <a href="#documentcursorinfield">Document.cursorInField</a>, <a href="#documentinsertfield">Document.insertField</a>, or <a href="#documentgetfields">Document.getFields</a></td></tr>
  </tbody>
</table>

#### Returns

null

### Field.select

Moves the current cursor position to encompass a field.

#### Parameters

<table>
  <tbody>
    <tr><td>fieldID</td><td>Integer</td><td>String</td><td>The fieldID, as originally returned by <a href="#documentcursorinfield">Document.cursorInField</a>, <a href="#documentinsertfield">Document.insertField</a>, or <a href="#documentgetfields">Document.getFields</a></td></tr>
  </tbody>
</table>

#### Returns

null

### Field.removeCode

Removes the field code from a field, leaving it as plain text.

#### Parameters

<table>
  <tbody>
    <tr><td>fieldID</td><td>Integer</td><td>String</td><td>The fieldID, as originally returned by <a href="#documentcursorinfield">Document.cursorInField</a>, <a href="#documentinsertfield">Document.insertField</a>, or <a href="#documentgetfields">Document.getFields</a></td></tr>
  </tbody>
</table>

#### Returns

null

### Field.setText

Sets the (visible) text of a field.

#### Parameters

<table>
  <tbody>
    <tr><td>fieldID</td><td>Integer</td><td>String</td><td>The fieldID, as originally returned by <a href="#documentcursorinfield">Document.cursorInField</a>, <a href="#documentinsertfield">Document.insertField</a>, or <a href="#documentgetfields">Document.getFields</a></td></tr>
    <tr><td>text</td><td>String</td><td colspan="2">The text</td></tr>
    <tr><td>isRich</td><td>Boolean</td><td colspan="2">Whether the text should be interpreted as RTF if Document.outputFormat is RTF, otherwise always true</td></tr>
  </tbody>
</table>

#### Returns

null

### Field.getText

Gets the (visible) text of a field.

#### Parameters

<table>
  <tbody>
    <tr><td>fieldID</td><td>Integer</td><td>String</td><td>The fieldID, as originally returned by <a href="#documentcursorinfield">Document.cursorInField</a>, <a href="#documentinsertfield">Document.insertField</a>, or <a href="#documentgetfields">Document.getFields</a></td></tr>
  </tbody>
</table>

#### Returns

(String) The (visible) text

### Field.setCode

Sets the (hidden, persistent) code of a field.

#### Parameters

<table>
  <tbody>
    <tr><td>fieldID</td><td>Integer</td><td>String</td><td>The fieldID, as originally returned by <a href="#documentcursorinfield">Document.cursorInField</a>, <a href="#documentinsertfield">Document.insertField</a>, or <a href="#documentgetfields">Document.getFields</a></td></tr>
    <tr><td>code</td><td>String</td><td>The field code</td></tr>
  </tbody>
</table>

#### Returns

null

## Other resources

See:

-   [Dummy Document Client](https://github.com/zotero/zotero/blob/01f3159b2f5baacff6423297d14d58230970f4ec/test/tests/integrationTest.js#L14-L183) implementation in Zotero tests
-   The proper [implementation of the HTTP client](https://github.com/zotero/zotero-google-docs-integration/blob/267f45fb5203dec7bdbb9fea163b6d15bbe0ff16/src/connector/client.js#L112-L466) for our Google Docs plugin
