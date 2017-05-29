from celery import Celery
import Mediador
from Dropbox import subida

app1 = Celery('dropboxSubidaParaProcesar', broker="pyamqp://guest@localhost//")


@app1.task(name='worker1', no_ack=True)
def dropbox_subida_parap(data):
    subida(data)
    Mediador.mediador(2)

