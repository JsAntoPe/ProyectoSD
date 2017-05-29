from celery import Celery
import Procesar
import Cliente

app3 = Celery('procesarCelery', broker="pyamqp://guest@localhost//")


@app3.task(name='worker3', no_ack=True)
def procesar_excel(data):
    data_processed = Procesar.procesar(data)
    Cliente.cliente(4, data_processed)
