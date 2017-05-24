import scrapy


class RecSpider(scrapy.Spider):
    name = "Rec"
    start_urls = [
        'https://github.com/trending'
    ]



    def parse(self, response):
        print("Datos:\n")
        for language in response.css('div.f6'):
            print(language.css('span.mr-3::text')+"\n")
            yield {
                'language': language.css('span.mr-3::text'),
            }