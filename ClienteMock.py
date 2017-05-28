import dropboxSubidaParaProcesar


# Modificar esto para realizar la transferencia de archivos


"""array = numpy.array([['', 'Col1', 'Col2'],
                         ['Row1', 1, 2],
                         ['Row2', 3, 4]])

dataframe = pandas.DataFrame(array)
writer = pandas.ExcelWriter('myDataFrame.xlsx')
dataframe.to_excel(writer, 'dataframe')
writer.save()

with open('myDataFrame.xlsx', 'rb') as f:
    data = f.read()"""

for i in range(0, 10):
    dropboxSubidaParaProcesar.dropbox_subida_parap()
