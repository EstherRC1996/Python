from flask import Flask, render_template, request
                # Importa las clases y funciones necesarias de Flask. Flask es la 
                # clase principal para crear la aplicación, render_template se utiliza
                # para renderizar plantillas HTML y request se usa para manejar datos 
                # enviados por el usuario.
from EMTModulo import *
                # Importa todo desde el módulo EMTModulo, que se asume contiene la 
                # función GetArrivalBus.

#########################################################################
# Creamos una instancia de Flask
#########################################################################
app = Flask(__name__, template_folder="templates")
                  # Crea una instancia de la aplicación Flask y especifica el 
                  # directorio templates como el lugar donde Flask buscará las 
                  # plantillas HTML.  


#########################################################################
# Rutas de la aplicación Flask
#########################################################################

# Ruta: http://dominio.com/
@app.route("/")
def index():    
    return render_template("index.html")

"""
@app.route("/"): Define la ruta raíz de la aplicación (http://dominio.com/).

def index(): Define la función index que se ejecuta cuando se accede a la ruta raíz.

return render_template("index.html"): Renderiza y devuelve la plantilla index.html.
"""

# Ruta: http://dominio.com/listado
@app.route("/listado", methods=["POST"])
def listado():
    # parada = request.args.get("parada")               # Procesar formularios GET
    parada = request.form.get("parada")                 # Procesar formularios POST    
    infoData = GetArrivalBus(parada)

    return render_template("listado.html", info=infoData)

"""
@app.route("/listado", methods=["POST"]): Define la ruta /listado y especifica que solo aceptará solicitudes POST.

def listado(): Define la función listado que se ejecuta cuando se accede a la ruta /listado.

parada = request.form.get("parada"): Obtiene el valor del campo parada del formulario enviado mediante POST.

infoData = GetArrivalBus(parada): Llama a la función GetArrivalBus del módulo EMTModulo con el valor de parada y guarda el resultado en infoData.

return render_template("listado.html", info=infoData): Renderiza y devuelve la plantilla listado.html, pasando infoData a la plantilla.
"""



#########################################################################
# Ejecutar la aplicación de Flask en el servidor web integrado
#########################################################################
app.run()
        # Inicia la aplicación Flask en el servidor web integrado.