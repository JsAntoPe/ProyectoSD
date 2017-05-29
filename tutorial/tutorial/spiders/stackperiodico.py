import scrapy
from celery import Celery
from celery.schedules import crontab, timedelta
from scrapy.crawler import CrawlerProcess

class StackObjeto(scrapy.Item):
    tags = scrapy.Field()

class StackSpider(scrapy.Spider):
    name = "stack"

    def start_requests(self):
        urls = [
            "http://stackoverflow.com/questions?pagesize=50&sort=newest"
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

app = Celery(backend="rpc://")

# Configuración de tareas periódicas
@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
	# Parámetros de sender.add_periodic_class: 
	# (periodo, nombre_funcion.s(parametro), name=nombre_cualquiera)
	sender.add_periodic_task(10.0, empezar_crawl.s(), name='scrape every 10')
	"""sender.add_periodic_task(
		crontab(hour=7, minute=30, day_of_week=1),
		empezar_crawl.s(),
	)"""


app.conf.timezone = 'Europe/London'
# Necesario para que no se intente reiniciar el twisted reactor
app.conf.worker_max_tasks_per_child = 1

# Tarea que se va a ejecutar
@app.task(name = "procesa")
def empezar_crawl():
	print("funcionando")
	process = CrawlerProcess({
            'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)',
			'FEED_FORMAT' : 'json',
			'FEED_URI' : 'resultado.txt'
        })
	process.crawl(StackSpider)
	process.start()
