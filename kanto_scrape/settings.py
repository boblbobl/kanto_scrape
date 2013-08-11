# Scrapy settings for kanto_scrape project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#

BOT_NAME = 'kanto_scrape'

SPIDER_MODULES = ['kanto_scrape.spiders']
NEWSPIDER_MODULE = 'kanto_scrape.spiders'

ITEM_PIPELINES = [
  'scrapy.contrib.pipeline.images.ImagesPipeline',
  'scrapyelasticsearch.ElasticSearchPipeline'
]
IMAGES_STORE = '/Users/larshundebol/Projects/kanto/public/img/baboom'

ELASTICSEARCH_SERVER = 'localhost'
ELASTICSEARCH_PORT = 9200
ELASTICSEARCH_INDEX = 'kanto_test'
ELASTICSEARCH_TYPE = 'items'
ELASTICSEARCH_UNIQ_KEY = 'link'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'kanto_scrape (+http://www.yourdomain.com)'
