# Introduction 
Web app showing realtime update of NSE top gainers.
This app is based on a cherry backend with redis as storage.
Celery has been used for scheduling calls to scrap latest data from NSE's website.
This app has been deployed on http://13.55.191.51:8080


#Requirements
Please make sure that Rabbitmq(Default message broker for celery) and its dependencies have been installed.
Refer to: https://www.rabbitmq.com/install-rpm.html

Also install redis server using this link: https://redis.io/topics/quickstart

Python modules required have been mantioned in 'requirements.txt'

Please install it using: pip install -r requirements.txt 


#Deployment and testing 
For local deployment:
1. Start Redis server: redis-server
2. Start celery worker: celery -A stocks_scraper worker -B --loglevel=INFO
3. Start the Cherrypy server: python site.py 

This app is running on http://13.55.191.51:8080
You can test it there.



