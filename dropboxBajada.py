from celery import Celery
import Dropbox
import procesarCelery

app = Celery('dropboxBajada', broker="pyamqp://guest@localhost//")


@app.task(no_ack=True)
def dropbox_bajada():
    data = Dropbox.bajar()
    procesarCelery.procesar_excel(data, archivo)