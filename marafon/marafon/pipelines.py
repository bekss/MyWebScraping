# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
from .spiders import sql
import psycopg2
from .items import MarafonItem
# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class MarafonPipeline:
    def __init__(self, **kwargs):
        super(MarafonPipeline, self).__init__(**kwargs)
        self.connection()


    def connection(self):
        self.connect = psycopg2.connect(
            database="postgres",
            user="postgres",
            password="admin",
            host="127.0.0.1",
            port="5432"
        )
        self.cursor = self.connect.cursor()

    def process_item(self, item, spider):
        self.store_db(item)
        return item

    def create_table(self, item):
        # self.cursor.execute("""DROP TABLE IF EXISTS kibersports""")
        z = len(item['Category_label'])
        a = 0;
        while a <= z:
            self.cursor.executemany("""create table %s ( 
               NameTeam text not null, 
               Score text not null,
               Data text not null
               );""", (item['Category_label'][a]))
            self.connect.commit()
            a += 1;

    def store_db(self, item):
        b = 0;
        a = 0;
        table_name = len(item['Category_label'])
        total_name = len(item['Names'])
        while b <= table_name:
            while a <= total_name:
                self.cursor.executemany("insert into %s  values (%s,%s,%s); ",
                                    (item['Category_label'][b],
                                        item['Names'][a],
                                        item['Score'][a],
                                        item['Date'][a]
                                    ))
                self.connect.commit()
                a += 1;
            b += 1;
