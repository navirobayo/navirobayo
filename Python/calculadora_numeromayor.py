print("10/05/2022. Bienvenido a la calculadora.\nEste programa calculará el número de mayor cantidad dispuesto por el usuario.")

numero1 = int(input("Dame un número vaquero: "))
numero2 = int(input("Dame un número vaquero: "))
numero3 = int(input("Dame un número vaquero: "))

print("Estamos analizando los datos forastero...")

nganador = numero1

if numero2 > nganador: nganador = numero2

if numero3 > nganador: nganador = numero3

print("El número de mayor nomenclatura dispuesto por el viajero del tiempo es: ", nganador)
