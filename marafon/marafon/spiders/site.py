import scrapy
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from scrapy.spiders import CSVFeedSpider

from ..items import MarafonItem


PATH = "C:\Program Files (x86)\chromedriver.exe"


class MarafonSpiders(scrapy.Spider):
    name = 'marafon'
    allowed_domains = ['http://localhost/marafon.html']
    start_urls = ['http://localhost/marafon.html']

    def __init__(self, **kwargs):
        super(MarafonSpiders, self).__init__(**kwargs)
        self.driver = webdriver.Chrome(PATH)
        # self.driver.implicitly_wait(5)

    def parse(self, response):
        self.header = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
        options = Options()
        options.add_argument("--disable-notifications")
        options.add_argument("--incognito")
        options.add_argument("--disable-extensions")
        options.add_argument(" --disable-gpu")
        options.add_argument(" --disable-infobars")
        options.add_argument(" -–disable-web-security")
        options.add_argument("--no-sandbox")
        caps = options.to_capabilities()
        self.driver = webdriver.Chrome(PATH,
                                       desired_capabilities=caps)
        self.driver.get(response.url)
        buttons = self.driver.find_elements_by_class_name("week-date-selector-item")
        buttons[3].click()

        items = MarafonItem()
        NameTable = 'Kibersport'
        KibersportContent = response.css('div.result-sport-content')
        items['Category_label'] = KibersportContent.css('div.category-label::text').extract()
        items['Names'] = KibersportContent.css('td.label::text').extract()
        items['Score'] = KibersportContent.css('td.value::text').extract()
        items['Date'] = KibersportContent.css('td.date::text').extract()
        return items






    # script = response.xpath("//div[@class='result-sport']/text()").extract_first()










    # import scrapy
    # import selenium
    # from scrapy.selector import Selector
    # from selenium import webdriver
    #
    # driver = webdriver.Chrome('path/to/the/chromedriver')
    # driver.get(
    #     'https://www.airbnb.ae/s/Dubai/homes?refinement_paths%5B%5D=%2Fhomes&adults=0&children=0&infants=0&guests=0&place_id=ChIJRcbZaklDXz4RYlEphFBu5r0&query=Dubai&allow_override%5B%5D=&s_tag=CKxLe9y7')
    #
    # scrapy_selector = Selector(text=driver.page_source)
    # scrapy_selector.xpath('//*[@itemtype="http://schema.org/ListItem"]')  # returns the list of selectors















































       # self.driver.implicitly_wait(15)
        # sleep(15)
        # headers = {
        #     'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:45.0) Gecko/20100101 Firefox/45.0'
        # }
        # r = requests.get(url='https://www.marathonbet.ru/su/results.htm', headers= headers)
        # with open('test.html', 'w') as output_file:
        #     output_file.write(r.text)

            # page = response.url.split("/")[-2]
            # filename = 'quotes-%s.html' % page
            # with open(filename, 'wb') as f:
            #     f.write(response.body)



        # jmes_paths = {
        #     '12': '12',
        #     'categories': 'categories.[]',
        #     'email': 'email',
        #     'address': 'address.["zipcode", "city", "street", "suite"]',
        #     'phone': 'phone',
        #     'company': 'company.name',
        # }
        # for user in jsonresponse:
        #     loader = ItemLoader(item=MarafonItem())
        #     loader.default_input_processor = MapCompose(str)
        #     loader.default_output_processor = Join('')
        #
        #     for (field, path) in self.jmes_paths.items():
        #         loader.add_value(field, SelectJmes(path)(user))




        # items = MarafonItem()
        # Sports = response.css('div.sports')
        # items['Kibersport'] = Sports.xpath("//div[@class='result-sport']/text()").get()
        # items['Category_label'] = Sports.css('div.category-label::text').get()
        # items['Names'] = Sports.css('td.label::text').extract()
        # items['Score'] = Sports.css('td.value::text').extract()
        # items['Date']  = Sports.css('td.date::text').extract()
        # return items