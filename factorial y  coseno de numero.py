from math import factorial,cos, tan

def operaciones():
    numero = int(input("Ingrese un numero : "))
    facto =  factorial(numero)
    coseno = cos(numero)
    tangente = tan(numero)
    print(f'Factorial de {numero} es {facto}')
    print(f'coseno de {numero} es {coseno}')
    print(f'tangente de {numero} es {tangente}')


operaciones()