#####################################################################
# Declaración de Funciones Lamda                                    
#####################################################################
                                                                   
#   Sintaxis: lambda arguments : expression                         
                                                                   
#   Ejemplos:                                                       
#       x = lambda a : a + 10                                       
#       print(x(5))                                                 
                                                                   
#####################################################################

from functools import reduce

#####################################################################
# Función FILTER                                                    
#####################################################################
                                                                   
#  La función filter() busca elementos en un colección.             
                                                                   
#  Utiliza una función que devuelve True cuando el elemento cumple  
#  con los criterios de filtrado.                                   
                                                                   
#####################################################################

numeros = [1, 85, 200, 15, 152, 450, 5, 3061, 63, 77, 8]

# Escribe una función que retorne una lista con los número mayores de 100
def MayorDeCien(lista):
    resultado = []

    for numero in lista:
        if (numero > 100):
            resultado.append(numero)

    return resultado


print(f"Número mayores de 100 - Función Estándar: {MayorDeCien(numeros)}")


# Escribe una función que return TRUE cuando un número es mayor de 100, si no retorna FALSE
def NumMayorCien(numero):
    if (numero > 100):
        return True
    else:
        return False

print(f"Número mayores de 100 - FILTER + Función Estándar: {list(filter(NumMayorCien, numeros))}")

# Extraer número mayores de 100 utilizando FILTER y LAMBDA
print(f"Número mayores de 100 - FILTER + Función Lambda: {list(filter(lambda x: x > 100, numeros))}")


print(f"Número menores de 50: {list(filter(lambda x: x < 50, numeros))}")
print(f"Número pares: {list(filter(lambda x: x % 2 == 0, numeros))}")

#####################################################################
# Función MAP                                                       
#####################################################################
                                                                   
#  La función map() transformar una colección.                      
                                                                   
#  Partiendo de una coleccióin, utiliza una función que devuelve    
#  otra colección. La colección original no cambia                  
                                                                   
#####################################################################

print(f"Datos: {numeros}")
resultado = list(map(lambda x: (x + 10) / 2, numeros))
print(f"Resultado de sumar 10 y dividir entre 2: {resultado}")

# Ejemplo de REDUCE con una suma
print(f"Resultado SUM: {sum(numeros)}")
print(f"Resultado: {reduce(lambda x, y: x + y, numeros,)}\n")

print(f"Datos: {numeros}")
print(f"Pares: {list((map(lambda x: x % 2 == 0, numeros)))}")

print(f"Algún número es par: {any((map(lambda x: x % 2 == 0, numeros)))}")
print(f"Algún número es par: {any(x % 2 == 0 for x in numeros)}")

print(f"Todos los números pares: {all((map(lambda x: x % 2 == 0, numeros)))}")
print(f"Algún número es par: {all(x % 2 == 0 for x in numeros)}")



        # Lambda:
        # lambda simple:
        #   suma = lambda x, y: x + y
        #   print(suma(2, 3))  # Salida: 5

        # lambda con map()
        #   numeros = [1, 2, 3, 4]
        #   cuadrados = list(map(lambda x: x**2, numeros))
        #   print(cuadrados)  # Salida: [1, 4, 9, 16]

        # lambda con filter()
        #   numeros = [1, 2, 3, 4, 5, 6]
        #   pares = list(filter(lambda x: x % 2 == 0, numeros))
        #   print(pares)  # Salida: [2, 4, 6]

        # lambda con sorted()   
        #   palabras = ["banana", "manzana", "cereza"]
        #   palabras_ordenadas = sorted(palabras, key=lambda x: len(x))
        #   print(palabras_ordenadas)  # Salida: ['cereza', 'banana', 'manzana']

        # Caracteristicas y limitaciones:
        # Son anonimas.
        # Pueden contener solo una expresión
        # legibilidad
        # Utiles para funcion de corta duracion (map, filter, sorted)

            # Map:
            # Se utiliza para aplicar una función a todos los elementos de una secuencia (como una lista, tupla, etc.) y devolver 
            # un nuevo iterador con los resultados. Es útil cuando deseas transformar cada elemento de una secuencia de acuerdo con alguna lógica definida en una función.
            #
            # sintasis: filter(función, secuencia)
            #   función: Una función que toma un solo argumento y devuelve un valor.
            #   secuencia: La secuencia de elementos a transformar (puede ser una lista, tupla, conjunto, etc.).
            

            # Filter:
            # Se utiliza para construir una secuencia (como una lista, tupla, etc.)
            # El resultado es un objeto iterador que contiene todos los elementos de la secuencia para los cuales la función ha devuelto True.
            # 
            # sintasis: filter(función, secuencia)
            #   función: Una función que toma un solo argumento y devuelve True o False
            #   secuencia: La secuencia de elementos a filtrar (puede ser una lista, tupla, conjunto, etc.).
            
            # Sorted
            # Se utiliza para ordenar una secuencia (como una lista, tupla, etc.) y devuelve una nueva lista ordenada.
            #
            # sintasis: sorted(iterable, key=None, reverse=False)
            #   iterable: La secuencia de elementos a ordenar (puede ser una lista, tupla, conjunto, etc.).
            #   key: Una función que sirve de clave para la comparación de elementos. Es opcional.
            #   reverse: Un valor booleano. Si es True, la lista se ordenará en orden descendente. El valor predeterminado es False (orden ascendente).


