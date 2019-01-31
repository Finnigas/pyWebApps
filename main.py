# -*- coding: utf-8 -*-
from flask import Flask, render_template, request
import feedparser 

app = Flask(__name__)
  
# Gives the feed then parses back everything in that feed 
def fetch_rss_feed(url): 
    # https://pythonhosted.org/feedparser/common-rss-elements.html 
    rss_doc = feedparser.parse(url) 
    return rss_doc.feed, rss_doc.entries  

@app.route('/view_feed')
def view_feed():
    feed_url = request.args.get('feed-url')
    feed, entries = fetch_rss_feed(feed_url)
    return render_template('view-feed.html', feed=feed, entries=entries)
 
@app.route('/prl_feed') 
def prl_feed(): 
    feed, entries = fetch_rss_feed('http://feeds.aps.org/rss/recent/prl.xml') 
    return str(feed)
#    return render_template('index.html', feed=feed, entries=entries) 
#    return render_template('view-feed.html', feed=feed, entries=entries) 


# Where / is the root and the others are pages
@app.route('/')
def index():
    return "Hello world"

# Added another page and input information
@app.route('/whodunnit')
def detective():
    criminal = request.args.get('who')
    return criminal + ' commited the crime'

# Uses the basic.html template to style the page
@app.route('/templated-index')
def templated_index():
    thing_to_greet = 'World'
    return render_template('basic.html',
        thing_to_greet=thing_to_greet)

# Uses a nicer looking style but employing index.html (which overwrites block elements in basic.html)
@app.route('/prettyish-index')
def prettyish_index():
    return render_template('index.html')

# Created a 'calculator' function and created the calculator.html from a copy of index.html
@app.route('/add-numbers')
def add_numbers():
    a = request.args.get('a')
    b = request.args.get('b')
    ab_sum  = a + b
    return render_template('calculator.html', a=a, b=b, ab_sum=ab_sum)
