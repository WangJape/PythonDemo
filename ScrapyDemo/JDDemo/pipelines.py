# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import scrapy
from itemadapter import ItemAdapter
from scrapy.pipelines.images import ImagesPipeline


# 首先在配置文件中开启管道 ITEM_PIPELINES
class FileSavePipeline:
    file = None

    # 重写，此方法只在开始爬虫的时候调用一次
    def open_spider(self, spider):
        print("爬虫开始。。。")
        self.file = open('./JDDemo/file/jd.txt', 'w', encoding='utf-8')

    # 用于处理item类型对象
    def process_item(self, item, spider):
        self.file.write(item['title'] + '\n')
        self.file.write(item['price'] + '\n')
        self.file.write(item['shop_name'] + '\n')
        self.file.write(item['url'] + '\n')
        self.file.write(item['image'] + '\n')
        self.file.write('\n')
        self.file.flush()
        return item  # 将item传递给下一个pipeline类

    def close_spider(self, spider):
        print("爬虫结束！！！")
        self.file.close()


# setting中配置 IMAGES_STORE 存储路径
class ImageSavePipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        yield scrapy.Request(url=item['image'])

    def file_path(self, request, response=None, info=None, *, item=None):
        file_name = request.url.split('/')[-1]
        return file_name

    def item_completed(self, results, item, info):
        return item
