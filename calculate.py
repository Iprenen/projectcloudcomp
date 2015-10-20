from celery import Celery
import urllib2
import sys
import subprocess



app = Celery('tasks', backend='amqp', broker='amqp://worker:worker@192.168.0.53/rabbithost')

@app.task
def calculate(adresses,args):
    print "started"
 
    print "started with:"
    for adress in adresses:
        print adress
        curl = "curl -o " + adress +  " http://smog.uppmax.uu.se:8080/swift/v1/g6proj/" + adress
        subprocess.call(curl, shell = True)
        line = "navier_stokes_solver/airfoil " + args + " " + adress
        print "line to run " + line 

        subprocess.call(line, shell = True)
        subprocess.call("rm " + adress, shell = True)
        print "done with calculate"
        toReturn = open("results/drag_ligt.m", 'r').read()
        return toReturn



        
    
