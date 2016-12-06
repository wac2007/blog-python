Category: Desenvolvimento
Date: 2016-05-19 12:45:17
Description: Neste tutorial ensino como realizar a instalação do Python 3.5 no Windows, utilizando o Windows 10 como exemplo.
Tags: Development, Python, Windows, Python 3.5, Instalação, Configuração
Keywords: Development, Python, Windows, Python 3.5, Instalação, Configuração]
Title: Instalar Python 3.5 no windows


Neste tutorial, irei ensinar a instalar o Python 3.5 no Windows 10 (porém, serve para versões anteriores, como 7, 8 e 8.1).

### - Instalação

Primeiramente, baixe a versão do Python compatível com sua versão:

* [Python 3.5 - x32](https://www.python.org/ftp/python/3.5.1/python-3.5.1.exe)

* [Python 3.5 - x64](https://www.python.org/ftp/python/3.5.1/python-3.5.1-amd64.exe)

Após baixado, abra o instalador do Python (clique com o botão direito e execute como administrador)

Logo na primeira tela, marque o checkbox Add Python 3.5 to PATH e em seguida clique em Customize installation


![Instalador do Python](/images/instalar-python-windows/img1.png)

Nesta tela, deixe tudo marcado (ou personalize, se souber o que está fazendo) e clique em next.

![Funcionalidades Opcionais](/images/instalar-python-windows/img2.png)

Nesta tela, marque o primeiro checkbox (Install for all users) e grave o caminho onde o Python será instalado - *Customize install location* - pois precisaremos dele mais tarde (ou não).
Clique em Install.

![Funções Avançadas](/images/instalar-python-windows/img3.png)

Vamos testar se tudo está ok. Abra o prompt de comando e digite:

```
python --version
```

Se tudo estiver ok, você verá a versão do Python na tela, caso contrário, você verá que aparecerá um erro.

Sucesso: ![Instalado com sucesso](/images/instalar-python-windows/img8.png)


Erro: ![Erro na instalação](/images/instalar-python-windows/img9.png)


Caso você esteja desafortunado e obteve o erro, vamos fazer uma configuração manual (não, não fuja, é facinho de fazer :D)

### - Configuração Manual - Adicionando o Python no PATH do Windows

Primeiramente abra a configuração de Sistema. (Existem diversas formas de fazer isso, painel de controle, configurações, etc).
A forma mais fácil de abri-la é apertar a tecla windows + pause break. 

Feito isso, abra as configurações avançadas do sistema.

![Configurações de Sistema](/images/instalar-python-windows/img4.png)

Na guia avançado, abra variáveis de ambiente.

![Guia Avançado](/images/instalar-python-windows/img5.png)

Clique em novo (1). Na caixa que se abre digite o nome *PYTHON_HOME*. Lembra de onde instalamos o Python no passo lá de cima? O caminho do Python é o valor aqui. No meu caso é *C:\Program Files\Python 3.5*

Clique em ok.

![Variáveis de Ambiente](/images/instalar-python-windows/img6.png)

Não desista agora... Estamos perto do fim!

Na lista de variáveis, procure pela variável chamada **Path**, clique sobre ela e clique em editar (1). Na caixa que se abre, vá até o final do valor da variável, adicione o código abaixo (atenção ao ponto e vírgula na frente!!).
```
;%PYTHON_HOME%;%PYTHON_HOME%\Scripts
``` 

![Editor de Variável](/images/instalar-python-windows/img7.png)

É isso. Vá clicando em ok para salvar e fechar as janelas e está pronto.

Vamos realizar o último teste para mostrar que funcionou. Rode novamente o comando e você deverá ver a versão do Python instalada.

```
python --version
```

![Instalado com sucesso](/images/instalar-python-windows/img8.png)

Termina aqui mais um tutorial. Espero que tenha sido útil :D

Dúvidas ou comentários, só colocar abaixo.