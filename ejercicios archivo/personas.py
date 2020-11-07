with open(r'D:\python\PycharmProjects\cursods\ejercicios archivo\personas.txt', 'r', encoding='utf-8') as f:  # lee un archivo de txt con el texto de data
    lineas = f.readlines()   # creo una lista
    f.close()

# creo el diccionario
personas = []  # creo el diccionario vacio
campos = ()
for linea in lineas:
    # Borro los saltos de línea y separamos
    campos = linea.replace("\n", "").split(";")  # split separa con los ;
    persona = {"id": campos[0],
               "nombre": campos[1],
               "apellido": campos[2],
               "nacimiento": campos[3]
               }
    personas.append(persona)  # agrega elementos a la lista


for p in personas:
    print(f'id: {p["id"]}')
    print(f'nombre: {p["nombre"]}')
    print(f'apellido: {p["apellido"]}')
    print(f'nacimiento: {p["nacimiento"]}')





