import psycopg2
import re
from .items import MarafonItem
from itemadapter import ItemAdapter


class MarafonPipeline:
    def __init__(self, **kwargs):
        super(MarafonPipeline, self).__init__(**kwargs)
        self.connection()


    def connection(self):
        self.connect = psycopg2.connect(
            database="total",
            user="postgres",
            password="admin",
            host="127.0.0.1",
            port="5432"
        )
        self.cursor = self.connect.cursor()

    def process_item(self, item, spider):
        self.create_table(item)
        self.store_db(item)
        return item

    def create_table(self, item):
        table = {}
        tables = {}
        array = len(item['Table'])
        for a in range(array):
            # tables = re.sub(r"[-+' '()^%$%_/,.?:#%!@*]", "", str(item["Table"][1]))
            # print(tables[0])
            table["table{0}".format(a)] = re.sub(r"[^\w]", "", item["Table"][a])                                      # создает все переменные с значениями имен таблиц
            tables["table{0}".format(a)] = " create table " + table["table{0}".format(a)] + " (NameTeam text not null, Score text not null, Data text not null );" # в созданные переменные дается значения
            self.cursor.execute(tables["table{0}".format(a)])
            self.connect.commit()

        print(tables)





        # for x in range(len(item['Table'])):
        #     if item['Table']:
        #
        #   table1 =  " create table " + item['Table'][0]+ " (NameTeam text not null, Score text not null, Data text not null );"
        #
        # self.cursor.execute(table1)
        # self.connect.commit()

        # self.cursor.execute("""DROP TABLE IF EXISTS Kibersports""")
        # self.cursor.execute("""create table Kib (
        #    NameTeam text not null,
        #    Score text not null,
        #    Data text not null
        #    );""")
        # self.connect.commit()

    def store_db(self, item):
        table = {}
        table_name = []
        array = len(item['Table'])
        print('-----------------')
        print(item)
        print('-----------------')
        total = item['Count']
        print(item['Count'])

        # for a in range(array):
        #     # tables = re.sub(r"[-+' '()^%$%_/,.?:#%!@*]", "", str(item["Table"][1]))
        #     # print(tables[0])
        #     table["table{0}".format(a)] = re.sub(r"[-+' '()^%$%_/',.?:#%!@*]", "", str(item["Table"][a]))
        # print(table)

        print(len(total))
        total_name = len(item['Names']) # размер
        # while (c < len(total)) & ( b < array):
        ad = 0;
        for b in range(array):

            table["table{0}".format(b)] = re.sub(r"[^\w]", "", item["Table"][b])
            number = table["table{0}".format(b)]
            names = table_name.append(str(number))
            print(table_name[b])
            table_sorted_name = re.sub(r"[^\w]", "", table_name[b])

            # while d < address:
            address = total[b]

            for f in range(ad, ad+address):

                self.cursor.execute(f"insert into {table_sorted_name} values (%s, %s, %s);",
                                    (   item['Names'][f],
                                        item['Score'][f],
                                        item['Date'][f]
                                    ))
                self.connect.commit()
                if f == ad+address-1:
                    ad+= address;


        # final_item = []
        #
        # final_item.append(zip(item['Names'],
        #                       item['Score'],
        #                       item['Date']))
        # for n in final_item:
        #     print(tuple(n))

# def main():
#     url = 'https://www.marathonbet.ru/su/react/results/list'
#     html = get_html(url)
#
#
# if _name == 'main_':
#     main()a
