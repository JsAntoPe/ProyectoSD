import dropbox
import pendulum
import threading
import os
import pandas

token = "kvbe4Epe2OAAAAAAAAAACFLOXRE34frCMWlvINIBHhfGehOAifIhED4gxvvVfhyU"
dbx = dropbox.Dropbox(token)
#mutex = threading.Lock()
#mutex2 = threading.Lock()


def subida(data):
    now = pendulum.now('Europe/Madrid')
    fname = "/ParaProcesar/Datos_" + now.isoformat() + ".xlsx"
    response = dbx.files_upload(data, fname, mute=True)
    print("uploaded2:", response)


def bajar():
    bajar.mutex = threading.Lock()
    bajar.mutex.acquire()
    path = '/ParaProcesar'
    array = dbx.files_list_folder(path).entries
    if array[0] is not None:
        dbx.files_download_to_file(array[0].name, path + '/' + array[0].name)
        data = pandas.read_Excel(array[0].name)
        dbx.files_delete(path + '/' + array[0].name)
        bajar.mutex.release()
        os.remove(array[0].name)
        return data
    else:
        bajar.mutex.release()
        return None


def subidaProcesada(data):
    Month = pendulum.now('Europe/Madrid')
    print("Subiendo")
    fname = "/Procesado/Datos_" + Month.isoformat() + ".xlsx"
    response = dbx.files_upload(data.encode(), fname, mute=True)
    print("uploaded2:", response)


def bajarArchivoDatos():
    bajarArchivoDatos.mutex2 = threading.Lock()
    bajarArchivoDatos.mutex2.acquire()
    path = '/Procesado'
    array = dbx.files_list_folder(path).entries
    if array[0] is not None:
        dbx.files_download_to_file(array[0].name, path + '/' + array[0].name)
        with open(array[0].name, 'rb') as f:
            data = f.read()
        bajarArchivoDatos.mutex.release()
        os.remove(array[0].name)
        return data
    else:
        bajarArchivoDatos.mutex.release()
        return None

