import math

class Punto:  # creo la clase
    def __init__(self, x=0, y=0):  # creo el constructor
        self.x = x
        self.y = y

    def __str__(self):  # sobreescribo el metodo string
        return f'El punto ({self.x}; {self.y})'  # imprimo el punto (x;y)

    def cuadrante(self):

        """ indico a que cuadrante pertenece el punto """

        if self.x == 0:
            if self.y > 0:
                print(f'{self} esta sobre el eje y positivo')
            elif self.y == 0:
                print(f'{self} esta en el origen de coordenadas')
            elif self.y < 0:
                print(f'{self} esta sobre el eje y negativo')

        elif self.x > 0:
            if self.y > 0:
                print(f'{self} pertenece al primer cuadrante')
            elif self.y == 0:
                print(f'{self} esta sobre el eje x positivo')
            elif self.y < 0:
                print(f'{self} pertenece al cuarto cuadrante')

        elif self.x < 0:
            if self.y > 0:
                print(f'{self} pertenece al segundo cuadrante')
            elif self.y == 0:
                print(f'{self} esta sobre el eje x negativo')
            elif self.y < 0:
                print(f'{self} pertenece al tercer cuadrante')

    def vector(self, p):  # puede un método de la clase producir interacciones entre muchos objetos de la misma

        # punto= Punto() herencia indirecta en el lugar de p
        """ vector que tome otro punto y calcule el vector resultante entre los dos puntos."""

        return f'El vector entre {self} y {p} es ({p.x - self.x}, {p.y - self.y})'

    def distancia(self, p):

        """ Método llamado distancia, que tome otro punto y calcule la
        distancia entre los dos puntos y la muestre por pantalla. """

        d = math.sqrt((p.x - self.x)**2 + (p.y - self.y)**2)
        print(f'La distancia entre los puntos {self} y {p} es {d}')

class Rectangulo:
    def __init__(self, pInicial=Punto(), pFinal=Punto()):  # creo el constructor, indico que los objetos deben ser de la clase Punto
        self.pInicial = pInicial
        self.pFinal = pFinal

        # no llamo los atributos igual que los metodos xq podria sobreescribir

    def base(self):
        base = abs(self.pFinal.x - self.pInicial.x)
        return base

    def altura(self):
        altura = abs(self.pFinal.y - self.pInicial.y)
        return altura

    def area(self):
        area = self.base() * self.altura()
        print(f'El área del rectángulo es {area}')


# creo los puntos y los imprimo por pantalla
a = Punto(2, 3)
b = Punto(5, 5)
c = Punto(-3, -1)
d = Punto(0, 0)
print(f'El punto A = {a}')
print(f'El punto B = {b}')
print(f'El punto C = {c}')
print(f'El punto D = {d}')
print('--------------------')

# consulto a que cuadrante pertenecen
a.cuadrante()
c.cuadrante()
d.cuadrante()
print('--------------------')

# consulto los vectores
vector_ab = a.vector(b)  # vector AB
print(vector_ab)
vector_ba = b.vector(a)  # vector BA
print(vector_ba)
print('--------------------')

# distancia
distancia_ab= a.distancia(b)
distancia_ac= a.distancia(c)
print('--------------------')

# creo el rectángulo
rectangulo_ab = Rectangulo(a, b)

# consulto base del rectángulo
print(f'La base es: {rectangulo_ab.base()}')
print(f'La base es: {rectangulo_ab.altura()}')
rectangulo_ab.area()


