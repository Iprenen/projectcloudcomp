from celery import Celery
import urllib2
import sys
import subprocess


print "Working"
app = Celery('tasks', backend='amqp', broker='amqp://worker:worker@192.168.0.152/rabbithost')
print "Working"
@app.task
def calculate(adresses):
    print "Working"
    subprocess.call("export LC_ALL=C",shell = True)
    print "Working"
    for adress in adresses:
       # crul = 'curl -o ' + adress +  ' http://smog.uppmax.uu.se:8080/swift/v1/g6proj/' + address
       # subprocess.call(curl, shell = True)
        req = urllib2.Request("http://smog.uppmax.uu.se:8080/swift/v1/g6proj/" + adress)
        response = urllib2.urlopen(req)
        #obj = response.read()
        line = "navier_stokes_solver/airfoil 1 0.0001 10. 0.1 "
        subprocess.call([line,response], shell = True)
        print "done with calculate"



        #
    
