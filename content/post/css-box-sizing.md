Category: Desenvolvimento
Description: Uma dica sensacional de como utilizar o Box Sizing correamente. Retirado do Origamid.
Tags: Development, CSS
Date: 2016-03-04 10:22:11
Title: Dica CSS - Box Sizing


O **box-sizing: border-box**; pode "salvar a sua vida".

Por padrão quando você define uma largura (width) de 100px, um padding (right e left) de 10px e um border (right e left) de 5px, você terá um elemento com 130px de largura.

Isso acontece devido ao box-sizing ter por padrão o valor content-box. Isso faz com que os valores do width/height sejam somados ao do padding e border para gerar a largura total do elemento. Neste exemplo seria:

100px + 10px + 10px + 5px + 5px = 130px.

Você pode mudar isso com o valor **border-box**. Com ele o padding e border passam a ser incorporados à largura total do elemento. Sendo assim o elemento continua com um total de 100px de largura, porém a sua área de conteúdo interno passa para 70px (uma vez que o padding e border vão ocupar 15px de cada lado no exemplo citado).

Com isso você não precisa mais ficar fazendo cálculos para saber qual será o total do elemento. Isso facilita principalmente quando se está trabalhando com porcentagens.


Fonte: [origamid.com](https://www.origamid.com/codex/dica-01-css-box-sizing/)