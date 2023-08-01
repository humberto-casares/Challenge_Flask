# Challenge_Flask
API REST sencilla que recibe una lista de oraciones en español y devuelva una lista de las entidades nombradas identificadas en cada oración.

## Description
Esta API es una aplicación web basada en Flask que proporciona reconocimiento de entidad con nombre (NER) para texto en español utilizando el modelo spaCy NER. Puede procesar oraciones individuales o una lista de oraciones y devolver las entidades detectadas y sus etiquetas correspondientes.

## Comenzando
### Instalación

1. Clonar este repositorio: git clone https://github.com/humberto-casares/Challenge_Flask.git
2. Crea un entorno virtual y actívalo: python -m virtualenv venv # Para crear entorno virtual
   activación de venv: source venv/bin/activate # Para Windows, usar "venv\Scripts\activate"
3. Instala las dependencias requeridas: pip install -r requirements.txt

### Uso
1. Ejecute el servidor de API en entorno local: python main.py
2. Realice solicitudes POST a `http://127.0.0.1:5000/ner_es` con payload JSON que contenga el campo `oraciones`. El servidor responderá con las entidades detectadas.
3. Cabe mencionar que la API también esta en un servidor remoto CentOS7 con gunicorn en `http://prolab.duckdns.org:8009/ner_es`.

4. Solicitud de ejemplo:
{
  "oraciones": [
    "Apple está buscando comprar una startup del Reino Unido por mil millones de dólares.",
    "San Francisco considera prohibir los robots de entrega en la acera."
  ]
}

Ejemplo de respuesta::
{'resultado': [{'entidades': {'Apple': 'ORG', 'Reino Unido': 'LOC'}, 'oración': 'Apple está buscando comprar una startup del Reino Unido por mil millones de dólares.'}, {'entidades': {'San Francisco': 'LOC'}, 'oración': 'San Francisco considera prohibir los robots de entrega en la acera.'}]}

4. Puede ejecutar el arcivo request.py para ver la respuesta de la api, hay 2 opciones en la variable url, si está corriendo Flask en localhost entonces habilita la url con localhost. Si no está ejecutando Flask entonces puede correr el archivo con la url remota habilitada.
   
Endpoints de la API
Reconocimiento de entidad nombrada (NER)
URL: /ner_es
Método: POST
Cuerpo de la solicitud: JSON con campo "oraciones" que contiene una lista de oraciones.
Respuesta: JSON con campo "resultado" que contiene las entidades detectadas para cada frase.

Créditos
spaCy: para la biblioteca NLP utilizada en esta API.
Flask: para el micro framework de la aplicación web.
Gunicorn: para el servidor listo para producción.
