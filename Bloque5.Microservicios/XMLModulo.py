import xml.etree.ElementTree as ET
"""
Importación de un Módulo: La línea de código está importando un módulo de Python. 
Específicamente, está importando el módulo ElementTree del paquete xml.etree.

xml.etree.ElementTree: xml.etree.ElementTree es un módulo en la biblioteca estándar 
de Python que proporciona una API simple y eficiente para analizar y crear datos XML. 
XML (Extensible Markup Language) es un formato de datos ampliamente utilizado para el
intercambio de datos estructurados.

Alias 'ET': La parte as ET crea un alias para el módulo ElementTree. Esto significa 
que en el resto del código, en lugar de tener que escribir xml.etree.ElementTree, 
puedes simplemente escribir ET. Esto hace que el código sea más corto y más fácil de 
leer.
"""

def object_to_xml(object, tag="item"):
    """
Definimos función: 
    object: El objeto de Python que deseas convertir a XML.
    tag="item": Un parámetro opcional que especifica la etiqueta del elemento raíz en el XML. Si no se proporciona, se usará "item" por defecto.
"""
    # Crear el elemento raíz
    root = ET.Element(tag)
    """
    Crea un nuevo elemento XML con la etiqueta especificada por tag y lo asigna a root. Este será el elemento raíz del XML.
    """
    
    # Añadir subelementos basados en los atributos del objeto
    for atributo, valor in vars(object).items():
        elem = ET.SubElement(root, atributo)
        elem.text = str(valor)
    """
    vars(object): Obtiene un diccionario de los atributos del objeto (es decir, sus variables de instancia).
    items(): Devuelve un iterador de pares clave-valor para el diccionario.
    ET.SubElement(root, atributo): Crea un subelemento de root con la etiqueta atributo.
    elem.text = str(valor): Establece el texto del subelemento como el valor de atributo convertido a cadena.
    """
    # Convertir el árbol XML a una cadena
    contenido_xml = ET.tostring(root, encoding='utf-8', method='xml').decode('utf-8')
    """
    ET.tostring(root, encoding='utf-8', method='xml'): Convierte el árbol XML (el elemento raíz y sus subelementos) en una cadena de bytes usando la codificación UTF-8.
    .decode('utf-8'): Decodifica la cadena de bytes a una cadena de texto en formato UTF-8.
    """

    return contenido_xml
    """Devuelve la representación XML como una cadena de texto."""

def dict_to_xml(dicc, tag="item"):  # Convierte un diccionario en una cadena XML, creando un elemento raíz con una etiqueta opcional.
    elem = ET.Element(tag)
    _dict_to_xml_recurse(dicc, elem)
    return ET.tostring(elem, encoding='utf-8', method='xml').decode('utf-8')


def _dict_to_xml_recurse(dicc, parent):     # Función recursiva que construye el XML para el diccionario, manejando diccionarios anidados, listas y otros tipos de valores.
    for key, value in dicc.items():
        if isinstance(value, dict):
            child = ET.SubElement(parent, key)
            _dict_to_xml_recurse(child, value)
        elif isinstance(value, list):
            for item in value:
                child = ET.SubElement(parent, key)
                if isinstance(item, dict):
                    _dict_to_xml_recurse(child, item)
                else:
                    child.text = str(item)
        else:
            child = ET.SubElement(parent, key)
            child.text = str(value)