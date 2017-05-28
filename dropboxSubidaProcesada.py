from celery import Celery
import Dropbox

app = Celery('dropboxSubidaProcesada', broker="pyamqp://guest@localhost//")


@app.task(no_ack=True)
def dropbox_subida_procesado(data):
    Dropbox.subidaProcesada(data)
