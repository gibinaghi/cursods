'''
Crear un programa que pregunte al usuario su edad y muestre por pantalla todos los
años que ha cumplido (desde 1 hasta su edad).
'''

entered_age = int(input("Enter your age: "))

age = 0
while age < entered_age:
    age += 1
    print(age)


