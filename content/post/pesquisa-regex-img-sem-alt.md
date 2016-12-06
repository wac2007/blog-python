Category: Desenvolvimento
Description: Regex para pesquisar imagens sem alt
Tags: Desenvolvimento, SEO, HTML
Date: 2016-01-19 00:29:11
Title: Regex para pesquisar imagens sem alt

Sabe aquele teste de SEO que você passou no seu site, e o mesmo apontou que seu site possui imagens sem o atributo alt? Resolver isso procurando um a um, é doloroso, porém existe uma forma mais fácil.

Os grandes (e pequenos) editores de código, geralmente vem com pesquisas em arquivos e com o poder de utilizar [REGEX (Expressões Regulares)](https://pt.wikipedia.org/wiki/Express%C3%A3o_regular) em suas pesquisas.

Abra seu editor favorito, procure o comando *find in files* (pesquisar em arquivos), marque a opção de regex (se houver) e utilize o seguinte código para pesquisar:

```<img(?!.*alt).*?>```

Editores testados: 

* Sublime Text 3
* Notepad++
* Visual Studio
* Webstorm (E toda a Família do JetBrains)