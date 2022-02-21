peneultimo = 0 
ultimo = 1
siguiente = 0
i = 1

while(i<=10):
    print(siguiente)
    peneultimo = ultimo
    ultimo = siguiente
    siguiente = ultimo + peneultimo
    i +=1


