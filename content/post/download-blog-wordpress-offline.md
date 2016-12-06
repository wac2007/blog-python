Category: Desenvolvimento
Description: Download blog Wordpress para rodar Offline
Tags: Desenvolvimento, Wordpress, PHP
Date: 2016-01-18 19:59:10
Title: Download blog Wordpress para rodar Offline


Muitas vezes nos deparamos com clientes que possuem sites rodando no Wordpress e desejam fazer alterações, porém, mexer em um site enquanto o mesmo está no ar perigoso, pois um detalhe e podemos colocar tudo à perder (inclusive perder o cliente).
Portanto, vamos aprender como instalar o Wordpress já de um site existente para  fazer as alterações e enviar apenas o necessário de volta ao servidor.

Neste tutorial vou assumir que você tenha:

* Servidor de php  como *WAMP, XAMP ou LAMP*
* Tenha instalado um banco de dados MySQL (e um software para se conectar como **phpMyAdmin** ou **MySQLWorkbench**)
* Saiba instalar um Wordpress do zero
* Tenha um usuário com permissões administrativas, para logar no site que deseja baixar.

Primeiramente, vamos entrar no site em produção e instalar o plugin **UpdraftPlus Backup and Restoration**.

![Instalar UpdraftPlus](/images/tutorial-download-blog/a1.PNG)

Após instalar o plugin, já ative-o e abra sua página de configuração em **Settings > UpdraftPlus Backups** 

![Configurações UpdraftPlus](/images/tutorial-download-blog/a2.PNG)

Na nova página que abrir, clique em **Backup Now** 

![Backup UpdraftPlus](/images/tutorial-download-blog/a3.PNG)

Você verá que após clicar, haverá uma barra de progresso, aguarde até que o backup 
termine e você verá que o campo *Last Log message* será alterado para **The Backup apparently succeeded**, isso mostra que o backup possivelmente está ok (Sim, ele não nos dá 100% de certeza).

![Progresso do Backup](/images/tutorial-download-blog/a4.PNG)

![Fim do Backup](/images/tutorial-download-blog/a5.PNG)

Clique na aba **Existing Backups** e você verá a data e hora dos backups (um por linha).
Na coluna Backup data, clique em todos os botões para baixar seus respectivos arquivos (Database, Plugins, Themes, Uploads e Others)

![Download arquivos Backup](/images/tutorial-download-blog/a6.PNG)

Para cada botão que você clicou, uma mensagem será criada. Clique em **Download to your computer** para começar a baixar os arquivos.

![Download arquivos Backup](/images/tutorial-download-blog/a7.PNG)

Ao terminar de baixar os arquivos, crie uma nova instalação do Wordpress na sua máquina (recomendo que seja da mesma versão que está em produção pra não dar problemas).

Instale o plugin UpdraftPlus nesta nova instalação e vá para a página de administração do plugin.

Vá para a aba **Existing Backups** e clique em **Upload backup files**, abrirá uma seção para adicionar os arquivos. Simplesmente arraste os arquivos baixados do servidor para a seção (ou use o botão select files) 

![Importação dos arquivos de Backup](/images/tutorial-download-blog/b1.PNG)

Você verá que foi criado um novo registro de backup, clique no botão restore.

![Backup já importado](/images/tutorial-download-blog/b2.PNG)

Na janelinha que abrir, marque todas as opções e clique em restore.

![Backup já importado](/images/tutorial-download-blog/b3.PNG)

Pode ser que você recebe um Warning, dizendo que o backup é de um site diferente, neste caso, apenas ignore e clique em Restore novamente.

![Backup já importado](/images/tutorial-download-blog/b4.PNG)

Aguarde a restauração. Se ao término, tudo ocorrer bem, você verá a mensagem **Restore Successful!** (Calma, já está acabando!)

![Backup já importado](/images/tutorial-download-blog/b5.PNG)

Acesse o banco de dados da sua máquina (Importante! É o da máquina, não o de produção!) e entre no schema associado ao Wordpress. Na tabela options, altere os registros da imagem (siteurl e home) com a url local.

**Antes**

![Banco antes](/images/tutorial-download-blog/b6.PNG)

**Depois**

![Banco depois](/images/tutorial-download-blog/b7.PNG)

Depois disso, entre na url local e teste. Se tudo ocorreu bem, você já está podendo ver o mesmo rodando. Agora é só fazer as alterações, testá-las localmente, e enviar apenas as alterações (FTP por exemplo).

**Nota:** Caso seu site possua links permanentes (permalinks) é importante gerá-los novamente, para não ter erros. Basta ir em Settings > Permalinks (Configurações > Links Permanentes) e clicar em save novamente. 

