Pré-Requisitos
--------------

Como pré-requisitos é necessário instalar os seguintes pacotes:

- python-setuptools
- python-virtualenv
- libxml2-dev
- libxslt-dev
- Python 3

No Debian (e suas variantes) utilize o seguinte comando:

.. code::

        $ sudo aptitude install python3 python-setuptools python-virtualenv libxml2-dev libxslt-dev python3.3-dev

No Fedora (e suas variantes) utilize o seguinte comando:

.. code::

        $ sudo yum install python3 python-setuptools python-virtualenv libxml2-devel libxslt-devel

No Arch Linux utilize o seguinte comando:

.. code::

        $ pacman -S python-setuptools python-virtualenv libxml2 libxslt

Em seguida crie um ambiente virtual (`virtualenv`) para poder instalar o pelican:

.. code::

        $ mkdir ~/venv
        $ virtualenv -p /usr/bin/python3 --prompt "(pelican-3.4)" ~/venv/pelican-3.4

Agora obtenha o código fonte do site Mind Bending:

.. code::

        $ git clone git@github.com:magnunleno/MindBending-pt.git
        $ cd MindBending-pt

Popule o ambiente virtual (`virtualenv`) criado anteriormente utilizando os pacotes especificados em `requirements.txt`_:

.. code::

        $ . ~/venv/pelican-3.4/bin/activate; pip3 install -r ./requirements.txt; deactivate

**Nota:** Repare que antes do ambiente virtual existe um ponto.

.. _requirements.txt: https://github.com/magnunleno/MindBending-pt/blob/master/requirements.txt

Compilando o Site
-----------------

Existem algumas formas de se compilar o site para testes, dependendo de como você irá visualizá-lo:

- Utilizando o servidor web embutido no python;
- Utilizando o firefox/chrome navegando via sistema de arquvios (caminhos relativos);
- Utilizando o NGINX.

**Nota:** Eu sempre uso o NGINX pois reproduz fielmente o ambiente de produção.

Servidor NGINX
~~~~~~~~~~~~~~

Primeiramente instale o NGINX, e copie o arquivo `/.conf/nginx-mindbending.dev` para `/etc/nginx/site-avaiable/mindbending.dev`. Em seguida crie um link simbólico no diretório `sites-enabled`:
.. code::

        $ sudo ln -s /etc/nginx/sites-available/mindbending.dev /etc/nginx/sites-enabled/

Inicie o NGINX e compile o site com o seguinte comando:

.. code::

        $ make nginx

Após a conclusão da compilação acesse o site através do navegador utilizando a URL http://localhost.

Caso você possua outras páginas repondendo por localhost, você pode alterar a entrada no arquivo `/etc/hosts` para que fique similar ao abaixo:

.. code::

        $ 127.0.0.1       localhost mindbending.dev

Com isso, você poderá acessar o site através da URL http://mindbending.dev

Servidor Web Embutido no Python
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A segunda forma, e a mais utilizada por pessoas que utilizam o Pelican por aí, é utilizar a infraestrutura provida pelo próprio Python/Pelican. Para isso compile o site da seguinte forma:

.. code::

        $ make html

Em seguida inicie o servidor através do seguinte comando:

.. code::

        $ make server

Ou faça tudo em um comando só:

.. code::

        make html && make server

Em seguida acesse o site através da URL http://localhost:8000

Navegando via Sistema de Arquvios (Caminhos Relativos)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Por último, temos a forma mais simples que não requer nenhum tipo de servidor (NGINX ou embutido no Python), que é acessar os arquivos compilados diretamente pelo navegador utilizando o sistema de arquivos. Mas para que isto funcione, é necessário que o site seja compilado com suporte a caminhos relativos. Para isso utilize o seguinte comando:

.. code::

        $ make relative

Com isso os arquivos gerados estarão em `./output` e podem ser acessados da seguinte forma:

.. code::

        $ firefox ./output/index.html

Ou simplesmente abra um navegador de arquivos e clique duas vezes sobre o arquivo.
