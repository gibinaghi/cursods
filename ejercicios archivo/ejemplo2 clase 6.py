import re

texto = 'mi nombre es Gimena'
buscar = 'nombre'

if re.search(buscar, texto):
    print(f'La cadena contiene {buscar} entre sus caracteres')
else:
    print(f'La cadena no contiene {buscar} entre sus caracteres')

texto_encontrado = re.search(buscar, texto)   # si es falso no puedo aplicar los metodos
print(texto_encontrado.start())  # n de nombre esta en la posicion 3
print(texto_encontrado.end())  # despues de nombre es el caracter 9 que es el espacio
print(texto_encontrado.span())  # devuelve el 3 y 9 como tupla

cadena = 'Me gusta la programacion, yo se programacion, estudio programacion'
buscar = 'programacion'
print(re.findall(buscar, cadena))  # devuelve una lista
print(len(re.findall(buscar, cadena)))  # devuelve la cantidad de veces que aparece programacion
