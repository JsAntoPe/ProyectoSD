import pika
import Dropbox

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='fileProcessing', durable=True)

# Modifcar esto para realizar la transferencia de archivos
for i in range(0, 99):
    message = Dropbox.bajar()

    channel.basic_publish(exchange='',
                          routing_key='fileProcessing',
                          body=message,
                          properties=pika.BasicProperties(
                              delivery_mode=2,  # make message persistent
                          ))
    print(" [i] Sent %r" % message)

connection.close()
