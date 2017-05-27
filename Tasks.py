from celery import Celery, task
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

app = Celery('extraccion', broker="pyamqp://guest@localhost//")

@app.task
def