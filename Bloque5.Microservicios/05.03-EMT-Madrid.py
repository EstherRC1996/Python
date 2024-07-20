#####################################################################
# Consultar timepo de llegada del autobus                           
#####################################################################

import requests, json

# Función para procesar las información
def InfoBus(item):
    data = {}
    data["linea"] = item["line"]
    data["distancia"] = item["DistanceBus"]

    if (item["estimateArrive"] < 60):
        data["tiempo"] = "está en la parada."
    else:
        time = item["estimateArrive"] / 60
        if(time >= 20):
            data["tiempo"] = "llegará en 20 min o más."
        else:
            data["tiempo"] = f"llegará aproximadamente en {time:1.0f} min."

    data["mensaje"] = f"el {data["linea"]} {data["tiempo"]} ({data["distancia"]} m.)"
    
    return data

"""
Definición de la Función InfoBus: Procesa la información de llegada de un autobús.
Inicialización del Diccionario data: Almacena los datos procesados.
Extracción de la Línea y Distancia del Autobús:
    data["linea"] obtiene la línea del autobús.
    data["distancia"] obtiene la distancia del autobús a la parada.
Calculo del Tiempo de Llegada:
    Si estimateArrive (tiempo estimado de llegada en segundos) es menor a 60 segundos, indica que el autobús está en la parada.
    Si no, se convierte a minutos y se evalúa si el tiempo es mayor o igual a 20 minutos, o menos, para proporcionar el mensaje adecuado.
Construcción del Mensaje: Combina los datos en un mensaje descriptivo.
Retorno de Datos: La función retorna el diccionario data con los datos procesados.

"""

# Colección de URLs utilizadas
urls = {
    "base": "https://openapi.emtmadrid.es/v2/",
    "login": "mobilitylabs/user/login/",
    "timeArrivalBus": "transport/busemtmad/stops/<stopId>/arrives/"
}
            # Define un diccionario urls con las partes de las URLs que se usarán 

# Variable para alamacenar el token (una variable token inicializada en None para almacenar el token de acceso.)
token = None

# Preguntamos al usuario que parada quiere consultar y lo almacenamos en la variable parada
parada = input("Número de la parada: ")

#####################################################
# Obtener token de acceso al API
#####################################################
try:
    # La variable endpoint contiene el resultado de concatenar los valores de dos claves del diccionario
    # https://openapi.emtmadrid.es/v2/mobilitylabs/user/login/
    endpoint = urls["base"] + urls["login"]

    # Cabecera para el login en la API
    headers = {
        "X-ClientId": "25d3d248-fc0c-479d-8276-78ac52c647f2",
        "passKey": "141FE2B578702B63F6EE4E03049F95AB594A28BA9B67A7CAFF0D08BDB8B045463A14B6EADF5885D589B00DA11919CB9D12FFC012A317404D1EF97656E67A86B0"
    }

    # Llamda al API, login para obtener el token de acceso
    response = requests.get(endpoint, headers=headers)

    # Comprobamos que código de estado es 200 y recogemos del mensaje de respuesta el token,
    # que almacenamos en la variable token
    if(response.status_code == 200):
        token = response.json()["data"][0]["accessToken"]
    else:
        print(f"Error ({response.status_code}): {response.reason}")
        quit()
    """
    Construcción de la URL del Endpoint: Concatenando las partes del diccionario urls.
    Definición de las Cabeceras: Se definen las cabeceras necesarias para la autenticación.
    Solicitud de Token: Se realiza una solicitud GET al endpoint de login con las cabeceras definidas.
    Validación de la Respuesta: Si el estado de respuesta es 200, se extrae y almacena el token de acceso. Si no, se muestra un mensaje de error y se termina la ejecución.
    """

    # Si tenemos token realizamos una segunda llamda al API para obtener la información
    # de los autobuses proximos a la parada de autobus

    #####################################################
    # Obtener listado autobuses
    #####################################################

    # La variable endpoint contiene el resultado de concatenar los valores de dos claves del diccionario
    # https://openapi.emtmadrid.es/v2/transport/busemtmad/stops/<stopId>/arrives/
    # Remplazamos el texto <stopId> por el número de la parada almacenado en la variable parada
    endpoint = urls["base"] + urls["timeArrivalBus"].replace("<stopId>", parada)

    # Datos del HEADER, incluye el token de acceso obtenido anteriormente
    headers = {"accessToken": token}

    # Datos del BODY
    data = {
        "cultureInfo": "ES",
        "Text_StopRequired_YN": "Y",
        "Text_EstimationsRequired_YN": "Y",
        "Text_IncidencesRequired_YN": "N",
        "DateTime_Referenced_Incidencies_YYYYMMDD": "20240514"
    }

    # Llamada al API, para obtener información sobre los autobuses
    # Dos opciones posible para pasar los datos del BODY del mensaje

    response = requests.post(endpoint, headers=headers, json=data)
    # response = requests.post(endpoint, headers=headers, data=json.dumps(data))

    # Comprobamos que código de estado es 200 y recogemos del mensaje de respuesta
    # Procesamos la respuesta mostrando el listado de autobuses por llegar a la parada indicada
    if (response.status_code == 200):
        # Opción A
        datos = map(InfoBus, response.json()["data"][0]["Arrive"])
        for item in datos: 
            print(item["mensaje"])

        # Opción B
        # for item in response.json()["data"][0]["Arrive"]:
        #     print(InfoBus(item)["mensaje"])
    else:
        print(f"Error ({response.status_code}): {response.reason}")

    """
Construcción de la URL del Endpoint: Concatenando las partes del diccionario urls y reemplazando <stopId> con el número de parada.
Definición de las Cabeceras: Incluyendo el token de acceso.
Definición de los Datos del Body: Especificando parámetros necesarios para la solicitud.
Solicitud de Información de Autobuses: Se realiza una solicitud POST al endpoint con las cabeceras y datos definidos.
Procesamiento de la Respuesta: Si el estado de respuesta es 200, se procesa la información de llegada de los autobuses usando la función InfoBus y se imprime el mensaje. Si no, se muestra un mensaje de error.
    """


except Exception as e:
    print(f"Error: {e}")
"""
Captura cualquier excepción que ocurra durante la ejecución del bloque try y muestra un mensaje de error.
"""