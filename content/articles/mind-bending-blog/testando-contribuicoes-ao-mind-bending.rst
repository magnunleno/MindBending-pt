Testando Contribuições ao Mind Bending
######################################
:date: 2014-08-14 15:27
:category: Mind Bending Blog
:tags: pelican, git, make, makefile, fork, pull request, pip, python
:image: /images/MB_Logo_2014.png
:description: Finalmente consegui um tempo para documentar a forma de prever suas contribuições ao Mind Bending Blog antes de enviar seu pull-request.

Quando anunciei que o `blog estava aberto a contribuições`_ por meio de `pull-requests no GitHub`_, eu ainda não havia concluído a documentação sobre como realizar testes e previsões. Sim o `Hack 'n' Cast`_ estava tomando muito tempo!

.. image:: {filename}/images/misc/contribute.jpg
        :target: {filename}/images/misc/contribute.jpg
        :alt: Mind Bending Blog
        :align: center

Bem, agora está tudo documentado e utilizando o Pelican 3.4 (sua versão mais recente). Boa parte deste processo está documentado `aqui`_

.. more

Pré-Requisitos
--------------

Todos sabemos que o site é feito utilizando Pelican. Entretanto, não iremos instalar este (e suas dependências) diretamente no sistema operacional, iremos utilizar ambientes virtuais para o Python.

No sistema operacional é necessário instalar apenas:
``setuptools`` (que provê o comando ``pip``),  Como pré-requisitos é necessário instalar os seguintes pacotes:

Python 3
        A versão mais recente do Python, já que o Pelican 3.4 não está se dando muito bem com o Python 2.
python-setuptools
        Este pacote provê o comando ``pip``.
python-virtualenv
        Este pacote provê o comando ``virtualenv``.
libxml2-dev
        Este pacote é necessário para compilar a biblioteca ``lxml``.
libxslt-dev
        Este pacote é necessário para compilar a biblioteca ``lxml``.

Para instalar no Debian (e suas variantes) utilize o seguinte comando:

.. code::

        $ sudo aptitude install python3 python-setuptools python-virtualenv libxml2-dev libxslt-dev python3.3-dev

Para instalar no Fedora (e suas variantes) utilize o seguinte comando:

.. code::

        $ sudo yum install python3 python3-devel python-setuptools python-virtualenv libxml2-devel libxslt-devel

Para instalar no Arch Linux utilize o seguinte comando:

.. code::

        $ pacman -S python-setuptools python-virtualenv libxml2 libxslt

Criando o Ambiente Virtual
^^^^^^^^^^^^^^^^^^^^^^^^^^

Existem pessoas que não gostam, mas eu recomendo fortemente a utilização de ambiente virtual (*virtual env*) para evitar qualquer problema de compatibilidade de pacotes. Te garanto que da forma como eu estruturei o ``Makefile`` você não vai nem perceber que está utilizando um ``virtual env``.

Em seguida crie um ambiente virtual (``virtualenv``) para poder instalar o Pelican:

.. code::

        $ mkdir ~/venv
        $ virtualenv -p /usr/bin/python3 --prompt "(pelican-3.4)" ~/venv/pelican-3.4

Pronto! Viu, nem doeu!

Obtendo o Código
^^^^^^^^^^^^^^^^

Agora é só obter o código fonte do site através do ``git``:

.. code::

        $ git clone git@github.com:magnunleno/MindBending-pt.git
        $ cd MindBending-pt

Populando o Ambiente Virtual
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Popule o ambiente virtual (``virtualenv``) criado anteriormente utilizando os pacotes especificados em `requirements.txt`_:

.. code::

        $ . ~/venv/pelican-3.4/bin/activate; pip3 install -r ./requirements.txt; deactivate

**Nota:** Repare que antes do ambiente virtual existe um ponto.

Esta será a primeira e última vez que você precisará acessar este ambiente virtual diretamente, todas as outras vezes o ``make`` o fará por você.

Compilando o Site
-----------------

Existem algumas formas de se compilar o site para testes, dependendo de como você irá visualizá-lo:

#. Utilizando o NGINX.
#. Utilizando o servidor web embutido no python;
#. Utilizando o firefox/chrome navegando via sistema de arquvios (caminhos relativos);

**Nota:** Eu sempre uso o NGINX pois reproduz fielmente o ambiente de produção.

Note que as formas acima são independentes mas não mutuamente excludentes. Se você optar pelo modo 1, não precisa ler o modo 2. Mas se você quiser testar outros modos e ver qual mais lhe agrada, sinta-se a vontade. Gastei um bom tempo organizando o site para funcionar de todas as formas possíveis.

Servidor NGINX
^^^^^^^^^^^^^^

Primeiramente instale o NGINX, e copie o arquivo ``nginx-mindbending.dev`` localizado em ``.conf`` para diretório ``/etc/nginx/site-avaiable/mindbending.dev``. Em seguida crie um link simbólico no diretório ``sites-enabled`` um diretório para hospedar os arquivos estáticos gerados pelo Pelican:

.. code::

        $ cp ./conf/nginx/mindbending.dev /etc/nginx/site-avaiable/mindbending.dev
        $ sudo ln -s /etc/nginx/sites-available/mindbending.dev /etc/nginx/sites-enabled/
        $ sudo mkdir /var/www/MindBending
        $ chmod -R 777 /var/www/MindBending

Inicie o NGINX e compile o site com o seguinte comando:

.. code::

        $ make nginx

Após a conclusão da compilação todos os arquivos são movidos para ``/var/www/MindBending`` e não é necessário reiniciar ou recarregar o NGINX, apenas acesse o site através do navegador utilizando a URL http://localhost.

Caso você possua outras páginas respondendo por ``localhost``, você pode alterar a entrada no arquivo ``/etc/hosts`` para que fique similar ao abaixo:

.. code::

        $ 127.0.0.1       localhost mindbending.dev

Com isso, você poderá acessar o site através da URL http://mindbending.dev

Servidor Web Embutido no Python
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

A segunda forma, e a mais utilizada por pessoas que utilizam o Pelican por aí, é utilizar a infraestrutura provida pelo próprio Python/Pelican. Para isso compile o site da seguinte forma:

.. code::

        $ make html

Em seguida inicie o servidor através do seguinte comando:

.. code::

        $ make serve

Ou faça tudo em um comando só:

.. code::

        make html && make server

Em seguida acesse o site através da URL http://localhost:8000

Navegando via Sistema de Arquvios (Caminhos Relativos)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Por último, temos a forma mais simples que não requer nenhum tipo de servidor (NGINX ou embutido no Python), que é acessar os arquivos compilados diretamente pelo navegador utilizando o sistema de arquivos. Mas para que isto funcione, é necessário que o site seja compilado com suporte a caminhos relativos. Para isso utilize o seguinte comando:

.. code::

        $ make relative

Com isso os arquivos gerados estarão em ``./output`` e podem ser acessados da seguinte forma:

.. code::

        $ firefox ./output/index.html

Ou simplesmente abra um navegador de arquivos e clique duas vezes sobre o arquivo.

Conclusão
---------

Como vocês viram, não é muito difícil nem complicado. Essa forma aí é garantida para funcionar em qualquer GNU/Linux e é quase certo que funcionamento perfeitamente no Mac OS (mas não tenho um para testar e confirmar). Diria quase o mesmo para o Windows, mas como nunca pesquisei sobre ``virtualenv`` para Windows, não posso afirmar. Se alguém aí tiver alguma dessas plataformas e quiser tirar a prova, e só fazer um fork no github e documentar tendo como base este mesmo artigo.

Até a próxima.

.. _blog estava aberto a contribuições: http://mindbending.org/pt/aberto-a-contribuicoes
.. _pull-requests no GitHub: https://github.com/magnunleno/MindBending-pt
.. _Hack 'n' Cast: /pt/category/hack-n-cast
.. _aqui: https://github.com/magnunleno/MindBending-pt/blob/master/INSTALLING.rst
.. _requirements.txt: https://github.com/magnunleno/MindBending-pt/blob/master/requirements.txt
