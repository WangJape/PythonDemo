import scrapy

from JDDemo.items import JdItem


class ItcastSpider(scrapy.Spider):
    name = 'jd_page'
    keyWord = '电脑'
    page_no = 1
    url = 'https://search.jd.com/Search?keyword={}&page={}'.format(keyWord, page_no)
    start_urls = [url]

    def parse(self, response):
        print("当前解析第%d页" % self.page_no)
        lis = response.xpath('//*[@id="J_goodsList"]/ul/li')

        items = list()
        for li in lis:
            item = JdItem()
            item['title'] = li.xpath('div/div[3]/a/em/text()').extract_first()
            item['price'] = li.xpath('div/div[2]/strong/i/text()').extract_first()
            item['shop_name'] = li.xpath('div/div[5]/span/a/text()').extract_first()
            item['url'] = li.xpath('div/div[3]/a/@href').extract_first()
            item['image'] = li.xpath('div/div[1]/a/img/@data-lazy-img').extract_first()
            items.append(item)
            yield item  # 生成器，框架调用pipelines的process_item()

        # 下一页手动调用
        if self.page_no < 10:
            self.page_no += 1
            self.url = 'https://search.jd.com/Search?keyword={}&page={}'.format(self.keyWord, self.page_no)
            yield scrapy.Request(url=self.url, callback=self.parse)
