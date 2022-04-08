def meses(numero_mes):
    meses = {
        1:"enero",
        2:"febrero",
        3:"marzo"
    }

    return meses.get(numero_mes,"Mes no valido")

numero_mes = int(input("Numero mes ? "))
print(meses(numero_mes))


