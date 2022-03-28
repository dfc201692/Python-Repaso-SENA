def nombre_mes(numero_mes):
    meses = {
        1:"enero",
        2: "febrero",
        3:"marzo",
        4:"abril",
        5:"mayo",
        6:"junio",
        7:"julio"
    }
    
    return meses.get(numero_mes,"Mes no valido")
numero_mes = int(input("Digita Numero del mes: "))
print(nombre_mes(numero_mes))