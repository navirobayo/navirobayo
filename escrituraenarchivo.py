archivodelectura = []
documento = open("devices.txt", "a")
while True:
    nuevoitem = input("Ingresa el nuevo dispositivo")
    if nuevoitem == "exit":
        print("¡Todo listo!")
        break
    documento.write(nuevoitem + "\n")
documento.close()
documento = open("devices.txt", "r")
for i in documento:
    print(i)
documento.close()
