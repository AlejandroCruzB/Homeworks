from google.appengine.ext import ndb

class Email(ndb.Model):
    remitente = ndb.StringProperty()
    destinatario = ndb.StringProperty()
    asunto = ndb.TextProperty()
    message = ndb.TextProperty()
    created = ndb.DateTimeProperty(auto_now_add=True)
    deleted = ndb.BooleanProperty(default=False)
