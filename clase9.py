import numpy as np

array = np.array(([1, 2, 3, 5], [0, 1, 2, 8]))
print(array)
array_2 = np.append(array, ([1, 7, 3, 0], [0, 0, 0, 8]), axis=0)
print(array_2)  # agrega filas, axis=1 agrega columna
print("---------------")

np.random.seed(0)  # todas las veces ejecuta la misma matriz con seed
a = np.random.randint(0, 55, (6, 6))  # genera una matriz aleatoria
print(a[0, 3:5])  #slicing
print("----------")

# para copiar, sirve para copiar un data frame y trabajar con la copia
array_3 = np.copy(array)
print(id(array_3))  # id me dice el espacio de memoria que esta ocupando, no sobreescribo
array_4 = array[:]
print(id(array_4))
print("--------------")

# array boolean, sirve para chequear si hay datos faltantes por ejemplo, o comparar para saber si falta un dato
array = np.array([1, 0, 0, 1, 0], dtype=bool)  # da con true o false
print(array)
array_1 = np.array([1, 0, 0, 1, 0])  # da con 0 y 1
print(array_1)
array_2 = np.array([1, 0, 1, 1, 1], dtype=bool)
print(array_2)
# or devuelve true cuando al menos uno es true
array_3 = array | array_2
print(array_3)
# and devuelve true siempre que ambos son true, sino es false
array_4 = array & array_2
print(array_4)
#  logical_or es lo mismo que hacer con |
array_5 = np.logical_and(array, array_2)
print(array_5)
print(all(array))  # si todos son true o algo que se convierte a true, all seria como true, any es algunos
# or recorre y cuando encuetra el true ya devuelve el tru, no recorre mas las otras filas
# lo mismo con el anda y el false
# es muy comun en data frame q falten datos, hay que chequear si faltan datos, busco donde falta
# me fijo si borro, relleno las filas o columnas, no puede faltar datos
# broadcasting se usa cuando en los arreglos no hay la misma dimension




