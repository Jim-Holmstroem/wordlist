crawl:
	scrapy crawl wordlist
startmongo:
	mongod --dbpath data/ --port 1337 --fork --logpath data/log/mongodb.log
