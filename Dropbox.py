import dropbox
import pendulum

token = "kvbe4Epe2OAAAAAAAAAACFLOXRE34frCMWlvINIBHhfGehOAifIhED4gxvvVfhyU"
dbx = dropbox.Dropbox(token)

def subida(file):
    now = pendulum.now('Europe/Madrid')

    #En este hueco debe ir la toma de datos, para pasarla a la variable.
    with open(file, "rb") as f:
        data = f.read()
    #

    print("Subiendo")
    fname = "/ParaProcesar/Datos_"+ now.isoformat()+".txt"
    response = dbx.files_upload(data.encode(), fname, mute=True)
    print("uploaded2:", response)

def bajar():
    return 0