from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

from meetup.items import PicItem


class PicSpider(CrawlSpider):
    name = 'pic'
    allowed_domains = ['www.reddit.com']
    start_urls = ['https://www.reddit.com/r/pics/?count=0']

    rules = [
        Rule(LinkExtractor(allow=['https://www.reddit.com/r/pics/?count=0', '/r/pics/\?count=\d*&after=\w*']),
            callback='parse_start_urls',
            follow=True)
    ]


    def parse_start_url(self, response):


        selector_list = response.css('div.thing')

        for selector in selector_list:
            item = PicItem()
            item['image_urls'] = selector.xpath('a/@href').extract()
            item['title'] = selector.xpath('div/p/a/text()').extract()
            item['url'] = selector.xpath('a/@href').extract()

            yield item