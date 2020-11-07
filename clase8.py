import numpy as np
from scipy import stats

lista_numeros = [100, 9, -150, 800, 8, 8, -1, -55, -7, 58, 8, 6]  # la lista separa cada elemento con comas
arr_numeros = np.array(lista_numeros)  # creo el arreglo a partir de la lista, el arreglo lo separa con 2 espacios
print(arr_numeros)

# calculo la media
media = np.mean(arr_numeros)
print(f'La media es: {media}')
media_redondeo = round(media, 2)  # cantidad, el 2 son los decimales, sino pongo me redondea a la unidad
print(f'La media redondeada es: {media_redondeo}')

# calculo la moda
moda = stats.mode(arr_numeros)
print(f'La moda es: {moda}')

# calculo la mediana, es el Q2
mediana = np.median(arr_numeros)
print(f'La mediana es: {mediana}')

# calculo percentil Q1 y Q3
cuartil_1 = np.percentile(arr_numeros, 25, interpolation='midpoint')
print(f'El cuartil 1 es: {cuartil_1}')

cuartil_3 = np.percentile(arr_numeros, 75, interpolation='midpoint')
print(f'El cuartil 3 es: {cuartil_3}')

# varianza
varianza = np.var(arr_numeros)
print(f'La varianza es: {varianza}')
varianza_redondeo = round(varianza, 3)
print(f'La varianza redondeada es: {varianza_redondeo}')

# desvío estándar
desvio_e = np.std(arr_numeros)
print(f'El desvio estandar es: {desvio_e}')
print("-----------------")

# creo areglo: matriz uni-dimensional
lista_numeros2 = [1, 5, 80, 9, 27, 78, 150, 6]
arr_numeros2 = np.array(lista_numeros2)
print(arr_numeros2)
print(type(arr_numeros2))
print(arr_numeros2[0])  # posicion 0, primer elemento
print(arr_numeros2[-1])  # posicion -1, ultimo lugar
print("-----------------")

# creo areglo: matriz bi-dimensional
'''si en la lista hay distintos datos, float, string, lo hace igual pero me 
convierte todo al dato menos limitante, por ejemplo string si tengo palabras (con comillas)'''

lista_numeros3 = [[1, 5, 80], [9, 27, 78]]  # filas con 3 columnas
arr_numeros3 = np.array(lista_numeros3)
print(arr_numeros3)
print(type(arr_numeros3))
print(arr_numeros3[0, 1])  # accedo a elemento fila 0, columna 1
print(arr_numeros3[1, 2])
print("--------------")

# arreglos vacios
# arreglo de uno
unos = np.ones(3) # arreglo unidimensional de 3 elementos, en float
print(unos)

unos = np.ones((3, 4))  # filas y 4 columnas, en float
print(unos)

unos = np.ones(3, dtype=np.int64)  # cambio el tipo de dato a int
print(unos)
print("--------")

# arreglo de ceros
ceros = np.zeros(3) # arreglo unidimensional de 3 elementos, en float
print(ceros)

ceros = np.zeros((3, 4))  # filas y 4 columnas, en float
print(ceros)

ceros = np.zeros(3, dtype=np.int64)  # cambio el tipo de dato a int
print(ceros)
print("--------")

# arreglos aleatorios
numeros = np.random.random(3)  # crea numeros float positivos entre 0 y 1 aleatorios
print(numeros)

numeros = np.random.random((3, 4))
print(numeros)

numeros = np.random.randint(1, 8, 6, dtype=np.int64)  # cambio el float a int
print(numeros)
print("--------")

# arreglos de un solo valor
nueve = np.full((6, 6), 9)  # matriz 6x6 con 9
print(nueve)

