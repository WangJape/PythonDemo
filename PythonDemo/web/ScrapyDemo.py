import scrapy


# scrapy建立单独的工程命令 scrapy startproject projectName
class DemoSpider(scrapy.Spider):  # 继承Spider类
    name = "dmoz"  # 爬虫的唯一标识，不能重复，启动爬虫的时候要用
    allowed_domains = ["www.baidu.com"]  # 限定域名，只爬取该域名下的网页
    # 这里写上你要爬取的页面链接
    start_urls = [
        "https://www.baidu.com/"
    ]

    # 爬取的方法
    def parse(self, response, **kwargs):
        filename = response.url.split("/")[-2]  # 获取url，用”/”分段，获取倒数第二个字段
        with open(filename, 'a') as f:
            f.write(response.body)  # 把访问的得到的网页源码写入文件
