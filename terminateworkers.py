import os

config = {'username':os.environ['OS_USERNAME'], 
          'api_key':os.environ['OS_PASSWORD'],
          'project_id':os.environ['OS_TENANT_NAME'],
          'auth_url':os.environ['OS_AUTH_URL'],
           }
from novaclient.client import Client
nc = Client('2',**config)

# Terminate all your running instances
ser_list = nc.servers.findall()
for server in ser_list:
    if("G6-Project-worker" in server.name):
        server.delete()
        print "Terminated instance: " + server.name
        print "Bye bye! :)"
