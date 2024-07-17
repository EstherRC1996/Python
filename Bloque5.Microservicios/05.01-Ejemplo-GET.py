#####################################################################
# Trabajando Request                                                
#####################################################################

# Importar los módulos necesarios (Importa los módulos requests para hacer solicitudes
#  HTTP y pprint para imprimir datos de manera legible.)
import requests, pprint

# En el ejemplo consultamos una base de datos de direcciones IP
# La dirección IP es suministrada por el usuario (Solicita al usuario que ingrese una
#  dirección IP pública y guarda el valor en la variable ip.) 
ip = input("Dirección IP pública: ")

# El usuario determina el formato de la respuesta ( Solicita al usuario que ingrese 
# el formato de respuesta deseado (JSON o XML) y guarda el valor en la variable 
# responseType.)
responseType = input("Formato de respuesta JSON o XML: ")

# Endpoint del microservicio APIRest (Construye la URL del endpoint del microservicio
#  API REST usando el formato de respuesta y la dirección IP proporcionados por el 
# usuario.)
endpoint = f"http://ip-api.com/{responseType.lower()}/{ip}"

try:
    # Utilizamos la función get() para llamar al microservicio
    # La función get() retorna el mensaje de respuesta
    response = requests.get(endpoint) # Utiliza la función get de requests para hacer 
                                      # una solicitud HTTP GET al endpoint y guarda la 
                                      # respuesta en la variable response.

    # La variable response contiene el mensaje de respuesta
    # Mostramos el código de estado
    # Mostramos el código de estado en modo texto utilizando REASON
    print(f"Estado: {response.status_code} / {response.reason}") # Imprime el código de estado de la respuesta HTTP 
                                                                 # (status_code) y su descripción (reason).

    if(response.status_code == 200): # Verifica si el código de estado de la respuesta es 200 (OK).
    
        # Mostramos las cabeceras del mensaje de respuesta
        print(f"Cabeceras: {response.headers}\n")                                                   # Imprime las cabeceras de la respuesta HTTP.
        print(f"Content-Type: {response.headers["Content-Type"]}")                                  # Imprime el valor de la cabecera Content-Type que indica el formato de la información en el cuerpo de la respuesta.
        print("Content-Type, indica el formato de la información enviada en el BODY.\n")            # Explica el propósito de la cabecera Content-Type.
        print(f"Content-Length: {response.headers["Content-Length"]} bytes")                        # Imprime el valor de la cabecera Content-Length que indica el tamaño en bytes del cuerpo de la respuesta.
        print("Content-Length, indica el tamaño en bytes de la información enviada en el BODY.\n")  # Explica el propósito de la cabecera Content-Length.

        # Mostramos el contenido del cuerpo del mensaje de respuesta
        print(f"  Contenido en bytes: {response.content}\n")                # imprime el contenido del cuerpo de la respuesta en formato de bytes.
        print(f"Contenido como texto: {response.text}\n")                   # Imprime el contenido del cuerpo de la respuesta como texto.

        if ("application/json" in response.headers["Content-Type"].lower()):  # Verifica si el Content-Type de la respuesta es application/json.
            data = response.json()  # La función JSON retorna un objeto de tipo diccionario de python

            print(f"   Ubicación: {data["regionName"]} ({data["country"]})")    # Imprime la región y el país obtenidos de la respuesta JSON.
            print(f"     Latitud: {data["lat"]}")                               # Imprime la latitud obtenida de la respuesta JSON.
            print(f"    Longitud: {data["lon"]}")                               # Imprime la longitud obtenida de la respuesta JSON.
            print(f"Organización: {data["isp"]} - {data["org"]}")               # Imprime el proveedor de servicios de Internet (ISP) y la organización obtenidos de la respuesta JSON.
        else:                                                                   # Si la respuesta no es JSON.
            print("La respuesta no es JSON.\n")                                 # Imprime un mensaje indicando que la respuesta no es JSON.
    else:                                                                       # Si el código de estado de la respuesta no es 200.
        print(f"{response.reason}")                                             # Imprime la razón del fallo de la solicitud.


except requests.ConnectionError as err:     # Indica errores de DNS
    print(f"{err}")
except requests.Timeout as err:             # Timeout superado
    print(f"{err}")
except requests.TooManyRedirects as err:    # Demasiados redirecionamientos
    print(f"{err}")
except requests.HTTPError as err:           # Errores que retornan códigos HTTP 4xx o 5xx
    print(f"{err}")
except requests.RequestException as err:    # Genérico de requests
    print(f"{err}")
except Exception as err:                    # Genérico de python
    print(f"{err}")         # Imprime error
