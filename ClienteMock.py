import numpy
import pandas
import Procesar

array = pandas.DataFrame(data=numpy.array([[3, 2, 2, 1, 5, 3]]),
                         columns=['java', 'cSharp', 'javascript', 'python', 'html', 'php'],
                         index=['Row1'])
Procesar.procesar(array)
