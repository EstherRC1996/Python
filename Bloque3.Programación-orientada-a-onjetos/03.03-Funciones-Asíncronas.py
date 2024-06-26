#####################################################################
# Procesamiento Asíncrono                                           
#####################################################################

import asyncio

async def main():
    print("async main -> Hola ......")
    await asyncio.gather(func1(), func2(), func3())
    print("async main -> ...... Adios !!!")

async def func1():
    print("async func1 -> Hola 1 ......")
    await asyncio.sleep(5)
    print("async func1 -> ...... Adios 1 !!!")

async def func2():
    print("async func2 -> Hola 2 ......")
    for i in range(11):
        print (f"async func2 - > {i}")
        await asyncio.sleep(0.6)
    print("async func2 -> ...... Adios 2 !!!")


async def func3():
    print("async func3 -> Hola 3 ......")
    for i in range(11):
        print(f"async func3 - > {i}")
        #await asyncio.sleep(0.2)
    print("async func3 -> ...... Adios 3 !!!")

# Hilo principal siempre es Síncrono
print("Inicio Sync")
asyncio.run(main())
print("Fin Sync")
print("")


quit()

    # Utiliza la palabra clave async y await para definir funciones asíncronas y esperar la finalización de operaciones sin bloquear el hilo principal.
    # Hilos (threads): Permite ejecutar múltiples tareas en paralelo utilizando el módulo threading.
    # Permite la ejecución paralela utilizando múltiples procesos, útil para cargas de trabajo intensivas en CPU.
    # Las funciones asíncronas permiten que otras partes del programa sigan ejecutándose mientras esperan que se completen operaciones costosas. Esto se logra mediante el uso de bucles de eventos (event loops), como el proporcionado por el módulo asyncio en Python.
    # Al permitir que varias tareas se ejecuten simultáneamente de manera eficiente, las funciones asíncronas pueden mejorar significativamente el rendimiento de aplicaciones que manejan múltiples solicitudes o tareas de manera concurrente.
    



#####################################################################
# Procesamiento Síncrono                                            
#####################################################################

def main():
    print("main -> Hola ......")
    print("main -> ...... Adios !!!")


print("Inicio Sync")
main()
print("Fin Sync")
print("")



    # Caracteristicas: Son secuenciales.
    # Pueden bloquear el hilo de ejecucion si durante la ejecucion del codigo, alguna parte requiere de más tiempo
    # son faciles de entender y depurar.
