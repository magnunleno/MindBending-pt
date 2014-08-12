Servindo Sites Estáticos Com o NGINX
####################################
:date: 2014-04-07 00:40
:category: Pelican
:tags: pelican, nginx, gzip, cache, instalação, rewrite
:image: /images/nginx_logo_square.png
:series: Migrando Para o Pelican

Três fatos me deixaram muito satisfeitos ao migrar para o `Pelican`_, conforme informado `nesses`_ `outros`_ artigos. O primeiro deles foi não ter que utilizar mais nenhum editor WYSIWYG (*what you see is what you get*), agora escrevo apenas no VIM. O segundo deles foi utilizar o Pelican em conjunto com o Git, tanto para versionamento de artigos, configurações, temas, plugins e etc, quanto para fazer publicações, através do Git Hooks. Por último, mas não menos importante, foi o fato de finalmente parar de o usar o `Apache`_ e migrar para o `NGINX`_!

.. image:: {filename}/images/nginx_logo.gif
        :align: center
        :target: {filename}/images/nginx_logo.gif
        :alt: NGINX Logo

Lembrando que tudo que será apresentado neste artigo é usável (sob certos ajustes) tanto para ambientes de produção (para o servidor que "roda" seu site) quando para ambientes de desenvolvimento (sua estação de trabalho).

.. more

Quem é o NGINX
--------------

Eu gosto de dizer que o NGINX é um Apache-Killer. Em termos mais técnicos o NGINX (pronuncia-se *engine-ex*) é um servidor web com foco em concorrência, alta performance e reduzido uso de memória. Além disso o NGINX possui capacidade para servir os protocolos (além do HTTP e HTTPS) SMTP, POP3 e IMAP, e funcionar como uma balanceador de carga, cache HTTP e compressão de conteúdo. Além disso, a sua sintaxe de configuração é (em minha opinião) inúmeras vezes mais simples qua a sintaxe adotada pelo Apache.

Se você ainda tem dúvidas se o NGINX é realmente relevante, basta pesquisar por comparativos entre NGINX e Apache que você verá depoimentos como o de `funcionários da Automattic`_ (ou Wordpress.com), da `WebFaction`_ (vejam os gráficos de requisições por segundo e de consumo de memória) ou da `DreamHost`_.

Para vocês terem uma ideia, segue abaixo um exemplo simples de como configurar o NGINX para servir uma site puramente HTML:

.. code-block:: nginx

        server {
                server_name mindbending.org;
                root /home/mindbending/blog;
                index index.html;
        }

Muito mais simples que o Apache, não? Mas calma, vamos fazer algumas otimizações.


Instalando o NGINX
------------------

Instalar o NGINX hoje em dia é bem simples, ele está disponível no repositório oficial da maioria das distribuições. Quando comecei a brincar com o NGINX era necessário compilá-lo na mão, então aproveitem:

.. code-block:: bash

        $ sudo aptitude install nginx nginx-full

Configuração Básica
-------------------

O arquivo de configuração do NGINX fica em `/etc/nginx/` e de forma similar ao Apache, ele utiliza os diretórios `sites-avaiable` e `sites_enabled`. 

A primeira configuração a editar ficam em `/etc/nginx/nginx.conf`, remova o comentário das seguintes linhas:

.. code-block:: conf

        server_tokens off;
        server_names_hash_bucket_size 64;

A primeira linha desabilita o envio de informações de versão do NGINX e da plataforma (distribuição GNU/Linux) utilizada. Eu gosto de desabilitar pois dificulta o uso de *exploits* específicos. Já a segunda linha permite o uso de nomes de domínios mais longos, o valor padrão é `32`, e como meu domínio é longo eu mudei para `64`.

Outra linha que **pode** se alterar é a `worker_processes 1;`, ela é responsável por definir o número de processos que irão ser levantados para atender às solicitações. Este número está intimamente ligado ao número de cores do seu servidor, na documentação oficial do NGINX é recomendado `1 worker_process por core`_.

Para mais customizações de performance do NGINX sugiro a seguinte leitura: `Battle Ready NGINX`_

Configurando Um Site
--------------------

A configuração de um site é bem simples. Segue abaixo a que eu estou usando neste momento.

.. code-blocK:: nginx

        # Redireciona o domínio www.mindbending.org para mindbending.org
        server {
                server_name  www.mindbending.org;
                rewrite ^(.*) http://mindbending.org$1 permanent;
        }

        # Configurações do domínio mindbending.org
        server {
                ### Configuração básica
                listen *:80;                  # Ouve em todos os endereços
                server_name mindbending.org;  # Responde apenas pelo nome mindbending.org
                index index.html index.htm;   # busca os seguintes arquivos
                root /home/mindbending/blog;  # Onde está o meu site

                ### Logs
                error_log  /var/log/nginx/mindbending-error.log  warn;
                access_log /var/log/nginx/mindbending-access.log;

                ### Redirects e rewrites
                # Remove barras no final do endereço
                rewrite ^/(.*)/$ /$1 permanent;
                # Redirectiona antigas requisições para wp-contents (resíduos de redes sociais)
                rewrite ^/wp-content/.*/(.*)$ /$1/images/$2 permanent;

                ### Locations
                location ~* \.(js|css)$ {    # Configurações para JavaScripts e CSS
                        gzip_static on;      # Compressão GZIP ativada
                        expires 1w;          # Browser cache de 1 semana
                }

                location ~* \.(jpg|jpeg|png|gif|ico)$ {        # Configurações para imagens
                        gzip_static on;                        # Compressão GZIP ativada
                        expires 2w;                            # Browser cache de 2 semana
                }

                location / {                                            # Configurações para o restante do site
                        gzip_static on;                                 # Compressão em todo o site
                        try_files $uri.html $uri/index.html $uri =404;  # Ordem de busca de páginas (ou retorna 404)
                        error_page 404 /404;                            # Página de erro customizada
                        expires 1d;                                     # Browser cache de 1 dia
                }
        }

Toda a configuração está comentada e explicada. Mas vou passar por algumas linhas importantes:

`rewrite ^/wp-content/.*/(.*)$ /$1/images/$2 permanent;`
        Esta linha é extremamente útil para mim pois eu tenho o hábito de analisar os logs de erro do NGINX, com isso percebi incontáveis erros (HTTP 404) de redes sociais buscando antigos links de imagens e outros anexos no caminho com o seguinte padrão: `/wp-content/uploads/sites/4/2013/02/logo-grande-300x300.png`. Com a regra de `rewrite` acima posso redirecionar o link para o novo padrão do Pelican: `/images/logo-grande-300x300.png`
`gzip_static on;`
        Esta linha é fundamental para reduzir o tráfego de dados entre o servidor e o cliente, pois orienta o NGINX a servir o arquivo compactado, reduzindo drasticamente o consumo de banda.
`expires 1w;`
        Esta linha orienta o NGINX e informar ao cliente (*browser*), através do cabeçalho da resposta HTTP, que este conteúdo deve ser armazenado em cache local por uma semana. Desta forma reduzimos significativamente o número de requisições ao servidor e o consumo de banda.


Demonstração de Redirect www
----------------------------

Sempre que realizamos estes tipos de configurações é bom certificar-se do bom funcionamento de todas as regras, e é nessas horas que a linha de comando do GNU/Linux é a sua melhor amiga. Veja como certificar-se de que o redirecionamento de `www.mindbending.org` para `mindbending.org` está funcionando corretamente:

.. code-block:: bash

        $ curl -I http://www.mindbending.org
        HTTP/1.1 301 Moved Permanently
        Server: nginx
        Date: Thu, 03 Apr 2014 15:09:14 GMT
        Content-Type: text/html
        Content-Length: 178
        Connection: keep-alive
        Location: http://mindbending.org/

O comando `curl` é capaz de buscar páginas web e apresentá-las no terminal. Como nosso interesse é apenas no cabeçalho da resposta, utilizei a chave `-I` para que o `curl` não apresente apenas o cabeçalho HTTP. Nele podemos ver que recebemos uma resposta `HTTP/1.1 301 Moved Permanently`, que orienta ao browser a buscar esta página em outro endereço. Este outro endereço é informado na seguinte linha: `Location: http://mindbending.org/`. Ou seja, exatamente como pretendíamos.

Demonstração de Server Tokens
-----------------------------

Conforme citado anteriormente, a configuração `server_tokens` oculta informações da versão do NGINX e da sua plataforma (distribuição GNU/Linux, neste caso) que são enviadas aos clientes no cabeçalho HTTP. No exemplo anterior vemos que na resposta temos uma informação vaga de qual servidor está provendo essa página: `Server: nginx`. Veja abaixo como seria o resultado de uma requisição como esta caso a configuração `server_token` estivesse habilitada (o comportamento padrão do NGINX):

.. code-block:: bash

        $ curl -I http://mindbending.org
        HTTP/1.1 200 OK
        Server: nginx/1.4.1 (Ubuntu)
        Date: Thu, 03 Apr 2014 17:21:14 GMT
        Content-Type: text/html
        Content-Length: 8428
        Last-Modified: Thu, 03 Apr 2014 03:45:36 GMT
        Connection: keep-alive
        ETag: "533cd960-20ec"
        Expires: Fri, 04 Apr 2014 17:21:14 GMT
        Cache-Control: max-age=86400
        Accept-Ranges: bytes

Podemos ver que agora sabemos a distribuição GNU/Linux que está operando neste servidor, bem como a versão do NGINX (1.4.1), facilitando assim a realização de ataques maliciosos direcionados a esta versão do NGINX.

Demonstração de Cache
---------------------

No meu site eu utilizei uma politica de cache da seguinte forma:

.. table::
        :class: table

        ====================  ===============================
        Conteúdo               Tempo de Cache
        ====================  ===============================
        Imagens                2 semanas
        JavaScript e CSS       1 semana
        Outros                 1 dia
        ====================  ===============================

Então para isso terei que realizar três requisições. Vamos começar pela imagem:

.. code-block:: bash

        $ curl -I http://mindbending.org/pt/images/MB_Logo_2014.png
        HTTP/1.1 200 OK
        Server: nginx
        Date: Thu, 03 Apr 2014 15:34:52 GMT
        Content-Type: image/png
        Content-Length: 4755
        Last-Modified: Thu, 03 Apr 2014 03:42:17 GMT
        Connection: keep-alive
        ETag: "533cd899-1293"
        Expires: Thu, 17 Apr 2014 15:34:52 GMT
        Cache-Control: max-age=1209600
        Accept-Ranges: bytes

Podemos ver que o servidor respondeu com uma mensagem `HTTP/1.1 200 OK` informando a data/hora da requisição `Date: Thu, 03 Apr 2014 15:34:52 GMT` e a que esse conteúdo expira (`Expires: Thu, 17 Apr 2014 15:34:52 GMT`), exatos 14 dias (2 semanas). Para ter certeza do valor, você pode também conferir o seguinte campo: `Cache-Control: max-age=1209600`. Este campo apresenta em segundos o tempo que esse conteúdo ficará no cache (14 dias * 24 horas * 60 minutos * 60 seguntos = 1209600 segundos).

Agora vamos ver o conteúdo CSS:

.. code-block:: bash

        $ curl -I http://mindbending.org/pt/theme/css/style.css
        HTTP/1.1 200 OK
        Server: nginx
        Date: Thu, 03 Apr 2014 15:24:16 GMT
        Content-Type: text/css
        Content-Length: 7548
        Last-Modified: Thu, 03 Apr 2014 03:40:54 GMT
        Connection: keep-alive
        ETag: "533cd846-1d7c"
        Expires: Thu, 10 Apr 2014 15:24:16 GMT
        Cache-Control: max-age=604800
        Accept-Ranges: bytes

Da mesma forma temos uma resposta `HTTP/1.1 200 OK` feita em `Thu, 03 Apr 2014 15:24:16 GMT` e que expirará em `Thu, 10 Apr 2014 15:24:16 GMT`, isto é, `max-age=604800` (em segundos).

Para finalizar vamos ver um outro conteúdo qualquer, por exemplo um artigo:

.. code-block:: bash

        $ curl -I http://mindbending.org/pt/adeus-wordpress
        HTTP/1.1 200 OK
        Server: nginx
        Date: Thu, 03 Apr 2014 15:42:16 GMT
        Content-Type: text/html
        Content-Length: 27702
        Last-Modified: Fri, 07 Mar 2014 00:08:00 GMT
        Connection: keep-alive
        ETag: "53190de0-6c36"
        Expires: Fri, 04 Apr 2014 15:42:16 GMT
        Cache-Control: max-age=86400
        Accept-Ranges: bytes

Podemos ver que um artigo, solicitado em `Thu, 03 Apr 2014 15:42:16 GMT` possui um cache que irá expirar em `Fri, 04 Apr 2014 15:42:16 GMT`, ou seja, `max-age=86400` (em segundos). Com isso vemos que a política de cache está funcionando perfeitamente.

Demonstração da Compactação GZIP
--------------------------------

A configuração `gzip_static` é uma das que mais me empolgou, pois em conjunto com o plugin `gzip_cache` do Pelican, eu consigo reduzir consideravelmente o consumo de recursos de processamento do servidor e o consumo de trafego. A redução do consumo de tráfego é óbvia pois, uma vez que é enviado para o cliente a versão compactada da sua página, o tráfego é bem menor. Mas por quê a redução do consumo de recuso de processamento? Bem, isso se deve ao fato de que se eu quisesse utilizar esse tipo de recurso no NGINX eu poderia permitir que ele compactasse minhas páginas antes de enviá-la ao cliente. Porém, isso implica que o meu servidor vai perder tempo (e processamento) a cada requisição realizando a compactação das páginas. Mas será que vale a pena mesmo compactar a página? Vamos fazer uma análise rápida:

.. code-block:: bash

        $ curl -Is http://mindbending.org/pt | grep Length
        Content-Length: 77688
        $ curl -Is -H 'Accept-Encoding: gzip' http://mindbending.org/pt | grep Length
        Content-Length: 10933

Na primeira linha temos uma requisição comum ao índice do meu blog, e temos como resposta 77.688 Bytes. Já na segunda requisição, onde informamos que nosso 'navegador' pode tem capacidade de receber arquivos compactados, temos uma resposta de apenas 10.933 Bytes. Isto é, uma resposta 7.1 vezes menor que a primeira, ou uma economia de 66.755 Bytes.

E em uma página menor, será que teremos um ganho menos significativo? Vamos fazer um teste com a URL `http://mindbending.org/pt/adeus-wordpress`:

.. code-block:: bash

        $ curl -Is http://mindbending.org/pt/adeus-wordpress | grep Length
        Content-Length: 27702
        $ curl -Is -H 'Accept-Encoding: gzip' http://mindbending.org/pt/adeus-wordpress | grep Length
        Content-Length: 6197

Em valores absolutos sim, nosso ganho foi menor. Apenas 21.505 Bytes economizados, ou um seja, uma requisição 4.47 vezes menor. Mas mesmo assim é uma economia considerável.

Para termos uma ideia, vamos tomar como base que um site receba 100 visitas por dia e vamos assumir que todas as visitas vejam apenas um artigo e que todos esse artigo possue a taxa de economia de 21 KBytes. Ao final do mês teremos uma economia de 65.100.00 Bytes, ou seja 65.1 MBytes.

Fechamento
----------

O NGINX é um monstro, tudo o que eu demonstrei é apenas um porcento das funcionalidades dele. Se esse aperitivo despertou usa curiosidade sugiro que você pesquise e leia muito, existem diversos tutoriais, guias e livros sobre este ótimo servidor web. Boa diversão!

Até mais...

.. _Pelican: http://docs.getpelican.com/en/3.3.0/
.. _nesses: /pt/adeus-wordpress
.. _outros: /pt/migrando-do-wordpress-para-o-pelican
.. _Apache: http://www.apache.org/
.. _NGINX: http://nginx.org/
.. _funcionários da Automattic: http://barry.wordpress.com/2008/04/28/load-balancer-update/
.. _WebFaction: http://blog.webfaction.com/2008/12/a-little-holiday-present-10000-reqssec-with-nginx-2/
.. _DreamHost: http://wiki.dreamhost.com/Web_Server_Performance_Comparison
.. _1 worker_process por core: http://wiki.nginx.org/CoreModule#worker_processes
.. _Battle Ready NGINX: http://blog.zachorr.com/nginx-setup/
