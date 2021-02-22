# Ejercicio 1: Mision TIC Colombia

calificaciones = list()

# Ingresar 10 calificaciones:
for i in range(10):
    while True:
        try: # Verifica que el input sea correcto
            calificacion = int(input(f'Ingrese la calificacion {i}: '))
            break
        except:
            print('Ingrese un valor correcto...')
            
    calificaciones.append(calificacion)

# Imprime todas las calificaciones
print(calificaciones)

# List comprehension (LC): Genera una lista que cumplan la condición: calificacion >= 7 a partir de la lista calificaciones
mayores_o_iguales_a_7 = [calificacion for calificacion in calificaciones if calificacion >= 7]

# Imprime la lista mayores_o_iguales_a_7
print(f'Calificaciones mayores o iguales a 7: {mayores_o_iguales_a_7}')

# Imprime la cantidad de elementos en la lista mayores_o_iguales_a_7
print(f'Hay {len(mayores_o_iguales_a_7)} mayores o iguales a 7')
print(f'Hay {len(calificaciones) - len(mayores_o_iguales_a_7)} menores a 7')


## Adicional
# En caso se desee guardar el índice de las calificaciones: key,value = index,calificacion
dict_index_calificacion = dict()

for index in range(len(calificaciones)):
    if calificaciones[index] >= 7:
        dict_index_calificacion[index] = calificaciones[index]
        
print(dict_index_calificacion)    