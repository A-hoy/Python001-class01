# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class MaoyanMoviePipeline:
    def process_item(self, item, spider):
        name = item['name']
        film_type = item['film_type']
        release_date = item['release_date']
        film_info = f'{name}|\t|{film_type}|\t|{release_date}\r\n'
        
        with open('./film.csv', 'a', encoding='utf-8') as fout:
            fout.write(film_info)
        
        return item
