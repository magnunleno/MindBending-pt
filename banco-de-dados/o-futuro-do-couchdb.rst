O Futuro do CouchDB
###################
:date: 2012-01-05 09:04
:category: Bancos de Dados
:tags: apache, banco de dados, couchbase, couchdb, nosql, notícia
:image: /images/couchdb.jpg

Neste último dia 04/01 (Quarta-Feira) Damien Katz, um dos criadores do
projeto `Apache CouchDB`_, divulgou em seu blog que ele e o `time de
desenvolvimento Couchbase`_ não terão mais o CouchDB como projeto
principal.

.. image:: {filename}/images/couchdb.jpg
	:align: center
	:target: {filename}/images/couchdb.jpg
	:alt: CouchDB

Conforme dito por Katz, o novo foco de desenvolvimento é o **Couchbase
Server**:

    Não quer dizer que o CouchDB não é incrível. Simplesmente estamos
    criando seu sucessor: Couchbase Server. Um produto e projeto com
    capacidades e objetivos similares, porém mais rápido, mais
    escalável, mais customizável e com foco nos desenvolvedores. E
    definitivamente não será parte da Apache.

.. more

Muitos devem se perguntar **"Porquê não continuar evoluindo o
CouchDB?"**, Damien Katz explica que o desenvolvimento do Apache CouchDB
foi governado pelo **consenso da comunidade**, o que o levou a seguir
caminhos que (hoje) ele considera como não sendo os melhores. Pode
parecer um descaso com a Apache, mas ele explica: "**A Apache foi a
grande responsável pelo sucesso do CouchDB**, sem isso o CouchDB não
teria alcançado o sucesso repentino que alcançou. Mas em minha opinião,
o projeto alcançou um ponto onde a abordagem consensual limitou a
competitividade do projeto. Não é pessoal, é negocial."

O foco inicial do desenvolvedor é tornar o `CouchBase Server 2.0`_
**pronto para uso em ambiente produtivo** e tornando-o o banco de dados
NoSQL mais fácil, rápido e confiável, além de reescrever o núcleo do
projeto utilizando C/C++.

O CouchDB é um dos bancos de dados NoSQL mais famosos e utilizados
atualmente. Boa parte desta fama é resultado do esforço de divulgação e
de algumas decisões estratégicas tomadas pela Fundação Apache, tornando
o CouchDB um SGBD único e com grande apelo para os desenvolvedores Web.
Por isso os usuários do Apache CouchDB podem continuar despreocupados,
**o projeto é forte e ativo**, pois continuará sendo desenvolvido pelo
restante da equipe/comunidade. Não há chances do projeto ser
descontinuado, pois possui diversos patrocinadores como, Cloudera, Right
Scale, Canonical, Red Hat, Heroku, AppFirst, Fusion-io, HP e VMWare.
Claro que nenhum apoio/patrocínio do mundo pode suprir a perda de um dos
principais "cabeças" do projeto, logo podemos esperar uma possível
mudança no ritmo de desenvolvimento do CouchDB. Se você está curioso
para saber um pouco mais sobre o COuchDB, sugiro dar uma olhada neste
outro artigo publicado aqui no blog Mind Bending: `Python e CouchDB na
Prática`_

É interessante perceber que esta notícia mostra tanto o lado bom quanto
o lado perigoso do mundo Open Source. Ao mesmo tempo que este modelo
permitiu que Damien Katz utilizasse o código do CouchDB como base para o
CouchBase Server, este mesmo modelo é **parcialmente** culpado pelo
caminho que o CouchDB tomou. Existem diversos modelos para o
desenvolvimento OpenSource, o modelo adotado pela Apache permite que
diversas "pessoas" tenham poder para interferir no caminho que seus
software tomam, por isso usei a palavra **"parcialmente"**.

Dando uma olhada na `sessão de download do CouchBase Server`_, acabei me
decepcionando, e muito. O CouchBase está sendo distribuído em duas
modalidades: *Enterprise Edition* e *Community Edition*. A *Community
Edition* é voltado para pequenas aplicações e não oferece atualizações
e/ou *hotfixes* imediatamente. Já a *Enterprise Edition* é o produto
completo, submetido a testes de performance e funcionalidade, e **é o
único produto ao qual os desenvolvedores oferecem suporte**. A
*Enterprise Edition* também é dividida em dois tipos, a versão paga e a
versão gratuita. A versão gratuita só pode ser utilizada em até 2
servidores de produção.

Exposto isto, eu entendo que o único produto Livre que eles irão
distribuir é o CouchBase Community Server (ao qual não é oferecido
suporte), pois, ao restringir o uso da *Enterprise Edition* eles ferem
as regras da liberdade de uso do software. Creio que isso impedirá que
muitas pessoas pensem em migrar do CouchDB.

.. _Apache CouchDB: http://damienkatz.net/2012/01/the_future_of_couchdb.html
.. _time de desenvolvimento Couchbase: http://www.couchbase.com/
.. _CouchBase Server 2.0: http://www.couchbase.org/get/couchbase/2.0.0
.. _Python e CouchDB na Prática: /pt/destaques-da-pycon2011-python-and-couchdb-in-practice/
.. _sessão de download do CouchBase Server: http://www.couchbase.com/downloads
