# import celery import crontab
import os
from celery import Celery, task
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

app = Celery('extraccion', broker="pyamqp://guest@localhost//")

"""process = CrawlerProcess(get_project_settings())
process.crawl('data', domain='scrapinghub.com')"""


@app.task
def extraccion(no_ack=True):
    # process.start()
    return os.system('scrapy crawl data -o Data.json')
