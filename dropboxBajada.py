from celery import Celery
from Dropbox import bajar
import procesarCelery

app2 = Celery('dropboxBajada', broker="pyamqp://guest@localhost//")


@app2.task(no_ack=True)
def dropbox_bajada():
    newdata = bajar()
    if newdata is not None:
        procesarCelery.procesar_excel.apply_async(newdata)

