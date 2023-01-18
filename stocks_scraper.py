import redis
from time import time
from celery import Celery
import requests
import urllib2, cookielib
import json



app = Celery("hello" )
app.config_from_object("celeryconfig")
# celery -A stocks_scraper worker -B --loglevel=INFO

@app.task
def stocks():
    
    site= "https://www1.nseindia.com/live_market/dynaContent/live_analysis/gainers/niftyGainers1.json"
    #mimick the request as browser to have the access permission
    hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
           'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
           'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
           'Accept-Encoding': 'none',
           'Accept-Language': 'en-US,en;q=0.8',
           'Connection': 'keep-alive'}
    
    req=urllib2.Request(site, headers=hdr)
    #get the data otherwise throw error 
    try:
        page=urllib2.urlopen(req)
    except urllib2.HTTPError, e:
        print e.fp.read()
    content=page.read()
    content=json.loads(content)
    print content
    print type(content)  
    

    #insert into redis with data_list as key
    r = redis.StrictRedis(host='localhost', port=6379, db=0)
    #replace the key value in redis at every function call
    r.delete('data_list')
    for company in content["data"]:
        r.rpush('data_list',json.dumps(company))      



    #print r.lrange('data_list',0,-1)
    #r.hmset('data',content)
    return content
