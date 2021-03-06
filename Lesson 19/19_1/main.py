#!/usr/bin/env python
import os
import jinja2
import webapp2
from models import Message

template_dir = os.path.join(os.path.dirname(__file__), "templates")
jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir), autoescape=False)


class BaseHandler(webapp2.RequestHandler):

    def write(self, *a, **kw):
        return self.response.out.write(*a, **kw)

    def render_str(self, template, **params):
        t = jinja_env.get_template(template)
        return t.render(params)

    def render(self, template, **kw):
        return self.write(self.render_str(template, **kw))

    def render_template(self, view_filename, params=None):
        if params is None:
            params = {}
        template = jinja_env.get_template(view_filename)
        return self.response.out.write(template.render(params))


class MainHandler(BaseHandler):
    def get(self):
        return self.render_template("index.html")

class Libro_VisitasHandler(BaseHandler):
    def get(self):
        messages = Message.query().fetch()
        params = {"messages": messages}
        return self.render_template("libro_visitas.html", params=params)

class DatosHandler(BaseHandler):
    def post(self):
        nombre = self.request.get("nombre")
        if not nombre:
            nombre = "Anonimo"
        email = self.request.get("email")
        message = self.request.get("message")

        msg = Message(nombre=nombre, email=email, message=message)
        msg.put()

        return self.redirect_to("book")

class DetallesHandler(BaseHandler):
    def get(self, message_id):
        message = Message.get_by_id(int(message_id))
        params = {"message": message}
        return self.render_template("detalles.html", params=params)

app = webapp2.WSGIApplication([
    webapp2.Route('/', MainHandler),
    webapp2.Route('/datos', DatosHandler),
    webapp2.Route('/libro_visitas', Libro_VisitasHandler, name="book"),
    webapp2.Route('/message/<message_id:\d+>', DetallesHandler),
], debug=True)
