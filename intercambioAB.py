def intercambio (n1,n2):
    aux = n1
    n1 = n2
    n2 = aux

    return n1, n2

a = int(input("Ingrese a: "))
b = int(input("Ingrese b: "))
a, b = intercambio(a,b)
print('a = ',a)
print('b = ',b)