#!/usr/bin/python
# -*- coding: utf-8 -*-

from google.appengine.ext import ndb

class RSSFeed(ndb.Model):
    name = ndb.StringProperty(default="")
    url  = ndb.StringProperty(default="")

    created = ndb.DateTimeProperty(auto_now_add=True)
