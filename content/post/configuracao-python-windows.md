Category: Desenvolvimento
Description: Configuração Do Python e Django com Virtual Env no Windows
Tags: Git, Python, Django, Windows, Configuração
Date: 2016-01-30 21:54:10
Title: Configuração Python e Django no Windows


Este tutorial é baseado nas vídeo aulas do curso <a href="http://welcometothedjango.com.br/" target="_blank">Welcome to the Django</a> do <a href="http://henriquebastos.net/" target="_blank">Henrique Bastos</a>. 

Primeiramente você precisa ter o Python Instalado. Caso ainda não tenha, [veja aqui como baixar e instalar o Python 3.5]({{< ref "instalar-python-windows.md" >}})

Crie uma nova variável de sistema chamada **PYTHON_DIR** e coloque o endereço de instalação do Python.

Adicione **%PYTHON_DIR%** e **%PYTHON_DIR%\Scripts** à variável path.

Chega de enrolar e vambora.

Crie uma pasta em um lugar acessível com o nome que você deseja, eu criei em 

```C:\python_apps```

Abra o terminal e vá na pasta que acabamos de criar. Digite o comando para o virtual env 

```python -m venv .python_apps```

Obs: O final precisa ter o mesmo nome da pasta criada.

Vamos ativar agora o Python do virtual env. Vá no terminal e digite o comando:

```.\python_apps\Scripts\activate.bat```

Para instalar o Django digite 

```pip install django```

Daí já podemos iniciar um novo projeto

```django-admin startproject novo-projeto .```

Vamos então configurar o manage, para poder acessar de qualquer pasta. Dentro da pasta .python_apps\Scripts, crie um arquivo chamado **manage.bat** com o seguinte comando:

```@python "%VIRTUAL_ENV%\..\manage.py" %*```

Daí já está tudo arrumado, e já podemos colocar a mão na massa com o Django!