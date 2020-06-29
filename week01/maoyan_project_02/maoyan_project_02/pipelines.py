# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

# useful for handling different item types with a single interface
# from itemadapter import ItemAdapter


class MaoyanMoviePipeline:
    def open_spider(self, spider):
        with open('film.csv', 'w', encoding='utf-8') as fout:
            fout.write('电影名称, 影片类型, 上映日期\n')

    def process_item(self, item, spider):
        name = item['name']
        film_type = item['film_type']
        release_date = item['release_date']
        film_data = f'{name}, {film_type}, {release_date}\n'

        with open('film.csv', 'a', encoding='utf-8') as fout:
            fout.write(film_data)

        return item
