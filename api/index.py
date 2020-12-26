from http.server import BaseHTTPRequestHandler
from urllib import parse
import requests

class handler(BaseHTTPRequestHandler):

	def do_GET(self):
		s = self.path
		dic = dict(parse.parse_qsl(parse.urlsplit(s).query))
		self.send_response(200)
		self.send_header('Content-type','text/plain')
		self.end_headers()

		if "name" in d:
    		message = "Hello, " + dic["name"] + "!"
    	else:
    		message = "Hello, stranger!"

		self.wfile.write(message.encode())
		return