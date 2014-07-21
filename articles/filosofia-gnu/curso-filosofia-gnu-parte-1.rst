Curso de Filosofia GNU - Parte 1
################################
:date: 2014-04-07 11:42
:category: Filosofia GNU
:tags: curso, filosofia gnu, cdtc, richard stallman, FSF, free software, open source
:image: /images/The_GNU_logo-300x293.png
:series: Curso de Filosofia GNU
:description: A Filosofia GNU e o conceito de Software Livre estão muito difundidos hoje em dia, porém em qual contexto histórico ele ocorreu e quais acontecimentos levaram a sua concepção? A primeira parte deste curso cobre estes assuntos.

Olá pessoa! Há muito tempo eu descobri o `Projeto CDTC`_ (Centro de Difusão de Tecnologia e Conhecimento), onde fiz alguns cursos na área de tecnologia utilizando softwares livres. O Projeto CDTC visa a promoção e o desenvolvimento de ações que incentivem a disseminação de soluções que utilizem padrões abertos e não proprietários de tecnologia, em proveito do desenvolvimento social, cultural, político, tecnológico e econômico da sociedade brasileira.

.. image:: {filename}/images/The_GNU_logo-300x293.png
        :target: {filename}/images/The_GNU_logo-300x293.png
        :alt: GNU
        :align: center

Alguns dos cursos disponibilizados por eles me chamaram muito a atenção pelo simples fato de não ter visto antes um agregado de informações tão bem elaborado sobre certos assunto, um destes assuntos é o curso de Filosofia GNU. Uma vez que o conteúdo do curso é disponibilizado sobre os termos da `FDL`_ (*GNU Free Documentation License*) eu tenho o direito de reproduzi-lo aqui (mantendo os créditos).

.. more

1. Processo Histórico
---------------------

1.1 Como era o mundo nos anos 70?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Em geral, quando falamos em software livre, as pessoas tendem automaticamente a pensarem que se existe algo que é livre, então, comparativamente, tem uma outra "coisa" que é "presa", "amarrada", "acorrentada", sendo isso uma compreensão verdadeira. No decorrer deste curso você vai poder observar que estas correntes que prendem o software estão diretamente ligadas a conceitos de Propriedade Intelectual ou se preferir, as licenças.

Nossa história começa nos anos 70, quando era muito comum para um programador trocar suas experiências de programação com outros parceiros. Quando alguém desenvolvia uma rotina para calcular um intervalo de datas (por exemplo) e um outro programador tinha conhecimento que aquela rotina já estava produzida por alguém, ele tomava a iniciativa de pedi-la ou obtê-la junto ao criador do programa, aproveitando o código e inserindo noutros programas.

Logo, podemos afirmar que no início do mundo da programação os programas de computadores já eram livres, e que os técnicos da área já compartilhavam entre si as soluções tecnológicas, aproveitando o trabalho individual e transformando-o em uma solução coletiva.

É importante observar que durante este mesmo período dos anos 70, as escolas de uma forma geral tinham objetivos mais nobres, voltados ao ensino participativo, como por exemplo: se ao chegar a hora do lanche, uma criança não tinha levado sua merenda, a professora pedia a outra criança que compartilhasse, que dividisse o lanche com o coleguinha. Essa iniciativa da professora gerava nas crianças um aprendizado sobre relacionamento humano com a prática do compartilhamento, do apoio àqueles que tinham necessidade, e muitas outras questões que serviam para o desenvolvimento da sociedade.


1.2 O que mudou nos anos 80?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Nos idos dos anos 80 surgiram licenciamentos de software que até então não eram utilizados, impedindo a cooperação dos programadores. Fatos como limites de usuários por produtos, limitação no número de processadores utilizados, e inúmeras outras alternativas se propagavam nas licenças de software.

Até os anos 70 ainda era comum adquirir-se os sistemas computacionais junto com os códigos fonte. Na década posterior, os fontes já não faziam mais parte das negociações, os sistemas eram apenas vendidos com uma concessão de uso, as limitações quanto a utilização dos programas eram restritas e diferiam de toda e qualquer relação anteriormente exercida no mercado consumidor.

Nunca em toda historia da humanidade houve uma restrição tão grande. Comparando a outros produtos, imagine comprar uma televisão que poderia apenas ser vista por um limitado número de pessoas, e quando sua família crescesse, seria necessário adquirir mais uma licença, pagando um adicional. Além disso, tome ainda como exemplo que a cada dois anos você teria de adquirir um novo televisor para poder assistir a programações mais atuais, pois a TV não teria a capacidade de "entender" a nova grade de programação, que só seria entendida pela versão mais nova.

É notável ainda que nos anos 80 (especificamente nos Estados Unidos) as escolas passam a impedir os alunos de distribuírem programas de computador através de CDs ou Disquetes, ensinando às crianças uma obediência e respeito aos conceitos de propriedade intelectual, como se isto fosse natural a todos, diferenciando o anterior ensino cidadão dos anos 70, por uma educação a conceitos não naturais a nossa sociedade.

`Richard Stallman`_ (também designado como RMS) era uma das pessoas que trabalhavam no `MIT`_ e que havia vivido a fase da liberdade entre os programadores. RMS tinha um sentimento muito forte com relação à liberdade e à comunidade solidária que ele fazia parte.

.. figure:: {filename}/images/filosofia-gnu/Richard-Stallman.jpg
        :target: {filename}/images/filosofia-gnu/Richard-Stallman.jpg
        :alt: Richard Stallman
        :align: center

        Richard Matthew Stallman

A história do software livre começa com uma impressora laser que o MIT havia ganho, e que substituiria uma impressora matricial que era utilizada há vários anos pelos técnicos.

Como a impressora antiga fazia parte da história em que a liberdade era comum no uso da tecnologia, o driver utilizado na matricial já continha inserções no código produzidas pelos técnicos do MIT, que permitia informações tais como o momento em que iniciava ou terminava um trabalho de impressão, erros no processo, entre outros. No entanto, a impressora laser não continha essas facilidades, o que causava um grande transtorno.

RMS toma a iniciativa e procura o representante da impressora para tentar negociar com ele a inserção das mesmas facilidades da impressora matricial. A resposta que ele ouviu foi a mesma que qualquer pessoa ouviria ao tentar negociar uma alteração com uma empresa de software proprietário, que seria algo mais ou menos como: nós somos os donos do software e se você quiser alguma alteração, peça-nos, que nós vamos avaliar e implementar se acharmos adequado.

RMS ainda tentou convencer o representante, que ao final de um longo debate ofertou um contrato para que os programadores assinassem, basicamente constituído por cláusulas de não revelação, ou seja, *Nondisclosure agreement*, uma maneira de conceder acesso a um código, impedindo a divulgação do que fosse visto, conhecido.

Os contratos de não revelação já eram comuns desde a época dos PDPs (*Programmable Data Processor*, uma linha de computadores que foi produzida pela Digital *Equipment Corporation* -- DEC -- entre 1960 e 1972, indo do modelo PDP-1 ao PDP-16. O modelo mais popular foi o PDP-11 de 1970), e tinha dois objetivos básicos:

#. O mundo da informática (tanto do ponto de vista do software quanto de hardware) era uma novidade, e as empresas de tecnologia da época tentavam estabelecer mecanismos que garantissem o mercado;
#. A guerra fria era um motivo forte, e havia o receio dos americanos de que os seus adversários pudessem utilizar os computadores para fazerem cálculos vetoriais, e com isso, lançassem uma bomba atômica sobre os EUA.

Finalmente, a proposta do representante da impressora foi considerada por RMS como uma agressão a liberdade. Afinal, como seria possível assinar um acordo antecipado em que você se negaria a ajudar qualquer pessoa, seja ela quem fosse. Além disso, o trabalho do MIT seria incorporado a um produto que continuaria em poder do fabricante, e outras pessoas não teriam oportunidade de aproveitar-se das facilidades que seriam incorporadas pelos técnicos.

Foi a partir dai que Richard Stallman se deu conta que não havia sentido trabalhar em algo proprietário, e que aquele era um momento importante onde as pessoas deviam ter direito ao livre acesso da tecnologia, e para tanto, deu meia volta e começou ainda em 1983 o movimento *Free Software*, tendo em 1984 fundado a *Free Software Foundation*.

Inicialmente Richard Stallman criou o GCC, que é o compilador livre para a linguagem C, o editor de textos EMACS, permitindo assim que vários programadores ao redor do mundo começassem a contribuir na construção de um sistema operacional e de um *kernel* livre.

O `primeiro email enviado por Richard Stallman`_ (`traduzido aqui`_) foi disponibilizado para as listas *net.unix-wizards* e *net.usoft*, contendo as ideias básicas do que ele pretendia fazer, isto aconteceu em 27/09/1983.


Créditos
--------

O material foi desenvolvido por Djalma Valois Filho e é o resultado de uma compilação das duvidas mais usuais que surgiram ao longo das inúmeras palestras apresentadas desde o ano 2000 pelo CIPSGA - Comitê de Incentivo a Produção do Software GNU e Alternativo em todo Brasil.

Todo o conteúdo encontrado neste curso é oriundo dos textos publicados pela FSF, bem como outros textos publicados pelo CIPSGA até a presente data. Críticas e sugestões construtivas são bem vindas a qualquer tempo, podendo ser enviadas para *email [at] dvalois [dot] net*.

.. _Projeto CDTC: http://cursos.cdtc.org.br/
.. _FDL: http://www.gnu.org/licenses/fdl.html
.. _primeiro email enviado por Richard Stallman: https://groups.google.com/forum/#!msg/net.unix-wizards/8twfRPM79u0/1xlglzrWrU0J
.. _traduzido aqui: http://www.gnu.org/gnu/initial-announcement.html
.. _Richard Stallman: http://stallman.org
.. _MIT: http://web.mit.edu/
