#https://docs.scrapy.org/en/latest/topics/items.html
import scrapy


class MarafonItem(scrapy.Item):
    Count = scrapy.Field()# количество строк данных в одной колонке в будущем возможно пригодиться
    Table = scrapy.Field() #имя таблицы
    Names = scrapy.Field()#названия имен
    Score = scrapy.Field()# количество голов
    Date = scrapy.Field() #дата игры

