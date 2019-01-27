from flask import request

@app.route('/view-feed')
def view_feed():
    rss_url = request.args.get('rss_url')
    feed, entries = fetch_rss_feed(rss_url)
    return render_template('view-feed.html', feed=feed, entries=entries)
