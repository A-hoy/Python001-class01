# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

# useful for handling different item types with a single interface
# from itemadapter import ItemAdapter
import pymysql


class MaoyanMysqlPipeline:
    def __init__(self, host, user, password, db, charset):
        self.host = host
        self.user = user
        self.password = password
        self.db = db
        self.charset = charset

    @classmethod
    def from_crawler(cls, crawler):
        return cls(host=crawler.settings.get('HOST'),
                   user=crawler.settings.get('USER'),
                   password=crawler.settings.get('PASSWORD'),
                   db=crawler.settings.get('DB'),
                   charset=crawler.settings.get('CHARSET'))

    def open_spider(self, spider):
        self.conn = pymysql.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            db=self.db,
            charset=self.charset,
        )

    def process_item(self, item, spider):
        # print(item['film_name'], item['film_type'], item['release_date'])
        print(item)

        # with self.conn.cursor() as cursor:
        #     sql = 'INSERT INTO `maoyan_film` (`film_name`,  `release_date`)'\
        #           'VALUES (%s, %s)'
        #     cursor.execute(sql, (item['film_name'], item['release_date']))

        #     sql = 'INSERT INTO `film_type` (`film_name`, `type`) VALUES '\
        #           '(%s, %s)'
        #     for film_type in item['film_type']:
        #         cursor.execute(sql, (item['film_name'], film_type))

        # self.conn.commit()

        return item

    def close_spider(self, spider):
        self.conn.close()


# class
