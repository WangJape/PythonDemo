import scrapy

from JDDemo.items import JdItem


class ItcastSpider(scrapy.Spider):
    name = 'jd_images'
    keyWord = '电脑'
    url = 'https://search.jd.com/Search?keyword={}'.format(keyWord)
    start_urls = [url]

    def parse(self, response):
        lis = response.xpath('//*[@id="J_goodsList"]/ul/li')
        for li in lis:
            item = JdItem()
            item['title'] = li.xpath('div/div[3]/a/em/text()').extract_first()
            item['price'] = li.xpath('div/div[2]/strong/i/text()').extract_first()
            item['shop_name'] = li.xpath('div/div[5]/span/a/text()').extract_first()
            item['url'] = 'http://' + li.xpath('div/div[3]/a/@href').extract_first()[2:]
            item['image'] = 'http://' + li.xpath('div/div[1]/a/img/@data-lazy-img').extract_first()[2:]
            yield item
