import pika
import Dropbox
import threading

mutex = threading.Lock()

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='fileProcessing', durable=True)

# Modifcar esto para realizar la transferencia de archivos
while True:
    mutex.adquire()
    message = Dropbox.bajar()
    mutex.release()
    if message is not None:
        channel.basic_publish(exchange='',
                              routing_key='fileProcessing',
                              body=message,
                              properties=pika.BasicProperties(
                                  delivery_mode=2,  # make message persistent
                              ))
        print(" [i] Sent %r" % message)

connection.close()
