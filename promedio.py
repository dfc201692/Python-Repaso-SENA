def media(*numeros):
    total = 0

    for i in numeros:
        total += i

    return total / len(numeros)

a, b, c, d, e = 10, 15, 25, 30, 50
print('Promedio de ',a, ' ',b, ' ',c, ' ',d, ' ',e, ' es ', media(a,b,c,d,e))
print(f'Promedio de {a} {b} {c} {d} {e} es {media(a,b,c,d,e)}')