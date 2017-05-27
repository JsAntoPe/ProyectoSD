from time import sleep

import pika
import tutorial.extraccion



connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='fileTrans', durable=True)

# Modificar esto para realizar la transferencia de archivos
for i in range(0, 5):
    result = tutorial.extraccion.ext.delay()
    sleep(2)

message = result.get()

channel.basic_publish(exchange='',
                      routing_key='fileTrans',
                      body=message,
                      properties=pika.BasicProperties(
                          delivery_mode=2,  # make message persistent
                      ))

connection.close()
