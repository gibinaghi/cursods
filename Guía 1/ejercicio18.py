'''
Crear un programa que pida al usuario una palabra y luego muestre por pantalla una a
una las letras de la palabra introducida empezando por la última.
'''

def mostrar_letras(palabra):
    for i in reversed(palabra):
        print(i)


mostrar_letras("gimena")