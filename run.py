#!flask/bin/python

import subprocess
import sys
import os
import json
import time
import urllib2
import sys
from flask import Flask, render_template
from flask import request, redirect
from celery import Celery
from celery import group
from calculate import calculate
from collections import Counter
from plot import plotMfile

import subprocess
import urllib2

app = Flask(__name__)

@app.route('/run', methods = ['POST'])
def run():
    sampels = request.form['sampels']
    viscosity = request.form['viscosity']
    speed = request.form['speed']
    timeVar = request.form['time']
    
    args = sampels + " " + viscosity + " " + speed + " " + timeVar
    mesh = []
    req = urllib2.Request("http://smog.uppmax.uu.se:8080/swift/v1/g6proj")
    response = urllib2.urlopen(req)
    meshObject = response.read().split()

    for t in meshObject:
        if t.endswith(".xml"):
                mesh = []
                mesh.append(t)
                calculate.(mesh,args)
   # A = mesh[:5]
   # B = mesh[5:10]
   # C = mesh[10:15]
   # D = mesh[15:20]
   # E = mesh[20:26]
   # F = mesh[26:]

    #A = mesh[:5]
    #job = group(calculate.s(A,args))
   # job = group(calculate.s(A,args), 
   #         calculate.s(B,args),
   #         calculate.s(C,args),
    #        calculate.s(D,args),
    #        calculate.s(E,args),
     #       calculate.s(F,args))

    #meshTask = job.apply_async()
    meshTask = meshObject.apply_async()
    print "Celery is working..."
    counter = 0
    while (meshTask.ready() == False):
        print "... %i s" %(counter)
        counter += 5
        time.sleep(5)
        
    results = meshTask.get()
    names = []
    print results
    for mFiles in results:
        for mFile in mFiles:
            names.append(plotMfile(mFile))
        
    
    print "The task is done!"
    #return redirect('/')
    return render_template('getData.html',name=names)

@app.route('/')
def hello_world():
    return render_template('getData.html',name='empty')

if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True)





