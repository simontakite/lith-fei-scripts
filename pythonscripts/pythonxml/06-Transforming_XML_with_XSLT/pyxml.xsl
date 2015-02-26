<?xml version="1.0" encoding="UTF-8" ?>
<xsl:stylesheet
 xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
 version="1.0">

<xsl:output method="html"/>

<xsl:template match="pyxml">
<html>
  <body bgcolor="#FFFFFF" text="#3333FF">
    <xsl:apply-templates/>
  </body>
</html>
</xsl:template>

<xsl:template match="file">
  <p><table cellpadding="0" cellspacing="0" border="1"
      bordercolor="#000000" width="540">
    <tr>
      <td align="center">Source file:
        <b><font color="#FF0000">
          <xsl:value-of select="./@name"/>
        </font></b>
      </td>
    </tr>
    <xsl:apply-templates/>
  </table></p>
</xsl:template>

<xsl:template match="class">
  <tr>
    <td>Class: <b><xsl:value-of
                   select="./@name"/></b>
    </td>
  </tr>
  <xsl:apply-templates/>
</xsl:template>

<xsl:template match="method">
  <tr>
    <td align="left">
      <font color="#000000">
        <xsl:value-of select="./@name"/>
      </font>
    </td>
  </tr>
</xsl:template>

</xsl:stylesheet>
