from celery import Celery
import Procesar
import dropboxSubidaProcesada

app3 = Celery('procesarCelery', broker="pyamqp://guest@localhost//")


@app3.task(no_ack=True)
def procesar_excel(data):
    data_processed = Procesar.procesar(data)
    dropboxSubidaProcesada.dropbox_subida_procesado.apply_async(data_processed)
