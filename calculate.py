from celery import Celery
import urllib2
import sys
import subprocess



app = Celery('tasks', backend='amqp', broker='amqp://worker:worker@192.168.0.152/rabbithost')

@app.task
def calculate(adresses,args):
    print "started"
    subprocess.call("export LC_ALL=C",shell = True)
    print "started with:"
    for adress in adresses:
        print adress
        curl = "curl -o " + adress +  " http://smog.uppmax.uu.se:8080/swift/v1/g6proj/" + adress
        subprocess.call(curl, shell = True)
        #req = urllib2.Request("http://smog.uppmax.uu.se:8080/swift/v1/g6proj/" + adress)
        #response = urllib2.urlopen(req)
        #obj = response.read()
        line = "navier_stokes_solver/airfoil " + args + " " + adress
        subprocess.call(line, shell = True)
        print "done with calculate"



        #
    
