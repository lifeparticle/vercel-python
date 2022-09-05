from http.server import BaseHTTPRequestHandler
from urllib import parse

class handler(BaseHTTPRequestHandler):

	def do_GET(self):
		s = self.path
		dic = dict(parse.parse_qsl(parse.urlsplit(s).query))
		self.send_response(200)
		self.send_header('Content-type','text/plain')
		self.end_headers()

		if "name" in dic:
			message = "Добрий день, " + dic["name"] + "!"
		else:
			message = "Добрий день, stranger!"

		self.wfile.write(message.encode())
		return
