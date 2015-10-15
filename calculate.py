from celery import Celery
import urllib2
import sys
import subprocess

app = Celery('tasks', backend='amqp', broker='amqp://worker:worker@192.168.0.152/rabbithost')

@app.task
def calculate():
   # for adress in adresses:
adress = 'r2a9n200.msh.xml'
req = urllib2.Request("http://smog.uppmax.uu.se:8080/swift/v1/g6proj/" + adress)
response = urllib2.urlopen(req)
obj = response.read()

line = "sudo navier_stokes_solver/airfoil 1 0.0001 10. 0.1"
subprocess.call(line, obj)



