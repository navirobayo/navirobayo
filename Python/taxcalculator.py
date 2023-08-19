income = float(input("Introduce el ingreso anual:"))

exfiscal = 556.2

if income <= 85528:
    porcentaje = (income*18)/100
    tax = porcentaje - exfiscal
    if tax <= 0:
        tax = 0 
    else:
        tax
    
else:
    if income <= 0:
        tax = 0 
    else:
        excedente = income - 85528
        porcentaje = (excedente*32)/100
        tax = 14839.2 + porcentaje
    

tax = round(tax, 0)
print("El impuesto es:", tax, "pesos")
