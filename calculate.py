from celery import Celery
import urllib2
import sys
import subprocess



app = Celery('tasks', backend='amqp', broker='amqp://worker:worker@192.168.0.105/rabbithost')

@app.task
def calculate(adresses,args):
    print "started"
    subprocess.call("export LC_ALL=C",shell = True)
    print "started with:"
    result = []
    for adress in adresses:
        print adress
        curl = "sudo curl -o " + adress +  " http://smog.uppmax.uu.se:8080/swift/v1/g6proj/" + adress
       subprocess.call(curl, shell = True)
        line = "sudo navier_stokes_solver/airfoil " + args + " " + adress
        print "line to run " + line 
        subprocess.call("export LC_ALL=en_US.UTF-8",shell = True)
        subprocess.call(line, shell = True)
        subprocess.call("sudo rm " + adress, shell = True)
        print "done with calculate"


        #not thread safe....
        file = open("results/drag_ligt.m", 'r').read()
        result.append((file, adress))
     
    return result




    
