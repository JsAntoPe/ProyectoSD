import matplotlib.pyplot as plt
import numpy

def procesar(newdata):
    plt.rcdefaults()
    fig, ax = plt.subplots()

    # Example data
    languages = newdata.columns.values
    values = newdata.as_matrix()
    y_pos = numpy.arange(len(languages))
    performance = values[0]

    ax.barh(y_pos, performance, xerr=0, align='center', color='green', ecolor='black')
    ax.set_yticks(y_pos)
    ax.set_yticklabels(languages)
    ax.invert_yaxis()   #labels read top-to-bottom
    ax.set_xlabel('Etiquetas')
    ax.set_title('Lenguajes')

    plt.show()
