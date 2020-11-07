'''
Una juguetería tiene mucho éxito en dos de sus productos: payasos y muñecas. Suele
hacer venta por correo y la empresa de logística les cobra por el peso de cada paquete
así que deben calcular el peso de los payasos y muñecas que saldrán en cada paquete
a demanda. Cada payaso pesa 112 g y cada muñeca 75 g. Crear un programa que lea
el número de payasos y muñecas vendidos en el último pedido y calcule el peso total
del paquete que será enviado. Mostrar el resultado por pantalla.
'''

# declaro variables - peso (weigth)
weight_clown = 112
weight_doll = 75

# ingreso pedido (cantidad)
print("Ingrese su pedido")
pedido_clown = int(input("Ingrese su pedido de payasos: "))
pedido_doll = int(input("Ingrese su pedido de muñecas: "))

# calculo peso total = pedido por peso
clown_total = pedido_clown * weight_clown
doll_total = pedido_doll * weight_doll

# imprimo total de muñecas y payasos
print(clown_total)
print(doll_total)

# sumo los pesos totales y lo muestro por pantalla

suma = clown_total + doll_total
print(f"El peso total es {suma}")





