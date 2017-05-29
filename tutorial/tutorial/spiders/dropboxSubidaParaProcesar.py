from celery import Celery
import dropboxBajada
from Dropbox import subida
import matplotlib.pyplot

def dropbox_subida_parap(data):
    subida(data)
    print("subida")
    dropboxBajada.dropbox_bajada()

