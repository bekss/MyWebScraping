# import scrapy
# import json
# from scrapy.loader import ItemLoader
# from scrapy.loader.processors import Join,MapCompose,SelectJmes
# from..items import MarafonItem
#
#
# class JsonSpider(scrapy.Spider):
#     name = 'json'
#     allowed_domains = ['jsonplaceholder.typicode.com/users']
#     start_urls = ['http://jsonplaceholder.typicode.com/users/']
#
#     jmes_paths = {
#         'user_id': 'id',
#         'name': 'name',
#         'email': 'email',
#         'address': 'address.["zipcode", "city", "street", "suite"]',
#         'phone': 'phone',
#         'company': 'company.name',
#     }
#
#     def parse(self, response):
#         jsonresponse  = json.loads(response.body_as_unicode())
#
#         for user in jsonresponse:
#             loader = ItemLoader(item=MarafonItem())
#             loader.default_input_processor = MapCompose(str)
#             loader.default_output_processor = Join('')
#
#             for (field, path) in self.jmes_paths.items():
#                 loader.add_value(field, SelectJmes(path)(user))
#             yield loader.load_item()