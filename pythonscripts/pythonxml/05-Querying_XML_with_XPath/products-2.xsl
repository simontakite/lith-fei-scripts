<?xml version="1.0" encoding="iso-8859-1"?>
<xsl:stylesheet version="1.0"
                xmlns:xsl="http://www.w3.org/1999/XSL/Transform">

<xsl:template match="/">
  <html>
    <body>
      <table>
        <xsl:apply-templates/>
      </table>
      <p>Your Total:
         <xsl:value-of select="sum(//@price)"/>
      </p>
    </body>
  </html>
</xsl:template>

<xsl:template match="item">
  <tr><td><b>Item: </b><xsl:value-of select="@name"/></td>
      <td><b>Price: </b><xsl:value-of select="@price"/></td>
  </tr>
</xsl:template>

</xsl:stylesheet>
