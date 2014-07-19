Destaques da PyCon2011: Python and CouchDB in Practice
######################################################
:date: 2011-12-21 09:41
:category: PyCon
:tags: couchdb, livro, nosql, palestra, português, pycon2011, python
:image: /images/pycon2010.png
:series: Destaques da Pycon 2011

Mais uma palestra que destaco da PyCon2011 ocorrida em Atlanta. Esta
palestra ministrada por Luke Gotszling fala sobre Python e CouchDB, um
banco de dados NoSQL orientado a documento.

.. raw:: html

        <p style="text-align: center;"><object width="600" height="366" id="player"><param value="http://blip.tv/scripts/flash/showplayer.swf?file=http://blip.tv/rss/flash/4897385" name="movie"><param value="true" name="allowFullScreen"><param value="always" name="allowscriptaccess"><param value="transparent" name="wmode"><embed width="600" height="366" allowfullscreen="true" allowscriptaccess="always" type="application/x-shockwave-flash" src="http://blip.tv/scripts/flash/showplayer.swf?file=http://blip.tv/rss/flash/4897385"></object></p>

Agora algumas informações complementares...

.. more

O Que É CouchDB?
----------------

O CouchDB é o banco de dados orientado a documento *open source* da
Fundação Apache escrito quase inteiramente em `Erlang`_. Ele oferece uma
replicação incremental com detecção e resolução de conflito
bidirecional. O CouchDB oferece uma API JSON RESTful que pode ser
acessada através de requisições HTTP.

O termo "Couch" é um acrônimo para "Cluster Of Unreliable Commodity
Hardware", que reflete a meta do CouchDB de ser extremamente escalável,
oferecendo alta disponibilidade e confiabilidade.

Para quem quiser aprender mais sobre o CouchDB, existe um livro online
gratuito muito bom (também está disponível nas versões impressa e ebook)
chamado `CouchDB: The Definitive Guide`_. Este livro esta disponível em
Inglês, Francês e alemão.

Mas O Que É NoSQL
-----------------

NoSQL é o termo utilizado para se referir a uma nova classe de
estruturas de armazenamento, geralmente referenciadas como "Bancos de
Dados Não-Relacionais", distribuídos e escaláveis. Este novo conceito de
banco de dados, que visa sobstituir o modelo relacional, tem como
objetivo abandonar a rigidez do modelo relacional apresentando modelos
mais flexíveis, sem perder a performance e a escalabilidade. Esta troca
de modelo visa principalmente possibilitar que a estrutura dos dados
sejam criados e alterados com mais eficiência. Não há uma restrição de
modelo, alguns utilizam pares de chave/valor, colunas amplas,
armazenamento em tuplas, grafos, XML, orientações a objetos e/ou
orientações a documento.

Estas novas tecnologias têm surgido principalmente dentro de grandes
empresas globais, que precisam recolher, armazenar e analisar
regularmente grandes conjuntos de dados com altíssima taxa de
transferência transacional e baixa latência, situações estas que os
sistemas tradicionais de banco de dados relacional não conseguiram
escalar para o nível necessário. Conforme citado anteriormente, existem
dezenas de variantes deste novo modelo, cada uma com capacidades
diferenciadas e alguns *trade-offs*, mas todos compartilham uma
propriedade em comum, o abandono do design relacional tão
tradicionalmente praticado em sistemas de gerenciamento de banco de
dados como Oracle, Sybase, Postgre, MySQL e etc.

.. _Erlang: http://en.wikipedia.org/wiki/Erlang_(programming_language)
.. _`CouchDB: The Definitive Guide`: http://guide.couchdb.org/
