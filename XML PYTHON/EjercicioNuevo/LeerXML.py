from lxml import etree

# Habilita la resolución de entidades externas
varParser = etree.XMLParser(resolve_entities=True, load_dtd=True)

# Carga el archivo XML
xml_path = "Practica_Variables2.xml"
elParser = etree.parse(xml_path, varParser)

# Mostrar el XML procesado
print(etree.tostring(elParser, pretty_print=True).decode())