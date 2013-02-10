# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/topics/item-pipeline.html

from pymongo import MongoClient

class WordlistMongoDatabasePipeline(object):
    """Saves the items to a mongodatabase"""
    def process_item(self, item, spider):
        if( self.connection.wordlist.words.find( dict(item) ).count()==0 ):
            obj_id = self.connection.wordlist.words.insert( dict(item) )
        return item

    def open_spider(self, spider):
        self.connection = MongoClient('localhost', 1337)

    def close_spider(self, spider):
        self.connection.disconnect()

