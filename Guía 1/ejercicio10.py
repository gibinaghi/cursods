'''
Crear un programa que pida al usuario su edad y muestra por pantalla si es mayor de
edad o no, siendo 18 años la mayoría de edad.
'''

age = int(input("Ingrese su edad: "))

# analizo si es mayor de edad o no

if age >= 18:
    print("La persona es mayor de edad")
else:
    print("La persona es menor de edad")