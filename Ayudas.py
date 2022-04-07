monto = int(input("Introduzca la cantidad a retirar: "))
billetes1000 = 0
billetes500= 0
billetes100= 0
billetes10 = 0
billetes1000=monto//1000
monto-=billetes1000*1000
billetes500=monto//500
monto-=billetes500*500
billetes100=monto//100
monto-=billetes100*100
billetes10=monto//10
print(billetes1000+billetes500+billetes100+billetes10)