from google.appengine.ext import ndb

class Message(ndb.Model):
    titulo = ndb.StringProperty()
    valoracion = ndb.IntegerProperty()
    imagen = ndb.TextProperty()
    created = ndb.DateTimeProperty(auto_now_add=True)
