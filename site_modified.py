import json
import redis
from pymongo import MongoClient
import cherrypy
from os import path, curdir

class StackMirror(object):
    #db = MongoClient("localhost", 27017)["nse_gainers"]

    @cherrypy.expose
    def index(self):
        return file("index.html")

    @cherrypy.expose
    def update(self, timestamp=None):
        try:
            timestamp = int(timestamp)
        except TypeError:
            timestamp = 0
        #coll = self.db["shares"]
        #records = coll.find({"fetched": {"$gt":timestamp}}).sort(
        #            "fetched", direction=-1)
        #records=coll.find({},{"data":1})
        #gainers=[]
        #for e in records:
            #print e["data"]
        #   for cmpny in e["data"]:
        #        gainers.append(cmpny)
        r = redis.StrictRedis(host='localhost', port=6379, db=0)
        #gainers=r.hgetall('data')
        #print gainers
        #print type(gainers)
        #print gainers["data"]
        #print type(gainers["data"])
        gainers=r.lrange('data_list',0,-1)
        return json.dumps([json.loads(cmpny) for cmpny in gainers])

cherrypy.quickstart(StackMirror(), "/", { "/static": {
                        "tools.staticfile.on": True,
                        "tools.staticfile.filename" : path.join(path.abspath(curdir), "realtime.js")}})
