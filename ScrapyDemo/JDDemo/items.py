# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapydemoItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class JdItem(scrapy.Item):
    title = scrapy.Field()  # 标题
    price = scrapy.Field()  # 价格
    shop_name = scrapy.Field()  # 店铺名称
    url = scrapy.Field()  # 商品链接
    image = scrapy.Field()  # 图片链接
