from pyasn1_modules.rfc2315 import data
import pika
import sys
#import extraccion

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='fileTrans', durable=True)

"""for i in range(0, 5):
    result = extraccion.ext.delay()"""

#Modifcar esto para realizar la transferencia de archivos
message = ' '.join(sys.argv[1:]) or "Hello World!"


channel.basic_publish(exchange='',
                      routing_key='fileTrans',
                      body=message,
                      properties=pika.BasicProperties(
                          delivery_mode=2,  # make message persistent
                      ))
print(" [x] Sent %r" % message)
connection.close()