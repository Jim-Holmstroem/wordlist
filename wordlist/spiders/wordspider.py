from scrapy.selector import HtmlXPathSelector
from scrapy.spider import BaseSpider
from scrapy.http import Request

from scrapy.utils.markup import remove_tags

from wordlist.items import WordlistItem

class WordSpider(BaseSpider):
    name = 'wordlist'
    allowed_domains = ['majortests.com']
    start_urls = [
        'http://www.majortests.com/word-lists/',
    ]

    def parse(self, response):
        hxs = HtmlXPathSelector(response) 

        for url in map(
            lambda l: "http://www.majortests.com"+l, 
            hxs.select("//div[@class='grid_4 alpha']//a/@href")
            .extract()[::2]
        ):
            yield Request(
                url, 
                callback=self.sub_parse
            )

    def sub_parse(self, response):
        """parse the words"""
        hxs = HtmlXPathSelector(response)
        
        words = map(
            remove_tags, 
            hxs.select("//table[@class='wordlist']//th").extract()
        )
        descs = map(
            remove_tags,
            hxs.select("//table[@class='wordlist']//td").extract()
        )
        for word, desc in zip(words, descs):
            word_entry = WordlistItem()
            word_entry['word'], word_entry['desc'] = word, desc
            print word, "=", desc
            yield word_entry

