import scrapy


class DetailSpider(scrapy.Spider):
    name = 'first'
    url = 'http://www.baidu.com/'
    headers = {'': ''}

    def start_requests(self):
        yield scrapy.Request(self.url, callback=self.parse, method='POST', headers=self.headers)

    def parse(self, response):
        print(response.body)

        # 进入url进一步爬取明细
        detail_url = ''
        yield scrapy.Request(url=detail_url, callback=self.detail_parse, method='POST', headers=self.headers)

    def detail_parse(self, response):
        print(response.body)
