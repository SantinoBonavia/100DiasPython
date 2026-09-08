## Simulación de un cajero automático
balance=180000
amount=int(input("Ingrese el monto a retirar: "))
if amount<=balance:
    balance-=amount
    print("Retiro exitoso. Su nuevo balance es: ", balance)
else:
    print("Fondos insuficientes. Su balance actual es: ", balance)