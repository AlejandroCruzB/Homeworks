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
        return self.render_template("hello.html")

    def post(self):
        result_m = self.request.get("some_text")
        author = self.request.get("author")
        city = self.request.get("city")



        msg = Message(message_text=result_m, author=author, city=city)
        msg.put()

        params = {"result": result_m, "author": author, "city": city}
        return self.render_template("result.html", params=params) #para que el mensaje aparezca en una plantilla
        #return self.write(result) > imprime el resultado

class MessageListHandler(BaseHandler):
    def get(self):
        messages = Message.query().fetch()
        params = {"messages": messages}
        return self.render_template("messages_list.html", params=params)

app = webapp2.WSGIApplication([
    webapp2.Route('/', MainHandler),
    webapp2.Route('/list', MessageListHandler),

], debug=True)
