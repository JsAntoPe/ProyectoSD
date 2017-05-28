from celery import Celery
import Dropbox
import procesarCelery

app2 = Celery('dropboxBajada', broker="pyamqp://guest@localhost//")


@app2.task(no_ack=True)
def dropbox_bajada():
    newdata = Dropbox.bajar()
    procesarCelery.procesar_excel.apply_async(newdata)
