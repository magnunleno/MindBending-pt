Contribuindo com o Mundo Open Source
####################################
:date: 2013-11-27 13:34
:category: Web2Py
:tags: contribuição, foss, framework, open, openldap, source, web2py
:image: /images/The_GNU_logo-300x293.png
:slug: contribuindo-mundo-open-source

É relativamente comum ver na comunidade Python pessoas com um bom conhecimento e capacidade para colaborar com alguns projetos. Mas muitos se abstêm com a famosa frase: "não sou bom o suficiente". Entretanto, este é um grande erro. Não somente o fato de achar que seu conhecimento é insignificante quanto o comportamento padrão de "endeusar" o desenvolvedor e considerá-lo detentor da sabedoria suprema. Este texto mostra (de forma empírica) como qualquer um pode contribuir para um projeto FOSS (*Free Open Source Software*).

.. image:: {filename}/images/muro.jpg
	:align: center
	:target: {filename}/images/muro.jpg
	:alt: muro

É claro que em projetos mais complexos, como o kernel Linux, CPython, NGINX e etc, muitos de nos realmente é incapaz de contribuir e somos meras amebas acéfalas perto dos desenvolvedores. Entretanto, em projetos mais simples como *frameworks*, bibliotecas e aplicativos, uma simples vivência com alguma ferramenta pode ser um grande diferencial. Todo projeto FOSS é como um grande muro, onde cada um põe um tijolo, alguns põem mais tijolos que outros mas são todos extremamente importantes.

.. more

O Desenvolvedor Não Sabe De Tudo
--------------------------------

O primeiro conceito que temos que esquecer é que o desenvolvedor **sempre** sabe mais que você. Recentemente comecei a desenvolver um aplicativo simples para um necessidade específica aqui no meu trabalho (note que não sou desenvolvedor por profissão, sou analista de infraestrutura), e tive a necessidade de utilizar o `Web2py`_ com PostgreSQL e OpenLDAP.

Para minha surpresa, a DAL do Web2py não suporta nativamente o conceito de *schemas* do PostgreSQL. Para quem não tem familiaridade com PostgreSQL, um *schema* (ou esquema) é algo similar a um agrupamento de tabelas, com o intuito de criar contextos e segmentar a informação e as permissões de acesso. Consequentemente resolvi pesquisar como configurar o Web2py para trabalhar em um *schema* diferente do *public* e encontrei este `bug`_. Durante a leitura tive um grande surpresa. Notem que a primeira resposta é do próprio Massimo DiPierro, criador do Web2py, e nela fica óbvio que ele não tem a mínima noção do que são *schemas* em um banco de dados. Não me entendam mal, não estou tentando difamar o criador deste *framework*, pelo contrário, estou tentando mostrar que ele não sabe de tudo e precisa da colaboração de diversas pessoas com conhecimentos heterogêneos para construir um bom *framework*. Foi esta constatação que me fez escrever este texto.

O segundo problema foi com o OpenLDAP. Como este serviço hospeda diversas informações sensíveis do usuários, é comum que os administradores deste serviço desabilitem a consulta anônima à base, sendo necessário a utilização de uma "conta de administração" para a realização do *bind* na base para posteriormente executar a consulta e autenticação. Para quem não está familiarizado com estes conceitos, a "conta de administração" nada mais é que uma conta de usuário utilizado apenas pelo serviço (meu sistema) para se autenticar no OpenLDAP antes de autenticar o usuário que loga no sistema. Curiosamente o Web2py só suporta o *bind* com uma "conta de administração" para o LDAP da Microsoft, mais conhecido como Active Directory (AD).

Saindo da Inércia
-----------------

Pesquisando rapidamente no código fonte do Web2py percebi que toda a autenticação é tratada no arquivo ``web2py/gluon/contrib/login_methods/ldap_auth.py`` pela função ``ldap_auth_aux`` (linha 162). Na especificação da função existem os argumentos ``ldap_binddn`` e ``ldap_bindpw``, responsáveis por receber o nome do usuários de administração e a sua respectiva senha. Pesquisando por ``ldap_bindpw`` encontramos a implementação da autenticação prévia no AD:

.. code-block:: python

    if ldap_mode == 'ad':
        # ...
        if ldap_binddn:
            # need to search directory with an admin account 1st
            con.simple_bind_s(ldap_binddn, ldap_bindpw)
        else:
            # credentials should be in the form of username@domain.tld
            con.simple_bind_s(username, password)

Podemos notar que a implementação não é complexa, e deve ser similar para o OpenLDAP. Lendo mais o código, encontrei onde o OpenLDAP realiza a autenticação (linha 268) e adicionei duas linhas conforme abaixo (baseado no que vi para o AD):

.. code-block:: python

    if ldap_mode == 'cn':
        # OpenLDAP (CN)
        if ldap_binddn and ldap_bindpw:
            con.simple_bind_s(ldap_binddn, ldap_bindpw)

Após os testes a comunicação com o OpenLDAP estava funcionando conforme eu esperava.

Como podem ver, é um código extremamente simples e que qualquer outro usuário do Web2py teria feito. A pergunta que fica é: "Porquê ninguém o escreveu?". Meu palpite é que ninguém tinha uma infraestrutura pronta para testes e/ou tinha conhecimento que o OpenLDAP pode funcionar assim.  Por isso digo, nunca ache que o desenvolvedor sabe tudo.

Devolvendo à Comunidade
-----------------------

Muito bem, neste ponto (em que temos uma solução testada e que pode ser utilizada pela comunidade) muitos não enviam a alteração para o desenvolvedor, provavelmente por dois motivos: receio de uma má recepção; ou não saber trabalhar com versionadores/patches/diffs.

E é aí, meus amigos, que eu tenho uma outra boa lição: para contribuir com softwares livre no `GitHub`_ você não é obrigado a conhecer o Git ou trabalhar com patches/diffs. Vejam como eu fiz a contribuição (na forma de prova de conceito):

-  Encontre o `arquivo a ser alterado`_;
-  Clique no botão *Edit*;
-  Altere o código fonte;
-  Preencha o *Commit summary:* e o *Extended description: (optional)*;
-  Pressione o botão *Propose File Change*;
-  Em seguida preencha os dados do *Pull Request* (título e descrição);
-  Agora aguarde...

Como podem ver, a única coisa que eu utilizei para devolver esta contribuição para o desenvolvedor foi o meu browser. No fim temos o `seguinte resultado`_: uma contribuição aceita.

Conclusão
---------

Como afirmado anteriormente na introdução deste artigo, todo projeto FOSS é como um muro onde cada um põe seu tijolo, alguns contribuem em maior número, outros em pouca quantidade mas de suma criticidade e outros contribuem esporadicamente. Mas o que importa não é o tamanho ou a importância da contribuição, mas a contribuição em si, pois a heterogeneidade do conhecimento é que propicia o desenvolvimento de um bom software.

Desta forma, esqueça seu receio de contribuir e nunca ache que sua contribuição não tem importância.

Happy hacking...

.. _Web2py: https://github.com/web2py/web2py
.. _bug: http://code.google.com/p/web2py/issues/detail?id=693
.. _GitHub: http://github.com
.. _arquivo a ser alterado: https://github.com/web2py/web2py/blob/master/gluon/contrib/login_methods/ldap_auth.py
.. _seguinte resultado: https://github.com/web2py/web2py/pull/293
