#####################################################################
# Trabajando con mongoDB                                            
#####################################################################

from pymongo import MongoClient, collection
        # from pymongo import MongoClient, collection: MongoClient es la clase 
        # principal para conectarse a un servidor MongoDB. collection es parte del 
        # módulo pymongo que se utiliza para trabajar con colecciones en MongoDB.

from bson.objectid import ObjectId
        # from bson.objectid import ObjectId: ObjectId es un tipo de dato específico 
        # de MongoDB que se utiliza para identificar de manera única los documentos en
        # una colección.

from pprint import pprint
        # from pprint import pprint: pprint es una función que se utiliza para imprimir
        # estructuras de datos de manera más legible.

import sys, json
        # import sys, json: sys proporciona acceso a algunas variables y funciones del
        # sistema, y json permite trabajar con datos en formato JSON.


######################################################
# CONECTAR CON UN SERVIDOR mongoDB
######################################################

#clientDB = MongoClient("127.0.0.1", "27017")           # Crea una conexión a un servidor MongoDB en la máquina local usando la IP 127.0.0.1 y el puerto 27017.
#clientDB = MongoClient("localhost", "27017")           # Hace lo mismo que la línea anterior, ya que localhost es un alias para 127.0.0.1.
#clientDB = MongoClient("mongodb://USER:PASSWORD@<IP>:<PORT>/")      # Crea una conexión usando una cadena de conexión que incluye las credenciales de usuario (USER y PASSWORD), la IP del servidor (<IP>) y el puerto (<PORT>).
#clientDB = MongoClient("mongodb://127.0.0.1:27017/")           # Conexión usando la cadena de conexión estándar para un servidor MongoDB en la máquina local.


######################################################
# EJECUTAR COMANDO - Mostrar el estado del servidor
######################################################

# Creamos un objeto que almacenamos en la variable clientDB
# El objeto representa el cliente para trabajar con las bases de datos de mongoDB
# Se requiere una cadena de conexión
clientDB = MongoClient("mongodb://localhost:27017/")

"""Crea un objeto MongoClient que representa la conexión al servidor MongoDB 
        en la máquina local (localhost) en el puerto 27017. Este objeto clientDB será 
        utilizado para interactuar con las bases de datos de MongoDB"""


# Nos posicionamos sobre una base de datos, en el ejemplo sobre la base de datos ADMIN
db = clientDB.admin
"""Selecciona la base de datos admin del servidor MongoDB. En MongoDB, la base de datos
 admin es una base de datos especial que se utiliza para operaciones administrativas y
de supervisión."""

# Ejecutamos un comando utilizando la función COMMAND
# El comando serverStatus nos retorna el estado del servidor en formato JSON
result = db.command("serverStatus")
"""Ejecuta el comando serverStatus en la base de datos admin. Este comando devuelve 
una variedad de información sobre el estado del servidor MongoDB, como estadísticas de
uso, información de la memoria, estado de las conexiones, y más. El resultado se 
almacena en la variable result."""

# Mostramos el resultado de la ejecución del comando
print(result)
"""mprime el resultado del comando serverStatus en la consola. result es un diccionario 
en formato JSON que contiene toda la información sobre el estado del servidor MongoDB."""


######################################################
# TRABAJAR CON BASES DE DATOS Y SUS COLECCIONES
######################################################

# Mostrar el nombre de las bases de datos
print(clientDB.list_database_names())
"""Este método devuelve una lista con los nombres de todas las bases de datos 
disponibles en el servidor MongoDB."""

# El listado de bases de datos es una LISTA de python que podemos recorrer con un FOR
for db in clientDB.list_database_names():                   # Itera sobre cada nombre de base de datos en la lista.
    print(f"Nombre: {db}")                                  # Imprime el nombre de cada base de datos.
    print(f" -> {clientDB[db].list_collection_names()}\n")  # Imprime la lista de colecciones de cada base de datos.

# Seleccionar una base de datos con la que vamos a trabajar
db = clientDB.northwind             # Sintaxis de Objeto.  Selecciona la base de datos northwind utilizando la sintaxis de objeto.
db2 = clientDB["northwind"]         # Sintaxis de Colección. Selecciona la base de datos northwind utilizando la sintaxis de diccionario. Ambas líneas hacen lo mismo, solo que utilizan diferentes formas de acceder a la base de datos.

# Motrar las colecciones que tiene una base de datos
# Las colecciones son equivalente a las tablas en las bases de datos relacionales
# db.list_collection_names(): Devuelve una lista con los nombres de todas las colecciones en la base de datos db.
print(db.list_collection_names())       # Imprime la lista de colecciones de db.
print(db2.list_collection_names())      # Imprime la lista de colecciones de db2. Ambos prints deberían dar el mismo resultado, ya que db y db2 se refieren a la misma base de datos northwind.

# Seleccionar una colección con la que vamos a trabajar
collection = clientDB.northwind.customers       # Selecciona la colección customers en la base de datos northwind utilizando la sintaxis de objeto.
collection = clientDB["northwind"]["customers"] # Selecciona la colección customers en la base de datos northwind utilizando la sintaxis de diccionario.
collection = db.customers                       # Selecciona la colección customers en la base de datos db (que es northwind).
collection = db["customers"]                    # Selecciona la colección customers en la base de datos db (que es northwind). Estas líneas muestran diferentes formas de acceder a la misma colección.

# Mostramos el número de documentos en la colección
# Los documentos son equivalentes a los registros en bases de datos relacionales
print(f"{collection.estimated_document_count()} documentos en {collection.name}")
"""collection.estimated_document_count(): Devuelve una estimación del número de documentos en la colección collection.
collection.name: Devuelve el nombre de la colección.
print(f"{collection.estimated_document_count()} documentos en {collection.name}"): Imprime el número estimado de documentos en la colección customers."""

######################################################
# TRABAJAR CON LOS DOCUMENTOS DE LAS COLECCIONES
######################################################

# Mostrar el documento por identificador del objeto
# Filtro: _id = identificador
result = collection.find_one({"_id": ObjectId("663a105807258656ed9eae3a")})
pprint(result)
print("")

# Mostrar el primer el documento que coincide con el filtro
# Filtro: Country = USA
result = collection.find_one({"Country": "USA"})
print(type(result))
pprint(result)
print("")

# Mostrar el todos los documentos que coincide con el filtro
# Filtro: Country = USA
# Retornar un cursor
cursor = collection.find({"Country": "USA"})
print(type(cursor))

# Mostrar el número de documentos de una búsqueda
# print(f"Resultado de la búsqueda {cursor.count()} documentos.")    # No disponible desde la versión
print(f"Resultado de la búsqueda {collection.count_documents({"Country": "USA"})} documentos.")

# Cuando ALIVE retorna TRUE significa que tenemos documentos pendientes de leer en el cursor
print(f"Documentos pendientes de leer: {cursor.alive}")
print("")

# Utilizamos WHILE para mostrar los documentos del cursor
# El bloque del WHILE se ejecuta mientras ALIVE retorne TRUE (documentos pendientes de leer)
# Con la función .NEXT() para posicionarnos en el siguiente documentos del cursor
while (cursor.alive == True):
    document = cursor.next()
    pprint(document)
    print("")

# Cuando ALIVE retorna FALSE significa que no tenemos documentos pedientes de leer en el cursor
print(f"Documentos pendientes de leer: {cursor.alive}")
print("")

######################################################
# EJEMPLOS DE BÚSQUEDAS Y UTILIZACIÓN DE OPERADORES
######################################################

"""
===================================================
 Listado de operadores relacionales
===================================================
$eq     - equal - igual
$lt     - low than - menor que
$lte    - low than equal - menor o igual que
$gt     - greater than - mayor que
$gte    - greater than equal - mayor o igual que
$ne     - not equal - distinto
$in     - in - dentro de
$nin    - not in - no dentro de
$regex  - cumple con la expresión regular
"""

cursor = collection.find({"Country": "USA"})
cursor = collection.find({"Country": "USA"}).limit(3)
cursor = collection.find({"Country": "USA"}).skip(5)
cursor = collection.find({"Country": "USA"}).skip(5).limit(5)
cursor = collection.find({"Country": "USA"}).sort("City")               # Ordenados de A a W
cursor = collection.find({"Country": "USA"}).sort({"City": 1})          # Ordenados de A a W
cursor = collection.find({"Country": "USA"}).sort({"City": -1})         # Ordenados de W a A

# Buscar clientes de USA, ejemplos con y sin operador
cursor = collection.find({"Country": "USA"})                            # Sin operador
cursor = collection.find({"Country": {"$eq": "USA"}})                   # Con operador

# Buscar clientes fuera de USA
cursor = collection.find({"Country": {"$ne": "USA"}})

# Buscar clientes de USA y Mexico, ordenados por país y ciudad
cursor = collection.find({"Country": {"$in": ["USA", "Mexico"]}}).sort([("Country", 1), ("City", 1)])

# Buscar clientes que contenienen DE en la clave CustomerID
cursor = collection.find({"CustomerID": {"$regex": "DE"}})

# Buscar clientes que el CustomerID comienza por A y finaliza con 4 carácteres más
cursor = collection.find({"CustomerID": {"$regex": "1[A-Z]{4}"}})

# Buscar clientes de la ciudad de San Francisco en USA
# El operador AND NO se especifica, pero se aplica de forma implicita o por defecto
cursor = collection.find({"Country": "USA", "City": "San Francisco"})

# Buscar clientes de la ciudad de San Francisco en USA utilizando el operador AND
# El operador AND SI se especifica y se aplica de forma explicita
cursor = collection.find({"$and": [{"Country": "USA"}, {"City": "San Francisco"}]})

# Buscar clientes de GERMANY o USA utilizar el operador OR
# El operador OR se especifica y se aplica de forma explicita
cursor = collection.find({"$or": [{"Country": "Germany"}, {"Country": "USA"}]})

# Buscar los clientes de Mexico y sus pedidos
cursor = collection.find({"Country": "Mexico"})

while (cursor.alive == True):
    document = cursor.next()
    print(f"{document["CustomerID"]}# {document["CompanyName"]} - {document["City"]} ({document["Country"]})")

    pedidos = clientDB.northwind.orders.find({"CustomerID": document["CustomerID"]})
    while (pedidos.alive):
        pedido = pedidos.next()
        print(f">>> {pedido["OrderID"]}# - {pedido["OrderDate"]}")

    print("")

# Buscar los clientes de Mexico y sus pedidos utilizando agregación AGGREGATE
cursor = db.customers.aggregate([
    {"$match": {"Country": "Mexico"}},
    {"$sort": {"City": 1}},
    {"$lookup": {
        "from": "orders",
        "localField": "CustomerID",
        "foreignField": "CustomerID",
        "as": "Pedidos"
    }}
])

while (cursor.alive == True):
    doc = cursor.next()
    print(f"{doc["CustomerID"]}# {doc["CompanyName"]} - {doc["City"]} ({doc["Country"]})")

    for pedido in doc["Pedidos"]:
        print(f" >> {pedido["OrderID"]}# - {pedido["OrderDate"]}")

    print("")


# Buscamos todos los productos con UnitsInStock distinto de cero
# Convertir UnitsInStock y UnitPrice en valores númericos
# Calcular la suma de multiplica el precio por unidades de cada producto
cursor = clientDB.northwind.products.find({"UnitsInStock": {"$ne": "0"}})

total = 0

while (cursor.alive):
    p = cursor.next()
    unidades = int(p["UnitsInStock"])
    precio = float(p["UnitPrice"])
    total = total + (unidades * precio)

print(f"Valor de stock: {total:1.2f}")


# Utilizamos AGGREGATE para calcular el valor del stock
query = [
    {"$match": {"UnitsInStock": {"$ne": "0"}}},
    {"$addFields": {
        "Precio": {"$toDouble": "$UnitPrice"},
        "Unidades":  {"$toInt": "$UnitsInStock"}
    }},
    {"$group": {
        "_id": "Valor del Stock",
        "Total": {"$sum": {"$multiply": ["$Precio", "$Unidades"]}},
        "Productos": {"$sum": 1}
    }}
]

cursor = clientDB.northwind.products.aggregate(query)
pprint(cursor.next())


######################################################
# INSERTAR DOCUMENTOS
######################################################

# Insertamos un documento partiendo de un objeto de python
class Customer:
    CustomerID = None
    CompanyName = None
    ContactName = None
    ContactTitle = None
    Address = None
    City = None
    Region = None
    PostalCode = None
    Country = None
    Phone = None
    Fax = None


cliente = Customer()
cliente.CustomerID = "DEMO1"
cliente.CompanyName = "Empresa Uno, SL"
cliente.ContactName = "Borja"
cliente.ContactTitle = "Gerente"
cliente.Address = "Calle Uno, S/N"
cliente.City = "Madrid"
cliente.Region = "Madrid"
cliente.PostalCode = "28016"
cliente.Country = "España"
cliente.Phone = "900100100"
cliente.Fax = "900100200"

# Todos los objetos de python tiene una variable o propiedad que es __dict__
# que retorna un diccionario de todas sus variables
pprint(cliente.__dict__)

id = collection.insert_one(cliente.__dict__).inserted_id
print(f"ID del nuevo documento: {id}")

# Insertamos partiendo de un diccionario

cliente2 = {"CustomerID": "DEMO2",
            "CompanyName": "Empresa Dos, SL",
            "ContactName": "Borja Cabeza",
            "ContactTitle": "Gerente",
            "Address": "Calle Dos S/N",
            "City": "Madrid",
            "Region": "Madrid",
            "PostalCode": "28019",
            "Country": "España",
            "Phone": "910 101 102",
            "Fax": "910 101 103"}

id = collection.insert_one(cliente2).inserted_id
print(f"ID del nuevo documento: {id}")


######################################################
# ACTUALIZAR DOCUMENTOS
######################################################

cliente = collection.find_one({"CustomerID": "DEMO1"})
pprint(cliente)

# Actualizamos uno o varios documentos de una colección
query = {"CustomerID": "DEMO1"}

# Los nuevo valores para el documento o documentos que vamos actualizar
newValues = {"$set": {
    "ContactName": "Ana Sanz",
    "PostalCode": "28013"
}}

# Actualizar el primer documento que retorna la consulta
result = collection.update_one(query, newValues)

print(f"{result.matched_count} documentos encontrados")
print(f"{result.modified_count} documentos modificados")
print(result)

# Actualizar el todos los documentos que retorna la consulta
result = collection.update_many(query, newValues)

print(f"{result.matched_count} documentos encontrados")
print(f"{result.modified_count} documentos modificados")
print(result)

pprint(collection.find_one(query))


######################################################
# ELIMINAR DOCUMENTOS
######################################################

# Eliminar el primer documento coincidente con el filtro de búsqueda
result = collection.delete_one({"CustomerID": "DEMO2"})
print(result)
print(f"{result.deleted_count} documentos eliminados.")

# Eliminar todos los documentos coincidentes con el filtro de búsqueda
result = collection.delete_many({"CustomerID": "DEMO2"})
print(result)
print(f"{result.deleted_count} documentos eliminados.")