(function() {
    if (window.myBookmarklet !== undefined) {
        myBookmarklet();
    } else {
        document.body.appendChild(document.createElement('script')).src = '/static/js/bookmarklet.js?r=' + Math.floor(Math.random() * 9999999999999999);
    }
})();