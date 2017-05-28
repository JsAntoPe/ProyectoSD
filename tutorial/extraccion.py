from celery import Celery, task
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
import tutorial.tutorial.spiders.pruebastack2

app = Celery('extraccion', broker="pyamqp://guest@localhost//")

process = CrawlerProcess(get_project_settings())
process.crawl('data', domain='scrapinghub.com')


@app.task
def ext(no_ack=True):
    tutorial.tutorial.spiders.pruebastack2.iniciar()
