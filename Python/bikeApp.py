# Biker app. Ver 1.0 
# Ivan Robayo. COL. 2022.  
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - READ.ME - - - - - - - - - - - - - - -
# Este programa interactua con el usuario para brindar información útil acerca de las especificaciones de la motocicleta que se requiera analizar.
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - GitHub: host-2077 - - - - - - - - - - - - - -

import time
print("Bienvenido a Biker App.")
user_name = input("Para iniciar ingresa tu nombre.")
user_bike = input("Asigna un nombre a tu motocicleta.")
intro_app = "Hola ", user_name, " soy ", user_bike, "\nEste programa y tu teclado servirán como herramientas para comunicarnos efectivamente.\n> > > >\n"

# Loop visual. 
 
for i in intro_app:
    print(i, end="", flush=True)
    time.sleep(0.1)

intro_vel_max = "Iniciemos con los análisis. \nEmpezaremos por la velocidad máxima que puedes alcanzar con tu peso actual.\n"

# Loop visual.

for i in intro_vel_max:
    print(i, end="", flush=True)
    time.sleep(0.1)

data_vel_max = "Necesitarás: \n- Cilindraje (CC) \n- Caballos de fuerza (HP) \n- Mi peso (" + user_bike + ") (KG), \n- Tu peso (" + user_name + ") (KG) \n- El peso de tu acompañante (KG)\n> > > > > >\n"

# Loop visual.

for i in data_vel_max:
    print(i, end="", flush=True)
    time.sleep(0.1)

# Ingreso de información a las variables requeridas.
cilindraje = input("Ingresa el cilindraje (CC)")
horse_power = input("Ingresa los caballos de fuerza (HP)")
bike_kg = input("Ingresa el peso de la motocicleta (KG)")
user_kg = input("¿Cuánto pesas? (KG)")
user2_kg = input("¿Cuánto pesa tu acompañante? (KG) > > > Si no tienes acompañante escribe '0'")
masa = float(bike_kg) + float(user_kg) + float(user2_kg)

# Loop visual.

loading = "A N A L I S A N D O D A T O S / "
loadingprompt = loading * 3
for i in loadingprompt:
    print(i, end="", flush=True)
    time.sleep(0.1)

# Cálculo velocidad máxima de la motocicleta. Velocidad máxima en Metros / Segundos (M/S).

velocidadMaxMS = (float(horse_power) / 0.3) * 2.5 * masa

# Velocidad máxima en KM/H

velocidadMaxKh = velocidadMaxMS * 3.6 / 1000

# Resultado velocidad máxima. 

print("\n")
vel_max = user_name, " con tu peso actual y con la capacidad de ", user_bike, " podrás alcanzar una velocidad máxima de ", round(velocidadMaxKh, 2), " KM/H", "\nIncreíble.\n"
for i in vel_max:
    print(i, end="", flush=True)
    time.sleep(0.1)

# Prueba de eficiencia de gasolina. - - - - - - - - - - PHASE 2 - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# Loop Visual 

loading2 = "F A S E 2 / "
loadingprompt2 = loading2 * 3
for i in loadingprompt2:
    print(i, end="", flush=True)
    time.sleep(0.1)

intro_gas_ef = "Ahora realizaremos una prueba de eficiencia de gasolina.\n Necesitarás tener el tanque de", user_bike, "a su máxima capacidad para iniciar la prueba.\nSúbete a la motocicleta, enciende el motor y verifica los siguientes datos\n> > > > > >\n"

# Loop Visual

for i in intro_gas_ef:
    print(i, end="", flush=True)
    time.sleep(0.1)


gas_tank_full = input("Ingresa la capacidad total del tanque > > > ")
odo_data_1 = input("¿Cuantos KM ves en tu odometro? > > >")
money_data = input("¿Cuanto pagaste por un galón de gasolina?")
prompt_gas_ef = "Ahora vas a utilizar tu motocicleta hasta que el tanque de gasolina esté a la mitad de su capacidad. Una vez tengas esta información el programa hará los análisis necesarios para determinar el rendimiento de", user_bike, "\nSi estás listo. Ready. Set. Go. > > > "

# Loop Visual

for i in prompt_gas_ef:
    print(i, end="", flush=True)
    time.sleep(0.1)
    
odo_data_2 = input("Ingresa los KM que ves en el odometro ahora que has terminado ")
distancia_recorrida = float(odo_data_2) - float(odo_data_1)
gas_tank_fact = float(gas_tank_full) / 2

# Cálculo de eficiencia de combustible. 

def g_per_km(gas_tank_fact, distancia_recorrida):
    return gas_tank_fact / distancia_recorrida

gas_ef_result = g_per_km(gas_tank_fact,distancia_recorrida)

gas_used = distancia_recorrida * gas_ef_result
money_used = int(gas_used) * int(money_data)
money_used_km = money_used / distancia_recorrida

# Resultado eficiencia de combustible.

gas_ef = "Perfecto. Has recorrido", distancia_recorrida, "KM.", "\nLo que quiere decir que tienes una eficiencia de comustible de ", gas_ef_result, "\n", user_bike, "esta costandote actualmente ", money_used_km, ".", "\nEn este recorrido y en este tiempo has gastado ", money_used, "."

for i in gas_ef:
    print(i, end="", flush=True)
    time.sleep(0.1)