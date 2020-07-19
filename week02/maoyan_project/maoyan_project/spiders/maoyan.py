from maoyan_project.items import FilmItem
import scrapy
# import lxml


class MaoyanSpider(scrapy.Spider):
    name = 'maoyan'
    allowed_domains = ['maoyan.com']
    start_urls = ['https://maoyan.com/films?showType=3']

    def parse(self, response):
        movies_info = response.xpath('//div[@class="movie-hover-info"]')

        film = FilmItem()
        div_elements = movies_info.xpath('div[1]')
        film['name'] = div_elements.xpath('./span[1]/text()').getall()
        film['score'] = div_elements.xpath('string(./span[2])').getall()
        film['film_type'] = movies_info.xpath(
            'normalize-space(./div[2]/text()[2])').getall()
        film['release_date'] = movies_info.xpath(
            'normalize-space(./div[last()]/text()[2])').getall()
        yield film

    # def parse(self, response):
    # html = lxml.etree.HTML(response.text)
    # movies_info = html.iterfind('.//div[@class="movie-hover-info"]')

    #     # film = FilmItem()
    #     for _ in range(10):
    #         try:
    #             info = next(movies_info)
    #         except StopIteration:
    #             pass
    #         else:
    #             # film['film_name'] = info[1].get('title')
    #             # film['film_type'] = info[1][0].tail.strip().replace('／', ',')
    #             # film['release_date'] = info[-1][0].tail.strip()
    #             # yield film
    #             yield {
    #                 'film_name': info[1].get('title'),
    #                 'film_type': info[1][0].tail.strip().replace('／', ','),
    #                 'release_date': info[-1][0].tail.strip()
    #             }
