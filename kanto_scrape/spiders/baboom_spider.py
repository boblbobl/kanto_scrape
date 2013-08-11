from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from kanto_scrape.items import SearchItem
from random import randrange
from datetime import datetime, timedelta

class BaboomSpider(BaseSpider):
    name = "baboom"
    allowed_domains = ["baboom.dk"]
    
    # TODO: Make this dynamic
    page_no = 2
    
    start_urls = []
    for n in range(1, page_no): 
      start_urls.append("http://www.baboom.dk/marked/sogeresultat?page=" + str(n))
      
    def get_random_date(self):
      
      end = datetime.now()
      start = datetime(2013, 1, 1)
      
      delta = end - start
      int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
      random_second = randrange(int_delta)
      return start + timedelta(seconds=random_second)

    def parse(self, response):
      
      hxs = HtmlXPathSelector(response)
      adds = hxs.select('//div[@class="item"]')
      items = []
      for add in adds:
        item = SearchItem()
        item['title'] = add.select('div[@class="markettitle"]//a//text()').extract()[0]
        item['link'] = 'http://www.baboom.dk/marked/' + add.select('div[@class="markettitle"]//a//@href').extract()[0]
        item['image_urls'] = []
        
        for url in add.select('div[@class="image"]//a//img//@src').extract():
          url = url + "?mode=max"
          item['image_urls'].append(url.replace('/thumb/100/75', '/thumb/236/1000'))
        
        # TODO: Move this pipeline
        item['desc'] = ''
        _desc = add.select('div[@class="markettitle"]//div[@class="description"]//text()').extract()
        for line in _desc:
          item['desc'] += line.strip()
        item['price'] = add.select('div[@class="marketprice"]//text()').extract()[0].strip().replace('kr. ', '')
        item['created'] = self.get_random_date()
        item['comments'] = randrange(2)
        item['favorites'] = randrange(2)
        
        _type_and_location = add.select('div[@class="markettitle"]//div[@class="typeandlocation"]//text()').extract()[0].split(', ')
        item['kind'] = _type_and_location[0].strip()
        item['region'] = _type_and_location[1].strip()

        items.append(item)
      return items