horas = int (input("Ingrese las horas trabajadas:"))
tarifa = float(input("Ingrese la tarifa de cada hora: "))
hora_extras= 0
valor_hora_extra=0
total_extras=0

if(horas>40):
    hora_extras = horas-40
    valor_hora_extra = tarifa * 1.50
    total_extras = hora_extras * valor_hora_extra

salario = horas * tarifa + total_extras

print("Su salario es: ", salario)