import webapp2
import json

# api_key = "CHOOSE-A-RANDOM-KEY-AND-PLACE-IT-HERE"
api_key = "1234"

def api_key_required(handler):
    def check_api_key(self, *args, **kwargs):
        if self.request.get("api_key") == api_key:
            return handler(self, *args, **kwargs)
        else:
            self.render_error("The API key is invalid or missing.")
    return check_api_key


class APIHandler(webapp2.RequestHandler):
    def render_json(self, response):
        self.response.headers['Content-Type'] = 'application/json'
        self.response.write(json.dumps(response))

    def render_error(self, error_description):
        self.render_json({"error": True, "error_type": "Service API Exception", "error_description": error_description})
