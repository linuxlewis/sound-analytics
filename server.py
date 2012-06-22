from flask import Flask, request, json
import urllib2
import time
import threading

app = Flask(__name__)
port = 8080


listeners = []

@app.route('/register', methods=['POST'])
def register():
	if request.form.has_key('ip'):
		listeners.append(request.form['ip'])

@app.route('/email', methods=['POST'])
def email():
	if request.form.has_key('event'):
		event = {'event':{'name':'something', 'sound':request.form['event']['sound']}}
		send_update(event)

def check_alive():
	for listener in listeners:
		request = urllib2.Request("http://"+listener+":"+str(port)+"/heartbeat")
		try:
			urllib2.urlopen(request).read()
		except Exception as ex:
			listeners.remove(listener)

def send_update(event):
	for listener in listeners:
		request = urllib2.Request("http://"+listener+":"+str(port)+"/event")
		request.add_data(event)
		try:
			urllib2.urlopen(request).read()
		except Exception as ex:
			print ex

class Timer(threading.Thread):
	def __init__(self, seconds):
	 	self.runTime = seconds
 		threading.Thread.__init__(self)
 	def run(self):
	 	time.sleep(self.runTime)
		check_alive()
		self.run()

Timer(60*5)
app.run(port=port)


