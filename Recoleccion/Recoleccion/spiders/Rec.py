import scrapy


class RecSpider(scrapy.Spider):
    name = "Rec"

    def start_requests(self):
        start_urls = [
            'https://github.com/trending'
        ]
        for url in start_urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        yield response.css('//li[contains(@id, "pa-")]').extract()
        """for language in response.css('//li[contains(@class, pa)]'):
            yield {
                'language': language.css('//span[@class=mr-3]/text()').extract(),
            }"""