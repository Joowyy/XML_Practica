from lxml import etree

# Habilita la resolución de entidades externas
varParser = etree.XMLParser(resolve_entities=True, load_dtd=True, no_network=False)

# Carga el archivo XML
xml_path = "Practica.xml"
elParser = etree.parse(xml_path, varParser)

# Mostrar el XML procesado
print(etree.tostring(elParser, pretty_print=True).decode())