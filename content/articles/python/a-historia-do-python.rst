A História do Python
####################
:date: 2014-10-08 14:21
:category: Python
:tags: python, história, cwi, amoeba
:image: /images/logos/python-logo-background.jpg
:description: Há alguns anos eu comecei um projeto de escrever um livro sobre Python. Como nunca concluí esse trabalho acabei com diversos resultados de pesquisas interessantes que realizei. Um deles é a história do Python, que apresento em uma versão resumida e direta.

Julgo que a história do Python é extremamente importante para a comunidade, pois ela além de mostrar fatos importantes da linguagem, explica algumas de suas características e como seus desenvolvedores lutaram para manter esse projeto um dentro dos moldes do Software Livre e Open Source (antes mesmo de existir esse termo).

.. image:: {filename}/images/python/python-brand.png
        :target: {filename}/images/python/python-brand.png
        :alt: Python Branding
        :align: center

História
--------

.. image:: {filename}/images/python/CWI.jpg
        :target: {filename}/images/python/CWI.jpg
        :alt: CWI
        :align: right

A Linguagem Python foi concebida no fim dos anos 80. A primeira ideia de implementar o Python surgiu mais especificamente em 1982 enquanto Guido Van Rossum trabalhava no `CWI`_ (*Centrum Wiskunde & Informatica*, Centro de Matemática e Ciência da Computação) em Amsterdã, Holanda, no time de desenvolvimento da Linguagem ABC. Neste mesmo local também foi desenvolvida a linguagem `Algol 68`_.

Posteriormente, em 1987, com o fim da linguagem ABC, Guido foi transferido para o grupo de trabalho `Amoeba`_  -- um sistema operacional Microkernel liderado por Andrew Tanenbaum. Foi neste grupo que Guido percebeu a necessidade de uma linguagem para escrever programas intermediários, algo entre o C e o Shell Script.

        Percebi que o desenvolvimento de utilitários para administração de sistema em C (do Amoeba) estava tomando muito tempo. Além disso, fazê-los em shell Bourne não funcionaria por diversas razões. O motivo mais importante foi que, sendo um sistema distribuído de microkernel com um design novo e radical, as operações primitivas do Amoeba eram diferiam muito (além de serem mais refinadas) das operações primitivas disponíveis no shell Bourne. Portanto, havia necessidade de uma linguagem que "preencheria o vazio entre C e o shell". Por um tempo longo, esse foi o principal objetivo do Python.

        --- Guido Van Rossum

Tendo como base um código de demonstração da linguagem ABC (abaixo) podemos ver que alguns elementos de sintaxe (e a indentação obrigatória) do Python foram fortemente inspiradas nesta linguagem.

.. code::

    HOW TO RETURN words document:
       PUT {} IN collection
       FOR line IN document:
          FOR word IN split line:
             IF word not.in collection:
                INSERT word IN collection
       RETURN collection


Em 1989 o desenvolvimento do Python realmente teve início, nos primeiros meses de 1990 o autor já possuía uma versão mínima e operacional, pelo fim do ano de 1990 Python já era mais utilizada no CWI que a própria linguagem ABC.

Primeira *Release*
~~~~~~~~~~~~~~~~~~

No ano de 1991 Guido foi transferido do grupo Amoeba para o grupo Multimídia. De acordo com o próprio Guido "ABC me deu a inspiração crucial para Python, o grupo Amoeba a motivação imediata e o grupo de multimídia fomentou seu crescimento". Ainda neste ano, no dia 20 de Fevereiro, foi lançada a primeira versão do Python, então denominada de v0.9.0. O anúncio foi feito no grupo de discussão (*newsgroup*) `alt.sources`_. A primeira *release* era composta de 21 partes `uuencoded`_ que juntos formavam um arquivo ``.tar``. Velhos tempos...

Nesta primeira versão, o Python já contava com classes, herança, tratamento de exceções, funções, sistema de módulos (empresado da linguagem Modula-3) e os tipos de dado nativos ``list``, ``dict``, ``str``, e etc.

Desde à primeira versão -- e todas as outras versões lançadas dentro do CWI (Python 1.2) -- possuíam uma licença derivada da licença MIT (na época utilizada pelo projeto X11), substituindo apenas a entidade legal responsável para "*Stichting Mathematisch Centrum*", organização pai do CWI. Abaixo um pequeno histórico de todas as versões lançadas no CWI:

.. table::
        :class: table

        ================== =======================
        Mês/Ano            Versão
        ================== =======================
        Fevereiro de 1991  0.9.0
        Fevereiro de 1991  0.9.1
        Outubro de 1991    0.9.2
        Dezembro de 1991   0.9.4
        Janeiro de 1992    0.9.5 (Macintosh only)
        Abril de 1992      0.9.6
        Janeiro de 1993    0.9.8
        Julho de 1993      0.9.9
        Janeiro de 1994    1.0.0
        Fevereiro de 1994  1.0.2
        Maio de 1994       1.0.3
        Julho de 1994      1.0.4
        Outubro de 1994    1.1
        Novembro de 1994   1.1.1
        Abril de 1995      1.2
        ================== =======================

É importante ressaltar que apesar da linguagem Python ter sido desenvolvida nas premissas do CWI, este não financiou ou providenciou fundos oficialmente para o desenvolvimento da linguagem.

Origem do Nome
~~~~~~~~~~~~~~

.. image:: {filename}/images/python/monty-python-flying-circus.jpg
        :target: {filename}/images/python/monty-python-flying-circus.jpg
        :alt: Monty Python Flying Circus
        :align: left

No início de seu projeto, Guido sabia que não queria siglas ou um nome fraco, como era o caso da linguagem ABC, ele queria que o nome da linguagem fosse marcante e forte, mas não fazia questão que o nome possuísse um significado profundo.

Foi então que Guido usou a primeira coisa que veio a sua cabeça: `Monty Python's Flying Circus`_. O que se encaixou perfeitamente no "padrão" de nomear uma linguagem em homenagem a pessoas famosas -- ex: Pascal, Ada, Eiffel…-- e à tradição do CWI de utilizar nomes de programas de TVs para projetos.

Por anos o autor evitou vincular a linguagem ao réptil (a cobra píton) mas desistiu quando a editora O'Reilly -- que possui a tradição de utilizar animais nas capas de seus livros -- sugeriu colocar uma cobra píton na capa do seu primeiro livro "Programming Python".


Evolução da Comunidade
~~~~~~~~~~~~~~~~~~~~~~

A primeira "comunidade" do Python surgiu formalmente com a criação do *newsgroup* *news:comp.lang.python* na *Usenet*, em março de 1993. Posteriormente, este *newsgroup* foi migrado para uma lista de discussão por e-mail, tendo como base o GNU Mailman, um gerenciador de listas software livre escrito em Python.

No verão de 1994, o grupo iniciou uma discussão intitulada "`Se Guido fosse atingido por um ônibus?`_". Por mais mórbido que essa discussão soava ela tocava no âmago da comunidade Python, pois Guido era seu principal desenvolvedor e ele tomava as decisões, criando assim o medo do Python desaparecer junto com seu criador. Muitos justificavam que a política de "um homem só" reduziam as possibilidades de doação e investimento na linguagem. Nesta discussão nasceu a necessidade de se criar um padrão ou organização responsável pelo Python, desvinculando Guido como o único responsável (e detentor de seus direitos) e garantindo assim a existência prolongada da linguagem.


Breve estadia no CNRI
~~~~~~~~~~~~~~~~~~~~~

Em Novembro de 1994 ocorreu o primeiro Python Workshop, com aproximadamente 20 participantes. Dentre estes, pelo menos metade ainda são desenvolvedores ativos do Python e alguns se tornaram líderes de projetos Open Source, como Jim Fulton (Zope) e Barry Warsaw (GNU Mailman).

.. image:: {filename}/images/python/cnri.jpg
        :target: {filename}/images/python/cnri.jpg
        :alt: CNRI
        :align: right

Como resultado deste Workshop Guido recebeu uma nova proposta de emprego. Em Abril de 1995 Guido foi trabalhar na CNRI (*Corporation for National Research Initiatives*), um laboratório de pesquisa sem fins lucrativos em Reston, Virginia.

Neste período o Python recebeu verbas da `DARPA`_ (*Defense Advanced Research Projects Agency*) e Guido liderou e auxiliou um time no desenvolvimento de um sistema de agente móvel escrito puramente em Python. Este mesmo time, veio a criar a primeira organização ao redor do Python, a "*Python Software Activity*" que, apesar de não ser uma entidade legal, auxiliou na criação e suporte da infraestrutura para a comunidade Python como, o site `python.org`_, um servidor CVS, listas de email e SIGs (*Special Interest Groups*, traduzindo livremente: grupos de interesses específicos).

Os SIGs tratavam de pesquisa, estudo e desenvolvimento de tópicos específicos dentro do Python, como por exemplo processamento XML, processamento de Strings, Python na Educação, Objetos Distribuídos, dentre outros.

Na CNRI foram lançadas as versões 1.3 até a versão 1.5.2 e era utilizada uma licença semelhante à utilizada na CWI (baseada na licença MIT) apenas alterando o responsável para "CNRI".

Em 1999, com o crescente sucesso do Python (e dado o sucesso de iniciativas como o `W3C`_ e X Consortia) a CNRI tentou criar um modelo para obter patrocínio para o desenvolvimento da linguagem, o `Python Consortium`_. Apesar deste modelo ter subsidiado a implementação de *strings* Unicodes e a biblioteca de expressões regulares (com o apoio da Hewlett-Packard) ele não se mostrou muito promissor e foi "fechado" pouco depois.

Neste período foram lançadas as seguintes versões do Python:

.. table::
        :class: table

        ================== =======================
        Mês/Ano            Versão
        ================== =======================
        Outubro de 1995    1.3
        Outubro de 1996    1.4
        Janeiro de 1998    1.5
        Outubro de 1998    1.5.1
        Abril de 1999      1.5.2
        Setembro de 2000   1.6
        ================== =======================

Período de Tormenta
~~~~~~~~~~~~~~~~~~~

No inicio de 2000, Guido, Barry Warsaw, Jeremy Hylton e Fred Drake receberam o convite para ser juntar à *startup* BeOpen.com, uma iniciativa que estava recrutando diversos desenvolvedores Open Source. Antes de deixar a CNRI os desenvolvedores foram forçados a lançar a versão 1.6, para finalizar o ciclo de desenvolvimento do Python.

Para a versão 1.6 a CNRI insistiu em utilizar uma licença escrita pelos seus próprios advogados. Como esperado, esta licença era diferente da utilizada até o momento, era bem longa e com muito "juridiquês", visando controlar "os direitos do Python" e submetendo o software às leis do estado da Virginia. Como o Python era utilizado pelo GNU Mailman, a FSF (*Free Software Foundation*) estavam receosa que essa nova licença pudesse restringir o uso de ambos os softwares. Richard Stallman e Eben Moglen (ambos da PSF), analisaram a licença e chegaram a conclusão de que esta não era uma licença compatível com as premissas do software livre. Com o apoio de Eric Raymond e da PSF a licença foi reescrita para satisfazer tanto a FSF quanto a CNRI. A versão 1.6 foi lançada em Setembro de 2000, sendo que o grupo de desenvolvedores já estavam na BeOpen.com desde Maio de 2000.

.. image:: {filename}/images/python/fsf.png
        :target: {filename}/images/python/fsf.png
        :alt: Free Software Foundation
        :align: center

Devido a esta história do Python, a licença do Python era vista "em camadas". Na base tínhamos a licença do CWI, seguida pela licença do CNRI (no meio) e por último a licença da BeOpen.com. Apesar da confusão, a licença era compatível com o modelo OSI que define uma licença Open Source e também é compatível com a GNU GPL (General Public License), garantindo as liberdades de um software livre.

BeOpen.com e Digital Creations
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Ja na BeOpen.com foi formado o grupo PythonLabs e a versão 2.0 do Python foi lançada em Outubro de 2000. O Python 2.0 utilizava uma versão alterada da licença presente na versão 1.6 (alterando apenas o responsável para BeOpen.com).

Nesta estadia o Python (como comunidade e linguagem) evoluiu significativamente:

- Os desenvolvedores passaram a se focar exclusivamente para o Python;
- O desenvolvimento foi centralizado, utilizando um servidor CVS no SourceForge;
- Por volta de 30 pessoas possuíam acesso de commit;
- Banco de dados de patches e bugs também eram hospedados no SourceForge; e
- Criação das PEPs (*Python Enhancement Proposal*).

.. image:: {filename}/images/python/zope.png
        :target: {filename}/images/python/zope.png
        :alt: Zope
        :align: right

A estadia na BeOpen.com rendeu apenas uma *release* do Python, a versão 2.0 citada anteriormente, pois em Outubro de 2000 ocorreu a falência e desmembramento da BeOpen.com e o PythonLabs foi contratado pela empresa Digital Creations. Em paralelo à esta contratação, o PythonLabs recebeu também convites de outras duas empresas, a VA Linux e a ActiveState.

Posteriormente a Digital Criations mudou de nome e ficou conhecida como `Zope Corporation`_, referência ao seu produto mais conhecido, o Web CMS (*Content Managing System*) Zope.

Parte da mudança para a Digital Creation/Zope Corporaton foi influenciada pela certeza de que o futuro do Python não podia ser influenciado pelos objetivos e ideais daqueles para os quais Guido trabalhava. Foi então que criaram a *Python Software Foundation* (PSF). Por isso não houve nenhuma *release* do Python com direitos direcionados à Zope Corporation.


Em 2001 o PythonLab ainda foi "forçado" a realizar mais uma *release* do Python sobre a licença do CNRI, contendo apenas algumas correções de bugs.

Python Software Foundation
~~~~~~~~~~~~~~~~~~~~~~~~~~

Em 2001 foi criada a `Python Software Foundation`_ (PSF), uma organização sem fins lucrativos constituída por membros da equipe de desenvolvimento (daquela época) e por Eric Raymond. Ela tem como objetivo ser dona de qualquer propriedade intelectual relacionada ao Python, e como missão promover e proteger o avanço da linguagem Python, além suportar e auxiliar o crescimento de comunidades de programadores Python.

Ela possui diversos patrocinadores como:

- ActiveState;
- Advanced Simulation Technology Inc. (ASTi);
- Array BioPharma, Inc.;
- Beslist.nl;
- BizRate.com;
- Canonical;
- CCP Games.;
- cPacket Networks;
- Edgestream Partners, L.P.;
- Enthought, Inc.;
- Globo;
- Google;
- Hood Media GmbH;
- KNMP;
- Lincoln Loop;
- Lucasfilm;
- Microsoft;
- Online Degree Reviews;
- OpenEye Scientific Software;
- O'Reilly Media, Inc.;
- Red Hat;
- SEO Moves;
- Uniblue Systems Ltd.;
- Wargaming.com;
- ZeOmega, LLC.;

Atualmente
~~~~~~~~~~

Após a criação da PSF todas as releases desde a 2.1 foram feitas utilizando a *PSF License Agreement*, uma licença que atribui todos os direitos do Python à PSF. A licença está disponível na íntegra na `documentação oficial do Python`_.

Uma vez que o futuro do Python (e a sua evolução) se desvinculou dos empregadores de seu criado, existem poucos relatos e registros. Segue alguns destaques:

- Em Julho de 2003 o PythonLab saiu da Zope Corporation para trabalhar na `Elemental Security`_ em San Mateo, California;
- Em Dezembro de 2005 Guido foi trabalhar no Google em Mountain View, Califórnia;
- Em Janeiro de 2013 Guido foi trabalhar para o Dropbox.

.. _Monty Python's Flying Circus: http://en.wikipedia.org/wiki/Monty_Python%27s_Flying_Circus
.. _CWI: https://www.cwi.nl/
.. _Algol 68: http://en.wikipedia.org/wiki/ALGOL_68
.. _Amoeba: http://en.wikipedia.org/wiki/Amoeba_distributed_operating_system
.. _alt.sources: http://www.faqs.org/faqs/alt-sources-intro/
.. _Se Guido fosse atingido por um ônibus?: http://legacy.python.org/search/hypermail/python-1994q2/1040.html
.. _uuencoded: http://en.wikipedia.org/wiki/Uuencoding
.. _Python Workshop: http://legacy.python.org/workshops/1994-11/attendees.pics.html
.. _DARPA: http://www.darpa.mil/default.aspx
.. _python.org: http://python.org
.. _Python Consortium: http://www.xray.mpe.mpg.de/mailing-lists/perl5-porters/1999-10/msg01371.html
.. _W3C: http://www.w3.org/
.. _Zope Corporation: http://www.zope.com
.. _Python Software Foundation: http://www.python.org/psf
.. _Elemental Security: http://www.elementalsecurity.com/
.. _documentação oficial do Python: https://docs.python.org/3/license.html

