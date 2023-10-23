import matplotlib.pyplot as plot
from Lib_Complex_Vec_y_Mat import *


def final_Matrix(matrix):
    """Función que halla la magnitud de una matriz de imaginarios"""
    row = len(matrix)
    column = len(matrix[0])
    for i in range(row):
        numRow = []
        for j in range(column):
            numRow.append([(modulo(matrix[i][j]) ** 2), 0])

        matrix[i] =  numRow
    return matrix


def sistema_probabilistico_quantico(matrix, vectIni, clicks):
    """Función que simula un sistema probabilistico cuantico"""
    if (clicks >= 0) and (type(clicks) is int):
        length = len(vectIni)
        copyMatrix = matrix[:]

        for x in range(clicks):
            matrix = multi_matriz(matrix, copyMatrix)

        return final_Matrix(matrix)
    return -1


def sistema_probabilistico(matrix, vectIni, clicks):
    """Función que simula un sistema probabilistico clasico"""
    if (clicks >= 0) and (type(clicks) is int):
        length = len(vectIni)
        for x in range(clicks):
            vectIni = accion_matriz_vector(matrix, vectIni)
        return vectIni
    return -1


def canicas_booleanas(clicks, booleanMatrix, vectIni):
    """Funcion que simula experimento de canicas con coeficientes booleanos"""
    if (clicks >= 0 and type(clicks) is int):
        for c in range(clicks):
            vectIni = accion_vector_matriz_boolean(booleanMatrix, vectIni)

        return vectIni


def multiple_rendija_clasico(matrix, vectIni, clicks):
    """Función que simula el experimento de multiples rendijas clasico"""
    return sistema_probabilistico(matrix, vectIni, clicks)


def multiple_rendija_cuantico(matrix, vectIni, clicks):
    """Función que simula el experimento de multiples rendijas cuantico"""
    return sistema_probabilistico_quantico(matrix, vectIni, clicks)


def Diagrama(vector):
    """Funcion que grafica un diagrama de barras que muestre las probabilidades de un vector de estados y la imagen se puede guardar."""
    data = len(vector)
    x = np.array([x for x in range(data)])
    y = np.array([round(vector[x][0] * 100, 2) for x in range(data)])

    plot.bar(x, y, color='c', align='center')
    plot.title('Probabilidades Vector')
    plot.show()


