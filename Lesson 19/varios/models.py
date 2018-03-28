from google.appengine.ext import ndb

class Message(ndb.Model):
    message_text = ndb.StringProperty()
    author = ndb.StringProperty()
    city = ndb.StringProperty()