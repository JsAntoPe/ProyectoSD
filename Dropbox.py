import dropbox
import tempfile
import pendulum

token = "kvbe4Epe2OAAAAAAAAAACFLOXRE34frCMWlvINIBHhfGehOAifIhED4gxvvVfhyU"
dbx = dropbox.Dropbox(token)

now = pendulum.now('Europe/Madrid')

#En este hueco debe ir la toma de datos, para pasarla a la variable.
data = 'Buenas'
#

print("Subiendo")
fname = "/ParaProcesar/Datos_"+ now.isoformat()+".txt"
response = dbx.files_upload(data.encode(), fname, mute=True)
print("uploaded2:", response)