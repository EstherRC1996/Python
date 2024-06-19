#####################################################################
# Conversión de variables                                           
#####################################################################


# Declaración de variables
a = 5.3
b = "25"
c = "25.7"
d = "a 8.4"

# Converión de números a texto con STR 
print("El valor de A es: " + str(a))
print("El valor de B es: " + b)
print("")

# Conversión de texto a número con INT y FLOAT
print(f"Valor de B: {b}")
print(type(b))

print(f"Valor de B: {int(b)}")
print(type(int(b)))

print(f"Suma: { b + c}   <-- El resultado es una concatenación del texto.")
print(type(b + c))

print(f"Suma: {int(b) + float(c)}")
print(type(int(b) + float(c)))

print(f"Número: {d}  <-- No se puede convertir a Float por contener una a")


# La conversión es muy importante cuando se trabajan datos de diferente
# tipo, las conversiones se realizan añadiendo el tipo en el que quieres
# convertir la variable ejemplos:
# tupla = tuple(lista)      convierte de lista a tupla
# lista = list(tupla)       convierte de tupla a lista
# numero = int(n)           convierte en numero entero
# float(n)                  convierte en numero decimal
# cadena = str(n)           convierte en texto
# booleano = bool(n)        convierte en bool (verdadero o falso)