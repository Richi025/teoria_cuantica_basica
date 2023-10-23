## Jose Ricardo Vasquez Vega
import math
import numpy as np
##Adición de vectores complejos.
def sum_complex_Vector(vec_a,vec_b):
    result = []
    if len(vec_a)==len(vec_b):
        for i in range(len(vec_a)):
            result.append(vec_a[i]+vec_b[i])
        return result
    return "Error, ajuste el tamaño de los vectores para que tengan el mismo tamaño"
##Inverso (aditivo) de un vector complejos
def inver_complex_Vector(vec_a):
    inver = []
    for i in range(len(vec_a)):
        inver.append(-1*vec_a[i])
    return inver
##Multiplicación de un escalar por un vector complejo.
def mult_escalar_complex_Vector(num,vec_a):
    mult = []
    for i in range(len(vec_a)):
        mult.append(num*vec_a[i])
    return mult
##Adición de matrices complejas.
def add_complex_matriz(matr_a, matr_b):
    colum_a = len(matr_a[0])
    colum_b = len(matr_b[0])
    fila_a = len(matr_a)
    fila_b = len(matr_b)
    add_matriz = []
    if fila_a == fila_b and colum_a == colum_b:
        for i in range(fila_a):
            fila = []
            for j in range(colum_a):
                fila.append(matr_a[i][j]+matr_b[i][j])
            add_matriz.append(fila)
    else:
        add_matriz = "Error, los tamaños son diferentes"
    return add_matriz

##Inversa (aditiva) de una matriz compleja.
def inv_add_complex_matriz(matr_a):
    fila_a = len(matr_a)
    colum_a = len(matr_a[0])
    for x in range(fila_a):
        for y in range(colum_a):
            matr_a[x][y] = -matr_a[x][y]
    return matr_a

##Multiplicación de un escalar por una matriz compleja.
def mult_complex_num_matriz(num, matr_a):
    fila_a = len(matr_a)
    colum_a = len(matr_a[0])
    for x in range(fila_a):
        for y in range(colum_a):
            matr_a[x][y] = num*matr_a[x][y]
    return matr_a

##Transpuesta de una matriz/vector
def transp_complex_matriz_vector(matr_a):
    if isinstance(matr_a[0], complex):
        return [[i] for i in matr_a]
    fila = len(matr_a)
    colum = len(matr_a[0])
    transp_matriz = [[0j] * fila for z in range(colum)]
    for x in range(fila):
        for y in range(colum):
            transp_matriz[y][x] = matr_a[x][y]
    return transp_matriz

##Conjugada de una matriz/vector
def conjugada_matriz(matr_a):
    if isinstance(matr_a[0], complex):
        return [x.conjugate() for x in matr_a]
    filas = len(matr_a)
    columnas = len(matr_a[0])
    conjugada = [[0j] * filas for k in range(columnas)]
    for i in range(filas):
        for j in range(columnas):
            conjugada[i][j] = matr_a[i][j].conjugate()
    return conjugada

##Adjunta (daga) de una matriz/vector
def adjunta_matriz(matr_a):
    conjugada_matr = conjugada_matriz(matr_a)
    adjunta = transp_complex_matriz_vector(conjugada_matr)
    return adjunta

##Producto de dos matrices (de tamaños compatibles)
def mult_matriz_compatibles(matr_a, matr_b):
    colum_a = len(matr_a[0])
    fila_a = len(matr_a)
    colum_b = len(matr_b[0])
    fila_b = len(matr_b)
    if colum_a != fila_b:
        return print("El tamaño de las matrices no es compatible")
    mult_matriz = [[0j] * colum_b for m in range(fila_a)]
    for x in range(fila_a):
        for y in range(colum_b):
            product_s = 0j
            for v in range(colum_a):
                product_s += matr_a[x][v] * matr_b[v][y]
            mult_matriz[x][y] = product_s
    return mult_matriz

def accion_matriz_vector(matr_a, vector):
    acción = mult_matriz_compatibles(matr_a, [[i] for i in vector])
    return [i[0] for i in acción]

#Producto interno de dos vectores
def produc_intern_cplx(vec_a, vec_b):
    init = 0
    vec_a = conjugada_matriz(vec_a)
    if len(vec_a) == len(vec_b):
        for i in range(len(vec_a)):
            init += vec_a[i] * vec_b[i]
        return init
    return "Error, tamaños tamaño"

# Norma de un vector
def norma_vec_cplx(vec_a):
    Norma = math.sqrt(produc_intern_cplx(vec_a,vec_a).real)
    return Norma

#Distancia entre dos vectores
def dist_vec_cplx(vec_a,vec_b):
    sumvec = sum_complex_Vector(vec_a,inver_complex_Vector(vec_b))
    distan = norma_vec_cplx(sumvec)
    return distan


#Valores  y vectores propios de una matriz
def vec_propios(matr_a):
    matr_a = np.asarray(matr_a)
    tamaño = matr_a.shape
    fil_a = tamaño[0]
    col_a = tamaño[1]
    if fil_a == col_a:
        valoresp, vectoresp = np.linalg.eig(matr_a)
        vectoresp = np.transpose(vectoresp)
        valorpro = np.round(valoresp, 2)
        vectorpro = np.round(vectoresp, 2)
        return  vectorpro[0]
    else:
        return "Error,la matriz ingresada no es cuadrada"

def val_propios(matr_a):
    matr_a = np.asarray(matr_a)
    tamaño = matr_a.shape
    fil_a = tamaño[0]
    col_a = tamaño[1]
    if fil_a == col_a:
        valoresp, vectoresp = np.linalg.eig(matr_a)
        vectoresp = np.transpose(vectoresp)
        valorpro = np.round(valoresp, 2)
        vectorpro = np.round(vectoresp, 2)
        return  valorpro
    else:
        return "Error,la matriz ingresada no es cuadrada"

# Calcula los valores propios y vectores propios
def val_propios_and_vec_propios(matrix):
    try:

        val_propios, vec_propios = np.linalg.eig(matrix)
        return val_propios, vec_propios
    except Exception as e:
        return str(e)

#Revisar si una matriz es unitaria
def matriz_unitaria(matr_a):
    if len(matr_a) == len(matr_a[0]):
            adjunt = adjunta_matriz(matr_a)
            checker = mult_matriz_compatibles(matr_a,adjunt)
            check = True
            for i in range(len(checker)):
                for j in range(len(checker)):
                    if (i == j and checker[i][j] != 1) or (i != j and checker[i][j] != 0):
                        check = False
                        break
            if check:
                resp = "La matriz ingresada es unitaria"
            else:
                resp = "La matriz ingresada NO es unitaria"
    else:
        resp = "Error, tamaño de matriz ingresada incorrecto"
    return resp

#Revisar si una matriz es Hermitiana

def matriz_hermitiana(matr_a):
    filas = len(matr_a)
    columnas = len(matr_a[0])
    adjunta = adjunta_matriz(matr_a)
    for i in range(filas):
        for j in range(columnas):
            if abs(matr_a[i][j] - adjunta[i][j]) > 1e-10:
                return False
    return True

def produc_tensor_matriz_vec(matr_a, matr_b):
    lmatra = len(matr_a)
    lmatrb = len(matr_b)
    lmatra_1 = len(matr_a[0])
    lmatrb_1 = len(matr_b[0])
    fila = lmatra * lmatrb
    col = lmatrb_1 * lmatra_1
    result = [[0 for i in range (col)] for k in range(fila)]
    for j in range(fila):
        for k in range(col):
            result[j][k] = (matr_a[j//lmatrb][k//lmatrb_1])*(matr_b[j%lmatrb][k%lmatrb_1])
    return result

def suma (num1, num2):
    rest1 = num1[0] + num2[0]
    rest2 = num1[1] + num2[1]
    return (rest1, rest2)




def multCplx(num1, num2):
    real1, imag1 = num1.real, num1.imag
    real2, imag2 = num2.real, num2.imag

    rest1 = real1 * real2 - imag1 * imag2
    rest2 = real1 * imag2 + imag1 * real2

    return (rest1, rest2)


def modulo (num):
    rest = (num[0] ** 2 + num[1] ** 2) ** (1/2)
    return rest

def multi_matriz(mat1, mat2):
    row1, col1 = len(mat1), len(mat1[0])
    row2, col2 = len(mat2), len(mat2[0])
    if (col1 == row2):
        result = [[(0, 0) for t in range(col2)] for x in range(row1)]
        for i in range(row1):
            for j in range(col2):
                current = (0, 0)
                for k in range(row2):
                    multi = multCplx(mat1[i][k], mat2[k][j])
                    current = suma(current, multi)
                result[i][j] = current
        return result
    print("Las dimensiones de las matrices, no son los adecuados para su multiplicacion")

def accion_vector_matriz_boolean(matrix, vector):
    row, col = len(matrix), len(matrix[0])
    length = len(vector)
    if (col == length):
        result = [False for c in range(row)]
        for i in range(row):
            check = True
            for j in range(col):
                check= matrix[i][j] and vector[j]
                result[i] = result[i] or check
        return result
    print("Las dimensiones de las matrices no son correctas")


def accion_matriz_vector2(matrix, vector):
    row, col = len(matrix), len(matrix[0])
    length = len(vector)
    if (col == length):
        result = [[0, 0] for x in range(row)]
        for i in range(row):
            for j in range(col):
                multi = multCplx(matrix[i][j], vector[j])
                result[i] = suma(result[i], multi)
        return result
    print("Las dimensiones de las matrices no son correctas")

if __name__ == '__main__':


    print(matriz_hermitiana([[complex(3, 0), complex(1, 2)],
                                [complex(1, -2), complex(0, -1)]]))
    print(produc_tensor_matriz_vec([[2,3],[1,4]],[[5,3,2],[1,0,2],[-2,5,6]]))