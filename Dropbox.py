import dropbox
import pendulum
import threading

token = "kvbe4Epe2OAAAAAAAAAACFLOXRE34frCMWlvINIBHhfGehOAifIhED4gxvvVfhyU"
dbx = dropbox.Dropbox(token)
mutex = threading.Lock()


def subida(data):
    now = pendulum.now('Europe/Madrid')
    fname = "/ParaProcesar/Datos_" + now.isoformat() + ".xlsx"
    response = dbx.files_upload(data, fname, mute=True)
    print("uploaded2:", response)


def bajar():
    mutex.Lock()
    path = '/ParaProcesar'
    array = dbx.files_list_folder(path).entries
    if array[0] is not None:
        file = dbx.files_download_to_file(path + '/' + array[0].name)
        with open(file, 'rb') as f:
            data = f.read()
        dbx.files_delete(path + '/' + array[0].name)
        mutex.unlock()
        return data
    else:
        mutex.unlock()
        return None


def subidaProcesada(data):
    Month = pendulum.now('Europe/Madrid')
    print("Subiendo")
    fname = "/Procesado/Datos_" + Month.isoformat() + ".xlsx"
    response = dbx.files_upload(data.encode(), fname, mute=True)
    print("uploaded2:", response)
