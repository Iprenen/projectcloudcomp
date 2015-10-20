#Set up enviorment variables needed for autentication
import os
import time
import sys

config = {'username':os.environ['OS_USERNAME'], 
          'api_key':os.environ['OS_PASSWORD'],
          'project_id':os.environ['OS_TENANT_NAME'],
          'auth_url':os.environ['OS_AUTH_URL'],
           }
#Set up Nova client
from novaclient.client import Client
nc = Client('2',**config)

workerlist = []

def createserver(number, i): 
    #Create server
    k = 0
    while number-(i+k) > 0:
        k+=1
        if not nc.keypairs.findall(name="cloudproj"):
            with open(os.path.expanduser('cloudproj.pub')) as fpubkey:
                nc.keypairs.create(name="cloudproj", public_key=fpubkey.read())
        imagew = nc.images.find(name="MOLNS_OpenStack_Provider_1444166469")
        flavorw = nc.flavors.find(name="m1.medium")
        user_dataw = open("user_worker.yml", 'r')
        keynamew = "cloudproj"
        namew = "G6-Project-worker" + str(i+k)
        instancew = nc.servers.create(name=namew, image=imagew, flavor=flavorw, key_name=keynamew, userdata=user_dataw)
        workerlist.append(instancew)

    

 
 
    # Poll at 5 second intervals, until the status is no longer 'BUILD'
    for instance in workerlist:
        status = instance.status
        while status == 'BUILD':
            time.sleep(5)
            # Retrieve the instance again so the status field updates
            instance = nc.servers.get(instance.id)
            status = instance.status
            name = instance.name
        print "Instance " + str(name) + " have status " + str(status) + "\n"

i = 0
ser_list = nc.servers.findall()
for server in ser_list: 
    if ("G6-Project-worker" in server.name):
        i+=1

print "There are a total of " + str(i) + " workers."        
numberofw = raw_input("What is the total number of workers you need? (Included already deployed): ")
numberofw = int(numberofw)
if numberofw <= i:
    print "Aborting, you already have requested number of workers"
else:
    createserver(numberofw, i)
    print "Time out in 90 seconds to give the server(s) a chance to start services and install packages." + "\nWhy don't you get a cup of coffee?"
    time.sleep(90)
    print "Server(s) should be good to go. Please proceed."
