from http.server import BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs
import requests

class handler(BaseHTTPRequestHandler):

	def do_GET(self):
		# s = self.path
		# name = parse_qs(urlparse(s).query)['name'][0]
		self.send_response(200)
		self.send_header('Content-type','text/plain')
		self.end_headers()
		# message = "Hello " + name
		s = self.request.GET.get('name')

		self.wfile.write(s.encode())
		return