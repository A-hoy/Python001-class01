# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class FilmItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    film_type = scrapy.Field()
    release_date = scrapy.Field()
    
    
