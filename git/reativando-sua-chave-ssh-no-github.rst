Reativando sua Chave SSH no GitHub
##################################
:date: 2012-04-24 10:00
:category: Git
:tags: chave, git, github, gnu, linux, segurança, ssh
:image: /images/github_logo.png

Há 2 meses Egor Homakov `reportou`_ uma falha de segurança no framework
Ruby on Rails que acabou desencadeando `uma bela de uma confusão`_.
Consequentemente, para evitar que esta falha tenha sido utilizada para
prejudicar qualquer usuário, o `GitHub`_ revogou temporariamente todas
chaves SSH e enviou a todos os usuários um email. Porém (provavelmente
devido a falta de informações detalhadas no email) o "sensor anti-spam"
de muitos usuários disparou, e muitos não acreditaram no e-mail e/ou não
souberam como proceder.

.. image:: {filename}/images/github.png
	:align: center
	:target: {filename}/images/github.png
	:alt: GitHub Octocat

.. more

Para conhecimento de todos os leitores, segue o conteúdo do e-mail:

    **Action Required - SSH Key Vulnerability**

    A security vulnerability was recently discovered that made it
    possible for an attacker to add new SSH keys to arbitrary GitHub
    user accounts. This would have provided an attacker with clone/pull
    access to repositories with read permissions, and clone/pull/push
    access to repositories with write permissions. As of 5:53 PM UTC on
    Sunday, March 4th the vulnerability no longer exists.

    While no known malicious activity has been reported, we are taking
    additional precautions by forcing an audit of all existing SSH keys.

    **Required Action**

    Since you have one or more SSH keys associated with your GitHub
    account you must visit https://github.com/settings/ssh/audit to
    approve each valid SSH key.

    Until you have approved your SSH keys, you will be unable to
    clone/pull/push your repositories over SSH.

    **Status**

    We take security seriously and recognize this never should have
    happened. In addition to a full code audit, we have taken the
    following measures to enhance the security of your account:

    - We are forcing an audit of all existing SSH keys
    - Adding a new SSH key will now prompt for your password
    - We will now email you any time a new SSH key is added to your account
    - You now have access to a log of account changes in your Account Settings page

    Sincerely, The GitHub Team

    https://github.com support@github.com

Como podemos notar, o GitHub não foi muito detalhista, então resolvi
mostrar a vocês (leitores) como realizar esta verificação e reativar a
sua chave SSH! Primeiro devemos acessar o endereço de auditoria de
chaves do GitHub (`https://github.com/settings/ssh/audit`_), que deve
lhe apresentar uma página semelhante a esta:

.. image:: {filename}/images/github-sshkey-audit.png
	:align: center
	:target: {filename}/images/github-sshkey-audit.png
	:alt: GitHub SSH Key Audit Page

Em seguida abra um terminal no seu GNU/Linux e emita o comando
``ssh-keygen -lf ~/.ssh/id_rsa.pub``. A saída do seu comando deve ser
algo similar a isto:

.. image:: {filename}/images/export-local-sshkey.png
	:align: center
	:target: {filename}/images/export-local-sshkey.png
	:alt: Export Local SSH Key

Agora basta comparar as duas chaves, se houver alguma divergência,
clique em *"upload new key"* e siga o procedimento para inserir a chave
que você obteve com o comando no terminal. Se ambas forem iguais basta
clicar em **Approve**.

Pronto, agora sua conta está normalizada e você será capaz de clonar
repositórios e/ou realizar *pull/push* novamente!

.. _reportou: https://github.com/rails/rails/issues/5228
.. _uma bela de uma confusão: http://www.h-online.com/security/news/item/GitHub-security-incident-highlights-Ruby-on-Rails-problem-1463207.html
.. _GitHub: http://github.com/
.. _`https://github.com/settings/ssh/audit`: https://github.com/settings/ssh/audit
