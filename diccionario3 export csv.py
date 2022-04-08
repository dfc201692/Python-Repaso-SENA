import csv 

diccionario = {'id':1025, 'nombre': 'Sharon', 'area':'sistemas'}

with open('empleados.csv','w',newline='')as archivo:
    almacenar = csv.writer(archivo)
    almacenar.writerows(diccionario.items())