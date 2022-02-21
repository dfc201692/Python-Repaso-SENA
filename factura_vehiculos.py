kilometros = int (input('Kilometros: '))
tarifa_fija = 100000
pago_kilometros_extra1 = 0
pago_kilometro_extra2 = 0

if(kilometros <= 1000):
    pago_kilometros_extra1 = (kilometros - 300)*1000
else:
    pago_kilometro_extra2 = 700000+ (kilometros-1000)*500

pago = tarifa_fija + pago_kilometros_extra1 + pago_kilometro_extra2
print('Pago total = $',pago)