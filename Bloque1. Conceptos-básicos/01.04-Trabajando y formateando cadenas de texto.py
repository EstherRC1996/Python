#####################################################################
# Trabajando y formateando cadenas de texto                         
#####################################################################


# Declaración de variables
#        01234567890123456789    <--- Posiciones
texto = "   hola mundo !!!   "
print(texto)


# Mostar determinados caractéres de la cadena
# indicando su posición o un rango
print(f"Posición 3: {texto[3]}")
print(f"Desde la posición 3 incluida: {texto[3:]}")
print(f"Hasta la posición 6 NO incluida: {texto[:6]}")
print(f"Desla la posición 2 a la 6 NO incluida: {texto[2:6]}")
print(f"Los 4 primeros caractéres empezando por derecha: {texto[-5]} \n")


# Funciones que podemos utilizar con cadenas de texto
print(f"Número de caractéres: {len(texto)}") #Cuenta el numero de caracteres en la cadena
print(texto)
print(texto.lower())                        # Minuscula
print(texto.upper())                        # Mayuscula
print(texto.strip().capitalize())           # Elimina espacios en blanco y Primera letra en mayuscula
print(texto.title())                        # Con espacios a los lados
print(texto.strip())                        # Primera letra en mayuscula
print(texto.count("o"))                     # Devuelve el numero de o en el texto
print(f"Es un digito: {texto.isdigit()}")   # verifica si la cadena es un digito
print(f"Es un digito: {"57".isdigit()} \n")


# Formateando texto 
mensaje = "Mundo"

print("Hola " + mensaje + " !!!")

print("Hola {} !!!".format(mensaje))        # se utiliza para insertar el contenido de la variable
print("Hola {s} !!!".format(s=mensaje))
        
        # {} en el print es un marcador, el {} es sustituido con el contenido de la
        # variable mensaje, es decir, la que esta dentro del parentesis de .format()
        # En el segundo caso el marcador incluye una s, la diferencia es que en el .fortmat(),
        # dentro del parentesis hay que aclarar que s = mensaje.

print(f"Hola {mensaje} !!!")


# Formatenado números
resultado = 10 / 3

print("Resultado: " + str(resultado))
print("Resultado:", str(resultado))
print("Resultado:", resultado)

print("Resultado: {r}".format(r=resultado))
print("Resultado: {r:1.2f}".format(r=resultado))  

print(f"Resultado: {resultado}")
print(f"Resultado: {resultado:1.2f}")

# 1.2f especifica como debe formatearse
# el 1 indica el ancho minimo de caracteres, para el valor formateado
# el 2 indica que se deben mostrar dos digitos tras el punto decimal
# la f especifica que debe formatearse como un número de punto flotante.