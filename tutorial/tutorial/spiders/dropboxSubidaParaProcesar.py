from celery import Celery
from Intermediario import intermediario
from Dropbox import subida
#import matplotlib.pyplot

app1 = Celery('dropboxSubidaParaProcesar', broker="pyamqp://guest@localhost//")


@app1.task(name='worker1', no_ack=True)
def dropbox_subida_parap(data):
    subida(data)
    intermediario(2)

