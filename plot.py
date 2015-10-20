from flask import Flask, render_template, send_file
from flask import request, redirect
from celery import Celery, group
import os
import subprocess
import matplotlib
import numpy as np



def plotMfile(o):
    obj = o[0]
    task_name=o[1]
    print "task name: " + task_name
    tmp = obj.split()
    print "temp is: " + tmp
    tmp.pop(0)
  
    l1 = tmp[::3]
    l2=tmp[1::3]
    l3=tmp[2::3]
    print l1.pop(0) #+ str(l1.pop(0))
    print l2.pop(0) #+ str(l2.pop(0))
    print l3.pop(0) #+ str(l3.pop(0))
    a=np.array(l2, dtype=np.float)
    b=np.array(l3, dtype=np.float)
    c = a/b
    d= np.array(l1, dtype = np.float)
    pic_name = "air"+task_name + ".png"
    image = open("static/"+pic_name,'w')
    plot(image, d, a, b, 'r--')
    image.close

def plot(image, x, y, z, c):
	a = pyplot.figure()
	a.suptitle("Lift and Drag forces over time", fontsize=16)
	ax1 = a.add_subplot(211)
	ax1.set_title("Lift Force")
	ax1.plot(x, y, c)
	ax2 = a.add_subplot(212)
	ax2.set_title("Drag Force")
	ax2.plot(x, z, c)
	a.savefig(image, format='png')
