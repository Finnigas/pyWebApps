import feedparser

def fetch_rss_feed(url):
    # https://pythonhosted.org/feedparser/common-rss-elements.html
    rss_doc = feedparser.parse(url)
    return rss_doc.feed, rss_doc.entries


@app.route('/prl_feed')
def prl_feed():
    feed, entries = fetch_rss_feed('http://feeds.aps.org/rss/recent/prl.xml')
    return render_template('view-feed.html', feed=feed, entries=entries)
