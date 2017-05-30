from celery import Celery
from Dropbox import bajar
import procesarCelery

def dropbox_bajada():
    newdata = bajar()
    if newdata is not None:
        procesarCelery.procesar_excel(newdata)

