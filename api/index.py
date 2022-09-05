from http.server import BaseHTTPRequestHandler
from urllib import parse
import requests
from datetime import datetime
import pytz

class handler(BaseHTTPRequestHandler):

	def do_GET(self):
		s = self.path
		dic = dict(parse.parse_qsl(parse.urlsplit(s).query))
		self.send_response(200)
		self.send_header('Content-type','text/html; charset=UTF-8')
		self.end_headers()

		if "name" in dic:
			message = "Hello, " + dic["name"] + "!"
		else:
			message = "Hello, stranger!"

		
		

		#self.wfile.write(bytes("<html><head><link href=\'https://fonts.googleapis.com/css?family=Raleway\' rel=\'stylesheet\'><style> body {  font-family: Raleway;font-size: 22px;		}		</style><title>USDT - UAH conversion</title></head><body>","utf-8"))
		self.wfile.write(bytes("<html><head><style> body {  font-family: Arial;font-size: 22px; }</style><title>USDT - UAH conversion</title></head><body>","utf-8"))
		
		self.wfile.write(bytes("<p>USDT / UAH</p>","utf-8"))
		print('USDT / UAH');
		print('');

		#Binance

		response = requests.get("https://api.binance.com/api/v3/ticker/price?symbol=USDTUAH")
		#print(response.status_code)
		#print(response.json())

		binance_price = response.json()['price']
		print('Binance: ' + "%.2f" % float(binance_price) + ' грн')
		self.wfile.write(bytes("<p>Binance: " + "%.2f" % float(binance_price) + " грн</p>","utf-8"))

		#Huobi

		response = requests.get("https://api.huobi.pro/market/detail/merged?symbol=usdtuah")

		huobi_price_close = response.json()['tick']['close']
		huobi_price_bid = response.json()['tick']['bid']
		huobi_price_ask = response.json()['tick']['ask']

		print('');
		print('Huobi close закриття: ' + "%.2f" % float(huobi_price_close) + ' грн')
		print('Huobi bid купівля: ' + "%.2f" % float(huobi_price_bid[0]) + ' грн')
		print('Huobi ask продаж: ' + "%.2f" % float(huobi_price_ask[0]) + ' грн')
		self.wfile.write(bytes("<p>Huobi close: " + "%.2f" % float(huobi_price_close) + " uah</p>","utf-8"))
		self.wfile.write(bytes("<p>Huobi bid: " + "%.2f" % float(huobi_price_bid[0]) + " uah</p>","utf-8"))
		self.wfile.write(bytes("<p>Huobi ask: " + "%.2f" % float(huobi_price_ask[0]) + " uah</p>","utf-8"))


		#KUNA

		response = requests.get("https://api.kuna.io//v3/tickers?symbols=usdtuah")
		kuna = response.json()

		print('');
		print('KUNA close: ' + "%.2f" % float(kuna[0][7]) + ' грн')
		print('KUNA bid: ' + "%.2f" % float(kuna[0][1]) + ' грн')
		print('KUNA ask: ' + "%.2f" % float(kuna[0][3]) + ' грн')
		self.wfile.write(bytes("<p>KUNA close: " + "%.2f" % float(kuna[0][7]) + " uah</p>","utf-8"))
		self.wfile.write(bytes("<p>KUNA bid: " + "%.2f" % float(kuna[0][1]) + " uah</p>","utf-8"))
		self.wfile.write(bytes("<p>KUNA ask: " + "%.2f" % float(kuna[0][3]) + " uah</p>","utf-8"))



		now = datetime.now()
		
		tz_Kyiv = pytz.timezone('Europe/Kiev')
		datetime_Kyiv = datetime.now(tz_Kyiv)
		print("Kyiv time: ", datetime_Kyiv.strftime("%H:%M:%S"))

		self.wfile.write(bytes("<p>Kyiv Time: " + datetime_Kyiv.strftime("%H:%M:%S") + "</p>","utf-8"))
		
		self.wfile.write(bytes("</body></html>","utf-8"))

		#self.wfile.write(message.encode())



		return
