# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
from .spiders import sql
import psycopg2
# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class MarafonPipeline:
    def __init__(self, **kwargs):
        super(MarafonPipeline, self).__init__(**kwargs)
        self.connection()
        self.create_table()

    def connection(self):
        self.connect = psycopg2.connect(
            database="postgres",
            user="postgres",
            password="admin",
            host="127.0.0.1",
            port="5432"
        )
        self.cursor = self.connect.cursor()

    def create_table(self):
        self.cursor.execute("""DROP TABLE IF EXISTS kibersports""")
        self.cursor.execute("""create table kibersports ( 
        NameTeam text not null, 
        Score text not null,
        Data text not null
        );""")
        self.connect.commit()

    def process_item(self, item, spider):
        self.store_db(item)
        return item

    def store_db(self, item):

        a=0;
        z = len(item['Names'])
        while a<=z:
            self.cursor.execute("insert into kibersports ( NameTeam, Score, Data) values (%s,%s,%s) ", (
                item['Names'][a],
                item['Score'][a],
                item['Date'][a]
            ))
            self.connect.commit()
            a+=1;

        print(a)

        print('connected')
