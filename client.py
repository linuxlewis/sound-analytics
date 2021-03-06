from flask import Flask, request, json
import os
import urllib2
from urllib import urlencode
import socket

app = Flask(__name__)
app.config['TRAP_BAD_REQUEST_ERRORS'] = True
port = 1337


@app.route('/heartbeat', methods=['GET','POST'])
def heartbeat():
	return json.dumps({'alive':True})

@app.route('/event', methods=['POST'])
def event():
	sound = request.values['sound']
	print sound
	if sound == 'nuts':
		path = os.path.realpath("assets/lovenuts.mp3")
		os.system("afplay " + path)
	elif sound == 'pizza':
		path = os.path.realpath("assets/pizzaaaaaaaa.mp3")
		os.system("afplay " + path)
	elif sound == 'bagel':
		path = os.path.realpath("assets/pizzabagel.mp3")
		os.system("afplay "+path)
	elif sound == 'steemer':
		path = os.path.realpath("assets/steemer.mp3")
		os.system("afplay "+path)
	return 'ok'

#register client
ip = socket.gethostbyname(socket.gethostname())
data = urlencode({'ip': ip})
register = urllib2.Request("http://10.4.20.54:1337/register")
register.add_data(data)
urllib2.urlopen(register).read()
app.run(host='0.0.0.0', port=port, debug=True)
