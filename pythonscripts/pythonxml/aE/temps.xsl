<?xml version="1.0"?>
<xsl:stylesheet
 xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
 version="1.0">

<xsl:variable name="average"
     select="sum(//CalendarYear/Month/text()) div 12"/>
<xsl:template match="/">
<html>
<body>
  <p>
  <font face="tahoma,arial,helvetica" size="2">
    <xsl:value-of select="/CalendarYear/@data"/> for
    <xsl:value-of select="/CalendarYear/@value"/>:
  </font>
  </p>
  <table border="1"
         bordercolor="#000000"
         cellpadding="5"
         cellspacing="0"
         width="350">
    <xsl:apply-templates/>
    <tr>
      <td colspan="2" bgcolor="#88BBEE" width="350"
          align="right">
        <p>
          <font face="tahoma,arial,helvetica" size="2">
            <b>Average:
              <xsl:value-of select="format-number($average, '0.00')"/>
            </b>
          </font>
        </p>
       </td>
    </tr>
  </table>
</body>
</html>
</xsl:template>

<xsl:template match="Month">
  <tr>
    <td bgcolor="#CCCCCC" width="325" align="left">
      <p>
        <font face="tahoma,arial,helvetica" size="2">
          Month: <b><xsl:value-of select="@name"/></b>
        </font>
      </p>
    </td>
    <td bgcolor="#CCCCCC" width="25" align="left">
      <p>
        <font face="tahoma,arial,helvetica" size="2">
          <b><xsl:value-of select="./text()"/></b>
        </font>
      </p>
    </td>
  </tr>
</xsl:template>

</xsl:stylesheet>
