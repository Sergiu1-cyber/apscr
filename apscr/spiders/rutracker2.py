import scrapy

from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor


class Rutracker2Spider(CrawlSpider):
    name = 'rutracker2'
    allowed_domains = ['rutracker.net']
    start_urls = ['https://rutracker.net/forum/viewforum.php?f=1992']
    custom_setings = {
      'ROBOTSTXT_OBEY': False,
      #'ROBOTSTXT_OBEY': True,,
      'FEED_EXPORT_ENCODING': 'utf-8',
    }
    rules = (
      Rule(LinkExtractor(allow=('viewtopic\.php\?t\=',)), callback='parse_item'),
      )

    def parse_item(self, response):
      body = response.css('div.post_body').get().strip()
      yield {
        'href': body
      }

#allow=('viewtopic\.php?t',)
# , deny=('viewtopic\.php?p',)