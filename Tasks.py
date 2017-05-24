from celery import *

app = Celery()

@app.task
def extraccion():
    return 0