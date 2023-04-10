# Biker app. Ver 1.0 
# Ivan Robayo. COL. 2022.  
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - READ.ME - - - - - - - - - - - - - - -
# Este programa interactua con el usuario para brindar información útil acerca de las especificaciones de la motocicleta que se requiera analizar.
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - GitHub: host-2077 - - - - - - - - - - - - - -


# Prueba de eficiencia de gasolina. - - - - - - - - - - PHASE 2 - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

user_bike = input("Ingresa el nombre de tu motocicleta.")
intro_gas_ef = "Ahora realizaremos una prueba de eficiencia de gasolina.\n Necesitarás tener el tanque de", user_bike, "a su máxima capacidad para iniciar la prueba.\nSúbete a la motocicleta, enciende el motor y verifica los siguientes datos\n> > > > > >\n"

gas_tank_full = input("Ingresa la capacidad total del tanque > > > ")
odo_data_1 = input("¿Cuantos KM ves en tu odometro? > > >")
money_data = input("¿Cuanto pagaste por un galón de gasolina?")
prompt_gas_ef = "Ahora vas a utilizar tu motocicleta hasta que el tanque de gasolina esté a la mitad de su capacidad. Una vez tengas esta información el programa hará los análisis necesarios para determinar el rendimiento de", user_bike, "\nSi estás listo. Ready. Set. Go. > > > "
odo_data_2 = input("Ingresa los KM que ves en el odometro ahora que has terminado ")
distancia_recorrida = float(odo_data_2) - float(odo_data_1)
gas_tank_fact = float(gas_tank_full) / 2

# Definimos las funciones que se utilizaran de antemano en la siguiente computación. 

def g_per_km(gas_tank_fact, distancia_recorrida):
    return gas_tank_fact / distancia_recorrida

gas_ef_result = g_per_km(gas_tank_fact,distancia_recorrida)

gas_used = distancia_recorrida * gas_ef_result
money_used = gas_used * float(money_data)
money_used_km = money_used / float(distancia_recorrida)

# Resultado eficiencia de combustible.

gas_ef = "Perfecto. Has recorrido", distancia_recorrida, "KM.", "\nLo que quiere decir que tienes una eficiencia de comustible de ", gas_ef_result, "\n", user_bike, "esta costandote actualmente ", money_used_km, ".", "\nEn este recorrido y en este tiempo has gastado ", money_used, "."

print(gas_ef)