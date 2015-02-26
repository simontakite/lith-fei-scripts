<?xml version="1.0" encoding="iso-8859-1"?>
<xsl:stylesheet version="1.0"
 xmlns:xsl="http://www.w3.org/1999/XSL/Transform">

<xsl:template match="/">
  <html>
    <body>
      <xsl:apply-templates/>
    </body>
  </html>
</xsl:template>

<xsl:template match="item">
  <p><b>Item:</b> <xsl:value-of select="@name"/>
  Orig. Price: <xsl:value-of select="@price"/>, Our Price:
  <xsl:value-of select="@price * 0.8"/>
  </p>
</xsl:template>

</xsl:stylesheet>
