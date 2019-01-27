from models import RSSFeed

@app.route('/new-feed')
def new_feed():
    if request.method == 'GET':
        return render_template('new-feed.html')
    elif request.method == 'POST':
        new_feed = RSSFeed()
        new_feed.name = request.form.get('name')
        new_feed.url = request.form.get('url')
        new_feedg.put()
        return redirect(url_for('stored_feeds'))


# Check out localhost:8000 -> View Data store
