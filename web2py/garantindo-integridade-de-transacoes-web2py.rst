Garantindo a Integridade de Transações no Web2Py
################################################
:date: 2013-09-11 15:44
:category: Web2Py
:tags: banco, commit, dados, dal, database, exception, integridade, python, rollback, transação, web2py
:image: /images/web2py_logo.png

`Como`_ `já`_ `afirmei`_ `diversas`_ `vezes`_, a `DAL`_ do web2py é
fantástica. Entretanto, ela tem diversas funcionalidades que não são
muito divulgadas. Por exemplo, você sabia que todas as transações de
banco que a DAL (ou o próprio framework Web2py) executa, elas são
agrupadas em transações? Isso é bom, pois garante a "modularidade" das
mudanças de banco e torna possível a "reversão" (*rollback*) em caso de
erro.

.. image:: {filename}/images/web2py.jpg
	:align: center
	:target: {filename}/images/web2py.jpg
	:alt: web2py

Entretanto, quando você manipula o banco diretamente todas as alterações
são consideradas como estando dentro de uma mesma transação, e um
*rollback* resultaria na "reversão" de dados que estavam corretos.
Complicou? Vamos com calma.

.. more

Todas as transações de ``create``, ``drop``, ``insert``, ``truncate``,
``delete``, ou ``update`` (realizadas por você dentro de um
*controller*) não são "enviadas" para o banco imediatamente até o fim da
execução. Esta forma de implementação visa simplificar o conceito de
"transações", tornando cada *controller* o *container* de uma transação.

A implementação deste "*container*" é implementada da seguinte forma, ao
iniciar um *controller*, o web2py inicia uma transação. Ao fim deste
*controller*, o próprio web2py faz o *commit* das alterações e, em caso
de qualquer exceção (exceto *HTTP exceptions*) o framework realiza o
*rollback* da transação. Desta forma o framework te poupa do trabalho
capturar exceções, realizar *rollbacks* e *commits*. Essa abordagem
resolve 90% dos casos, para os outros 10% devemos realizar uma pequena
intervenção.

Digamos que na sua aplicação em algum momento você precisa realizar uma
dada alteração (automatizada e em *background*) em diversos clientes e,
em caso de erro, reverter as alterações apenas deste cliente e seguir em
frente, registrando os erros em uma tabela para análise posterior. Para
isso podemos utilizar a seguinte estrutura:

.. code-block:: python
    
    import datetime

    def atualiza_clientes():
        registros = db(
                (db.cliente.id == db.mensalidade.cliente) &
                (db.mensalidade.vencimento < datetime.date.today())
                ).select()
        for registro in registros:
            cliente = registro.cliente
            mensalidade = registro.mensalidade
            if mensalidade.pagamento:
                continue
            try:
                cliente.update_record(inadimplente=True)
                mensalidade.update_record(suspensa=True)
            except Exception as e:
                db.rollback()
                contexto = "Suspendendo cliente %s"%cliente.nome
                db.alertas.insert(contexto=contexto,
                            mensagem=e.message,
                            )
            else:
                db.commit()

Notem que toda a atualização de banco que corre o risco de ocasionar um
erro está sendo executada dentro de um bloco ``try ... except``. Neste
caso, já que é só um exemplo, eu estou capturando todos os tipos de erro
(o que não é uma boa prática). Para as alterações realizadas com sucesso
(bloco ``else``) apenas realizamos o ``commit``.

Esta forma de processamento garante que um erro não irá abortar a
execução do *controller*. E da mesma forma, garante que, após alterar o
cliente com sucesso, um erro na atualização da mensalidade não resultará
no uma tabela inconsistente, pois ao realizarmos o *rollback* desfazemos
todas as alterações no banco desde o último *commit*.

Como podem ver, o web2py já provê uma forma de operação que banaliza a
necessidade realizar *commits* e *rollbacks*, mas em dados momentos,
este conhecimento pode ser extremamente útil.

Até a próxima...

.. _Como: /pt/conhecendo-dal-framework-web2py
.. _já: /pt/melhorando-desempenho-das-consultas-web2py-2
.. _afirmei: /pt/paginando-consultas-web2py
.. _diversas: /pt/reutilizando-consultas-web2py
.. _vezes: /pt/web2py-abstraindo-dal-corretamente
.. _DAL: /pt/tag/dal
