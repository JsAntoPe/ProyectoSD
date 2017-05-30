from celery import Celery
import Procesar
import dropboxSubidaGrafica

def procesar_excel(data):
    data_processed = Procesar.procesar(data)
    dropboxSubidaGrafica.dropbox_grafica(data_processed)
