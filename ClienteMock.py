"""import numpy
import pandas
import dropboxSubidaParaProcesar"""

import Dropbox
result = Dropbox.bajar()


# Modificar esto para realizar la transferencia de archivos

"""
array = numpy.array([['', 'Col1', 'Col2'],
                         ['Row1', 1, 2],
                         ['Row2', 3, 4]])

dataframe = pandas.DataFrame(array)
writer = pandas.ExcelWriter('myDataFrame.xlsx')
dataframe.to_excel(writer, 'dataframe')
writer.save()

with open('myDataFrame.xlsx', 'rb') as f:
    data = f.read()

result = dropboxSubidaParaProcesar.dropbox_subida_parap(data)

result = result.get()

print(result)"""