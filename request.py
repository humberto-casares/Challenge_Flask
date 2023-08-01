import requests

#url = 'http://prolab.duckdns.org:8009/ner_es' # para ejecutar en servidor remoto
url = 'http://127.0.0.1:5000/ner_es' # para ejecutar en LocalHost

data = {
  "oraciones": [
    "Apple está buscando comprar una startup del Reino Unido por mil millones de dólares.",
    "San Francisco considera prohibir los robots de entrega en la acera."
  ]
}

try:
    response = requests.post(url, json=data)
    response.raise_for_status()  # Check for HTTP errors
    print(response.json())
except requests.exceptions.HTTPError as http_err:
    print(f"HTTP error occurred: {http_err}")
except requests.exceptions.RequestException as req_err:
    print(f"Request exception occurred: {req_err}")
except requests.exceptions.JSONDecodeError as json_err:
    print(f"JSON decoding error occurred: {json_err}")
    print(f"Response content: {response.content}")