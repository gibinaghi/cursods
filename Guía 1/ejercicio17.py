'''
Crear un programa que muestre por pantalla la tabla de multiplicar del 1 al 10.
'''

def tabla(j):
    print(f" La tabla de {j}")
    for i in range(11):
        print(f" {j} * {i} = {j*i}")


for j in range(1, 11):
    print('------------')
    tabla(j) #cambiar esto, ver j