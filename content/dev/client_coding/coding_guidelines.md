JavaScript code in Zotero should conform to the following coding and style guidelines. We encourage Zotero plugin writers to follow these guidelines as well for consistency and possible future integration of code into the Zotero codebase.

**Note:** Not all current code in Zotero conforms to these guidelines. While existing code generally should not be modified for the sole purpose of conforming, new code or modifications to existing code should follow these guidelines.

## Basic style

-   Indent using tabs (width 4), not spaces
-   Lines should generally be kept to 100 characters, except where doing so would seriously decrease readability
-   Objects should be CamelCased and namespaced (`Zotero.FooBar` within the [Zotero XPCOM object](dev/client_coding/javascript_api#the_zotero_object), `ZoteroFooBar` without)
-   Functions and variables should be lowercase (`Zotero.Date.sqlToDate()`, `var foo = true;`)
-   Code should comply with JavaScript strict mode, with "use strict"; at the top of files: variables should be initialized before using, etc.

## Braces

Braces should conform to [1TBS variant of the K&R style](http://en.wikipedia.org/wiki/Indent_style#Variant:_1TBS):

``` javascript
function abc() {
    ...
}

if (abc == 'def') {
    ...
}
```

Add a space after keywords to distinguish them from function calls:

Bad:

``` javascript
if(foo) {
```

Good:

``` javascript
if (foo) {
```

Braces must **always** be used for multi-line conditionals, even if the enclosed block contains a single line.

Bad:

``` javascript
if (!_initialized)
   init();
```

Good:

``` javascript
if (!_initialized) {
   init();
}
```

## Public/privileged/private/static methods and members

*For an explanation of the difference between public, privileged and private methods and members, please see Douglas Crockford's [Private Members in JavaScript](http://javascript.crockford.com/private.html).*

-   For objects that will be instantiated multiple times, public methods (defined using `prototype` outside the constructor) should be used rather than privileged methods (defined using `this` within) for memory and performance reasons:

``` javascript
Zotero.Item = function() {
    ...
}

Zotero.Item.prototype.numCreators = function () {
    ...
}
```

-   Singleton objects should use a wrapper object or object notation:

``` javascript
Zotero.FooBar = (function () {
    // Private members and methods
    var _foo = "bar";
    
    function foo {
        ...
    }

    // Public members and methods
    return {
        getFooObjects: function () {
            ...
        }
    };
}());
```

or

``` javascript
Zotero.FooBar = {
    getFooObjects: function () {
         ...
    },
    ...
};
```

-   Private members and pseudo-private members/methods (i.e., those that are actually privileged for technical reasons but that should be considered private) should be prefixed with an underscore (e.g. `var _initialized = false;`, `Zotero.Item.prototype._loadItemData = function() {...}`)

## Comments

Functions should be commented using JSDoc syntax:

``` javascript
/**
  * Does something or other
 *
  * @param {string} value - This is a value
  * @param {boolean} [optionalValue] - This is an optional value
  * @return {number[]} - Array of itemIDs
 */
function myFunction(value, optionalValue) {
   ...
}
```

For readability and neatness, add a space after the slashes in line comments, and capitalize the first word:

Bad:

``` javascript
//this is a comment
var foo = 'bar';
```

Good:

``` javascript
// This is a comment
var foo = 'bar';
```

## Additional notes

-   Variables should be defined in the smallest scope possible:

Bad:

``` javascript
function sum(num) {
    total = 0; // total is global!
    for (i=0; i<num; i++) { // i is global!
        total += i;
    }
    return total;
}
```

Good:

``` javascript
function sum(num) {
    var total = 0;
    for (let i=0; i<num; i++) { // i is local to the for loop
        total += i;
    }
    return total;
}
```

-   Semicolons should be used at the end of lines, including after anonymous functions:

``` javascript
var func = function (bar) {
    var foo = bar;
};
```

-   Abbreviations and acronyms should remain capitalized in names: `getID()`, `generateHTML()`
-   Global constants should be placed in the `ZOTERO_CONFIG` array in zotero.js and capitalized
-   Debugging messages should use the `Zotero.debug(message, level)` function. `level` is optional and defaults to 3. Error messages (i.e. things that should never happen and that can't be handled gracefully) should be thrown rather than passed to `debug()`.
-   When throwing an error, use `throw new Error()` instead of throwing a string (which doesn't generate a stack trace)
-   All user-viewable text should be put in the en-US locale rather than embedded directly into the code, for localization and maintenance purposes.
