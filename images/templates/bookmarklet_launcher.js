(function() {
    if (window.myBookmarklet !== undefined) {
        myBookmarklet();
    } else {
        document.body.appendChild(document.createElement('script')).src = 'social-photo-bookmarking.herokuapp.com/static/js/bookmarklet.js?r=' + Math.floor(Math.random() * 9999999999999999);
    }
})();