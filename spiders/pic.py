from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class PicSpider(CrawlSpider):
    name = 'pic'
    allowed_domains = ['www.reddit.com']
    start_urls = ['http://www.reddit.com/r/pics/']

    rules = [
        Rule(LinkExtractor(allow=['/r/pics/\?count=\d*&after=\w*']))
    ]