from flask import Flask, request, json
import os
import urllib2
from urllib import urlencode
import socket

app = Flask(__name__)
app.config['TRAP_BAD_REQUEST_ERRORS'] = True
port = 1337


@app.route('/heartbeat', methods=['POST'])
def heartbeat():
	return json.dumps({'alive':True})

@app.route('/event', methods=['POST'])
def event():
	event = request.json['event']
	if event['sound'] == 'nuts':
		path = os.path.realpath("assets/lovenuts.mp3")
		os.system("afplay "+path)
	elif event['sound'] == 'pizza':
		path = os.path.realpath("assets/pizzaaaaaaa.mp3")
		os.system("afplay "+path)
	elif event['sound'] == 'bagel':
		path = os.path.realpath("assets/pizzabagel.mp3")
		os.system("afplay "+path)
	elif event['sound'] == 'steemer':
		path = os.path.realpath("assets/steemer.mp3")
		os.system("afplay "+path)
	return 'ok'

#register client
ip = socket.gethostbyname(socket.gethostname())
data = urlencode({'ip': ip})
register = urllib2.Request("http://192.168.1.119:1337/register")
register.add_data(data)
urllib2.urlopen(register).read()
app.run(host='0.0.0.0', port=port, debug=True)