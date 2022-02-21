#ht = horas trabajadas
#he = horas extra
#vhe = valor hora extra
#vthet = valor total horas extra trabajadas

horas_trabajadas = int(input('Digite la cantidad de horas trabajadas '))
hora = 4167

if(horas_trabajadas > 40):
    he = horas_trabajadas-40
    vhe = (hora+(hora*50)/100)
    vthet= (he * vhe)
    salario = ((hora * horas_trabajadas)+vthet)
    print ('Su salario es de: ',salario, ' pesos, el numero de horas extra trabajadas es de: ', he,', el valor de la hora extra es de ',vhe,' y el valor total de horas extra es de: ',vthet)
else:
    salario1 = (horas_trabajadas * hora)
    print ('su salario es de: ',salario1)

