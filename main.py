import os, sys, requests
#sys.path.append('./venv/lib/python3.6/site-packages')

from flask import Flask, request
from flask_cors import CORS, cross_origin

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


message = 'It Works!!!!!'

#rota de registro do webhook
@app.route('/', methods=['GET'])
def verify():
	#verifica se está tentando cadastrar o bot na API
	if request.args.get("hub.mode") == "subscribe" and request.args.get("hub.challenge"):
	#verifica se o token usado no webhook é o mesmo do programa
		if not request.args.get("hub.verify_token") == "RandomTestToken":
			return "Verification token mismatch", 403
		return request.args["hub.challenge"], 200
	return "OK", 200

#Rota de recebimento de mensagens
@app.route('/', methods=['POST'])
def webhook():
	global message
	#Pegas os dados do request em formato Json
	data = request.get_json()
	#print(data)
	try:
		req = requests.post("http://34.95.151.238/chat/", json=data)
		#print(req.status_code)
		#print(req.json())
	except Exception as e:
		message = e

	return "OK", 200

@app.route('/test')
def test_http():
	global message
	return message


if(__name__ == '__main__'):
	app.threaded = True
	app.port = 5000
	app.run(host="0.0.0.0", debug=True)
