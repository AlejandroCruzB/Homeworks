#!/usr/bin/env python
import os
import jinja2
import webapp2


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
        return self.render_template("hello.html")
    def post(self):
        result = self.request.get("some_text")
        return self.render_template("hello.html")

   # def post(self):
    #    our_string = "User entered this text: "
     #   result = self.request.get("some_text")
      #  join_strings = our_string + result  # we join the two strings together
       # return self.write(join_strings)

#-class ResultHandler(BaseHandler):
  #-  def post(self):
    #-    result = self.request.get("some_text")
        #return self.render_template("hello.html") #una vez que se hace el imput te devuelve la pagina hello.html (para eso se pone en la otra clase como hemos hecho)
      #-  return self.write(result)

app = webapp2.WSGIApplication([
    webapp2.Route('/', MainHandler),
], debug=True)
