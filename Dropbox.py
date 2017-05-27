import dropbox
import pendulum

token = "kvbe4Epe2OAAAAAAAAAACFLOXRE34frCMWlvINIBHhfGehOAifIhED4gxvvVfhyU"
dbx = dropbox.Dropbox(token)


def subida(data):
    now = pendulum.now('Europe/Madrid')
    fname = "/ParaProcesar/Datos_" + now.isoformat() + ".xlsx"
    response = dbx.files_upload(data, fname, mute=True)
    print("uploaded2:", response)


def bajar():
    array = dbx.files_list_folder('/ParaProcesar').entries
    if array[0] is not None:
        with open(array[0], 'rb') as f:
            data = f.read()
        dbx.files_delete('/ParaProcesar/'+array[0])
        return data
    else:
        return None

def subidaProcesada(data):
    Month = pendulum.now('Europe/Madrid')

    # En este hueco debe ir la toma de datos, para pasarla a la variable.

    #
    print("Subiendo")
    fname = "/Procesado/Datos_" + Month.isoformat() + ".xlsx"
    response = dbx.files_upload(data.encode(), fname, mute=True)
    print("uploaded2:", response)
