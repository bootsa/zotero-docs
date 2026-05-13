// Web worker: keeps the Lunr index and runs queries off the main thread so
// the page stays responsive while typing. The main thread keeps its own copy
// of the docs metadata for rendering; this worker keeps another copy for
// phrase post-filtering (small relative to the index itself).

importScripts('/support/fragments/search/lunr.js');

var index = null;
var docs = null;

self.onmessage = function (e) {
    var data = e.data;
    if (data.type === 'init') {
        docs = data.docs;
        index = lunr(function () {
            this.ref('id');
            this.field('title', { boost: 10 });
            this.field('text');
            docs.forEach(function (d, i) {
                this.add({ id: i, title: d.title, text: d.text });
            }, this);
        });
        self.postMessage({ type: 'ready' });
    } else if (data.type === 'query') {
        var rawQuery = data.query;
        var phrases = [];
        var lunrQuery = rawQuery.replace(/"([^"]+)"/g, function (_, p) {
            phrases.push(p.toLowerCase());
            return p;
        });
        var results;
        try {
            results = index.query(function (q) {
                lunrQuery.toLowerCase().split(/\s+/).forEach(function (term) {
                    if (!term) return;
                    q.term(term, { boost: 100 });
                    q.term(term, {
                        boost: 10,
                        usePipeline: false,
                        wildcard: lunr.Query.wildcard.TRAILING
                    });
                });
            });
            if (phrases.length) {
                results = results.filter(function (r) {
                    var d = docs[r.ref];
                    var hay = ((d.text || '') + ' ' + (d.title || '')).toLowerCase();
                    return phrases.every(function (p) { return hay.indexOf(p) !== -1; });
                });
            }
        } catch (err) {
            results = [];
        }
        self.postMessage({
            type: 'results',
            requestId: data.requestId,
            results: results
        });
    }
};
