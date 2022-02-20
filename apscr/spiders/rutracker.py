import scrapy
from bs4 import BeautifulSoup


class RutrackerSpider(scrapy.Spider):
    name = 'rutracker'
    allowed_domains = ['rutracker.net']
    start_urls = ['https://rutracker.net/forum/viewforum.php?f=1260']
    custom_settings = {
        #'ROBOTSTXT_OBEY': True,
        'ROBOTSTXT_OBEY': False,
        'FEED_EXPORT_ENCODING': 'utf-8',
    }

    def parse(self, response):
      #dates = response.css('table.vf-table a.torTopic')
      #dates = response.css('table.vf-table a.torTopic').getall()
      
      soup = BeautifulSoup(response.text, 'lxml')
      dates = soup.find_all("a", class_="torTopic")
      
      nr = 1
      for z in dates:
        #b = z.css('::text').get()
        #c = z.css('::attr(href)').get()
        #r = z.get()
        #soup = BeautifulSoup(r, 'lxml')
        #w = soup.find("a")
        b = z.text
        c = z.get('href')
        
        yield {
          #"pagina": nr
          #b: c,
          'titlu': b,
          'href': c
        }
        
        nr += 1
        
      nextp = response.css('div.nav a')
      for ind in nextp:
        text_ind = ind.css('::text').get()
        href_ind = ind.css('::attr(href)').get()
        if text_ind == 'След.':
          yield response.follow(href_ind, callback=self.parse)
        
      
        """   
        rep = ['[', ']']
        for item in rep:
          if item in z:
            z = z.replace(item, '_')
        """    
     
     
     
