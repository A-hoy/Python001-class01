import scrapy
from maoyan_project_02.items import FilmItem


class MaoyanSpider(scrapy.Spider):
    name = 'maoyan'
    allowed_domains = ['https://maoyan.com/']
    start_urls = ['https://maoyan.com/films?showType=3']

    def parse(self, response):
        movies_info = response.xpath('//div[@class="movie-hover-info"]')[:10]
        
        film = FilmItem()
        for info in movies_info:
            div_element = info.xpath('div[2]')
            film['name'] = div_element.attrib['title']
            film['film_type'] = div_element.xpath('./text()').getall()[-1].strip()
            film['release_date'] = info.xpath('div[last()]/text()').getall()[-1].strip()
            yield film

        