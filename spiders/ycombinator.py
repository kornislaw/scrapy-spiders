
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.selector import Selector
from scrapy.http import Request

""" Run command:
    scrapy crawl ycombinator --nolog
"""

NUM_OF_NEWS_TO_CRAWL = 200

class YCombinatorSpider(CrawlSpider):
    name = 'ycombinator'
    allowed_domains = ['news.ycombinator.com']
    start_urls = ['https://news.ycombinator.com/newest']

    news_crawled = []

    rules = [
        Rule(LinkExtractor(
            allow=['newest\?next=\d*&n=\d*']),
            callback='parse_item',
            follow=True
             ),

        Rule(LinkExtractor(
            allow=['item\?id=\d*']),
            callback='parse_comments',
            follow=True
        ),
    ]

    def parse_item(self, response):
        print("#"*20, response.url, "#"*20)

        # for i in response.xpath("//a[@class='storylink']/@href").extract():
        #     self.news_crawled.append(i)
        #
        # if len(self.news_crawled) >= NUM_OF_NEWS_TO_CRAWL:
        #     for link in self.news_crawled[0:NUM_OF_NEWS_TO_CRAWL]:
        #         print(link)
        #         Request(link, callback=self.parse_comments)

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
