from unicodedata import numeric


def fibonacci(numeros):
    penultimo = 0
    ultimo = 1
    siguiente = 0
    fibo = []

    for i in range(numeros):
        fibo.append(siguiente)
        penultimo = ultimo
        ultimo = siguiente
        siguiente = penultimo + ultimo

    return fibo

numeros = int(input('Numeros: '))
print(fibonacci(numeros))