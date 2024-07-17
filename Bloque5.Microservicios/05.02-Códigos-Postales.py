# Importar los módulos necesarios
import requests, pprint                                           #  Importa los módulos requests para hacer solicitudes HTTP y pprint para imprimir datos de manera legible.


postalcode = input("Indica un código postal: ")                    # Solicita al usuario que ingrese un código postal y guarda el valor en la variable postalcode.
endpoint = f"https://api.zippopotam.us/es/{postalcode}"            # Construye la URL del endpoint del servicio API Zippopotam usando el código postal proporcionado por el usuario.


try:
    response = requests.get(endpoint)
    
    if (response.status_code == 200):
        data = response.json()

        print(f"{data["post code"]} {data["country"]}")
        for resultado in data["places"]:
            print(f" |-> {resultado["place name"]} ({resultado["state"]})")
    else:
        print(f"Error ({response.status_code}): {response.reason}")
    
except Exception as err:
    print(f"{err}")

"""
try: Inicia un bloque de código que manejará excepciones.

response = requests.get(endpoint): Utiliza la función get de requests para hacer una solicitud HTTP GET al endpoint y guarda la respuesta en la variable response.

if (response.status_code == 200): Verifica si el código de estado de la respuesta es 200 (OK).

data = response.json(): Convierte el cuerpo de la respuesta JSON en un diccionario de Python y guarda el resultado en la variable data.

print(f"{data["post code"]} {data["country"]}"): Imprime el código postal y el país obtenidos de la respuesta JSON.

print(f"{data["post code"]} {data["country"]}"): Imprime el código postal y el país obtenidos de la respuesta JSON.

else: Si el código de estado de la respuesta no es 200.

print(f"Error ({response.status_code}): {response.reason}"): Imprime un mensaje de error con el código de estado y la razón del fallo de la solicitud.

except Exception as err: Captura cualquier tipo de excepción que ocurra durante la ejecución del bloque try.

print(f"{err}"): Imprime el error.
"""