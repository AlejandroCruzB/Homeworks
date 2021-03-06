from google.appengine.ext import ndb

class Message(ndb.Model):
    nombre = ndb.StringProperty()
    email = ndb.StringProperty()
    message = ndb.TextProperty()
    created = ndb.DateTimeProperty(auto_now_add=True)
