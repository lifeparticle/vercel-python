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

		if "name" in dic:
			message = "Hello, " + dic["name"] + "!"
		else:
			message = "Hello, stranger!"

		
		

		message = 'USDT / UAH';
		message += '
		'
		print('USDT / UAH');
		print('');

		#Binance

		response = requests.get("https://api.binance.com/api/v3/ticker/price?symbol=USDTUAH")
		#print(response.status_code)
		#print(response.json())

		binance_price = response.json()['price']
		print('Binance: ' + "%.2f" % float(binance_price) + ' грн')

		#Huobi

		response = requests.get("https://api.huobi.pro/market/detail/merged?symbol=usdtuah")

		huobi_price_close = response.json()['tick']['close']
		huobi_price_bid = response.json()['tick']['bid']
		huobi_price_ask = response.json()['tick']['ask']

		print('');
		print('Huobi close закриття: ' + "%.2f" % float(huobi_price_close) + ' грн')
		print('Huobi bid купівля: ' + "%.2f" % float(huobi_price_bid[0]) + ' грн')
		print('Huobi ask продаж: ' + "%.2f" % float(huobi_price_ask[0]) + ' грн')

		#KUNA

		response = requests.get("https://api.kuna.io//v3/tickers?symbols=usdtuah")
		kuna = response.json()

		print('');
		print('KUNA close: ' + "%.2f" % float(kuna[0][7]) + ' грн')
		print('KUNA bid: ' + "%.2f" % float(kuna[0][1]) + ' грн')
		print('KUNA ask: ' + "%.2f" % float(kuna[0][3]) + ' грн')




		self.wfile.write(message.encode())




		return
