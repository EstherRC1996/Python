#####################################################################
# Clases - Miembros privados                                        #
#####################################################################

"""
 Las variables «privadas», que no pueden accederse excepto desde dentro de un objeto,
 no existen en Python. 

 Sin embargo, hay una convención que se sigue en la mayoría del código Python: un nombre 
 prefijado con un guión bajo (por ejemplo, _spam) debería tratarse como una parte no pública.

 Cualquier identificador con la forma __spam (al menos dos guiones bajos al principio,
 como mucho un guión bajo al final) es textualmente reemplazado por _nombredeclase__spam.
"""

class Demo:
    __Clave = "12345678a"

    def publico(self):
        print("Todos puede saber")

    def _privado(self):
        print("Nadie debería saber")

    def __secreto(self):
        print(f"Nadie puede saber el secreto: {self.__Clave}")

    def getSecreto(self, pw):
        if (pw == "1234"):
            self.__secreto()
        else:
            print("Sin acceso")


demo = Demo()

demo.publico()
demo._privado()
demo.getSecreto("1234")
print("")

print(dir(demo))
demo._Demo__secreto()
print(f"Clave: {demo._Demo__Clave}")


        # En Python, los miembros privados de una clase se utilizan para restringir 
        # el acceso directo a los atributos y métodos desde fuera de la clase. 
        # Aunque Python no tiene verdaderos miembros privados como otros lenguajes 
        # de programación (por ejemplo, Java o C++), se utiliza una convención de 
        # nomenclatura para indicar que un miembro es privado.

        # Convención para miembros privados
        # Para indicar que un atributo o método es privado, se utiliza un guion 
        # bajo (_) antes del nombre del miembro. Sin embargo, esto es solo una 
        # convención y no impide realmente el acceso desde fuera de la clase.
        # 
        # Para una mayor restricción, se pueden utilizar dos guiones bajos (__). 
        # Esto activa la name mangling, una técnica que cambia internamente el nombre
        #  del atributo para dificultar su acceso desde fuera de la clase.