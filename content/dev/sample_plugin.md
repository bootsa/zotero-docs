<p id="zotero-5-update-warning" style="color: red; font-weight: bold">We’re
in the process of updating the documentation for
<a href="https://www.zotero.org/blog/zotero-5-0">Zotero 5.0</a>. Some documentation
may be outdated in the meantime. Thanks for your understanding.</p>

# A Sample Zotero Plugin

To help you get started creating Zotero plugins, we’ve created a simple Hello World plugin that demonstrates how to access Zotero from an external extension. See [Interacting with Zotero from Within Firefox](dev/client_coding/javascript_api) for more information.

You can obtain the [Hello World code from github](https://github.com/zotero/zotero-hello-world).

For more information on the basic elements and layout of a Firefox extension, see the [XUL School Tutorial](https://developer.mozilla.org/en-US/docs/XUL_School) in the Mozilla Developer Center.

The most important code is in [chrome:*helloworldzotero/content/hello.js]], which defines a method to insert a new item into the Zotero database and registers a callback function with the Zotero Notifier to receive a notification when an item is modified. The script is loaded by [[https:*www.zotero.org/trac/browser/plugins/helloworld/trunk/chrome/content/helloworldzotero/include.js|chrome:*helloworldzotero/content/include.js]], which is included into the main overlay by [[https:*www.zotero.org/trac/browser/plugins/helloworld/trunk/chrome/content/helloworldzotero/overlay.xul|chrome/content/helloworldzotero/overlay.xul](https://www.zotero.org/trac/browser/plugins/helloworld/trunk/chrome/content/helloworldzotero/hello.js). The latter also adds a menu item to the Zotero Actions menu.

Once installed, the plugin will display an alert whenever an item is added, modified or deleted in Zotero. (You'll probably want your own plugin to do something slightly less annoying.)

**chrome/content/helloworldzotero/hello.js:**

*Note: This file is loaded by chrome://helloworldzotero/content/include.js, which makes sure the Zotero.HelloWorldZotero object is only created once.*

``` javascript
Zotero.HelloWorldZotero = {
    DB: null,
    
    init: function () {
        // Connect to (and create, if necessary) helloworld.sqlite in the Zotero directory
        this.DB = new Zotero.DBConnection('helloworld');
        
        if (!this.DB.tableExists('changes')) {
            this.DB.query("CREATE TABLE changes (num INT)");
            this.DB.query("INSERT INTO changes VALUES (0)");
        }
        
        // Register the callback in Zotero as an item observer
        var notifierID = Zotero.Notifier.registerObserver(this.notifierCallback, ['item']);
        
        // Unregister callback when the window closes (important to avoid a memory leak)
        window.addEventListener('unload', function(e) {
                Zotero.Notifier.unregisterObserver(notifierID);
        }, false);
    },
    
    insertHello: function() {
        var data = {
            title: "Zotero",
            company: "Center for History and New Media",
            creators: [
                ['Dan', 'Stillman', 'programmer'],
                ['Simon', 'Kornblith', 'programmer']
            ],
            version: '1.0.1',
            company: 'Center for History and New Media',
            place: 'Fairfax, VA',
            url: 'http://www.zotero.org'
        };
        Zotero.Items.add('computerProgram', data); // returns a Zotero.Item instance
    },
    
    // Callback implementing the notify() method to pass to the Notifier
    notifierCallback: {
        notify: function(event, type, ids, extraData) {
            if (event == 'add' || event == 'modify' || event == 'delete') {
                // Increment a counter every time an item is changed
                Zotero.HelloWorldZotero.DB.query("UPDATE changes SET num = num + 1");
                
                if (event != 'delete') {
                    // Retrieve the added/modified items as Item objects
                    var items = Zotero.Items.get(ids);
                }
                else {
                    var items = extraData;
                }
                
                // Loop through array of items and grab titles
                var titles = [];
                for each(var item in items) {
                    // For deleted items, get title from passed data
                    if (event == 'delete') {
                        titles.push(item.old.title ? item.old.title : '[No title]');
                    }
                    else {
                        titles.push(item.getField('title'));
                    }
                }
                
                if (!titles.length) {
                    return;
                }
                
                // Get the localized string for the notification message and
                // append the titles of the changed items
                var stringName = 'notification.item' + (titles.length==1 ? '' : 's');
                switch (event) {
                    case 'add':
                        stringName += "Added";
                        break;
                        
                    case 'modify':
                        stringName += "Modified";
                        break;
                        
                    case 'delete':
                        stringName += "Deleted";
                        break;
                }
                
                var str = document.getElementById('hello-world-zotero-strings').
                    getFormattedString(stringName, [titles.length]) + ":\n\n" +
                    titles.join("\n");
            }
            
            alert(str);
        }
    }
};

// Initialize the plugin
window.addEventListener('load', function(e) { Zotero.HelloWorldZotero.init(); }, false);


```
