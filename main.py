import os, sys
sys.path.append('./venv/lib/python3.6/site-packages')

from flask import Flask, request
from flask_socketio import SocketIO, send
from flask_cors import CORS, cross_origin

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socket = SocketIO(app)
CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


message = 'It Works!!!!!'

@socket.on('connect')
def test_connection():
	global message
	message = request.sid
@socket.on('test')
def test_socket(data):
	global message
	message = data
	socket.emit('test', data)

@app.route('/test')
def test_http():
	return message


if(__name__ == '__main__'):
	app.threaded = True
	app.port = 8080
	socket.run(app, port=8080, debug=True)
