data = ''' data esto es asi'''
with open('archivo.txt', 'w+') as f:  # crea un archivo de txt con el texto de data
    f.write(data)
    f.seek(0)  # vuelve el cursor al principio
    print(f.read())
    print(f.tell())