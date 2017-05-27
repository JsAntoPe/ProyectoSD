import pika
import Dropbox

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='fileTrans', durable=True)
print(' [*] Waiting for messages. To exit press CTRL+C')


def callback(ch, method, properties, body):
    Dropbox.subida(body)

channel.basic_qos(prefetch_count=1)
channel.basic_consume(callback,
                      queue='fileTrans',
                      no_ack=True)

channel.start_consuming()