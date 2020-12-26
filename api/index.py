from http.server import BaseHTTPRequestHandler

class handler(BaseHTTPRequestHandler):

	def do_GET(self):
		s = self.path
		name = parse_qs(urlparse(s).query)['name'][0]
		self.send_response(200)
		self.send_header('Content-type','text/plain')
		self.end_headers()
		message = "Hello " + name
		self.wfile.write(message.encode())
		return