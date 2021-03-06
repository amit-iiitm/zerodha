import json
import redis
import cherrypy
from os import path, curdir

class StackMirror(object):
    @cherrypy.expose
    def index(self):
        return file("index.html")

    @cherrypy.expose
    def update(self, timestamp=None):
        try:
            timestamp = int(timestamp)
        except TypeError:
            timestamp = 0
        #gainers=[]
        #for e in records:
            #print e["data"]
        #   for cmpny in e["data"]:
        #        gainers.append(cmpny)
        #query redis 
        r = redis.StrictRedis(host='localhost', port=6379, db=0)
        #gainers=r.hgetall('data')
        #print gainers
        #print type(gainers)
        #print gainers["data"]
        #print type(gainers["data"])

        #return data to frontend
        gainers=r.lrange('data_list',0,-1)
        return json.dumps([json.loads(cmpny) for cmpny in gainers])

cherrypy.quickstart(StackMirror(), "/", { "/static": {
                        "tools.staticdir.on": True,
                        "tools.staticdir.dir" : path.join(path.abspath(curdir), "static")}})
