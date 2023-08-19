year = int(input("Introduce un año:"))

if year < 1582:
    print("Sorry bro. Solo años de la era Gregoriana (Mayores a 1582)")
else: 
    if year % 4 != 0:
        print(year, "es un año común.")
    elif year % 100 != 0:
        print(year, "es un año bisiesto.")
    elif year % 400 != 0:
        print(year, "es un año común.")
    elif year % 400 == 0:
        print(year, "es un año bisiesto.")
