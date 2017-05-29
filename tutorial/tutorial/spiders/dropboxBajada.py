from celery import Celery
from Dropbox import bajar
import Mediador

app2 = Celery('dropboxBajada', broker="pyamqp://guest@localhost//")


@app2.task(name='worker2', no_ack=True)
def dropbox_bajada():
    newdata = bajar()
    if newdata is not None:
        Mediador.mediador(3, newdata)

