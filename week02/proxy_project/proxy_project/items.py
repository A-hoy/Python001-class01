# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from scrapy.loader.processors import TakeFirst, Join
import scrapy


class ProxyItem(scrapy.Item):
    scheme = scrapy.Field(output_processor=TakeFirst())
    netloc = scrapy.Field(output_processor=Join(separator=':'))
    url = scrapy.Field()
