
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.selector import Selector

""" Run command:
    scrapy crawl ycombinator --nolog
"""

class YCombinatorSpider(CrawlSpider):
    name = 'ycombinator'
    allowed_domains = ['news.ycombinator.com']
    start_urls = ['https://news.ycombinator.com/news']

    rules = [
        Rule(LinkExtractor(allow=['news\?p\=\d+']),
            callback='parse_start_url',
            follow=True
             ),

        Rule(LinkExtractor(allow=['item\?id=\d*']),
            callback='parse_comments',
            follow=True
        ),
    ]

    def parse_start_url(self, response):
        print("#"*20, response.url, "#"*20)

    def parse_comments(self, response):

        # Extracting article details:
        title = Selector(response=response).xpath('//a[@class="storylink"]/text()').extract()
        url = Selector(response=response).xpath('//a[@class="storylink"]/@href').extract()

        # Extracting comments' details:
        users = Selector(response=response).xpath('//a[@class="hnuser"]/text()').extract()
        author = users[0]
        commenters = users[1:len(users)]

        print(title[0], url[0])
        print(author, commenters)
        print("")
