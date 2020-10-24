import re

patron = 'hola$'
cadena = 'Buenos dias, hola'

if re.search(patron, cadena):
    print(True)