#  sumar resta multiplicacion y division

"""
pedir al usuario: nombre, 2 numeros para sumar restar multiplicar y dividir
"""

nombre = None
num1 = None
num2 = None

print("ingresa tu nombre:")

nombre= input("decime tu nombre:")

num1 = int(input("ingresa el primer valor"))

num2 = int(input("ingresa el segundo valor:"))

resultado = num1 + num2

print(nombre, "tu suma es:", resultado)

resultado = num1 - num2

print("a tu resta es:", resultado)

resultado = num1 * num2

print("a tu multiplicacion es:", resultado)

resultado = num1 / num2

print("a tu division es:", resultado)
