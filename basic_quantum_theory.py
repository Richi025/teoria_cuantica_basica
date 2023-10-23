import Lib_Complex_Vec_y_Mat as lc
import numpy as np
import math

# Importar la constante de Planck reducida desde el módulo scipy.constants
import numpy as np
from scipy.constants import hbar

def probSisLinea(vecEstado, pos):
    if pos >= 0 and pos <= len(vecEstado):
        moduloCuadrado = lc.norma_vec_cplx(vecEstado)
        modulo_pos = abs(vecEstado[pos])
        prob = (modulo_pos**2)/(moduloCuadrado**2)
        return prob
    return "la posicion es incorrecta"


def normalizeVector(vector):
    magnitude = math.sqrt(sum(abs(v) ** 2 for v in vector))
    if magnitude == 0:
        return vector
    normalizeVector = [v / magnitude for v in vector]
    return normalizeVector

def probabilityOfTransit(vector_1, vector_2):
    vector_1_normalize = normalizeVector(vector_1)
    vector_2_normalize = normalizeVector(vector_2)
    probaTransit = (abs(lc.produc_intern_cplx(vector_1_normalize, vector_2_normalize)))**2
    return probaTransit

def amplitudeOfTransit(vector_1, vector_2):
    vector_1_normalize = normalizeVector(vector_1)
    vector_2_normalize = normalizeVector(vector_2)
    probaTransit = (lc.produc_intern_cplx(vector_1_normalize, vector_2_normalize))
    return probaTransit

def mediaObservableKet(matrixObservable, Ket_vector):
    if(lc.matriz_hermitiana(matrixObservable)):
        result = lc.produc_intern_cplx(lc.accion_matriz_vector(matrixObservable, Ket_vector), Ket_vector).real
        return result
    return "La matriz observable no es hermitania"

def delta (matrixObservable,Ket_vector):
    fila = len(matrixObservable)
    delta = matrixObservable - lc.mult_complex_num_matriz(mediaObservableKet(matrixObservable,Ket_vector),np.eye(fila))
    return delta
def variationObservableKet(matrix,vector):
    if (lc.matriz_hermitiana(matrix)):
        delt = delta(matrix,vector)
        variation = mediaObservableKet(lc.mult_matriz_compatibles(delt,delt),vector)
        return variation
    return "La matriz observable no es hermitania"


def val_propios_and_probability_of_transition_to_vec_propios(vec_state, matrix_observable):
    val_propios = lc.val_propios_and_vec_propios(matrix_observable)[0]
    vec_propios = lc.val_propios_and_vec_propios(matrix_observable)[1]
    probabilities = []
    for i in vec_propios:
        probabilities.append(probabilityOfTransit(vec_state, i))
    return val_propios, probabilities

def sistem_dinamic(vec_state, matrix_s):
    end_state = vec_state
    for j in matrix_s:
        end_state = lc.accion_matriz_vector(j,end_state)
    return end_state

if __name__ == '__main__':

    print(probabilityOfTransit([complex(0, 1), complex(-1, 0)],[complex(1, 0), complex(0, -1)]))

    print(amplitudeOfTransit(
        [complex(2, 1), complex(-1, 3)], [complex(1, 1), complex(1, -1)]))

    print(amplitudeOfTransit(
        [complex(-1, -4), complex(2, -3), complex(-7, 6), complex(-1, 1), complex(-5, -3), complex(5, 0), complex(5, 8),
         complex(4, -4), complex(8, -7), complex(2, -7)],
        [complex(2, 1), complex(-1, 2), complex(0, 1), complex(1, 0), complex(3, -1), complex(2, 0), complex(0, -2),
         complex(-2, 1), complex(1, -3), complex(0, -1)]))


    print(mediaObservableKet([[complex(3, 0), complex(1, 2)],
                               [complex(1, -2), complex(-1, 0)]],
                              [complex(math.sqrt(2)/2,0),complex(-math.sqrt(2)/2,0)]))


    print(mediaObservableKet([[complex(1, 0), complex(0, -1)],
                               [complex(0, 1), complex(2, 0)]],
                              [complex(math.sqrt(2) / 2, 0), complex(0, math.sqrt(2) / 2)]))

    print(variationObservableKet([[complex(3, 0), complex(1, 8)],
                              [complex(1, -8), complex(-1, 0)]],
                             [complex(math.sqrt(2) / 2, 0), complex(-math.sqrt(2) / 2, 0)]))

    print(variationObservableKet([[complex(3, 3), complex(1, 5)],
                              [complex(1, -5), complex(-8, 0)]],
                             [complex(math.sqrt(2) / 2, 0), complex(-math.sqrt(2) / 2, 0)]))

    print("/")
    print("Problema 4.3.1")
    print("Los posibles estados despues de haber realizado una medición son:")
    print(lc.val_propios_and_vec_propios([[complex(0, 0), complex(hbar/2, 0)],
                                            [complex(hbar/2, 0), complex(0, 0)]])[1])

    print("/")
    print("Problema 4.3.2")
    result = val_propios_and_probability_of_transition_to_vec_propios([complex(1, 0), complex(0, 0)],
                                                                    [[complex(0, 0), complex(hbar/2, 0)],
                                                                    [complex(hbar/2, 0), complex(0, 0)]])
    landa1 = result[0][0]
    landa2 = result[0][1]
    probabilidad1 = result[1][0]
    probabilidad2 = result[1][1]
    print("probabilidad1 =", probabilidad1)
    print("probabilidad2 =", probabilidad2)
    print("probabilidad1 * landa1 + probabilidad2  * landa2 =", round((probabilidad2 * landa1 + probabilidad2  * landa2).real))

    print("/")
    print("Problema 4.4.1")
    u1 = [[complex(0, 0), complex(1, 0)],
          [complex(1, 0), complex(0, 0)]]
    u2 = [[complex(math.sqrt(2)/2, 0), complex(math.sqrt(2)/2, 0)],
          [complex(math.sqrt(2)/2, 0), complex(-math.sqrt(2)/2, 0)]]
    print("u1 * u1 =", lc.mult_matriz_compatibles(u1, lc.adjunta_matriz(u1)))
    print("u2 * u2 =", lc.mult_matriz_compatibles(u2, lc.adjunta_matriz(u2)))
    u3 = lc.mult_matriz_compatibles(u1, u2)
    print("u3 = u1 * u2 =", u3)
    print("u3 * u3 =", lc.mult_matriz_compatibles(u3, lc.adjunta_matriz(u3)))

    print("/")
    print("Problema 4.4.2")
    vec_state = [complex(1, 0), complex(0, 0), complex(0, 0), complex(0, 0)]
    u = [[complex(0, 0), complex(1/math.sqrt(2), 0), complex(1/math.sqrt(2), 0), complex(0, 0)],
         [complex(0, 1/math.sqrt(2)), complex(0, 0), complex(0, 0), complex(1/math.sqrt(2), 0)],
         [complex(1/math.sqrt(2), 0), complex(0, 0), complex(0, 0), complex(0, 1/math.sqrt(2))],
         [complex(0, 0), complex(1/math.sqrt(2), 0), complex(-1/math.sqrt(2), 0), complex(0, 0)]]
    for i in range(3):
        vec_state = lc.accion_matriz_vector(u,vec_state)
    print("El estato despues de tres iteraciones es:")
    print(vec_state)
    print("La probabilidad de estar en el punto 3 es :",abs(vec_state[3])**2)

    print("/")
    print("Los problemas 4.5.2 y 4.5.3 se encuentran en el README")