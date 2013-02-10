# Scrapy settings for wordlist project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#

BOT_NAME = 'wordlist'

SPIDER_MODULES = ['wordlist.spiders']
NEWSPIDER_MODULE = 'wordlist.spiders'

ITEM_PIPELINES = ['wordlist.pipelines.WordlistMongoDatabasePipeline']

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'wordlist (+http://www.yourdomain.com)'
