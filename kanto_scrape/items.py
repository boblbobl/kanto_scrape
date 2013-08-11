# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/topics/items.html

from scrapy.item import Item, Field

class SearchItem(Item):
	title = Field()
	link = Field()
	desc = Field()
	price = Field()
	image_urls = Field()
	images = Field()
	comments = Field()
	favorites = Field()
	created = Field()
	kind = Field()
	region = Field()