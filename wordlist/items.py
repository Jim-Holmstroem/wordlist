from scrapy.item import Item, Field

class WordlistItem(Item):
    word=Field()
    desc=Field()

