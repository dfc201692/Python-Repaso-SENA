import random

def juego():
    dado1 = random.randint(1,6)
    dado2 = random.randint(1,6)
    print("Dado1: ",dado1)
    print("Dado2: ",dado2)
    suma = dado1 + dado2
    if(suma>7):
        print('Usted Gano')
    else:
        print('Usted perdio')


juego()
