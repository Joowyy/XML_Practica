xslt_ampliadoCSS = """<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
    <xsl:template match="/">
        <html>
            <head>
                <title>Ejercicio 3 - OrdenaciÃ³n empleados por departamente</title>
                <style>
                    body {
                        font-family: Arial, sans-serif;
                        max-width: 1000px;
                        margin: 0 auto;
                        padding: 20px;
                        background-color: #f0f2f5;
                    }
                    h1, h2 {
                        color: #1a237e;
                        text-align: center;
                    }
                    .century-section {
                        background-color: white;
                        border-radius: 8px;
                        padding: 20px;
                        margin: 20px 0;
                        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
                    }
                    table {
                        width: 100%;
                        border-collapse: collapse;
                        margin: 15px 0;
                    }
                    th, td {
                        padding: 12px;
                        text-align: left;
                        border-bottom: 1px solid #ddd;
                    }
                    th {
                        background-color: #1a237e;
                        color: white;
                    }
                    tr:hover {
                        background-color: #f5f5f5;
                    }
                </style>
            </head>
            <body>
                <h1>Empleados</h1>
                <div class="century-section">
                    <h2>Departamento</h2>
                    <table>
                        <tr>
                            <th>Nombre</th>
                            <th>Departamento</th>
                        </tr>
                        <xsl:for-each select="empresa/empleado">
                            <xsl:sort select="departamento"/>
                            <tr>
                                <td><xsl:value-of select="nombre"/></td>
                                <td><xsl:value-of select="departamento"/></td>
                            </tr>
                        </xsl:for-each>
                    </table>
                </div>
            </body>
        </html>
    </xsl:template>
</xsl:stylesheet>"""

# Guardar el XSLT mejorado
with open('transformacion_ejercicio03B.xslt', 'w', encoding='utf-8') as f:
    f.write(xslt_ampliadoCSS)