from celery import Celery

app = Celery('tasks', backend='amqp', broker='amqp://worker:worker@192.168.0.152/rabbithost')

@app.calculate
def calculate(adresses):
    for adress in adresses:
        req = urllib2.Request("http://smog.uppmax.uu.se:8080/swift/v1/g6proj/" + adress)
        response = urllib2.urlopen(req)
        obj = response.read()
        
        line = "sudo ./airfoil 1 0.0001 10. 0.1"
        subprocess.call(line, obj)


