# cursods
Ejercicios prácticos del curso "Python en Ciencia de Datos" de Chicas Programando

Ejercicio 5:
Crear un programa que pregunte el nombre del usuario y después de que el usuario lo introduzca muestre por pantalla <NOMBRE> tiene <n> letras.

Ejercicio 6:
Crear un programa que realice la siguiente operación aritmética [(3+2)/2*5]2. Mostrar el resultado por pantalla.

Ejercicio 7:
Crear un programa que pida al usuario dos números enteros y muestre por pantalla la <n> entre <m> da un cociente <c> y un resto <r> donde <n> y <m> son los números
introducidos por el usuario, y <c> y <r> son el cociente y el resto de la división entera respectivamente.

Ejercicio 9:
Una juguetería tiene mucho éxito en dos de sus productos: payasos y muñecas. Suele
hacer venta por correo y la empresa de logística les cobra por el peso de cada paquete
así que deben calcular el peso de los payasos y muñecas que saldrán en cada paquete
a demanda. Cada payaso pesa 112 g y cada muñeca 75 g. Crear un programa que lea
el número de payasos y muñecas vendidos en el último pedido y calcule el peso total
del paquete que será enviado. Mostrar el resultado por pantalla.

Ejercicio 10:
Crear un programa que pida al usuario su edad y muestra por pantalla si es mayor de
edad o no, siendo 18 años la mayoría de edad.

Ejercicio 11:
Crear un programa que almacene la cadena de caracteres contraseña en una variable,
pregunte al usuario por la contraseña e imprima por pantalla si la contraseña
introducida por el usuario coincide con la guardada en la variable.

Ejercicio 15:
Crear un programa para una empresa que tiene salas de juegos para todas las edades
y quiere calcular de forma automática el precio que debe cobrar a sus clientes por
entrar. El programa debe preguntar al usuario la edad del cliente y mostrar el precio de
la entrada. Si el cliente es menor de 4 años puede entrar gratis, si tiene entre 4 y 18
años debe pagar 500 y si es mayor de 18 años, 1000.

Ejercicio 16:
Crear un programa que pregunte al usuario su edad y muestre por pantalla todos los
años que ha cumplido (desde 1 hasta su edad).

Ejercicio 17:
Crear un programa que muestre por pantalla la tabla de multiplicar del 1 al 10.

Ejercicio 18:
Crear un programa que pida al usuario una palabra y luego muestre por pantalla una a
una las letras de la palabra introducida empezando por la última

EJERCICIO INTEGRADOR POO
● Crear una clase llamada Punto con sus dos coordenadas X e Y.
● Añadir un método constructor para crear puntos fácilmente. Si no se recibe una
coordenada, su valor será cero.
● Sobreescribir el método string, para que al imprimir por pantalla un punto
aparezca en formato (X,Y)
● Añadir un método llamado cuadrante que indique a qué cuadrante pertenece el
punto, teniendo en cuenta que si X == 0 e Y != 0 se sitúa sobre el eje Y, si X != 0
e Y == 0 se sitúa sobre el eje X y si X == 0 e Y == 0 está sobre el origen.
● Añadir un método llamado vector, que tome otro punto y calcule el vector
resultante entre los dos puntos.
● (Optativo) Añadir un método llamado distancia, que tome otro punto y calcule la
distancia entre los dos puntos y la muestre por pantalla. 
● Crear una clase llamada Rectángulo con dos puntos (inicial y final) que
formarán la diagonal del rectángulo.
● Añadir un método constructor para crear ambos puntos fácilmente, si no se
envían se crearán dos puntos en el origen por defecto.
● Añadir al rectángulo un método llamado base que muestre la base.
● Añadir al rectángulo un método llamado altura que muestre la altura.
● Añadir al rectángulo un método llamado area que muestre el area.
Experimentación
● Crear los puntos A(2, 3), B(5,5), C(-3, -1) y D(0,0) e imprimelos por pantalla.
● Consultar a qué cuadrante pertenecen el punto A, C y D.
● Consultar los vectores AB y BA.
● (Optativo) Consultar la distancia entre los puntos 'A y B' y 'B y A'.
● (Optativo) Determinar cual de los 3 puntos A, B o C, se encuentra más lejos del
origen, punto (0,0).
● Crear un rectángulo utilizando los puntos A y B.
● Consultar la base, altura y área del rectángulo.

HERENCIA
Ejercicio 1
Vamos a crear una clase llamada Persona. Sus atributos son: nombre, edad y DNI.
Construir los siguientes métodos para la clase:
● Un constructor, donde los datos pueden estar vacíos.
● mostrar(): Muestra los datos de la persona.
● esMayorDeEdad(): Devuelve un valor lógico indicando si es mayor de edad.

Ejercicio 2
Crea una clase llamada Cuenta que tendrá los siguientes atributos: titular (que es una
persona) y cantidad (puede tener decimales). El titular será obligatorio y la cantidad es
opcional. Construir los siguientes métodos para la clase:
● Un constructor, donde los datos pueden estar vacíos.
● El atributo no se puede modificar directamente, sólo ingresando o retirando
dinero.
● mostrar(): Muestra los datos de la cuenta.
● ingresar(cantidad): se ingresa una cantidad a la cuenta, si la cantidad introducida
es negativa, no se hará nada.
● retirar(cantidad): se retira una cantidad a la cuenta. La cuenta puede estar en
números rojos.

Ejercicio 3
Vamos a definir ahora una “Cuenta Joven”, para ello vamos a crear una nueva clase
CuantaJoven que deriva de la anterior. Cuando se crea esta nueva clase, además del
titular y la cantidad se debe guardar una bonificación que estará expresada en tanto por
ciento. Construir los siguientes métodos para la clase:
● Un constructor.
● En esta ocasión los titulares de este tipo de cuenta tienen que ser mayor de
edad., por lo tanto hay que crear un método esTitularValido() que devuelve
verdadero si el titular es mayor de edad pero menor de 25 años y falso en caso
contrario.
● Además la retirada de dinero sólo se podrá hacer si el titular es válido.
● El método mostrar() debe devolver el mensaje de “Cuenta Joven” y la
bonificación de la cuenta.
● Pensar los métodos heredados de la clase madre que hay que reescribir.
