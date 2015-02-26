<?xml version="1.0" encoding="iso-8859-1"?>
<xsl:stylesheet version="1.0"
 xmlns:xsl="http://www.w3.org/1999/XSL/Transform">

<xsl:template match="story">
  <html>
    <head><title>The Story Page</title></head>
    <body>
      <form action="xslt.cgi" method="get">
        <xsl:apply-templates/>
      </form>
    </body>
  </html>
</xsl:template>

<xsl:template match="title">
  <h1><xsl:value-of select="."/></h1>
  <p>New Title:
    <input type="text" name="title" length="20"/>
  </p>
</xsl:template>

<xsl:template match="body">
  <p>New Body:
    <textarea rows="10" cols="50" name="body">
      <xsl:value-of select="."/>
    </textarea>
    <input type="hidden" name="mode" value="change"/>
    <p><input type="submit"/></p>
  </p>
</xsl:template>

</xsl:stylesheet>
