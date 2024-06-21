#####################################################################
# JSON - (JavaScript Object Notation)                               
#####################################################################
                                                                   
#   Convertir de Objeto a JSON utilizamos el método json.dumps()    
                                                                   
#   Convertir de JSON a Objeto utilizamos el método json.loads()    
                                                                   
#####################################################################

import json

frutas = ["naranja", "limón", "pomelo", "líma", "mandarina"]

# Conversión de objetos en JSON
frutasJSON = json.dumps(frutas)

# Comprobaciones, contenido de las variables y tipos
print(f"Lista: {frutas}")
print(f"Posición 2: {frutas[2]}")
print(f"{type(frutas)}")

print(f"JSON: {frutasJSON}")
print(f"Posición 2: {frutasJSON[2]}")
print(f"{type(frutasJSON)}")
print("")

# Conversión de JSON en objetos
frutas2 = json.loads(frutasJSON)
print(f"Lista: {frutas2}")
print(f"Posición 2: {frutas2[2]}")
print(f"{type(frutas2)}")



    # se usa con todo tipo de datos: Cadenas de Texto con "", 
    # Números: Enteros y flotantes, 
    # Booleanos: true y false, 
    # Listas, Colección desordenada de pares clave-valor 
    # y null: Representa un valor nulo o vacío.

    # usos:
    # Comunicación entre Servidor y Cliente: enviar datos estructurados desde un servidor web a una aplicación cliente (APIs).
    # Almacenamiento de Configuración: en aplicaciones.
    # Intercambio de Datos: transferencia de datos entre sistemas heterogéneos.
