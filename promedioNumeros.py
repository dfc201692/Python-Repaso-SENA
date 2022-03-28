def promedio(lista_numeros):
    suma = 0

    for i in lista_numeros:
        suma = suma + i

        return suma/len(lista_numeros)

numeros = [10, 20,30,40,50]
print(f'El promedio de numeros es {promedio(numeros)}')