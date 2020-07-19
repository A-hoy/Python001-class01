from proxy_project.items import ProxyItem
from scrapy.loader import ItemLoader
import scrapy


class ProxySpider(scrapy.Spider):
    name = 'proxy'
    allowed_domains = ['ip.ihuan.me']
    start_urls = ['https://ip.ihuan.me']

    # start_urls = ['https://ip.ihuan.me/address/5Lit5Zu9.html?page=4ce63706']

    def parse(self, response):
        china_proxy_page = response.xpath('//div')
        return response.follow()
        # tr_elements = response.xpath('//tbody/tr')
        # for tr in tr_elements:
        #     yield self.parse_proxy_ip(tr)

        # next_page = response.xpath('//ul[@class="pagination"]/li[last()]/a')
        # yield from response.follow_all(next_page, callback=self.parse)

    def parse_proxy_ip(self, element):
        def support_https():
            if element.xpath('td[5]/text()').get() == '支持':
                return True
            return False

        def is_high_anonymity():
            if element.xpath('td[7]/a/text()').get() == '高匿':
                return True
            return False

        if support_https() and is_high_anonymity():
            loader = ItemLoader(item=ProxyItem(), selector=element)
            loader.add_value('scheme', 'https')
            loader.add_xpath('netloc', 'td[1]/a/text()|td[2]/text()')
            yield loader.load_item()
