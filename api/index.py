from http.server import BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs
import requests

class handler(BaseHTTPRequestHandler):

	def do_GET(self):
		s = self.path
		dic = dict(parse.parse_qsl(parse.urlsplit(s).query))
		self.send_response(200)
		self.send_header('Content-type','text/plain')
		self.end_headers()
		message = "Hello " + dic
		self.wfile.write(s.encode())
		return