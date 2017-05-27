from celery import Celery
import Dropbox
import dropboxBajada

app = Celery('dropboxSubidaParaProcesar', broker="pyamqp://guest@localhost//")


@app.task(no_ack=True)
def dropbox_subida_parap(data):
    Dropbox.subida(data)
    result = dropboxBajada.dropbox_bajada()
    return result.get()