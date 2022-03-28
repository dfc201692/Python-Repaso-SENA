def potencia_v1(base, exponente):
    pot = 1

    for i in range(exponente):
        pot = pot * base

    return pot

potencia_v2 = lambda base, exponente:base ** exponente

base = int(input('base: '))
exponente = int(input('exponente: '))
pot = potencia_v2(base,exponente)
print(f'{base} elevado a la {exponente} es {pot}')