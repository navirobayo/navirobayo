capacidadcamion = int(input("Ingresa la capacidad del camión:"))
sacas = int(input("Ingresa el peso de las sacas en muelle:")) 
protocolo = (sacas/20) 
camiones = 20
print("La cantidad actual a cargar el día de hoy es:", sacas)
print("La cantidad de camiones disponibles es:", camiones)

while camiones > 0:
    if protocolo < capacidadcamion:
        print("Carga", protocolo, "kg. y despacha")
        sacas -= protocolo
        print("La cantidad restante a cargar el día de hoy es:", sacas)
        camiones -= 1 
        print("Camiones restantes:", camiones)
    
    
    else:
        print("carga al máximo de la capacidad del camión y despacha")
        sacas = (protocolo - capacidadcamion)
        print("La cantidad restante por cargar en el muelle es:", sacas, "kg.")
        camiones -= 1
        print("Camiones restantes:", camiones)
        
print("No hay más camiones disponibles. Cargar mañana.")
