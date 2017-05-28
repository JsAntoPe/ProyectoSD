import numpy
import pandas
import Dropbox
import Procesar
"""
array = pandas.DataFrame(data=numpy.array([[3, 2, 2, 1, 5, 3]]),
                         columns=['java', 'C#', 'javascript', 'python', 'html', 'php'],
                         index=['Row1'])

Dropbox.subida(array)
"""
data = Dropbox.bajar()
imagen = Procesar.procesar(data)
Dropbox.subidaGrafica(imagen)
