#import celery import crontab
from celery import Celery,  task
import scrapy

app = Celery('extraccion', broker="pyamqp://guest@localhost//")

@app.task
def extraccion(no_ack=True):
    scrapy.crawl("data")