from celery import Celery
import Dropbox

app4 = Celery('dropboxSubidaProcesada', broker="pyamqp://guest@localhost//")


@app4.task(no_ack=True)
def dropbox_grafica(data):
    Dropbox.subidaGrafica(data)
