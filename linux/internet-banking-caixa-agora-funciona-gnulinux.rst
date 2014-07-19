Internet Banking Caixa Agora Funciona no GNU/Linux
##################################################
:date: 2013-06-25 16:35
:category: Linux
:tags: banco, banking, caixa, gnu, internet, java, jdk, linux, openjdk
:image: /images/caixa-sqr.jpg

Nesta última semana a Caixa anunciou que o seu Internet Banking agora
suporta mais navegadores e mais sistemas operacionais. Curiosamente o
assunto não foi amplamente divulgado e recebeu apenas uma pequena nota
no site oficial do `banco`_ e do `serviço`_. Mas da mesma forma, essa é
uma grande vantagem para nos usuários GNU/Linux, que estamos acostumados
a sofrer com aplicações bancários.

.. image:: {filename}/images/caixa.jpg
	:align: center
	:target: {filename}/images/caixa.jpg
	:alt: Banner Caixa

Como vocês puderam ver, nos links informados não há muita informação
sobre quais navegadores (e suas respectivas versões) e sistemas
operacionais são suportados neste momento. Mas para aqueles que são
clientes, durante o processo de autenticação do computador é apresentada
a seguinte informação:

.. more

.. figure:: {filename}/images/internetbanking-caixa-requisitos.png
	:align: center
	:target: {filename}/images/internetbanking-caixa-requisitos.png
	:alt: Requisitos Internet Banking Caixa

        Requisitos do Internet Banking Caixa

Dessa forma podemos ver que esta nova versão do serviço suporta
GNU/Linux (com o Kernel 2.6 ou superior) e os navegadores: Mozilla
Firefox (3.6 ou superior); Google Chrome (4.0 ou superior); e Opera
(11.64 ou inferior).

Apesar da afirmar a obrigatoriedade da JVM Java Oracle Sun 1.7 ou
superior, eu consegui acessar e realizar transações bancárias
satisfatoriamente com a OpenJDK disponível no repositório do Arch Linux
(jdk7-openjdk 7.u40\_2.4.0-1).

Com essa atualização do Internet Banking da Caixa, creio que muitos
usuários GNU/Linux conseguiram se livrar de mais algumas amarras do
mundo Microsoft Windows.

.. _banco: http://caixa.gov.br/
.. _serviço: https://internetbanking.caixa.gov.br/SIIBC/index.processa
