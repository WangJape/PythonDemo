import scrapy


# 执行命令：scrapy crawl example [--nolog]不打印日志 [-o filepath]parse()返回数据写入到json、csv文件
class ExampleSpider(scrapy.Spider):
    # 爬虫唯一标识名称
    name = 'example'
    # 限定那些域名可以访问，可以不用
    allowed_domains = ['example.com']
    # 该list中url会被scrapy自动请求发送
    start_urls = ['http://example.com/']

    # 用作数据解析 response：请求成功的响应对象
    def parse(self, response):
        sel_list = response.xpath('')  # 返回一个Selector对象列表
        data_s = response.extract()  # list可直接调用extract()，返回每一个Selector的data字符串
        f_data = sel_list[0].extract()  # extract可以将Selector对象中data参数存储的字符串提取出来
        f_data = response.extract_first()  # 直接返回第一个的data，但xpath返回list必须仅且只有一个元素
        return data_s
