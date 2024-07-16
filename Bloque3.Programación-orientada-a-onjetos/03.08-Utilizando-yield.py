#####################################################################
# Utilizando yield                                                  #
#####################################################################

numeros = [8, 14, 65, 7, 14, 99, 745, 1, -35, 1408]

print(f"Datos: {numeros}")

def func1(lista):
    for i in lista:
        return i * 5
    
def func2(lista):
    resultado = []

    for i in lista:
        resultado.append(i * 5)

    return resultado   

print(f"Func 1: {func1(numeros)}")
print(f"Func 2: {func2(numeros)}")
print(f"Lambda: {list(map(lambda x: x * 5, numeros))}")


def func3(lista):
    for i in lista:
        yield i * 5

print(f"Func 3: {func3(numeros)}")  
print(f"Func 3 To-List: {list(func3(numeros))}")

# Utilizanción de los generadores
generador = func3(numeros)
print(next(generador))
print(next(generador))
print(next(generador))
print(next(generador))

generador = func3(numeros)
for i in generador:
    print(f">> {i}")

try:
    generador2 = ((i * 5) for i in numeros)
    print(f">>> {next(generador2)} *")
    print(f">>> {next(generador2)} *")
    for i in generador2:
        print(f">>> {i}")

    print(f">>> {next(generador2)} *")
except StopIteration as e:
    print(e)



        # El keyword yield en Python se utiliza dentro de una función para convertirla
        #  en un generador. Los generadores permiten crear iteradores de manera más 
        # sencilla y eficiente, especialmente cuando se trabaja con grandes volúmenes 
        # de datos o secuencias infinitas.

        # ¿Qué es un Generador? es una función que devuelve un iterador que produce 
        # una secuencia de valores uno a la vez, en lugar de devolver todos los 
        # valores a la vez. Cada vez que se llama a next() en el generador, la función
        #  se reanuda donde se quedó (justo después de la última declaración yield), 
        # con todas sus variables locales y el estado intactos.

        # Diferencias entre yield y return
        # return: Termina la función y devuelve un valor. Una vez que una función ejecuta 
        # return, se cierra.
        
        # yield: Pausa la función y devuelve un valor. La próxima vez que se llame al 
        # generador, la función continuará ejecutándose desde donde se quedó.