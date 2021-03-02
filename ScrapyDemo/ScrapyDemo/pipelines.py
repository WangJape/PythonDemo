# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import scrapy
from itemadapter import ItemAdapter
from scrapy.pipelines.images import ImagesPipeline


# 首先在配置文件中开启管道 ITEM_PIPELINES
class ScrapyDemoPipeline:

    # 重写，此方法只在开始爬虫的时候调用一次
    def open_spider(self, spider):
        print("爬虫开始。。。")

    # 用于处理item类型对象
    def process_item(self, item, spider):
        return item  # 将item传递给下一个pipeline类

    def close_spider(self, spider):
        print("爬虫结束！！！")
