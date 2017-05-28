from celery import Celery
import Dropbox
import dropboxBajada

app1 = Celery('dropboxSubidaParaProcesar', broker="pyamqp://guest@localhost//")


@app1.task(no_ack=True)
def dropbox_subida_parap(data):
    Dropbox.subida(data)
    dropboxBajada.dropbox_bajada.apply_async()

