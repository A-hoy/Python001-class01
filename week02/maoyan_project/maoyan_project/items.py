# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class FilmItem(scrapy.Item):
    film_name = scrapy.Field()
    film_score = scrapy.Field()
    film_type = scrapy.Field()
    release_date = scrapy.Field()
    first_week_box_office = scrapy.Field()
    total_box_office = scrapy.Field()
