######################################################################
# Declaración de Variables                                           
######################################################################
                                                                    
#  Sintaxis: [nombre de la variable] = [valor inical]                
                                                                    
#  Ejemplos:                                                         
#       numero = 20                                                  
#       saludo = "Hola Mundo !!!"                                    
                                                                    
######################################################################


# Declaración de variables
numero = 10
Numero = 20
saludo = "Hola Mundo !!!"

# Mostrar el contenido de las variables (print)
print(numero)
print(Numero)           # diferencía entre Mayúsculas y minúsculas
print(saludo)

print(numero + Numero)
print(numero - 25)
print("Saludo: " + saludo)

print(36)
print("Iniciamos la frase ...")
print("Iniciamos la frase \n y saltamos de parrafo ...") # /n salto de linea
print("")

# Mostrar el tipo de las variables
print(type(numero))    #tipo de variable
print(type(saludo))

print(type(3))                      #int
print(type(3.1))                    #float
print(type("3"))                    #texto
print(type("tres"))                 #texto
print(type(3 == 3))                 
print(3 == 3)                       
print(type(3 != 3))                 
print(3 != 3)                      
print(type(('1', '2', '3')))        
print(type(["1", "2", "3"]))        
print(type({"1", "2", "3"}))        
print(type([1, 2, 3]))              



# Una variable es un elemento de datos con nombre cuyo valor puede 
# cambiar durante el curso de la ejecución del programa (es decir, es 
# como una caja con un nombre, donde se guarda un valor).