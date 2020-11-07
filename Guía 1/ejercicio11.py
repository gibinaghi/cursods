'''
Crear un programa que almacene la cadena de caracteres contraseña en una variable,
pregunte al usuario por la contraseña e imprima por pantalla si la contraseña
introducida por el usuario coincide con la guardada en la variable.
'''

contrasena = 12568996

contrasena_ingresada = int(input("Ingrese su contraseña: "))

if contrasena_ingresada == contrasena:
    print("Su contraseña es correcta")
else:
    print("Su contraseña no es correcta, ingresela nuevamente")

# ver ejemplo video