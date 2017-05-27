from celery import Celery
import Procesar
import dropboxSubidaProcesada

app = Celery('procesarCelery', broker="pyamqp://guest@localhost//")


@app.task(no_ack=True)
def procesar_excel(data):
    data_processed = Procesar.procesar(data)
    dropboxSubidaProcesada.dropbox_subida_procesado(data_processed)