import scrapy

class DataSpider(scrapy.Spider):
    name = "data"

    def start_requests(self):
        urls = [
            'https://catalog.data.gov/dataset'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
    def parse(self, response):
        cadena = response.css('div.new-results::text').extract()
        resultado = cadena.pop(1)
        resultado = resultado.strip('\n')
        resultado = resultado.strip(' \n')
        resultado = resultado.strip('\n\n')
        yield {"title" : resultado}

