# Ejercicio 2: Mision TIC Colombia
import statistics
# Función que calculara la altura promedio
def altura_promedio(n: int):

    estaturas = [0] * n # Crea una lista de n ceros. No es necesario pero, al parecer, es más eficient

    for persona in range(n):
        while True:
            try:
                estatura = int(input('Ingrese la estatura en centimetros: '))
                break
            except:
                print('No ingreso un valor correcto')
        estaturas[persona] = estatura
    
    # Imprime las estaturas
    print(f'Estaturas: {estaturas}')
    
    # Imprime el valor promedio
    valor_promedio = sum(estaturas) / float(len(estaturas))
    print(valor_promedio)
    
    # Adicionalmente: Cálculo del promedio usando el paquete statistics
    # valor_promedio = statistics.mean(estaturas)
    # print(valor_promedio)


# Verifica que el input sea correcto
while True:
    try:
        n = int(input('Ingrese la cantidad de personas: '))
        break
    except:
        print('No ingreso un valor correcto')

# Llama a la función que calculará la altura promedio
altura_promedio(n)
