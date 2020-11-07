import sys

# creo el archivo con a+ si no existe, pero en caso de existir se posiciona al final
with open(r'D:\python\PycharmProjects\cursods\ejercicios archivo\contador.txt', 'a+') as f:
    f.seek(0)  # vuelve el cursor al principio
    contenido = f.readlines()   # creo una lista
    print(contenido)
    # print(f.tell())  # tell devuelve la posicion del cursor

    if len(contenido) == 0:   # len devuelve la longitud de la lista
        contenido = "0"
        f.write(contenido)  # leo el contenido
    f.close()

# Vamos a intentar transformar el texto a un número
try:
    contador = int(contenido[0])  # contenido es lista, 0 busca el primer elemento y lo transforma a numero

    # dependiendo lo que el usuario quiera
    if len(sys.argv) == 2:    # sys.argv retorna una lista con todos los argumentos pasados por línea de comandos
        if sys.argv[1] == "inc":
            contador += 1   # si la longitud es 2 incrementa
        elif sys.argv[1] == "dec":
            contador -= 1  # si la longitud es 1 decrementa
    print('contenido', contador)

    # vuelvo a escribir los cambios en el fichero
    with open('contador.txt', 'w') as f:
        f.write(str(contador))
        f.close()

except:
    print("Error: Fichero corrupto.")

# lo paso en la terminal python main.py inc