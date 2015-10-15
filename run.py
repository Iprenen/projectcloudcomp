#!flask/bin/python

import subprocess
import sys
import os
import swiftclient.client
import json
import time
import urllib2
sys.path.append('/navier_stokes_solver')
from celery import Celery
from celery import group
from tasks import wordcount
from flask import Flask, jsonify
from collections import Counter

import subprocess
import urkkib2
response = urllib2.urlopen()
#file = response.read()

line = "run.sh " + str(response)

subprocess.call(line)


toReturn = tweetTask.get()

mesh = []
req = urllib2.Request("http://smog.uppmax.uu.se:8080/swift/v1/g6proj")
response = urllib2.urlopen(req)
meshObject = response.read().split()

for t in meshObject:
    mesh.append(t)

A = mesh[:4]
B = mesh[4:8]
C = mesh[8:12]
D = mesh[12:16]
E = mesh[16:]

job = group(calculate.s(A), 
            calculate.s(B), 
            calculate.s(C),
            calculate.s(D),
            calculate.s(E))

tweetTask = job.apply_async()
print "Celery is working..."
counter = 0
while (tweetTask.ready() == False):
    print "... %i s" %(counter)
    counter += 5
    time.sleep(5)
print "The task is done!

'''

#!flask/bin/python

from celery import Celery
from celery import group
from tasks import wordcount
from flask import Flask, jsonify
import subprocess
import sys
import os
import swiftclient.client
import json
import time
import urllib2
from collections import Counter

app = Flask(__name__)

@app.route('/run', methods=['GET'])
def cow_say():
	tweetTask = job.apply_async()
	print "Celery is working..."
	counter = 0
	while (tweetTask.ready() == False):
		print "... %i s" %(counter)
		counter += 5
		time.sleep(5)
	print "The task is done!"

	toReturn = tweetTask.get()

	tweets = []
	req = urllib2.Request("http://smog.uppmax.uu.se:8080/swift/v1/tweets")
	response = urllib2.urlopen(req)
	tweetsObject = response.read().split()
	for t in tweetsObject:
		tweets.append(t)

	A = tweets[:4]
	B = tweets[4:8]
	C = tweets[8:12]
	D = tweets[12:16]
	E = tweets[16:]

	job = group(calculate.s(A), 
		calculate.s(B), 
		calculate.s(C),
		calculate.s(D),
		calculate.s(E))

	c = Counter()
	for d in toReturn:
		c.update(d)

	return jsonify(dict(c)), 200

if __name__ == '__main__':
	app.run(host='0.0.0.0',debug=True)

 '''
