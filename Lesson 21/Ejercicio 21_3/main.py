#!/usr/bin/env python
import os
import jinja2
import webapp2
from models import Message
import time

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

class ListadoHandler(BaseHandler):
    def get(self):
        titulo = Message.query().fetch()
        params = {"titulo": titulo}
        return self.render_template("listado.html", params=params)

class DatosHandler(BaseHandler):
    def post(self):
        titulo = self.request.get("titulo")
        valoracion = int(self.request.get("valoracion"))
        imagen = self.request.get("imagen")
        if "<script>" in imagen:
            return self.write("No Hack")

        msg = Message(titulo=titulo, valoracion=valoracion, imagen=imagen)
        msg.put()
        time.sleep(0.1)
        return self.redirect_to("book")

class DetallesHandler(BaseHandler):
    def get(self, titulo_id):
        titulo = Message.get_by_id(int(titulo_id))
        params = {"titulo": titulo}
        return self.render_template("detalles.html", params=params)

class EditHandler(BaseHandler):
    def get(self, titulo_id):
        titulo = Message.get_by_id(int(titulo_id))
        params = {"titulo": titulo}
        return self.render_template("edit.html", params=params)

    def post(self, titulo_id):
        nuevo_titulo = self.request.get("titulo")
        nueva_valoracion = int(self.request.get("valoracion"))
        nueva_imagen = self.request.get("imagen")
        titulo = Message.get_by_id(int(titulo_id))
        titulo.titulo = nuevo_titulo
        titulo.valoracion = nueva_valoracion
        titulo.imagen = nueva_imagen
        titulo.put()
        time.sleep(0.1)
        return self.redirect_to("book")

class DeleteHandler(BaseHandler):
    def get(self, titulo_id):
        titulo = Message.get_by_id(int(titulo_id))
        params = {"titulo": titulo}
        return self.render_template("delete.html", params=params)

    def post(self, titulo_id):
        titulo = Message.get_by_id(int(titulo_id))
        titulo.key.delete()
        time.sleep(0.1)
        return self.redirect_to("book")


app = webapp2.WSGIApplication([
    webapp2.Route('/', MainHandler),
    webapp2.Route('/datos', DatosHandler),
    webapp2.Route('/listado', ListadoHandler, name="book"),
    webapp2.Route('/titulo/<titulo_id:\d+>', DetallesHandler),
    webapp2.Route('/titulo/<titulo_id:\d+>/edit', EditHandler),
    webapp2.Route('/titulo/<titulo_id:\d+>/delete', DeleteHandler),

], debug=True)
