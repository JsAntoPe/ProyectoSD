import scrapy
from scrapy.crawler import CrawlerProcess

class StackObjeto(scrapy.Item):
    excerpt = scrapy.Field()
    tags = scrapy.Field()

class StackSpider(scrapy.Spider):
    name = "stack2"

    def start_requests(self):
        urls = [
            "http://stackoverflow.com/questions?pagesize=15&sort=newest"
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        preguntas = response.xpath('//div[@class="summary"]/div')

        for pregunta in preguntas:
            obj = StackObjeto()
            obj['tags'] = pregunta.xpath(
                'a[@class="post-tag"]/text()').extract()
            yield obj
            
process = CrawlerProcess({
        'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
    })
process.crawl(StackSpider)
process.start()

