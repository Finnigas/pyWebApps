# Web Apps course
Started with the main.py function and edited it a little.

Introduced a second page which used the request function to handle inputted information from the web address. 
E.g. in main.py takes in the value of the parameter who which is set in the web address following the ‘?’ symbol.
```
@app.route(‘/whodunnit’)
def detective():
    criminal = request.args.get(‘who’)
    return criminal + ‘ committed the crime’
```
On the page: http://localhost:8080/whodunnit?who=Mustard
You should see:
![](WebAppsCourse1/Screenshot%202019-01-30%20at%2023.41.11.png)


We then looked at templates, used to style the page. They use a templating language which here is jinja, with a lot of the syntax using { }.
We ran the templated index example using basic.html (in the templates directory)
```
@app.route(‘/templated-index’)
def templated_index():
    thing_to_greet = ‘World’
    return render_template(‘basic.html’,
        thing_to_greet=thing_to_greet) 
```
Where you can have a play with the things to greet text or edit the basic.html to change the ‘more text can be added here line’
basic.html shows the actual formatting for the whole page which you can do.
Another way rather than formatting the whole thing in the file is to use a base.html with the base format in and block elements in it which can be edited. We ran the next templating example: prettyish-index, to demonstrate this.:
```
@app.route(‘/prettyish-index’)
def prettyish_index():
    return render_template(‘index.html’)
```
The render template called here is the index.html which just extends the base.html and edits the block elements within it.

Next we edited the template ourselves and created a calculator function, setting multiple parameters (a and b).
Copy index.html as calculator.html and edit it to change the title and the block content.
calculator.html:
```
{% extends “base.html” %}
  
{# Overwrite “blocks" defined in the base template. This saves typing if you have lots of similar pages and ensure that pages look consistent #}
{% block title %}
    Calculator page
{% endblock %}

{% block content %}
    The sum of {{ a }} plus {{ b }} is {{ ab_sum }}
{% endblock %}
```

Add the calculator ‘function’ in main.py:
```
@app.route(‘/add-numbers’)
def add_numbers():
    a = request.args.get(‘a’)
    b = request.args.get(‘b’)
    ab_sum  = a + b
    return render_template(‘calculator.html’, a=a, b=b, ab_sum=ab_sum)
```
The render template now calls our new template: calculator.html

For the address: [Calculator page](http://localhost:8080/add-numbers?a=3&b=9). This page now also has a name from the calculator.html which shows at the top of the tab.
You should see:
![](WebAppsCourse1/Screenshot%202019-01-30%20at%2023.56.24.png)
Which is some pretty rad maths.

We then looked at pulling an RSS feed. The RSS feed is parsed in by the first function in main.py and the parser creates a feed object. Entries in the RSS feed such as ‘title’ or ‘link’ are attributes of the feed object and can be called.

Copy the view-feed.html from templates/snippets to templates or call the full path in main.py. view-feed.html has more templating examples ( <a> is a link and <hr> is hard rule). It again extends the base template and edits the block elements. 

We ran the /prl_feed example first. Use one of the three return commands and see the difference in the information displayed on the page.
```
@app.route(‘/prl_feed’)
def prl_feed():
    feed, entries = fetch_rss_feed(‘http://feeds.aps.org/rss/recent/prl.xml’)
    return str(feed)
#    return render_template(‘index.html’, feed=feed, entries=entries)
#    return render_template(‘view-feed.html’, feed=feed, entries=entries)
```

Finally, created a way to enter any RSS feed as a parameter and be able to view that feed.
```
@app.route(‘/view_feed’)
def view_feed():
    feed_url = request.args.get(‘feed-url’)
    feed, entries = fetch_rss_feed(feed_url)
    return render_template(‘view-feed.html’, feed=feed, entries=entries)
```
For example for the address:
[RSC - Phys. Chem. Chem. Phys. latest articles feed](http://localhost:8080/view_feed?feed-url=http://feeds.rsc.org/rss/cp.xml)
You will see some interesting (or boring) articles from the journal who’s identity crisis I can link with.

