from maoyan_project_02.items import FilmItem
import scrapy
import lxml


class MaoyanSpider(scrapy.Spider):
    name = 'maoyan'
    allowed_domains = ['maoyan.com']
    start_urls = ['https://maoyan.com/films?showType=3']

    def parse(self, response):
        html = lxml.etree.HTML(response.text)
        movies_info = html.iterfind('.//div[@class="movie-hover-info"]')

        film = FilmItem()
        for _ in range(10):
            info = next(movies_info)
            film['name'] = info[1].get('title')
            film['film_type'] = info[1][0].tail.strip()
            film['release_date'] = info[-1][0].tail.strip()
            yield film

    # def parse(self, response):
    #     movies_info = response.xpath('//div[@class="movie-hover-info"]')[:10]

    #     film = FilmItem()
    #     for info in movies_info:
    #         div_element = info.xpath('div[2]')
    #         film['name'] = div_element.attrib['title']
    #         film['film_type'] = div_element.xpath(
    #             './text()').getall()[-1].strip()
    #         film['release_date'] = info.xpath(
    #             'div[last()]/text()').getall()[-1].strip()
    #         yield film
