import pymssql  # mporta el módulo pymssql, que se utiliza para conectar y interactuar con bases de datos Microsoft SQL Server desde Python.


# Establecer la conexión con la base de datos
connection = pymssql.connect(
    server="hostdb2-eoi.database.windows.net",
    port="1433",
    user="Administrador",
    password="azurePa$$w0rd",
    database="Northwind"
)

"""
Establece una conexión con la base de datos SQL Server. Los parámetros incluyen:
-server: La dirección del servidor de la base de datos.
-port: El puerto en el que el servidor de base de datos está escuchando (por defecto es 1433 para SQL Server).
-user: El nombre de usuario para autenticarse en la base de datos.
-password: La contraseña del usuario.
-database: El nombre de la base de datos a la que deseas conectarte.
        """

# Creamos un cursor para ejecutar comando en la base de datos
# Creamos un cursor que retorna Tuplas
cursor = connection.cursor()
            # Crea un cursor. Un cursor es un objeto que se utiliza para ejecutar consultas y obtener resultados de la base de datos.

# Creamos un cursor que retorna Diccionarios
cursor = connection.cursor(as_dict=True)
"""
cursor: Esta es una variable que almacenará el cursor creado. Un cursor es un objeto que permite interactuar con la base de datos a través de la conexión establecida, permitiendo ejecutar consultas y recuperar resultados.

connection: Esta es la variable que contiene la conexión a la base de datos establecida previamente con pymssql.connect(...).

.cursor(...): Este es un método de la conexión que crea y devuelve un cursor.

as_dict=True: Este es un parámetro que se pasa al método cursor. Establece que los resultados de las consultas ejecutadas con este cursor se devolverán como diccionarios en lugar de tuplas.
"""

######################################################
# SELECT, leer registros de la base de datos
######################################################

# Ejemplos del comando SELECT, para leer registros de la base de datos
cursor.execute("SELECT * FROM dbo.Customers") 
        # Ejecuta una consulta SQL para seleccionar todos los registros de la tabla Customers en el esquema dbo.

# Mostar el contenido del cursor utilizando un WHILE
row = cursor.fetchone()     # Recupera el primer registro del conjunto de resultados.
while (row):                # Bucle que continúa mientras row no sea None.
    print(f"      ID: {row["CustomerID"]}")     # Imprime el valor del campo CustomerID del registro actual.
    print(f" Empresa: {row["CompanyName"]} - {row["City"]} ({row["Country"]})\n") # Imprime el valor de los campos CompanyName, City y Country del registro actual. 
    row = cursor.fetchone() # Recupera el siguiente registro del conjunto de resultados.

# El siguiente ejemplo comentado muestra como tratar los registros cuando se
# entregan como Tuplas en lugar de Diccionarios
"""
row = cursor.fetchone()
while (row):
    print(f"      ID: {row[0]}")
    print(f" Empresa: {row[1]} - {row[5]} ({row[8]})\n")
    row = cursor.fetchone()
"""

# Mostar el contenido del cursor utilizando un FOR
cursor.execute("SELECT * FROM dbo.Customers")
for row in cursor.fetchall():                       # Recupera todos los registros del conjunto de resultados y los itera.
    print(f">      ID: {row["CustomerID"]}")        # Imprime el valor del campo CustomerID del registro actual.
    print(f"> Empresa: {row["CompanyName"]} - {row["City"]} ({row["Country"]})\n") # Imprime el valor de los campos CompanyName, City y Country del registro actual.

# El siguiente ejemplo comentado muestra como tratar los registros cuando se
# entregan como Tuplas en lugar de Diccionarios
"""
for row in cursor.fetchall():
    print(f">      ID: {row[0]}")
    print(f"> Empresa: {row[1]} - {row[5]} ({row[8]})\n") 
"""

# Ejemplos del comando SELECT, para leer registros de la base de datos
cursor.execute("SELECT * FROM dbo.Customers")                               
cursor.execute("SELECT * FROM dbo.Customers WHERE Country = 'USA'")
cursor.execute("SELECT * FROM dbo.Customers WHERE Country = %d", "USA")
"""
cursor.execute("SELECT * FROM dbo.Customers"): Selecciona todos los registros de la tabla Customers.
cursor.execute("SELECT * FROM dbo.Customers WHERE Country = 'USA'"): Selecciona los registros donde el Country es 'USA'.
cursor.execute("SELECT * FROM dbo.Customers WHERE Country = %d", "USA"): Este comando está incorrecto, debería usar %s para parámetros de cadena.
"""

pais = input("Nombre del pais: ")
cursor.execute(f"SELECT * FROM dbo.Customers WHERE Country = '{pais}'")
cursor.execute("SELECT * FROM dbo.Customers WHERE Country = %d", pais)
"""
pais = input("Nombre del pais: "): Solicita al usuario que ingrese el nombre de un país.
cursor.execute(f"SELECT * FROM dbo.Customers WHERE Country = '{pais}'"): Ejecuta una consulta con el país ingresado por el usuario (vulnerable a inyección SQL).
cursor.execute("SELECT * FROM dbo.Customers WHERE Country = %d", pais): Incorrecto, debería usar %s.
"""


cursor.execute("SELECT * FROM dbo.Customers WHERE Country = 'USA' AND City = 'San Francisco'")
cursor.execute("SELECT * FROM dbo.Customers WHERE Country = 'USA' OR Country = 'Germany'")
"""
cursor.execute("SELECT * FROM dbo.Customers WHERE Country = 'USA' AND City = 'San Francisco'"): Selecciona registros donde el Country es 'USA' y la City es 'San Francisco'.
cursor.execute("SELECT * FROM dbo.Customers WHERE Country = 'USA' OR Country = 'Germany'"): Selecciona registros donde el Country es 'USA' o 'Germany'.
"""


cursor.execute("SELECT CustomerID, CompanyName, City, Country FROM dbo.Customers WHERE Country = 'USA'")
cursor.execute("SELECT * FROM dbo.Customers WHERE Country = 'USA' OR Country = 'Germany' ORDER BY Country")
cursor.execute("SELECT * FROM dbo.Customers WHERE Country = 'USA' OR Country = 'Germany' ORDER BY Country ASC")
cursor.execute("SELECT * FROM dbo.Customers WHERE Country = 'USA' OR Country = 'Germany' ORDER BY Country DESC")
cursor.execute("SELECT * FROM dbo.Customers WHERE Country = 'USA' OR Country = 'Germany' ORDER BY Country, City")

for row in cursor.fetchall():               # Recupera todos los registros y los itera.
    print(f"     ID: {row["CustomerID"]}")  # Imprime el valor del campo CustomerID.
    print(f"Empresa: {row["CompanyName"]} - {row["City"]} ({row["Country"]})")  # mprime el valor de los campos CompanyName, City y Country.


######################################################
# SELECT, ejemplos de JOIN
######################################################

# Ejemplo que comienza con una consulta y realiza 830 subconsultas dentro del for
# NO ES UN JOIN, son subconsultas que deben evitarse por rendimiento
cursor.execute("SELECT * FROM dbo.Orders")  # Ejecuta una consulta SQL que selecciona todos los registros (*) de la tabla Orders en el esquema dbo.

for row in cursor.fetchall():               # Utiliza un bucle for para iterar sobre todos los registros recuperados por la consulta SQL anterior. cursor.fetchall() devuelve todos los registros en una lista de diccionarios (si el cursor está configurado con as_dict=True).
    print(f" -> {row["OrderID"]}# - {row["CustomerID"]} {row["OrderDate"]}")    # Imprime el valor de las columnas OrderID, CustomerID y OrderDate del registro actual en el bucle, formateado como una cadena.

    cursor2 = connection.cursor(as_dict=True)    # Crea un nuevo cursor cursor2 que también devuelve los resultados como diccionarios (as_dict=True).
    cursor2.execute("SELECT * FROM dbo.Employees WHERE EmployeeID = %d", row["EmployeeID"])     # Ejecuta una consulta SQL con cursor2 para seleccionar todos los registros de la tabla Employees donde el valor de la columna EmployeeID coincide con el valor de EmployeeID del registro actual en el bucle row. Nota: Este método de parametrización es incorrecto para cadenas (debería ser para enteros).
    cursor2.execute(f"SELECT * FROM dbo.Employees WHERE EmployeeID = '{row["EmployeeID"]}'")    # Ejecuta una consulta SQL con cursor2 para seleccionar todos los registros de la tabla Employees donde el valor de la columna EmployeeID coincide con el valor de EmployeeID del registro actual en el bucle row. Nota: Este método es más seguro para evitar inyección SQL si se usa correctamente.
    employee = cursor2.fetchone()                # Recupera el primer registro del resultado de la consulta SQL ejecutada con cursor2 y lo almacena en la variable employee.

    print(f"    Pedido gestionado por el empleado {row["EmployeeID"]}: {employee["FirstName"]} {employee["LastName"]}")
                                                 # Imprime un mensaje que incluye el valor de EmployeeID del registro actual en el bucle row, y los valores de FirstName y LastName del registro employee recuperado de la tabla Employees.


# Ejemplo que ser realiza con una consulta
# query y query2 contienen el mismo JOIN con distinta sintaxis
query = """
    "SELECT o.OrderID, o.CustomerID, o.OrderDate, o.EmployeeID, e.FirstName, e.LastName 
    FROM dbo.Orders AS o, dbo.Employees AS e 
    WHERE o.EmployeeID = e.EmployeeID"
"""
    #  Aquí se está abriendo una cadena multilínea para definir la consulta SQL. Las comillas triples permiten que la cadena se extienda en varias líneas para mayor claridad y legibilidad.
    # La cláusula SELECT especifica las columnas que se desean recuperar de las tablas en la consulta. En este caso, se están seleccionando las siguientes columnas:
        # .OrderID: El ID de la orden desde la tabla Orders.
        # o.CustomerID: El ID del cliente desde la tabla Orders.
        # o.OrderDate: La fecha de la orden desde la tabla Orders.
        # o.EmployeeID: El ID del empleado desde la tabla Orders.
        # e.FirstName: El nombre del empleado desde la tabla Employees.
        # e.LastName: El apellido del empleado desde la tabla Employees.
    # La cláusula FROM especifica la tabla principal que se está consultando. En este caso, dbo.Orders es la tabla de órdenes, y o es un alias para esta tabla. El alias o se usa para referirse a la tabla Orders de una manera más corta en la consulta.
    # La cláusula JOIN se utiliza para combinar filas de dos o más tablas, basándose en una condición relacionada. En este caso:
        # JOIN dbo.Employees AS e: Especifica que se debe unir la tabla Employees (con alias e) a la tabla Orders.
        # ON o.EmployeeID = e.EmployeeID: Especifica la condición de unión. Las filas de Orders se combinarán con las filas de Employees donde los valores de EmployeeID coincidan.

query2 = """
    SELECT o.OrderID, o.CustomerID, o.OrderDate, o.EmployeeID, e.FirstName, e.LastName
    FROM dbo.Orders AS o
    JOIN dbo.Employees AS e
    ON o.EmployeeID = e.EmployeeID
"""
cursor.execute(query)

    # Iterar sobre los resultados y mostrar la información
for row in cursor.fetchall():
    print(f" -> {row["OrderID"]}# - {row["CustomerID"]} {row["OrderDate"]}")
    print(f"    Pedido gestionado por el empleado {row["EmployeeID"]}: {row["FirstName"]} {row["LastName"]}")


######################################################
# SELECT, las agrupaciones
######################################################

# Listado de clientes de USA y el número de pedidos de cada cliente
# NO ES UNA AGRUPACIÓN, es una subconsulta dentro del for que debemos evitar por rendimiento
cursor.execute("SELECT * FROM dbo.Customers WHERE Country = 'USA'")
for row in cursor.fetchall():
    cursor2 = connection.cursor()
    cursor2.execute(f"SELECT COUNT(*) FROM dbo.Orders WHERE CustomerID = '{row["CustomerID"]}'")
    print(f"{row["CustomerID"]}# {row["CompanyName"]} -> {cursor2.fetchone()[0]} pedidos")

"""
    Opcionalmente podemos trabajar con cursores que retornan diccionarios, pero estamos 
    obligados a definir alias para el dato calculado usando AS

    cursor2 = connection.cursor(as_dict=True)
    cursor2.execute(f"SELECT COUNT(*) AS NumPedidos FROM dbo.Orders WHERE CustomerID = '{row["CustomerID"]}'")
    print(f"{row["CustomerID"]}# {row["CompanyName"]} -> {cursor2.fetchone()["NumPedidos"]} pedidos")
"""

# Listado de clientes de USA y el número de pedidos de cada cliente
# Solo los cliente con más de 10 pedidos
query = """
    SELECT c.CustomerID, c.CompanyName, COUNT(o.OrderID) AS NumPedidos
    FROM dbo.Customers c
    JOIN dbo.Orders o
    ON c.CustomerID = o.CustomerID
    WHERE c.Country = 'USA'
    GROUP BY c.CustomerID, c.CompanyName
    HAVING COUNT(o.OrderID) > 10
"""
cursor.execute(query)
for row in cursor.fetchall():
    print(f"{row["CustomerID"]}# {row["CompanyName"]} -> {row["NumPedidos"]} pedidos")


######################################################
# INSERT, insertar nuevo registros
######################################################

# Definición de un objeto que representa el registro CUSTOMER 
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

# Instaciamos el objeto CUSTOMER
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

# cliente2 es un diccionario que también representa el registro CUSTOMER
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

# INSERT comando de inserción
command = """      
    INSERT INTO dbo.Customers(CustomerID, CompanyName, ContactTitle, City, Country)
    VALUES('BCR01', 'Company SL', 'Borja Cabeza', 'Madrid', 'España')
"""
                # command: Abre una cadena multilínea para definir el comando SQL. Las comillas triples permiten que la cadena se extienda en varias líneas para mayor claridad y legibilidad.
                    # dbo.Customers: Es el nombre de la tabla en la que se insertarán los datos.
                    # CustomerID, CompanyName, ContactTitle, City, Country: Son los nombres de las columnas en la tabla Customers donde se insertarán los valores correspondientes.
                # La cláusula VALUES especifica los valores que se insertarán en las columnas correspondientes de la tabla Customers. En este caso:
                    #'BCR01': Es el valor para la columna CustomerID.
                    # 'Company SL': Es el valor para la columna CompanyName.
                    # 'Borja Cabeza': Es el valor para la columna ContactTitle.
                    # 'Madrid': Es el valor para la columna City.
                    # 'España': Es el valor para la columna Country.


# Insertamos nuevos registros ejecutado el comando INSERT
#cursor.execute(command)

# Utilizamos la función commit() de la conexión para CONFIRMAR la transación
# tanto para operaciones de inserción, actualización y borrado
connection.commit()

# Utilizamos la función rollback() de la conexión para ANULAR la transación
# tanto para operaciones de inserción, actualización y borrado
connection.rollback()

# Ejemplo de un comando INSERT que indica las columnas o campos y sus valores
command = """
    INSERT INTO dbo.Customers(
        CustomerID, 
        CompanyName, 
        ContactTitle, 
        City, 
        Country) VALUES('BCR01', 'Company SL', 'Borja Cabeza', 'Madrid', 'España')
"""
# Ejemplo de un comando INSERT que indica las columnas o campos y comodines para los valores
command2 = """
    INSERT INTO dbo.Customers(
        CustomerID, 
        CompanyName, 
        ContactName,
        ContactTitle, 
        City, 
        Country) VALUES(%s, %s, %s, %s, %s, %s)
"""
                # VALUES(%s, %s, %s, %s, %s, %s)-->POSICION

# Al ejecutar el comando con comides, pasamos como segundo parámetros los valores en una lista
cursor.execute(command2, ["BCR02", "Company Demo, SL", "Borja", "CEO", "Valencia", "España"])

# El mismo ejemplo donde pasamos los valores en una tupla
cursor.execute(command2, ("BCR03", "Company Demo, SL", "Borja", "CEO", "Valencia", "España"))
connection.commit()

# Para insertar varios registros al mismo tiempo creamos una lista que contiene en cada posición
# una tupla con los valores de cada registro que vamos a insertar
data = []
data.append(("BCR10", "Company Demo 10, SL", "Borja", "CEO", "Sevilla", "España"))
data.append(("BCR11", "Company Demo 11, SL", "Carlos", "CEO", "Bilbao", "España"))
data.append(("BCR12", "Company Demo 12, SL", "Julian", "CEO", "Málaga", "España"))    

# Utilizamos las función .executemany() para insertar varios registro y pasamos como segundo
# parámetro la lista de tuplas con los valores de los diferentes registros
cursor.executemany(command2, data)
connection.commit()

# La propieda o variable .rowcount nos devuelve el número de registros insertados, actualizados o borrados
print(f"{cursor.rowcount} registros insertados.")

# Ejemplo de un INSERT donde se especifican valores para todos los campos o columnas del registro
command = """
    INSERT INTO dbo.Customers VALUES(
        'DEMO2',
        'Empresa Dos, SL',
        'Borja Cabeza',
        'Gerente',
        'Calle Dos S/N',
        'Madrid',
        'Madrid',
        '28019',
        'España',
        '910 101 102',
        '910 101 103')
"""

# Ejemplo de un INSERT donde se especifican comodines para los valores para todos los 
# campos o columnas del registro
command = """
    INSERT INTO dbo.Customers VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
"""


######################################################
# UPDATE, actulizar registros
######################################################

# Utilizamos UPDATE para actualizar registros en la base de datos
command = """
    UPDATE dbo.Customers
    SET Address = 'Calle Uno, S/N', ContactName = 'Carlos Sánchez'
    WHERE CustomerID = 'BCR11'
"""

# Ejecutamos el comando de actulización
cursor.execute(command)

# Confirmamos la transación y por tanto la operación de actulización
connection.commit()

# Mostramos los registros actualizados
print(f"{cursor.rowcount} registros actualizados.")

# Utilizamos UPDATE para actualizar registros en la base de datos
# El comando contiene comodine o parámetros para sustituir por valores en el momento de la ejecución
command = """
    UPDATE dbo.Customers
    SET Address = %s, ContactName = %s
    WHERE CustomerID = 'BCR12'
"""

# Ejecutamos el comando de actulización y pasamos los valores para los comodines o parámetros
cursor.execute(command, ("Calle Principal, 10", "María José Sanz"))

# Confirmamos la transación y por tanto la operación de actulización
connection.commit()

# Mostramos los registros actualizados
print(f"{cursor.rowcount} registros actualizados.")

# Utilizamos UPDATE para actualizar registros en la base de datos
# El comando contiene comodine o parámetros para sustituir por valores en el momento de la ejecución
command = """
    UPDATE dbo.Customers
    SET Address = %s, ContactName = %s
    WHERE CustomerID = %s
"""

# Ejecutamos el comando de actulización y pasamos los valores para los comodines o parámetros
cursor.execute(command, ("Calle Principal, 10", "María Sanz", "BCR12"))

# Confirmamos la transación y por tanto la operación de actulización
connection.commit()

# Mostramos los registros actualizados
print(f"{cursor.rowcount} registros actualizados.")


######################################################
# DELETE, eliminar registros
######################################################

# Utilizamos DELETE para eliminar registros en la base de datos
command = """
    DELETE FROM dbo.Customers
    WHERE CustomerID = 'BCR10'
"""

# Ejecutamos el comando y confirmamos la transación mediante connection.commit()
# Si se produce un error retrocedemos la transación mediante connection.rollback() y la operación de borrado se anual
# Siempre mostramos el número de registros eliminados
try:                        # Inicia un bloque try que intenta ejecutar las instrucciones dentro de él. Si ocurre una excepción, el flujo de control pasará al bloque except.
    cursor.execute(command) # Usa el cursor para ejecutar el comando SQL almacenado en la variable command. Este comando puede ser cualquier instrucción SQL, como INSERT, UPDATE, DELETE, etc.
    connection.commit()     # Confirma los cambios realizados por el comando SQL en la base de datos. Esto asegura que las modificaciones se guarden permanentemente.
except Exception as e:      # Este bloque captura cualquier excepción que ocurra durante la ejecución del código en el bloque try. La excepción capturada se almacena en la variable e.
    connection.rollback()   #  Si ocurre una excepción, se llama a rollback() para revertir cualquier cambio realizado en la base de datos durante la transacción actual. Esto asegura que la base de datos vuelva a su estado anterior antes de ejecutar el comando.
    print(f"Error: {e}")    # Imprime el mensaje de error capturado en la excepción. Esto ayuda a diagnosticar qué salió mal durante la ejecución del comando.
finally:                    # El bloque finally se ejecuta siempre, independientemente de si ocurrió una excepción o no. Esto asegura que ciertas acciones se realicen sin importar el resultado de los bloques try y except.
    print(f"{cursor.rowcount} registros eliminados.")   # Imprime el número de registros afectados por el comando ejecutado. cursor.rowcount devuelve el número de filas afectadas por la última operación ejecutada usando el cursor. Aunque el mensaje dice "registros eliminados", rowcount se aplica a cualquier operación que modifique filas (INSERT, UPDATE, DELETE).
    connection.close()      # Cierra la conexión a la base de datos para liberar recursos. Esto es importante para evitar conexiones abiertas que puedan agotar los recursos del sistema o la base de datos.

# Utilizamos DELETE para eliminar registros en la base de datos, el comando contiene parámetros
command = """
    DELETE FROM dbo.Customers
    WHERE CustomerID = %s
"""

# Ejecutamos el comando y suminstramos valores para los parámetros
try:
    cursor.execute(command, ("BCR11"))
    connection.commit()
except Exception as e:
    connection.rollback()
    print(f"Error: {e}")
finally:
    print(f"{cursor.rowcount} registros eliminados.")
    connection.close()