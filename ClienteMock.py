import pika
import numpy
import pandas
import os

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='fileTrans', durable=True)

# Modificar esto para realizar la transferencia de archivos

array = numpy.array([['', 'Col1', 'Col2'],
                         ['Row1', 1, 2],
                         ['Row2', 3, 4]])

dataframe = pandas.DataFrame(array)
writer = pandas.ExcelWriter('myDataFrame.xlsx')
dataframe.to_excel(writer, 'dataframe')
writer.save()

with open('myDataFrame.xlsx', 'rb') as f:
    data = f.read()

channel.basic_publish(exchange='',
                      routing_key='fileTrans',
                      body=data
                      )
os.remove('myDataFrame.xlsx')
connection.close()
