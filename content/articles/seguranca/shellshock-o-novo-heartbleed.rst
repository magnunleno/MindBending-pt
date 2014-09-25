Shellshock, o Novo Heartbleed?
##############################
:date: 2014-09-25 16:03
:category: Segurança
:tags: segurança, heartbleed, linux, bash, shellshock, apple, gnu
:image: /images/seguranca/shellshock-sqr.jpg
:description: Um bug descoberto no Bash está causando uma grande preocupação para especialistas de segurança para a Internet.

Um bug (`CVE-2014-7169`_ e `CVE-2014-6271`_) descoberto por Stephane Chazelas no Bash está causando uma enorme preocupação na Internet, alguns estão colocando este bug lado a lado com o `Heartbleed`_. Mas um bug em um shell deveria causar tanta preocupação assim? O Shell não passa ser executado apenas após você se autenticar no servidor via SSH ou FTP e outros serviços? Sim... e não.

.. image:: {filename}/images/seguranca/shellshock.jpg
        :target: {filename}/images/seguranca/shellshock.jpg
        :alt: Shellshock
        :align: center

.. more

Entendendo
----------

Pra começar vamos entender a falha. O bash é um shell, ou um "interpretador de comandos" utilizado em todos os GNU/Linux e nos computadores da Apple. Então, em suma, ele deveria interpretar isso como um erro:

.. code-block:: bash

        $ env x='() { :;}; echo vulnerable' bash -c "echo this is a test"

O que esse código faz? Em um ambiente (*environment*) segmentado ``env x``, ele executa uma função vazia não nomeada ``() { :;}``, finaliza a declaração dessa função (``;``), concatena com um simples ``echo`` para informar a falha e por fim fecha o ambiente. Em seguida temos apenas uma execução de um `'echo'` para informar que estamos realizando um teste. A saída esperada é a seguinte (caso você esteja vulnerável):

.. code-block:: bash

        $ env x='() { :;}; echo vulnerable' bash -c "echo this is a test"
         vulnerable
         this is a test

Caso seu bash não seja vulnerável, o resultado será o seguinte:

.. code-block:: bash

        $ env x='() { :;}; echo vulnerable' bash -c "echo this is a test"
        bash: warning: x: ignoring function definition attempt
        bash: error importing function definition for `x'
        this is a test

Mas o que isso tem a ver com a Internet?
----------------------------------------

O fato é que o bash é utilizado por certos *scripts* CGI (*Common Gateway Interface*) para realizar o processamento de cabeçalhos HTTP. Como foi provado por `Troy Hunt`_, com cabeçalhos da seguinte forma: 

.. code::

        Cookie:() { :; }; ping -c 3 209.126.230.74
        Host:() { :; }; ping -c 3 209.126.230.74
        Referer:() { :; }; ping -c 3 209.126.230.74

Enviados a páginas geradas por CGI é possível realizar pings coordenados e distribuídos:

.. image:: {filename}/images/seguranca/shellshock-responses.png
        :target: {filename}/images/seguranca/shellshock-responses.png
        :alt: Respostas Shellschok
        :align: center

Quer algo melhor? Nesta `resposta no Stackoverflow`_ foi demonstrado que um simples *script* CGI aliado a cabeçalhos pré-preparados poderiam ser utilizado para obter o conteúdo do ``/etc/passwd`` de um servidor. Oura opção é criar um *fork bomb*:

.. code-block:: bash

        $ () { :; }; :(){ :|: & };:

E travar o servidor remotamente sem precisar nem mesmo invadir o servidor.


Estou Vulnerável
----------------

Basicamente esse bug afeta **todas as versões do bash** até a versão 4.3. ou seja, quase 25 anos de versões do Bash estão suscetíveis a este bug.

O bom de se utilizar software livre é que tudo é consertado muito rápido. Atualmente a Red Hat, o CentOS, o Ubuntu e o Debian já possuem correções, bastando uma simples atualização de pacote.

.. code-block:: bash

        # Debian & Ubuntu
        $ sudo apt-get update && sudo apt-get install bash

        # Fedora, CentOS e Red Hat
        $ sudo yum update bash

Já em relação à Apple (OS X), eu não encontrei nenhum relato de correção...

**Fontes:** `NGINX`_, `ARS Technica`_ e `Security Blog`_

.. _Heartbleed: /pt/entendendo-o-heartbleed-e-previnindo-se
.. _Troy Hunt: http://www.troyhunt.com/2014/09/everything-you-need-to-know-about.html
.. _resposta no Stackoverflow: http://security.stackexchange.com/questions/68122/what-is-a-specific-example-of-how-the-shellshock-bash-bug-could-be-exploited

.. _Ubuntu: http://www.ubuntu.com/usn/usn-2362-1/
.. _Debian: https://www.debian.org/security/2014/dsa-3032
.. _Red Hat: https://access.redhat.com/articles/1200223G
.. _CentOS: http://lists.centos.org/pipermail/centos/2014-September/146099.html

.. _CVE-2014-6271: http://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2014-6271
.. _CVE-2014-7169: http://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2014-7169


.. _ARS Technica: http://arstechnica.com/security/2014/09/bug-in-bash-shell-creates-big-security-hole-on-anything-with-nix-in-it/
.. _NGINX: http://nginx.com/blog/nginx-cve-2014-6271-bash-advisory/
.. _Security Blog: https://securityblog.redhat.com/2014/09/24/bash-specially-crafted-environment-variables-code-injection-attack/
