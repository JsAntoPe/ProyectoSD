import numpy
import pandas
import matplotlib.pyplot as plt


def procesar(newdata):
    plt.rcdefaults()
    fig, ax = plt.subplots()

    # Example data
    languages = newdata.columns.values
    y_pos = len(languages)
    performance = newdata.loc[0]

    ax.barh(y_pos, performance, align='center',
            color='green', ecolor='black')
    ax.set_yticks(y_pos)
    ax.set_yticklabels(languages)
    ax.invert_yaxis()  # labels read top-to-bottom
    ax.set_xlabel('Etiquetas')
    ax.set_title('Lenguajes')

    plt.show()
