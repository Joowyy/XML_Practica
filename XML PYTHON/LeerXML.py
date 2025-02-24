import xmltodict
import requests

# URL del XML servidor
url = "http://127.0.0.1:00/MIS XML/catalogo_cd.xml"

responder = requests.get(url)

if responder.status_code == 200:
    datos = xmltodict.parse(responder.text)

    # Acceder a los CDs
    for cd in datos["CATALOG"]["CD"]:
        print(f"Titulo: {cd['TITLE']}, Artista: {cd['ARTIST']}, Año: {cd['YEAR']}")
    else:
        print("Error al acceder al XML: ", responder.status_code)