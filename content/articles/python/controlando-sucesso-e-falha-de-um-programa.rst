Controlando o Sucesso/Falha de Um Programa
##########################################
:date: 2015-03-04 21:16
:category: Python
:tags: python, exceptions, exit, fluxo, status, raise, logging
:image: /images/python.png
:description: Uma das partes mais importantes de um programa é o controle de
              seu sucesso ou falha, entretanto é uma das partes que, enquanto
              programamos, mais deixamos em segundo plano, juntamente com
              o registro de logs.

Outro dia, em uma conversa do Gupy-DF surgir uma dúvida sobre como controlar
o fluxo e o status de um programa. Epistem alguma formas de se realizar
essa tarefa, cada uma com suas vantagens e desvantagens.

.. image:: {filename}/images/python/zen-of-python-poster.png
        :target: {filename}/images/python/zen-of-python-poster.png
        :alt: Zen of Python
        :align: center

Mas por quê isso é importante? Um exemplo básico é que seu programa pode vir
a ser utilizado por outros programas (seja sob a forma de um programa externo
ou um biblioteca), e é importante repassar informações sobre a execução para
o "programa que o invocou". Uma outra situação é quando seu próprio programa
precisa fazer *logging* das ações executadas e dos erros encontrados.

.. more

Vamos a um pseudo código de exemplo:


.. code-block:: python

    import sys

    def satisfaz_condicoes(item):
        '''Verifica condições de negócio'''
        if condicoes:
            return True
        else:
            return False

    def obtem_dados(item):
        '''verifica dados dos item'''
        # E se houver erro durante a obtenção de dados?
        # Após obter todos os dados
        return dados

    def realiza_processamento(item, dado):
        '''Realiza processamento'''
        # E se houver erro durante o processamento?
        # Após o processamento
        return resultado

    def processa(item):
        if satisfaz_condicoes(item):
            dados = obtem_dados(item)
            if dados:
                return realiza_processamento(item, dados)
        else:
            print("Não satisfaz condicoes")

    if __name__ == '__main__':
        if len(sys.argv) <= 1:
            print("Usage: {} <item> ...".format(sys.argv[0]))
            exit(1)

        items = sys.argv[1:]
        for item in items:
            processa(item)
        exit(0)

Neste pseudo código meu programa irá processar diversos itens informados a ele.
Notem que o programa está estruturado de forma a separar a "interface CLI" (no
``if __name__``) e uma possível interface via importação (utilizando a função
``processa``). Entretanto, em nenhuma delas é repassado alguma informação
sobre o status da execução. Um "usuário" do programa estaria executando "às
cegas" e teria que verificar o sucesso manualmente.

Então chega o ponto principal, como implementar um controle de erros?

A Maneira Rápida e Fácil
------------------------

A maneira mais rápida e fácil e sair colocando ``print``'s e ``exit``'s em todos os pontos
de falha:

.. code-block:: python

    import sys

    def satisfaz_condicoes(item):
        '''Verifica condições de negócio'''
        if condicoes:
            return True
        else:
            return False

    def obtem_dados(item):
        '''verifica dados dos item'''
        # Em caso de erro durante a obtenção dos dados
        print("Erro XYZ, devido a ABC")
        exit(1)
        # Após obter todos os dados
        return dados

    def realiza_processamento(item, dado):
        '''Realiza processamento'''
        # Em caso de erro durante o processamento
        print("Não possível realizar tarefa ABC")
        exit(1)
        # Após processar com sucesso
        return resultado

    def processa(item):
        if satisfaz_condicoes(item):
            dados = obtem_dados(item)
            if dados:
                return realiza_processamento(item, dados)
        else:
            print("Não satisfaz condicoes")
        exit(1)

    if __name__ == '__main__':
        if len(sys.argv) <= 1:
            print("Usage: {} <item> ...".format(sys.argv[0]))
            exit(1)

        items = sys.argv[1:]
        for item in items:
            processa(item)
        exit(0)

Muito bem, o problema está resolvido. O programa para de executar ao encontrar
uma condição de "erro" prevista. Entretanto, quando este seu código for
utilizado por um colega na forma de uma biblioteca, estes ``exit``'s
inseridos irão causar a saída prematura do programa do seu colega.

Além disso, esta abordagem impede que você continue a execução ignorando
erros, por exemplo, processando todos os itens e informando apenas os que
foram ignorados devido a erros.

Além disso, observe que, a única forma de diferenciar o motivo do encerramento
do programa seria distribuindo ``print``'s ao longo do código. Não se esqueçam
de considerar que uma função pode abortar prematuramente por diversos motivos,
por exemplo, a função ``realiza_processamento``, pode resultar em erro pois
o dado é inconsistente, ou o item não está estruturado corretamente ou, até
mesmo, devido a comunicações de rede.

O que nos leva a outra possibilidade...

Retornar Status de Funções
--------------------------

Uma abordagem comum é retornar em todas as funções um status de sua execução,
o que é muito comum em linguagens que não suportam exceções, como C e Go.
Vejamos uma implementação rápida.

.. code-block:: python

    import sys

    def satisfaz_condicoes(item):
        '''Verifica condições de negócio'''
        if condicoes:
            return True
        else:
            return False

    def obtem_dados(item):
        '''verifica dados dos item'''
        # Em caso de erro durante a obtenção dos dados
        print("Erro XYZ, devido a ABC")
        return (False, None)
        # Após obter todos os dados
        return (True, dados)

    def realiza_processamento(item, dado):
        '''Realiza processamento'''
        # Em caso de erro durante o processamento
        print("Não possível realizar tarefa ABC")
        return (False, None)
        # Após o processamento
        return (True, resultado)

    def processa(item):
        if satisfaz_condicoes(item):
            (status, dados) = obtem_dados(item)
            if (status and dados):
                (status, resultado) = realiza_processamento(item, dados)
                return (status, resultado)
        else:
            print("Não satisfaz condicoes")
        return (False, None)

    if __name__ == '__main__':
        if len(sys.argv) <= 1:
            print("Usage: {} <item> ...".format(sys.argv[0]))
            exit(1)

        items = sys.argv[1:]
        for item in items:
            (status, resultado) = processa(item)
        exit(0)

Muito bem, essa abordagem parece bem mais interessante, certo? Eu tendo
a discordar. Vamos a alguns pontos, sempre que você invoca uma função que não
é de validação e que precisa retornar um valor próprio, você precisa retornar
uma tupla contendo o status da execução e conteúdo a ser retornado. Além disso
trazer mais trabalho manual, ela torna o código mais complexo pois nos obriga
a sempre verificar o status da última execução (vide chamadas
à ``realiza_processamento`` e ``obtem_dados``).

Ah, e antes que alguém diga "mas você pode retornar ``None`` para indicar um
erro". Eu já rebato: "E no caso de ``obtem_dados``, e se os dados que eu
obtive forem vazios, não seria bom retornar ``None`` para representar os dados
vazios?". Se eu convencionar que toda função que retorna ``None`` incorreu em
erro, uma hora ou outra você com certeza vai ter um conflito de valores.
Acredite, já passei por isso.

Não obstante, essa solução ainda não lhe provê a granularidade de distinguir
por quê uma função incorreu em erro. Uma possível melhoria seria retornar um
número indicando o motivo do erro, mas consequentemente você teria que criar
um dicionário para indicar o que cada código significa, além de tornar mais
complexo o código e lhe trazer mais esforço mental, ao ter que
decorar/consultar todos os códigos de erro.

Vamos para a melhor abordagem...

Utilizando Exceções
-------------------

Na minha visão a melhor forma para trabalhar com estas situações é o uso
de exceções. O primeiro passo é criar uma "biblioteca de exceções":

.. code-block:: python

    class MyAppBaseException(Exception):
        def __init__(self, msg, *args):
        self.msg = msg.format(*args)

    class ErroObtendoDados(MyAppBaseException):
        msg = "Erro XYZ, devido a ABC"

    class ErroAoComunicarComServidor(MyAppBaseException):
        pass

    class ErroAoProcessar(MyAppBaseException):
        pass

Note que todas as exceções herdam de uma exceção base, isso será útil no
código final.

.. code-block:: python

    import sys
    from minhas_excessoes import *

    def satisfaz_condicoes(item):
        '''Verifica condições de negócio'''
        if condicoes:
            return True
        else:
            return False

    def obtem_dados(item):
        '''verifica dados dos item'''
        # Em caso de erro durante a obtenção dos dados
        raise ErroObtendoDados("Erro XYZ, devido a ABC")
        # Em caso de erro durante a comunicação com o servidor
        raise ErroAoComunicarComServidor("Não foi possível comunicar "+\
                                         "com o servidor XYZ")
        # Após obter todos os dados
        return dados

    def realiza_processamento(item, dado):
        '''Realiza processamento'''
        # Em caso de erro durante o processamento
        raise ErroAoProcessar("Não possível realizar tarefa ABC")
        # Após processar com sucesso
        return resultado

    def processa(item):
        if satisfaz_condicoes(item):
            dados = obtem_dados(item)
            if dados:
                return realiza_processamento(item, dados)

    if __name__ == '__main__':
        if len(sys.argv) <= 1:
            print("Usage: {} <item> ...".format(sys.argv[0]))
            exit(1)

        items = sys.argv[1:]
        for item in items:
            try:
                processa(item)
            except MyAppBaseException as e:
                print(e.msg)
                exit(1)
        exit(0)

Note que a responsabilidade de imprimir a mensagem de erro é de quem utiliza
a função e não da função que incorreu em erro, isso é um dos pontos chaves
dessa abordagem pois segmenta o comportamento da sua aplicação e permite que
você trate cada caso separadamente.

Além disso essa abordagem:

* permite um controle minucioso do que pode ser mostrado (modo normal ou modo *verbose*, por exemplo);
* facilita a refatoração de código, pois reduz o número de ``if``'s;
* possibilita o reuso de código, boa parte dessas mensagem já podem estar
  dentro das classes que herdam de ``MyAppBaseException``, e receber como
  argumentos apenas os parâmetros;

Vamos ver uma forma de simplificar as mensagens de erro e ainda adicionar
a funcionalidade de *return codes* diferentes para cada tipo de erro. Primeiro
as exceções:

.. code-block:: python

    class MyAppBaseException(Exception):
        def __init__(self, **kwargs):
            if 'msg' in kwargs:
                self.msg= kwargs['msg']
            self.msg = self.msg.format(**kwargs)

    class ErroObtendoDados(MyAppBaseException):
        def __init__(self, **kwargs):
            self.msg = "Erro {erro}, devido a {razao}"
            self.code = 2
            super().__init__(**kwargs)

    class ErroAoComunicarComServidor(MyAppBaseException):
        def __init__(self, **kwargs):
            self.msg = "Não foi possível comunicar com o servidor {srv}"
            self.code = 3
            super().__init__(**kwargs)

    class ErroAoProcessar(MyAppBaseException):
        def __init__(self, **kwargs):
            self.msg = "Não possível realizar tarefa {tarefa}"
            self.code = 4
            super().__init__(**kwargs)

Agora adequando o código do programa.

.. code-block:: python

    import sys
    from minhas_excessoes import *

    def satisfaz_condicoes(item):
        '''Verifica condições de negócio'''
        if condicoes:
            return True
        else:
            return False

    def obtem_dados(item):
        '''verifica dados dos item'''
        # Em caso de erro durante a obtenção dos dados
        raise ErroObtendoDados(erro="XYZ", razao="ABC")
        # Uma exceção totalmente customizada
        raise ErroObtendoDados(msg="Dados inexistentes para {tipo}", tipo="XYZ")
        # Em caso de erro durante a comunicação com o servidor
        raise ErroAoComunicarComServidor(srv="XYZ")
        # Após obter todos os dados
        return dados

    def realiza_processamento(item, dado):
        '''Realiza processamento'''
        # Em caso de erro durante o processamento
        raise ErroAoProcessar(tarefa="ABC")
        # Após processar com sucesso
        return resultado

    def processa(item):
        if satisfaz_condicoes(item):
            dados = obtem_dados(item)
            if dados:
                return realiza_processamento(item, dados)

    if __name__ == '__main__':
        if len(sys.argv) <= 1:
            print("Usage: {} <item> ...".format(sys.argv[0]))
            exit(1)

        items = sys.argv[1:]
        for item in items:
            try:
                processa(item)
            except MyAppBaseException as e:
                print(e.msg)
                exit(e.code)
        exit(0)

Pronto, veja como ficou elegante o código! Permitindo até exceções
customizadas :)

Acho que por hoje é isso pessoal! Até a próxima!
