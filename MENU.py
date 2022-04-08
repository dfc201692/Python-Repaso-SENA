




def pedirNumeroEntero():
 
    correcto=False
    num=0
    while(not correcto):
        try:
            print ("")
            num = int(input("Seleccione una opción: "))
            correcto=True
        except ValueError:
            print('Error, introduce un numero entero')
     
    return num
 
salir = False
opcion = 0
 

from ast import Return
from math import factorial

def operaciones():
    numero = int(input("Ingrese un numero : "))
    facto =  factorial(numero)    
    print(f'Factorial de {numero} es {facto}')
    print ("")



def potencia():
    base = int(input("Ingrese un numero: "))
    potencia = int(input("Ingrese la potencia: "))
    a=pow(base,potencia)
    print(a)
    print ("")



def mediaaritmetica():
    lista = input("Ingrese una lisata de numeros: ").split(",")
    suma = 0
    cuantos_pos = 0
    for i in lista:
            num = int(i)
            if(num >0):
                suma += num
                cuantos_pos += 1
    media = suma/cuantos_pos

    print("media",media)
    print ("")


def fib():
    a = 0
    b = 1
    n = int(input("Ingrese los n terminos que desea imprimir de la sucesion de fibonacci: "))
    print(a,end=', ')
    print(b,end=', ')
    for i in range(n-2):
        c=a+b
        if i==n+3:
            print(c)
        else:
            print(c,end=', ')
            a=b
            b=c

    print ("")




while not salir:
    
    print ("MENU DE OPCIONES")
    print ("")
    print ("1. Factorial")
    print ("2. Potencia de un numero")
    print ("3. Media")
    print ("4. Fibonacci") 
    print ("5. Salir")
     
    #print ("Elige una opción")
 
    opcion = pedirNumeroEntero()
 
    if opcion == 1:
        #print ("factorial")
        operaciones()
        Return
        

    elif opcion == 2:
        #print ("potencia de un numero")
        potencia()
        Return

    elif opcion == 3:
        #print("Media")
        mediaaritmetica()
        Return
    elif opcion == 4:
        #print("fibonacci")
        fib()
        Return
        
    elif opcion == 5:
        salir = True
    else:
        print ("Introduce una opción")
 
print ("SALIR")



