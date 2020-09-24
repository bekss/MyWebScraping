# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class MarafonItem(scrapy.Item):
    Table = scrapy.Field()
    Names = scrapy.Field()
    Score = scrapy.Field()
    Date = scrapy.Field()

