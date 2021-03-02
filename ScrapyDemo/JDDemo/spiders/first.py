import scrapy


class ExampleSpider(scrapy.Spider):
    name = 'first'
    url = 'http://www.baidu.com/'
    headers = {}

    def start_requests(self):
        yield scrapy.Request(self.url, callback=self.parse, method='POST', headers=self.headers)

    def parse(self, response):
        print(response.body)
