Adeus Wordpress
###############
:date: 2014-03-06 19:08
:category: Mind Bending Blog
:tags: blog, wordpress, pelican
:image: /images/MB_Logo_2014.png

De uns tempos pra cá eu tenho percebido o quão desperdício de recursos computacionais (e humanos) é utilizar um blog em Wordpress. Pensem um pouco, eu comecei este blog em 2010, por qual motivo o 1º artigo que eu escrevi precisa ser "regerado" toda vez que que alguém o acessa? Ele poderia muito bem ser uma página HTML estática servida pelo Apache. E quanto a toda a interface web e administração? Já faz um ano que eu escrevo todos os artigos deste blog no VIM, diretamente em HTML.

.. image:: {filename}/images/pelican/flying_pelican.png
        :align: center
        :alt: Pelican
        :target: {filename}/images/pelican/flying_pelican.png

Por esses (e alguns outros poucos) motivos, migrei meu blog (na verdade dois) inteiro para o `Pelican`_, uma gerador de sites estáticos escrito em Python. E vocês aí achando que eu estava a toa este tempo todo.

.. more

Para aqueles que possam se interessar, eu não me arrependo nem um pouco da migração. Uma das coisas que mais me incomodava no Wordpress era a minha vontade incontrolável de customizá-lo/estendê-lo associada à minha grande inabilidade com a linguagem PHP. Agora, com o Pelican eu posso hackea-lo a vontade.

Na verdade, desde que comecei essa migração eu nunca programei tanto. Fiz alguns scripts em shell e outros em Python para processar os artigos antigos do Wordpress, alguns scripts em bash para automatizar a compilação do blog, aprendi a utilizar o `Jinja2`_, fiz alguns plugins para o Pelican (`este por exemplo`_), criei este tema baseado no `Bootstrap`_... É foram 2 meses bem ocupados.

Agora o Mind Bending Blog está em uma nova fase, com um workflow muito mais agradável para mim (VIM+GIT+Make+Pelican) rodando com o NGINX (estou feliz por abandonar o Apache também), em breve vou escrever aqui todo o processo de migração, as configurações do NGINX, Git e os scripts que utilizei para automatizar esse processo.

É isso aí pessoal. Até mais...

.. _Pelican: http://docs.getpelican.com/en/3.3.0/
.. _Jinja2: http://jinja.pocoo.org/
.. _este por exemplo: https://github.com/magnunleno/pelican-gist
.. _Bootstrap: http://getbootstrap.com/
