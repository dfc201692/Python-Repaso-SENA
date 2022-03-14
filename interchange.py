def interchange(numeros):
    aux = numeros[0]
    numeros[0] = numeros[1]
    numeros[1] = aux

numeros = [10, 15]
interchange(numeros)
print(numeros)