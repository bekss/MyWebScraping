#https://docs.scrapy.org/en/latest/topics/items.html
import scrapy


class MarafonItem(scrapy.Item):
    Count = scrapy.Field()
    Table = scrapy.Field()
    Names = scrapy.Field()
    Score = scrapy.Field()
    Date = scrapy.Field()

