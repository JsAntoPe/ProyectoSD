import pika
import Dropbox

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='fileProcessing', durable=True)
print(' [*] Waiting for messages. To exit press CTRL+C')


def callback(ch, method, properties, body):
    Dropbox.subidaProcesada(body)


channel.basic_qos(prefetch_count=1)

channel.basic_consume(callback,
                      queue='fileProcessing')

channel.start_consuming()
