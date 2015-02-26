<?xml version="1.0" encoding="iso-8859-1"?>
<xsl:stylesheet version="1.0"
 xmlns:xsl="http://www.w3.org/1999/XSL/Transform">

<xsl:template match="story">
  <html>
    <head><title>The Story Page</title></head>
    <body><xsl:apply-templates/>
    </body>
  </html>
</xsl:template>

<xsl:template match="title">
  <h1><xsl:apply-templates/></h1>
</xsl:template>

<xsl:template match="body">
  <p><xsl:apply-templates/></p>
  <p>
    <form action="xslt.cgi" method="get">
      <input type="hidden" name="mode" value="edit"/>
      <input type="submit" value="Edit Me"/>
    </form>
  </p>
</xsl:template>

</xsl:stylesheet>
