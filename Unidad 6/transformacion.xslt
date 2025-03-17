<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
    <xsl:template match="/">
        <html>
            <head>
                <title>Mi Biblioteca</title>
            </head>
            <body>
                <h1>Catálogo de Libros</h1>
                <table border="1">
                    <tr>
                        <th>Título</th>
                        <th>Autor</th>
                        <th>Año</th>
                    </tr>
                    <xsl:for-each select="biblioteca/libro">
                        <tr>
                            <td><xsl:value-of select="titulo"/></td>
                            <td><xsl:value-of select="autor"/></td>
                            <td><xsl:value-of select="año"/></td>
                        </tr>
                    </xsl:for-each>
                </table>
            </body>
        </html>
    </xsl:template>
</xsl:stylesheet>