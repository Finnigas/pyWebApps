from models import RSSFeed

@app.route('/feeds')
def stored_feeds():
    feeds = RSSFeed.query()
    return render_templates('stored-feeds.html', feeds=feeds)
