import scrapy


class LosstSpider(scrapy.Spider):
    name = 'losst'
    allowed_domains = ['losst.ru']
    start_urls = ['https://losst.ru/page/1']
    custom_settings = {
      'FEED_EXPORT_ENCODING': 'utf-8',
    }

    def parse(self, response):
      el = response.css('h2.post-title')
      
      for element in el:
        yield {
          'text' : element.css('a::text').get(),
          'href' : element.css('a::attr(href)').get()
        }
      
      next_page = response.css('li.nav-previous a::attr(href)').get()
      if next_page is not None:
        yield response.follow(next_page, callback=self.parse)
        #yield scrapy.Request(next_page, callback=self.parse)





