class Persona:
    def __init__(self, nombre="", edad=0, dni=0):
        self.nombre = nombre
        self.edad = edad
        self.dni = dni

    def mostrar(self):
        return f'El nombre es {self.nombre}, su edad es {self.edad} y su dni es {self.dni}'

    def esMayorDeEdad(self):
        if self.edad >= 18:
            print('La persona es mayor de edad')
        else:
            print('La persona es menor de edad')


class Cuenta:  # superclase de cuenta joven
    def __init__(self, titular=Persona(), cantidad=0.0):
        self.titular = titular
        self.cantidad = cantidad

    def mostrar(self):
        print(f'La persona {self.titular.nombre} tiene {self.cantidad} en su cuenta')

    '''El atributo no se puede modificar directamente, sólo ingresando o retirando dinero...como hago esto????'''

    def ingresar(self):
        cantidad = float(input('Escriba el monto a ingresar: '))
        if cantidad >= 0:
            ingreso = self.cantidad + cantidad
            self.cantidad = ingreso  # guardo el valor modificado de la suma asi despues me lo resta de eso
            print(f'El monto ingresado fue: {cantidad} en total tiene: {ingreso}')

    def retirar(self):
        cantidad = float(input('Escriba el monto a retirar: '))
        retiro = self.cantidad - cantidad
        print(f'El monto retirado fue: {cantidad} en total le queda: {retiro}')


class CuentaJoven(Cuenta):    # herencia
    def __init__(self, titular=Persona(), cantidad=0, bonificacion=0.0):   # tambien puedo poner float(0), titular=Persona() herencia indirecta
        super().__init__(titular, cantidad)
        self.bonificacion = bonificacion

    def esTitularValido(self):
        if 18 <= self.titular.edad < 25:
            return True
        else:
            return False

    def mostrar(self):
        print(f'Datos de la cuenta')
        print(f'Titular: {self.titular.nombre}')
        print(f'Cantidad: {self.cantidad}')
        print(f'Bonificación: {self.bonificacion}')

    def retirar(self, retiro):     # VER que me marca acá
        if self.esTitularValido():
            self.cantidad -= retiro
            print(f'El monto retirado fue: {retiro}')


# creo las persona
persona1 = Persona('Juan Perez', 15, 35869144)
print(persona1.mostrar())
persona1.esMayorDeEdad()
print('----------')
persona2 = Persona('Maria Rodriguez', 20, 35829147)
print(persona2.mostrar())
persona2.esMayorDeEdad()

# creo la cuenta
print('----------')
cuenta1 = Cuenta(persona1, 1500)
cuenta1.mostrar()
cuenta1.ingresar()
cuenta1.retirar()
print('----------')
cuenta2 = Cuenta(persona2, 3000)
cuenta2.mostrar()
cuenta2.ingresar()
cuenta2.retirar()
print('----------')

# creo la cuenta joven
print('---------Cuenta joven 1-----------')
cuenta_joven1 = CuentaJoven(persona1, 2000, 200)
print(cuenta_joven1.esTitularValido())  # si no pongo print no veo el true y false
cuenta_joven1.retirar(500)
cuenta_joven1.mostrar()
print('---------Cuenta joven 2-----------')
cuenta_joven2 = CuentaJoven(persona2, 5000, 300)
print(cuenta_joven2.esTitularValido())  # si no pongo print no veo el true y false
cuenta_joven2.retirar(800)
cuenta_joven2.mostrar()



