def uno():
    return "uno"

def dos():
    return "dos"

def tres():
    return "tres" 

def numero_en_letras(num):
    numeros = {
        1:uno(),
        2:dos(),
        3:tres()
    }

    return numeros.get(num,"Numero no encontrado")

numero = int(input("Ingrese un numero: "))
print(numero_en_letras(numero))