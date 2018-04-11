#!/usr/bin/env python
import os
import jinja2
import webapp2
import time  #time.sleep(0.1)
from models import Email
from google.appengine.api import users
import json
from google.appengine.api import urlfetch


template_dir = os.path.join(os.path.dirname(__file__), "templates")
jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir), autoescape=False)

def emailFilter(atr_name, value, email_list):
    for x in email_list:
        if x.atr_name != value:
            email_list.remove(x)
    return email_list


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

        user = users.get_current_user()
        params["user"] = user

        if user:
            logged_in = True
            logout_url = users.create_logout_url('/')
            params["logout_url"] = logout_url
        else:
            logged_in = False
            login_url = users.create_login_url('/')
            params["login_url"] = login_url

        params["logged_in"] = logged_in

        template = jinja_env.get_template(view_filename)
        return self.response.out.write(template.render(params))


class MainHandler(BaseHandler):
    def get(self):
        user = users.get_current_user()
        if user:
            self.redirect_to("inbox")
        else:
            return self.render_template("login.html")

class InboxHandler(BaseHandler):
    def get(self):
        user = users.get_current_user()
        emails = Email.query(Email.destinatario == user.email()).fetch()

        params = {"emails": emails, "user": user, "inbox": "recibidos"}
        self.render_template("inbox.html", params = params)

class SendboxHandler(BaseHandler):
    def get(self):
        user = users.get_current_user()
        emails = Email.query(Email.remitente == user.email()).fetch()

        params = {"emails": emails, "user": user, "inbox": "enviados"}
        self.render_template("inbox.html", params = params)

class SendHandler(BaseHandler):
    def get(self):
        return self.render_template("send.html")

    def post(self):
        remitente = users.get_current_user().email()
        destinatario = self.request.get("destinatario")
        asunto = self.request.get("asunto")
        message = self.request.get("message")

        email = Email(remitente = remitente, destinatario = destinatario, asunto = asunto, message = message)
        email.put()

        return self.render_template("mensaje_enviado.html")


class DetailsHandler(BaseHandler):
    def get(self, email_id):
        user = users.get_current_user()
        email = Email.get_by_id(int(email_id))

        params = {"email": email, "user": user}
        self.render_template("details.html", params = params)

class WeatherHandler(BaseHandler):
    def get(self):
        url = "http://api.openweathermap.org/data/2.5/weather?q=Malaga,es&units=metric&appid=00ddcb395e864919626ee170cece03a2"
        result = urlfetch.fetch(url)
        weather_info = json.loads(result.content)
        params = {"weather_info": weather_info}
        return self.render_template("weather.html", params = params)



app = webapp2.WSGIApplication([
    webapp2.Route('/', MainHandler),
    webapp2.Route('/inbox', InboxHandler, name = "inbox"),
    webapp2.Route('/sendbox', SendboxHandler),
    webapp2.Route('/send', SendHandler),
    webapp2.Route('/emails/<email_id:\d+>', DetailsHandler),
    webapp2.Route('/weather', WeatherHandler),
], debug=True)
