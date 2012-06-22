from flask import Flask, request, json
import urllib2
import time
from threading import Timer

app = Flask(__name__)
port = 8080


listeners = []

@app.route('/register', methods=['POST'])
def register():
	if request.form['ip'] not in listeners:
		listeners.append(request.form['ip'])
	return 'ok'

@app.route('/email', methods=['POST'])
def email():
	if request.json['event']:
		event = {'event':{'name':'something', 'sound':request.json['event']['sound']}}
		send_update(json.dumps(event))
		return 'ok'

def check_alive():
	while True:
		print '**** CHECKING ALIVE ****'
		for listener in listeners:
			request = urllib2.Request("http://"+listener+":"+str(port)+"/heartbeat")
			print request.get_full_url()
			try:
				urllib2.urlopen(request).read()
			except Exception as ex:
				listeners.remove(listener)
		time.sleep(60*3)

def send_update(event):
	print '**** SENDING UPDATE ****'
	for listener in listeners:
		request = urllib2.Request("http://"+listener+":"+str(port)+"/event", {'Content-Type':'application/json'})
		request.add_data(event)
		print request.get_full_url()
		try:
			urllib2.urlopen(request).read()
		except Exception as ex:
			print ex

Timer(2,check_alive).start()
app.run(host='0.0.0.0', port=port, debug=True)


