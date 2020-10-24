# creo lo que va a ir en el archivo de texto
data = ''' 
1;Carlos;Pérez;05/01/1989
2;Manuel;Heredia;26/12/1973
3;Rosa;Campos;12/06/1961
4;David;García;25/07/2006'''

with open('personas.txt', 'w+') as f:  # crea un archivo de txt con el texto de data
    f.write(data)
    f.seek(0)  # vuelve el cursor al principio
    lineas = f.readlines()   # creo una lista
    print(lineas)
    print(f.tell())  # tell devuelve la posicion del cursor
    f.close()

# creo el diccionario
personas = []  # creo el diccionario vacio
for linea in lineas:
    # Borro los saltos de línea y separamos
    campos = linea.replace("\n", "").split(";")  # split separa con los ;
    persona = {"id": campos[0],
               "nombre": campos[1],
               "apellido": campos[2],
               "nacimiento": campos[3]
               }
    personas.append(persona)

for p in personas:
    print(f'id: {p["id"]}')
    print(f'nombre: {p["nombre"]}')
    print(f'apellido: {p["apellido"]}')
    print(f'nacimiento: {p["nacimiento"]}')





