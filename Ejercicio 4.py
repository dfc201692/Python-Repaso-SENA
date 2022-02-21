numero1 = int(input('Digite el numero 1 '))
numero2 = int(input('Digite el numero 2 '))
numero3 = int(input('Digite el numero 3 '))

if (numero1 == numero2) and (numero1==numero3):
    print ('Todos los numeros son iguales')
else:
    if (numero1 > numero2) and (numero1 > numero3):
        print ('El numero mayor es: ',numero1)
    else:
        if(numero2 > numero1) and (numero2 > numero3):
            print ('El numero mayor es: ',numero2)
        else:
            print ('El numero mayor es: ',numero3)
