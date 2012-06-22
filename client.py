from flask import Flask, request, json
import os
import urllib2
from urllib import urlencode
import socket

app = Flask(__name__)
port = 1337


@app.route('/heartbeat', methods=['POST'])
def heartbeat():
	return json.dumps({'alive':True})

@app.route('/event', methods=['POST'])
def event():
	print request.form['event']
	if request.form['event']['sound'] == 'nuts':
		os.system("afplay ./assets/lovenuts.mp3")
	elif request.form['event']['sound'] == 'pizza':
		os.system("afplay ./assets/pizzaaaaaaa.mp3")
	elif request.form['event']['sound'] == 'bagel':
		os.system("afplay ./assets/pizzabagel.mp3")
	elif request.form['event']['sound'] == 'steemer':
		os.system("afplay ./assets/steemer.mp3")

	return 'ok'

#register client
ip = socket.gethostbyname(socket.gethostname())
data = urlencode({'ip': ip})
register = urllib2.Request("http://192.168.1.119:1337/register")
register.add_data(data)
urllib2.urlopen(register).read()
app.run(port=port)