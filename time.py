import time
import jinja2
import webapp2

class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.header['Content-Type'] = 'text/plain'

        printTime = "The current time is {{ timeobj.strftime('%H:%M') }}"
        jinjaOutput = jinja2.Template(output)

        self.response.write(jinjaOutput.render(timeobj = time))

app = webapp2.WSGIApplication([
    ('/', MainPage),
], debug = True)
