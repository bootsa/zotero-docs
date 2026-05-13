# LibreOffice Wire Protocol

The LibreOffice plugin uses a simple wire protocol to communicate with Zotero. (The Word for Mac and Word for Windows plugins both run in process, and use AppleEvents and COM respectively to communicate with the word processor.) The below documentation applies to Zotero 6.0 and newer.

## Basics

The Zotero client process operates a server on port 23116, which the extension residing within LibreOffice connects to. All frames consist of a 32 bits specifying the transaction ID, a big-endian 32-bit integer specifying the length of the payload, and the payload itself, which is either UTF-8 encoded JSON or an unescaped string beginning with "ERR:".

There are two types of commands: [integration command](#integration_commands), sent by the word processor to Zotero initiate an operation (e.g., to add a new citation), and [word processor commands](#word_processor_commands), sent from Zotero to the word process to retrieve data from a document or to make changes to the document. Integration commands are sent from the word processor to Zotero, and must never receive a response. Word processor commands are sent from Zotero to the word processor, and must always receive a response.

### Transaction ID

The transaction ID allows Zotero to determine whether the given frame is a response to another frame. When the client sends an [integration command](#integration_commands), it must send 0 as the transaction ID. [Word processor commands](#word_processor_commands) always specify a non-zero transaction ID, and the response to these commands must maintain the same transaction ID.

### An example

In order to add a citation to a document, LibreOffice sends the following:

                    TRANS ID    LENGTH      PAYLOAD
    HEXADECIMAL     00 00 00 00 00 00 00 0C 22 61 64 64 43 69 74 61 74 69 6F 6E 22
    INTERPRETATION  0           11          {"command": "setDocPrefs", "templateVersion": 1} 

Zotero then responds by asking for the active document, and supplying the API version it supports:

                    TRANS ID    LENGTH      PAYLOAD
    HEXADECIMAL     00 00 00 01 00 00 00 24 5B 22 41 70 70 6C 69 63 61 74 69 6F (...)
    INTERPRETATION  1           36          ["Application_getActiveDocument", 3]

The client then sends a response consisting of the API version it supports and the document ID:

                    TRANS ID    LENGTH      PAYLOAD
    HEXADECIMAL     00 00 00 01 00 00 00 24 5B 33 2C 20 31 5D
    INTERPRETATION  1           6           [3, 1]

You can observe frame payloads sent between Zotero and LibreOffice in the Zotero [debug output](debug_output).

## Integration Commands

These commands are sent from the word processor to Zotero, and do not receive a response. The command payload is always a JSON object with a \`command\` property, which is described below and a \`templateVersion\` property which is a number. The templateVersion number is used by Zotero to notify the integration user if the plugin installed in LibreOffice is outdated. The current up-to-date version is "1".

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

## Word Processor Commands

These commands are sent from Zotero to the word processor. They must always receive a response. The command payload is always JSON-encoded in the form

    [COMMAND_NAME, [...PARAMETERS...]]

If the request is successful, the client must send a response with a JSON-encoded payload. This response is often null if the command returns no output, but may also be an array, an integer, a string, or a boolean value depending on the command.

If the request is unsuccessful, the client must send a response with the payload:

    ERR:(Error string goes here).

Zotero will cancel the current operation, log this error, and present it to the user using the [Document_displayAlert](#document_displayalert) command if possible. If the subsequent Document_displayAlert command fails, Zotero will present the error using its own dialog box.

A full and up-to-date API of commands is available as part of [Zotero Integration tests](https://github.com/zotero/zotero/blob/master/test/tests/integrationTest.js) and [|LibreOffice plugin code](https://github.com/zotero/zotero-libreoffice-integration/blob/master/components/zoteroOpenOfficeIntegration.js#L358).

### Application_getActiveDocument

Gets information about the client and the currently active document.

#### Parameters

<table>
  <tbody>
    <tr><td>protocolVersion</td><td>int</td><td>The version of the wire protocol supported by Zotero. Since Zotero determines whether the client's protocol version is compatible and shows an appropriate error if necessary, it is unlikely that the client needs to make use of this.</td></tr>
  </tbody>
</table>

#### Returns

<table>
  <tbody>
    <tr><td>protocolVersion</td><td>Integer</td><td>The version of the protocol supported by the client.</td></tr>
    <tr><td>documentID</td><td>Integer</td><td>String</td><td>An ID corresponding to the document that is currently active</td></tr>
  </tbody>
</table>

### Document_displayAlert

Shows an alert.

#### Parameters

<table>
  <tbody>
    <tr><td>documentID</td><td>Integer</td><td>String</td><td>The documentID, as originally returned by <a href="#application_getactivedocument">Application_getActiveDocument</a></td></tr>
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

### Document_activate

Brings the document to the foreground. This is a no-op on non-Mac systems.

#### Parameters

<table>
  <tbody>
    <tr><td>0</td><td>documentID</td><td>Integer</td><td>String</td><td>The documentID, as originally returned by <a href="#application_getactivedocument">Application_getActiveDocument</a></td></tr>
  </tbody>
</table>

#### Returns

null

### Document_canInsertField

Indicates whether a field can be inserted at the current cursor position.

#### Parameters

<table>
  <tbody>
    <tr><td>0</td><td>documentID</td><td>Integer</td><td>String</td><td>The documentID, as originally returned by <a href="#application_getactivedocument">Application_getActiveDocument</a></td></tr>
  </tbody>
</table>

#### Returns

(Boolean) Whether a field can be inserted.

### Document_setDocumentData

Stores a document-specific persistent data string. This data contains the style ID and other user preferences.

#### Parameters

(Array)

<table>
  <tbody>
    <tr><td>0</td><td>documentID</td><td>Integer</td><td>String</td><td>The documentID, as originally returned by <a href="#application_getactivedocument">Application_getActiveDocument</a></td></tr>
    <tr><td>1</td><td>dataString</td><td>String</td><td>The data string</td></tr>
  </tbody>
</table>

#### Returns

null

### Document_getDocumentData

Retrieves data string set by [setDocumentData](#setdocumentdata). NOTE: If the document has been converted to the transfer format and the first line of the document reads "ZOTERO_TRANSFER_DOCUMENT", then this method should return "ZOTERO_TRANSFER_DOCUMENT".

#### Parameters

<table>
  <tbody>
    <tr><td>0</td><td>documentID</td><td>Integer</td><td>String</td><td>The documentID, as originally returned by <a href="#application_getactivedocument">Application_getActiveDocument</a></td></tr>
  </tbody>
</table>

#### Returns

(String) The document data string or "ZOTERO_TRANSFER_DOCUMENT"

### Document_cursorInField

Indicates whether the cursor is in a given field. If it is, returns information about that field.

#### Parameters

<table>
  <tbody>
    <tr><td>0</td><td>documentID</td><td>Integer</td><td>String</td><td>The documentID, as originally returned by <a href="#application_getactivedocument">Application_getActiveDocument</a></td></tr>
    <tr><td>1</td><td>fieldType</td><td>String</td><td>The type of field used by the document, either ReferenceMark or Bookmark</td></tr>
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

### Document_insertField

Inserts a new field at the current cursor position.

#### Parameters

<table>
  <tbody>
    <tr><td>0</td><td>documentID</td><td>Integer</td><td>String</td><td>The documentID, as originally returned by <a href="#application_getactivedocument">Application_getActiveDocument</a></td></tr>
    <tr><td>1</td><td>fieldType</td><td>String</td><td>The type of field used by the document, either ReferenceMark or Bookmark</td></tr>
    <tr><td>2</td><td>noteType</td><td>Integer</td><td>The type of note specified by the style: <code class="multiline">NOTE_IN_TEXT = 0&#10;NOTE_FOOTNOTE = 1&#10;NOTE_ENDNOTE = 2</code>If noteType is not NOTE_IN_TEXT, the implementation should create a new note before inserting the field</td></tr>
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

### Document_insertText

Inserts rich text (HTML) at cursor position. The rich text may contain citation placeholder hyperlinks (to <https://www.zotero.org/>?[placeholderID]) which are later converted to citations via [Document_convertPlaceholdersToFields](#document_convertplaceholderstofields).

#### Parameters

<table>
  <tbody>
    <tr><td>0</td><td>documentID</td><td>Integer</td><td>String</td><td>The documentID, as originally returned by <a href="#application_getactivedocument">Application_getActiveDocument</a></td></tr>
    <tr><td>1</td><td>text</td><td>String</td><td>The text</td></tr>
  </tbody>
</table>

#### Returns

null

### Document_getFields

Get all fields present in the document, in document order.

#### Parameters

<table>
  <tbody>
    <tr><td>0</td><td>documentID</td><td>Integer</td><td>String</td><td>The documentID, as originally returned by <a href="#application_getactivedocument">Application_getActiveDocument</a></td></tr>
    <tr><td>1</td><td>fieldType</td><td>String</td><td>The type of field used by the document, either ReferenceMark or Bookmark</td></tr>
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

### Document_convert

Converts all fields in a document to a different fieldType or noteType. Called upon style change from a an in-text to note type or vice-versa

#### Parameters

<table>
  <tbody>
    <tr><td>0</td><td>documentID</td><td>Integer</td><td>String</td><td>The documentID, as originally returned by <a href="#application_getactivedocument">Application_getActiveDocument</a></td></tr>
    <tr><td>1</td><td>fields</td><td>Array(String)</td><td>Array of field IDs to be converted</td></tr>
    <tr><td>2</td><td>toFieldType</td><td>Array(String)</td><td>Array of field types to be converted to. Each entry is either "ReferenceMark" or "Bookmark"</td></tr>
    <tr><td>3</td><td>toNoteType</td><td>Array(Number)</td><td>Array of note types to be converted to. Each array entry corresponds to a field in the <code>fields</code> parameter and is one of <code class="multiline">NOTE_IN_TEXT = 0&#10;NOTE_FOOTNOTE = 1&#10;NOTE_ENDNOTE = 2</code></td></tr>
    <tr><td>count</td><td>Number</td><td colspan="2">Size of the above arrays</td></tr>
  </tbody>
</table>

#### Returns

null

### Document_convertPlaceholdersToFields

Converts placeholders (which are text with links to <https://www.zotero.org/>?[placeholderID]) to fields and sets their field codes to strings in \`codes\` in the reverse order of their appearance

#### Parameters

<table>
  <tbody>
    <tr><td>0</td><td>documentID</td><td>Integer</td><td>String</td><td>The documentID, as originally returned by <a href="#application_getactivedocument">Application_getActiveDocument</a></td></tr>
    <tr><td>1</td><td>placeholderIDs</td><td>Array(String)</td><td>An array of placeholderID strings which are to be converted to citation fields in the document.</td></tr>
    <tr><td>2</td><td>noteType</td><td>Number</td><td>Note type to convert citation placeholders to. Is one of <code class="multiline">NOTE_IN_TEXT = 0&#10;NOTE_FOOTNOTE = 1&#10;NOTE_ENDNOTE = 2</code></td></tr>
    <tr><td>3</td><td>fieldType</td><td>Number</td><td>Field type to convert to. Either \<code>ReferenceMark\</code> or \<code>Bookmark\</code></td></tr>
    <tr><td>count</td><td>Number</td><td colspan="2">Size of the above arrays</td></tr>
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

### Document_importDocument

Called to convert Zotero document transfer format links to fields after Document_getDocumentData returns "ZOTERO_TRANSFER_DOCUMENT". Should reverse the export procedure. Note that citation links may contain trailing parameters, e.g. "<https://www.zotero.org/google-docs/?q15df3>"

#### Parameters

<table>
  <tbody>
    <tr><td>0</td><td>documentID</td><td>Integer</td><td>String</td><td>The documentID, as originally returned by <a href="#application_getactivedocument">Application_getActiveDocument</a></td></tr>
    <tr><td>1</td><td>fieldType</td><td>String</td><td>Specifies to what field type the import links should be converted. Should always be "ReferenceMark" for the LibreOffice wire protocol.</td></tr>
  </tbody>
</table>

#### Returns

\`true\` if field links and document data were found and imported, \`false\` otherwise

### Document_exportDocument

Converts the document to the Zotero transfer document format. The format is:
1. Insert 4 paragraphs at the beginning of the document, where first one reads "ZOTERO_TRANSFER_DOCUMENT" and third one has the \`transferDocumentInstructions\` supplied via a parameter.
2. Convert all citations to links that point to "<https://www.zotero.org/>" and the link text is set to the citation code.
3. At the end of the document insert a link that points to "<https://www.zotero.org/>" with the text set to documentData.

#### Parameters

<table>
  <tbody>
    <tr><td>0</td><td>documentID</td><td>Integer</td><td>String</td><td>The documentID, as originally returned by <a href="#application_getactivedocument">Application_getActiveDocument</a></td></tr>
    <tr><td>1</td><td>fieldType</td><td>String</td><td>The field type that the document stores Zotero citations in. Either "ReferenceMark" or "Bookmark".</td></tr>
    <tr><td>2</td><td>transferDocumentInstructions</td><td>String</td><td>A text string to be inserted at the start of the document explaining the document format</td></tr>
  </tbody>
</table>

#### Returns

null

### Document_setBibliographyStyle

Provides parameters for the dedicated bibliography formatting style (usually called "Bibliography").

#### Parameters

<table>
  <tbody>
    <tr><td>0</td><td>documentID</td><td>Integer</td><td>String</td><td>The documentID, as originally returned by <a href="#application_getactivedocument">Application_getActiveDocument</a></td></tr>
    <tr><td>1</td><td>firstLineIndent</td><td>Integer</td><td>First line indent in twips</td></tr>
    <tr><td>2</td><td>bodyIndent</td><td>Integer</td><td>Bibliography body indent in twips. Applies to first line too. First line indent is calculated by <code>firstLineIndent+bodyIndent</code></td></tr>
    <tr><td>3</td><td>lineSpacing</td><td>Integer</td><td>Line spacing in twips</td></tr>
    <tr><td>4</td><td>entrySpacing</td><td>Integer</td><td>Bibliography entry spacing in twips</td></tr>
    <tr><td>5</td><td>tabStops</td><td>Array(Integer)</td><td>Tabulator indents</td></tr>
    <tr><td>6</td><td>numTabStops</td><td>Integer</td><td>Length of tabStops array</td></tr>
  </tbody>
</table>

##### Example Parameters

    [1, -720, 720, 240, 0, [], 0]
    [1, -720, 720, 240, 0, [1], 720]

#### Returns

null

### Document_complete

Indicates that the given documentID will no longer be used and associated resources may be freed.

#### Parameters

<table>
  <tbody>
    <tr><td>documentID</td><td>Integer</td><td>String</td><td>The documentID, as originally returned by <a href="#application_getactivedocument">Application_getActiveDocument</a></td></tr>
  </tbody>
</table>

#### Returns

null

### Field_delete

Deletes a field from the document (both its code and its contents).

#### Parameters

<table>
  <tbody>
    <tr><td>documentID</td><td>Integer</td><td>String</td><td>The documentID, as originally returned by <a href="#application_getactivedocument">Application_getActiveDocument</a></td></tr>
    <tr><td>fieldID</td><td>Integer</td><td>String</td><td>The fieldID, as originally returned by <a href="#document_cursorinfield">Document_cursorInField</a>, <a href="#document_insertfield">Document_insertField</a>, or <a href="#document_getfields">Document_getFields</a></td></tr>
  </tbody>
</table>

#### Returns

null

### Field_select

Moves the current cursor position to encompass a field.

#### Parameters

<table>
  <tbody>
    <tr><td>documentID</td><td>Integer</td><td>String</td><td>The documentID, as originally returned by <a href="#application_getactivedocument">Application_getActiveDocument</a></td></tr>
    <tr><td>fieldID</td><td>Integer</td><td>String</td><td>The fieldID, as originally returned by <a href="#document_cursorinfield">Document_cursorInField</a>, <a href="#document_insertfield">Document_insertField</a>, or <a href="#document_getfields">Document_getFields</a></td></tr>
  </tbody>
</table>

#### Returns

null

### Field_removeCode

Removes the field code from a field, leaving it as plain text.

#### Parameters

<table>
  <tbody>
    <tr><td>documentID</td><td>Integer</td><td>String</td><td>The documentID, as originally returned by <a href="#application_getactivedocument">Application_getActiveDocument</a></td></tr>
    <tr><td>fieldID</td><td>Integer</td><td>String</td><td>The fieldID, as originally returned by <a href="#document_cursorinfield">Document_cursorInField</a>, <a href="#document_insertfield">Document_insertField</a>, or <a href="#document_getfields">Document_getFields</a></td></tr>
  </tbody>
</table>

#### Returns

null

### Field_setText

Sets the (visible) text of a field.

#### Parameters

<table>
  <tbody>
    <tr><td>documentID</td><td>Integer</td><td>String</td><td>The documentID, as originally returned by <a href="#application_getactivedocument">Application_getActiveDocument</a></td></tr>
    <tr><td>fieldID</td><td>Integer</td><td>String</td><td>The fieldID, as originally returned by <a href="#document_cursorinfield">Document_cursorInField</a>, <a href="#document_insertfield">Document_insertField</a>, or <a href="#document_getfields">Document_getFields</a></td></tr>
    <tr><td>text</td><td>String</td><td colspan="2">The text</td></tr>
    <tr><td>isRich</td><td>Boolean</td><td colspan="2">Whether the text should be interpreted as RTF</td></tr>
  </tbody>
</table>

#### Returns

null

### Field_getText

Gets the (visible) text of a field. Note that any RTF information from setText is not returned, just the visible plaintext.

#### Parameters

<table>
  <tbody>
    <tr><td>documentID</td><td>Integer</td><td>String</td><td>The documentID, as originally returned by <a href="#application_getactivedocument">Application_getActiveDocument</a></td></tr>
    <tr><td>fieldID</td><td>Integer</td><td>String</td><td>The fieldID, as originally returned by <a href="#document_cursorinfield">Document_cursorInField</a>, <a href="#document_insertfield">Document_insertField</a>, or <a href="#document_getfields">Document_getFields</a></td></tr>
  </tbody>
</table>

#### Returns

(String) The (visible) text

### Field_setCode

Sets the (hidden, persistent) code of a field.

#### Parameters

<table>
  <tbody>
    <tr><td>documentID</td><td>Integer</td><td>String</td><td>The documentID, as originally returned by <a href="#application_getactivedocument">Application_getActiveDocument</a></td></tr>
    <tr><td>fieldID</td><td>Integer</td><td>String</td><td>The fieldID, as originally returned by <a href="#document_cursorinfield">Document_cursorInField</a>, <a href="#document_insertfield">Document_insertField</a>, or <a href="#document_getfields">Document_getFields</a></td></tr>
    <tr><td>code</td><td>String</td><td>The field code</td></tr>
  </tbody>
</table>

#### Returns

null

### Field_convert

Converts a field from one type to another.

#### Parameters

<table>
  <tbody>
    <tr><td>documentID</td><td>Integer</td><td>String</td><td>The documentID, as originally returned by <a href="#application_getactivedocument">Application_getActiveDocument</a></td></tr>
    <tr><td>fieldID</td><td>Integer</td><td>String</td><td>The fieldID, as originally returned by <a href="#document_cursorinfield">Document_cursorInField</a>, <a href="#document_insertfield">Document_insertField</a>, or <a href="#document_getfields">Document_getFields</a></td></tr>
    <tr><td>fieldType</td><td>String</td><td>The type of field used by the document, either ReferenceMark or Bookmark</td></tr>
    <tr><td>noteType</td><td>Integer</td><td>The type of note specified by the style: <code class="multiline">NOTE_IN_TEXT = 0&#10;NOTE_FOOTNOTE = 1&#10;NOTE_ENDNOTE = 2</code></td></tr>
  </tbody>
</table>

#### Returns

null
