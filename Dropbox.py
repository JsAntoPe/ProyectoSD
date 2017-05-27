import dropbox
import pendulum
import pika
import time

token = "kvbe4Epe2OAAAAAAAAAACFLOXRE34frCMWlvINIBHhfGehOAifIhED4gxvvVfhyU"
dbx = dropbox.Dropbox(token)

connection1 = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel1 = connection1.channel()

channel1.queue_declare(queue='fileTrans', durable=True)
print(' [*] Waiting for messages. To exit press CTRL+C')

def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)
    time.sleep(body.count(b'.'))
    print(" [x] Done")
    ch.basic_ack(delivery_tag = method.delivery_tag)

channel1.basic_qos(prefetch_count=1)
channel1.basic_consume(callback,
                      queue='fileTrans')

def subida():
    now = pendulum.now('Europe/Madrid')

    #En este hueco debe ir la toma de datos, para pasarla a la variable.
    channel1.start_consuming()
    with open(file, "rb") as f:
        data = f.read()
    #

    print("Subiendo")
    fname = "/ParaProcesar/Datos_"+ now.isoformat()+".txt"
    response = dbx.files_upload(data.encode(), fname, mute=True)
    print("uploaded2:", response)

def bajar():
    return 0