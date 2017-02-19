import redis
from time import time
from hashlib import sha224

from celery import Celery
import requests
import urllib2, cookielib
from lxml import etree
from pymongo import  MongoClient
from pymongo.errors import DuplicateKeyError
import json
from bs4 import BeautifulSoup


app = Celery("hello" )
app.config_from_object("celeryconfig")
# celery -A stack_scrap worker -B --loglevel=INFO

@app.task
def questions():
    site= "https://www.nseindia.com/live_market/dynaContent/live_analysis/gainers/niftyGainers1.json"
    hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
           'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
           'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
           'Accept-Encoding': 'none',
           'Accept-Language': 'en-US,en;q=0.8',
           'Connection': 'keep-alive'}
    req=urllib2.Request(site, headers=hdr)
    try:
        page=urllib2.urlopen(req)
    except urllib2.HTTPError, e:
        print e.fp.read()
    content=page.read()
    content=json.loads(content)
    print content
    print type(content)  
    

    #insert into redis with data as key
    r = redis.StrictRedis(host='localhost', port=6379, db=0)
    #r.delete('data')
    r.delete('data_list')
    for company in content["data"]:
        r.rpush('data_list',json.dumps(company))
        



    #print r.lrange('data_list',0,-1)
    #r.hmset('data',content)
    #client = MongoClient("localhost", 27017)
    #db=client["nse_gainers"]
    #coll=db["shares"]
    #remove all contents in that collection and then insert new content
    #coll.remove({})
    #coll.insert(content)
    """db = client["stack_questions"]
    coll = db["questions"]
    
    for entry in root.xpath(".//entry"):
        author = "".join(entry.xpath(".//author/name/text()"))
        link = "".join(entry.xpath("././/link/@href"))
        title = "".join(entry.xpath("./title/text()"))
        entry = {
            # links should be unique
            # using them as _id will ensure we will
            # not insert duplicate entries
            "_id": sha224(link).hexdigest(),
            "author": author,
            "link": link,
            "title": title,
            "fetched": int(time())
        }
        try:
            coll.insert(entry)
        except DuplicateKeyError:
            # we alredy have this entry in db
            # so stop, no need to parse rest of xml doc
            break
    """
    return content