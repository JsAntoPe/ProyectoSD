from dropboxSubidaParaProcesar import dropbox_subida_parap
from dropboxBajada import dropbox_bajada
from procesarCelery import procesar_excel
from dropboxSubidaGrafica import dropbox_grafica

def intermediario(opcion, data):
    if opcion == 1:
        dropbox_subida_parap(data)
    if opcion == 2:
        dropbox_bajada()
    if opcion == 3:
        procesar_excel(data)
    if opcion == 4:
        dropbox_grafica.apply_async(data)


