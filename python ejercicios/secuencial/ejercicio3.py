# sumar restar y multiplicar

"""
pedir al usuario nombre y 2 valores para sumar restar y multiplicar
"""

nombre = None
num1= None
num2= None

print("ingresa tu nombre")

nombre = input("decime tu nombre:")

num1 = int(input("ingresa el primer valor:"))

num2 = int(input("ingresa el segundo valor:"))

resultado = num1 + num2

print(nombre, "tu suma es:", resultado)

resultado = num1 - num2

print( "tu resta es:", resultado)

resultado = num1 * num2

print("tu multiplicacion es:", resultado)
