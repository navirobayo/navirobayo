numeros_ganadores = [24, 45, 26, 59, 70]
numeros_usuario = [89, 78, 45, 59, 90]
found = False 
counter = 0

for i in range(len(numeros_ganadores)):
    found = numeros_ganadores[i] == numeros_usuario[i]
    if found:
        break
    
print("Has acertado con el número", i)

for i in numeros_usuario:
    if i in numeros_ganadores:
        counter += 1
        
print(counter)
