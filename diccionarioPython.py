meses_1 = {1: "enero", 2: "febrero",3:"marzo",4:"abril",5:"mayo",6:"junio",7:"julio"}
meses_2 = {8: "agosto", 9: "septimbre",10:"ocbubre",11:"noviembre",12:"diciembre"}
meses_1.update(meses_2) #se concatena meses_1 y meses_2

del(meses_1[12]) #elimina por valor
print(meses_1)



"""
###print(meses_1)
print(meses_1[7])
meses_1[8] = "agosto"
meses_1[1] = "xxxxxxx"
print(meses_1)
#meses.clear() eliminar 
"""