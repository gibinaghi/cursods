'''
Crear un programa que pregunte el nombre del usuario y después de que el usuario lo
introduzca muestre por pantalla <NOMBRE> tiene <n> letras.
'''

nombre = input('Ingresa tu nombre: ')

total_caracteres = len(nombre)
print(nombre + " tiene " + str(total_caracteres) + " letras")
