Migrando do Wordpress Para o Pelican
####################################
:date: 2014-03-12 15:17
:category: Pelican
:tags: pelican, wordpress, python, shell, migração
:image: /images/pelican/flying_pelican.png
:series: Migrando Para o Pelican

Conforme relatado `neste outro artigo`_, migrei este blog para o `Pelican`_. Entretanto, meu blog atualmente possui 123 artigos (em português, em inglês são mais 55 artigos), o que torna praticamente inviável uma migração manual. Para acelerar o processo acabei utilizando ótimas ferramentas. Como outras pessoas podem querer migrar para o Pelican, resolvi documentar aqui os meus passos.

.. image:: {filename}/images/pelican/pelican_blueprint.png
        :align: center
        :alt: Pelican
        :target: {filename}/images/pelican/pelican_blueprint.png

Claro que não consegui automatizar tudo, e parte do processo ainda foi manual, mas o uso de ferramentas como o sed e o shell scripts valem a menção.

.. more

Antes de tudo, certifique-se que você possui o Pelican instalado, caso contrario `eu já escrevi um artigo sobre isso`_. Em seguida acesse seu antigo site em Wordpress e `exporte seus artigos e páginas`_, faça isso separadamente, pois vai reduzir os erros durante e importação. Para exportar seus artigos no Wordpress acesse o menu *Tools > Export*, em seguida selecione *Posts* e clique em *Download Export File*. Em seguida repita o processo para as páginas do seu site.

Ao final do processo você terá dois arquivos, no meu caso `mindbending-pages.wordpress.2014-02-17.xml` e  `mindbending-articles.wordpress.2014-02-17.xml`. 

Importanto do XML
-----------------

Uma vez que o processo de importação gera muitos arquivos eu achei prudente criar um diretório diferenciado somente para esse processo:

.. code-block:: bash

        $ mkdir -p ~/mindbending/import/articles
        $ cp mindbending-articles.wordpress.2014-02-17.xml ~/mindbending/import/articles

Em seguida utilizei o script de importação do Pelican para processar o arquivo XML;

.. code-block:: bash

        $ cd ~/mindbending/import/articles
        $ pelican-import --wpfile mindbending-articles.wordpress.2014-02-17.xml -o .

Por padrão o `pelican-import` gera arquivos em ReStructuredText, caso prefira Markdown utilize o seguinte comando

.. code-block:: bash

        $ pelican-import --wpfile mindbending-articles.wordpress.2014-02-17.xml -o . -m markdown

.. raw:: html

        <div class="alert alert-info">

Aprendam ReStructuredText, é uma linguagem de marcação mais poderosa que o Markdown.

.. raw:: html

        </div>

Muito bem, agora temos um bando de arquivos com a extensão `.rst` (ou `.md`). Vamos trabalhar em cima disso.

Removendo Metadados Desnecessários
----------------------------------

Dependendo da versão que você possui do `pelican-import` (e da opção utilizada na exportação do Wordpress e da importação com o Pelican) ele pode ou não inserir os seguintes metadados nos seus artigos: `:slug:` e `:author:`. 

Caso seja do seu interesse não utilizar esses metadados e deixar que o Pelican utilize o autor padrão do site e gerar os *slugs* baseado no nome do arquivo, os seguintes comandos removem estas metainformações dos seus artigos:

.. code-block:: bash

        sed "/^:author:/d" *.rst -i
        sed "/^:slugs:/d" *.rst -i

Baixando Todas as Imagens Automaticamente
-----------------------------------------

Considerando que, assim como eu, você utiliza muitas imagens para ilustrar seus artigos, vocẽ deve ter também algumas centenas de imagens pra baixar. Claro que você pode também acessar seu servidor do Wordpress e copiar o diretório `wp-content` para o seu novo site. Mas nem todos tem essa opção ou não tem acesso FTP/SSH ao servidor do seu site atual. para isso fiz esse comando (quase um script):

.. code-block:: bash

        $ mkdir images && cd images
        $ for img in `grep -i "\.jpg\|\.jpeg\|\.png\|\.gif" ../*.rst | sed "s/^.*: \(http:.*\)/\1/" | uniq`; do wget $img --no-clobber; done
        $ cd ..

Toda a mágica desse comando é feito com 3 comandos: `grep`, `sed` e `wget`. O comando `grep` busca todas as referencias a imagens, com extensões `.jpg`, `.jpeg`, `.png` e/ou `.gif`. Caso você tenha alguma outra extensão basta adicionar no comando acima. Já o `sed` é responsável em todas as referencias a imagens um texto que case com a expressão regular que representa um link, isto é, começa com `http:`. Em seguida o `wget` assume o comando e baixa o link encontrado utilizando a opção `--no-clobber`, que evita que um mesmo arquivo seja baixado mais de uma vez, já que muitas vezes fazemos referência a uma mesma imagem mais de uma vez.

Corrigindo Referências à Imagens
--------------------------------

Uma vez que não estamos mais utilizando o Wordpress, o diretório de armazenamento de imagens não é mais o mesmo e precisamo corrigir todas as referências às imagens. O Pelican tem uma forma peculiar de se referir a imagens. Ao invés de fazer referência à *url* da imagem (por exemplo `http://mindbending.org/pt/wp-content/uploads/sites/4/2011/10/archlinux-curved2.png`), é recomendado utilizar a *tag*  `{filename}`, vide exemplo:

.. code-block:: rst

        .. image:: {filename}/images/image_name.png

Para converter as referências a essas imagens, eu utilizei o seguinte comando `sed`:

.. code-block:: bash

        $ sed "s#http://.*/\(.*\.\(png\|jpg\|jpeg\|gif\)\)#{filename}/images/\1#" *.rst -i

Utilizando URLs Relativas
-----------------------------

Talvez isso seja uma peculiaridade minha, mas eu preferi não usar URLs absolutas acabei optando por URLs relativas, isto é, ao invés de fazer referências à `http://meusite.org/meu-artigo` estou fazendo referências apenas a `/meu-artigo`. Desta forma posso utiliza o mesmo código tanto para meu ambiente de desenvolvimento (que utilizo o domínio `mindbending.dev`) quanto para meu ambiente de produção (que utiliza o domínio `mindbending.org`).

Para isso precisei editar **todas** as referências internas no meu site. Seria um trabalho imenso se eu não soubesse expressões regulares e não conhecesse o `sed`:

.. code-block:: bash

        $ sed "s#http://mindbending.org##" *.rst -i

Caracteres Não ASCII
--------------------

Não é recomendado que as slugs/nomes de arquivos possuam caracteres não ASCII, isso gera algumas dores de cabeça. Para buscar todos os arquivos que possuem nomes não-ASCII utilize o seguinte comando:

.. code-block:: bash

        $ ls . | grep --color -P "[\x80-\xFF]"
        $ ls images | grep --color -P "[\x80-\xFF]"

Infelizmente o processo de renomear as imagens e artigos é manual uma vez que você tem que tomar a decisão de qual será o novo nome.

Para buscar referências não ASCII nos arquivos `.rst` utilize os seguintes comandos:

.. code-block:: bash

        $ grep -n "\.png\|\.jpg\|\.jpeg\|\.gif" *.rst | grep --color -P "[\x80-\xFF]"

Da mesma forma que o nome dos arquivos, é necessário ainda corrigir manualmente as referências dentro dos arquivos `.rst` da mesma forma que o nome dos arquivos foram corrigidos.

Ultimos Retoques
----------------

Apesar do `pelican-import` fazer um ótimo trabalho, eu ainda precisei corrigir a forma como ele interpretou as referências de imagens no Wordpress. Por exemplo, ele gera referências conforme abaixo:

.. code-block:: rst

        [caption id="attachment\_1101" align="aligncenter" width="987"]\ |Nautilus 3.0| Nautilus 3.0[/caption]

Sendo que o esperado era algo conforme abaixo:

.. code-block:: rst

        .. image: {filename}/images/nautilus-3-0.png
                :alt: Nautilus 3.0

Apesar de ser possível automatizar esse processo, preferi fazê-lo manualmetne para garantir a qualidade das referências e manter a uniformidade no meu blog. Boa sorte pra vocês :)

Um Pouco do Meu Transtorno Obsessivo Compulsivo
-----------------------------------------------

Quando comecei a migrar meu site percebi a bagunça que estavam as tags dos meus artigos. Algumas com letras maiúsculas, outras somente minúsculas. Resolvi padronizar, mas teria que editar 123 artigos... Ou não:

.. code-block:: bash

        $ sed -e 's/^:tags: \(.*\)/:tags: \L\1/' *.rst -i

Pronto, agora todas as tags são apenas minúsculas, como elas devem ser.

Finalizando
-----------

Ao final de todo este trabalho, basta mover todo o conteúdo gerado para o diretório do site `criado anteriormente`_:

.. code-block:: bash

        $ cd ~/mindbending
        $ cp -r import/articles/* content/articles/
        $ cp -r import/images content/

Em seguida gere novamente o seu site:

.. code-block:: bash

        $ make html

Se não ocorrer nenhum erro, meus parabéns, você editou tudo perfeitamente. Mas se, assim como eu, você está recebendo diversos erros e não tem ideia do que fazer, utilize a opção `DEBUG`;

.. code-block:: bash

        $ DEBUG=1 make html

Agora boa sorte, os erros devem ser mínimos e fáceis de se corrigir com as mensagens de *debug*.

Quem migrar para o Pelican por causa deste artigo, por favor deixem nos comentários o link do seu site. Gostaria de ver todos os que eu consegui ajudar.

Até a próxima!

.. _neste outro artigo: /pt/adeus-wordpress
.. _Pelican: http://docs.getpelican.com/en/3.3.0/
.. _eu já escrevi um artigo sobre isso: /pt/instalando-o-pelican
.. _exporte seus artigos e páginas: http://en.support.wordpress.com/export/
.. _criado anteriormente: /pt/instalando-o-pelican
