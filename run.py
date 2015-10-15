#!flask/bin/python

import subprocess
import sys
import os
import swiftclient.client
import json
import time
import urllib2
import sys
sys.path.append("/navier_stokes_solver")
from celery import Celery
from celery import group
from calculate import calculate
from collections import Counter

import subprocess
import urllib2

mesh = []
req = urllib2.Request("http://smog.uppmax.uu.se:8080/swift/v1/g6proj")
response = urllib2.urlopen(req)
meshObject = response.read().split()

for t in meshObject:
    mesh.append(t)

A = mesh[:5]
B = mesh[5:10]
C = mesh[10:15]
D = mesh[15:20]
E = mesh[20:26]
F = mesh[26:]

job = group(calculate.s(A), 
            calculate.s(B),
            calculate.s(C),
            calculate.s(D),
            calculate.s(E),
            calculate.s(F))

meshTask = job.apply_async()
print "Celery is working..."
counter = 0
while (meshTask.ready() == False):
    print "... %i s" %(counter)
    counter += 5
    time.sleep(5)

print "The task is done!"



