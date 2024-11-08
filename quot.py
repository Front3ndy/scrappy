import scrapy


class QuotSpider(scrapy.Spider):
    name = "quot"
    allowed_domains = ["quotes.toscrape.com"]
    start_urls = ["https://quotes.toscrape.com"]

    def parse(self, response):
        
        self.logger.info('hello this is my first spider')
        quotes = response.css('div.quote')
        for quote in quotes:
            yield {
                'text': quote.css('.text::text').get(),
                'author': quote.css('.author::text').get(),
                'tags': quote.css('.tag::text').getall(),
            }
        next_page = response.css('li.next a::attr("href")').get()
        cnt = 0
        if next_page is not None or cnt<10:
          cnt+=1
          yield response.follow(next_page, self.parse)