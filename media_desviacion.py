def media_desviacion(*numeros):
    total = 0

    for i in numeros:
        total = total + i

    media = total / len(numeros)

    total = 0

    for i in numeros:
        total += (i - media) ** 2
    desviacion = (total / len(numeros)) ** 0.5

    return media,desviacion

a,b,c,d,e = 10,20,30,40,50
media,desviacion = media_desviacion(a,b,c,d,e)
print(f'Media de {a} {b} {c} {d} {e} es {media}')
print(f'Desviacion  de {a} {b} {c} {d} {e} es {desviacion}')