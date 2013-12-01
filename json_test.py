"""Test de connection json"""

import json
import urllib2
import random
import sys
import requests

id=0
#premiere connection
URL = "http://192.168.0.11:8090/web/session/get_session_info"
DATA = {
    "jsonrpc": "2.0",
    "method": "call",
    "params": {"context": {}, "session_id": None},
    "id":id,
}
res =  requests.post(URL,json.dumps(DATA) )
result = res.json()['result']
cookies = {'sid':res.cookies['sid'] }
SESSION_ID = result['session_id']
id = id + 1
URL = "http://192.168.0.11:8090/web/session/authenticate"
DATA = {
    "jsonrpc": "2.0",
    "method": "call",
    "params": {"db":"test","login":"admin","session_id":SESSION_ID,"password":"admin","base_location":"http://192.168.0.11:8090"},
    "id":id,
}
res =  requests.post(URL,json.dumps(DATA),cookies=cookies )
RESULT = res.json() 

if not RESULT.has_key("result"):
    print "Erreur de connection "
    print RESULT['error']['data']['debug']
    sys.exit()
else:
 
    print "Connection OK %s" % SESSION_ID

 

CONTEXT = RESULT["result"]['user_context']
id = id + 1
URL = "http://192.168.0.11:8090/web/dataset/call_kw"
DATA_READ = {
 
    "method": "call",
    "id":"r%s" % id,
    "params": {"context" : CONTEXT,
              "session_id" :  SESSION_ID,
              "model" : "res.partner",
              "args" : [[1],['name']],"context": {}, "kwargs": {},'method':'read',
             }}

res =  requests.post(URL,json.dumps(DATA_READ),cookies=cookies )


RESULT = res.json() 
print "result ",RESULT

id = id + 1
URL = "http://192.168.0.11:8090/web/dataset/search_read"
DATA_READ = {
 
    "method": "call",
    "id":"r%s" % id,
    "params": {"context" : CONTEXT,
                "session_id" : SESSION_ID,
               "model" : "res.partner",
               "domain" : [['customer','=',1]],

               "fields" : ['id','name'],
               "limit" : False,
               "offset" : 0,
               
               "sort":""
               }
             }

res =  requests.post(URL,json.dumps(DATA_READ),cookies=cookies )


RESULT = res.json() 
print "result ",RESULT



