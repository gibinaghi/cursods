'''
Crear un programa que pida al usuario dos números enteros y muestre por pantalla la
<n> entre <m> da un cociente <c> y un resto <r> donde <n> y <m> son los números
introducidos por el usuario, y <c> y <r> son el cociente y el resto de la división entera
respectivamente.
'''

num1 = int(input("Ingrese un número entero que será el dividendo: "))
num2 = int(input("Ingrese un núumero entero que será el divisor: "))

div = num1 // num2
resto = num1 % num2

print("La división entre " + str(num1) + " y " + str(num2) + " da como cociente " + str(div) + " y como resto " + str(resto))