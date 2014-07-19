Abstraindo a DAL do Web2Py
##########################
:date: 2013-09-04 13:26
:category: Web2Py
:tags: abstração, abstraction, dal, database, python, web2py
:image: /images/web2py_logo.png
:slug: abstraindo-dal-web2py

Apesar da `DAL`_ do `Web2Py`_ ser muito interessante, sua abordagem causa `alguns maus hábitos`_. Além disso, acho a forma de definições de tabelas do Django muito mais maduras.

.. image:: {filename}/images/web2py-tag-cloud.png
	:align: center
	:target: {filename}/images/web2py-tag-cloud.png
	:alt: web2py tag cloud

Pensando nisso comecei a trabalhar em um código que propicia as boas práticas de desenvolvimento em camadas. Como o código definitivo é um pouco complexo, vou apresentar primeiro uma versão simplificada que favorece o entendimento do conceito básico da proposta.

.. more

Definindo Uma Base
------------------

Para que esta demonstração possua um contexto, vou definir duas tabelas: ``cliente`` e ``profissao``. Abaixo a definição de ambas:

.. code-block:: python

    if "profissao" in db.tables:
        db.profissao.drop()
        db.commit()

    db.define_table("profissao",
        Field("nome", "string", length=50, default=None),
        migrate="profissao.table"
        )

    if "cliente" in db.tables:
        db.cliente.drop()
        db.commit()

    db.define_table("cliente",
        Field("nome", "string", length=100, default=None),
        Field("cpf", "string", length=11, default=None),
        Field("data_nascimento", "date", default=None),
        Field("email", "string", length=100, default=None),
        Field("apelido", "string", length=100, default=None),
        Field("ativo", "boolean", default=False),
        Field("profissao", db.profissao, default=None),
        format='%(nome)s',
        migrate="cliente.table")

Para popular a tabela com algum dado, utilizei o seguinte código:

.. code-block:: python

    if (db(db.cliente).count() == 0) and (db(db.profissao).count() == 0):
        import datetime
        profissoes = [
                     'Engenheiro',
                     'Programador',
                     'Designer',
                     'DBA',
                ]
        clientes = [
                {   'nome': 'José da Silva',
                    'cpf' : 92858805687,
                    'data_nascimento': datetime.date(1980, 10, 11),
                    'email': 'jose.silva@mail.com',
                    'apelido': 'Zé',
                    'ativo': True, 
                    'profissao': 1, 
                    },
                {   'nome': 'João Prado',
                    'cpf' : 52812396865,
                    'data_nascimento': datetime.date(1981, 9, 2),
                    'email': 'joao.prado@mail.com',
                    'apelido': 'João',
                    'ativo': True, 
                    'profissao': 2, 
                    },
                {   'nome': 'Marcos Alvares',
                    'cpf' : 35120397158,
                    'data_nascimento': datetime.date(1980, 3, 1),
                    'email': 'marcos.alvares@mail.com',
                    'apelido': 'Marcos',
                    'ativo': True, 
                    'profissao': 3, 
                    },
                {   'nome': 'Rodrigo Barbosa',
                    'cpf' : 51134260407,
                    'data_nascimento': datetime.date(1982, 1, 5),
                    'email': 'rodrigo.barbosa@mail.com',
                    'apelido': 'Rodrigo',
                    'ativo': False, 
                    'profissao': 4, 
                    },
                ]

        for profissao in profissoes:
            db.profissao.insert(nome=profissao)

        for cliente in clientes:
            db.cliente.insert(**cliente)

Um Pouco de Código
------------------

A ideia principal é criar algumas classes capazes de realiza a introspecção no banco de dados e criar seus atributos automaticamente.  Entretanto, para isso é necessário utilizar conceitos avançados de metaclasses. Por isso vamos começar com um modelo mais simples: abstrair as tabelas por meio de classes e realizar o acesso às tabelas por meio do ``__getitem__``.

.. code-block:: python

    import json
    import datetime

    class DALRecord(object):
        _table = None
        _fields = None
        def __new__(kls, *args, **kwargs):
            if kls == DALRecord:
                raise TypeError("This is a model class and should not " +\
                           "be instantiated")
            if not kls._fields:
                kls._fields = kls._table._fields
            return super(DALRecord, kls).__new__(kls, *args, **kwargs)

        def __init__(self, id=None, autoupdate=True):
            self.id = id

        @classmethod
        def __check_fields(kls, fields):
            return all([key in kls._fields for key in fields])

        @classmethod
        def __report_unknown(kls, fields):
            unknown = []
            for field in fields:
                if field not in kls._fields:
                    unknown.append(field)
            raise TypeError("Unknown fields: %s"%', '.join(unknown))

        @classmethod
        def __get_fields(kls, fields):
            return map(lambda x : getattr(kls._table, x), fields)

        @classmethod
        def all(kls):
            for row in db(kls._table).select(kls._table.id):
                yield kls(row.id)

        @classmethod
        def byId(kls, id):
            if not db(kls._table.id == id).isempty():
                return kls(id)
            raise TypeError("Unknown ID '%i'"%id)

        @classmethod
        def insert(kls, **kwargs):
            if kls.__check_fields(kwargs.keys()):
                return kls._table.insert(**kwargs)
            kls.__report_unknown(kwargs.keys())

        def update(self, **kwargs):
            if self.__check_fields(kwargs.keys()):
                return db(self._table.id == self.id).update(**kwargs)
            self.__report_unknown(kwargs.keys())

        def as_dict(self, *fields):
            if self.__check_fields(fields):
                fields = self.__get_fields(fields)
                return db(
                        self._table.id == self.id
                        ).select(*fields).first().as_dict()
            self.__report_unknown(fields)

        def __getitem__(self, key):
            if key == 'id':
                return self.id

            if key not in self._fields:
                raise TypeError("Unknown field '%s'"%key)
            else:
                key = getattr(self._table, key)
                row = db(self._table.id == self.id).select(key).first()
                return row[key]

        def __setitem__(self, key, value):
            if key == 'id':
                return self.id

            if key not in self._fields:
                raise TypeError("Unknown field '%s'"%key)
            else:
                db(self._table.id == self.id).update(**{key : value})

Esta é a classe que servirá como base para todas as outras. Nela são definidos alguns métodos que serão compartilhados por todas as outras classes que representam tabelas.

Uma das partes mais importantes nesta classe é o método ``__new__``, responsável por popular o atributo ``_fields`` na primeira vez que um objeto é instanciado.

Em seguida temos o método ``__init__``, é dispensável de explicações, alguns métodos auxiliares (``__check_fields``, ``__report_unknown`` e ``__get_fields``) e os métodos descritos abaixo:

-  ``all``: Que retorna todas as ocorrências desta tabela;
-  ``byId``: Que retorna a ocorrência da tabela vinculada a um ID;
-  ``insert``: Que insere uma nova ocorrência na tabela;
-  ``update``: Que atualiza uma ocorrência existente na tabela;
-  ``as_dict``: Que retorna um dicionário com os compos solicitados ou
   com todos os campos;

Por fim, temos os principais métodos desta implementação ``__getitem__`` e ``__setitem__``. Estes métodos são responsáveis por obter uma coluna do banco de dados ou atualizar o valor de uma coluna no banco de dados, respectivamente. É importante destacar que que estes métodos evitam a manipulação da coluna ``id`` de todas as tabelas.

Agora dois exemplos de implementação:

.. code-block:: python

    class Cliente(DALRecord):
        _table = db.cliente
        @classmethod
        def get_active_client(kls):
            for id in db(kls._table.ativo == True).select(kls._table.id):
                yield kls(id)

        def get_age(self):
            row = db(
                    self._table.id == self.id
                    ).select(db.cliente.data_nascimento).first()
            nascimento = row.data_nascimento
            hoje = datetime.date.today()
            try: 
                aniversario = nascimento.replace(year=hoje.year)
            except ValueError:
                # birth date is February 29 and the current year is not leap
                aniversario = nascimento.replace(year=hoje.year, day=born.day-1)
            if aniversario > hoje:
                return hoje.year - nascimento.year - 1
            else:
                return hoje.year - nascimento.year

        @property
        def profissao(self):
            return Profissao(id=self.id)

    class Profissao(DALRecord):
        _table = db.profissao

Neste exemplo definimos duas classes, ``Cliente`` e ``Profissao``. Sendo que esta segunda não possui nenhuma customização. Já a classe ``Cliente``, define três métodos ``get_active_client``, que retorna todos os clientes ativos, ``get_age``, que retorna a idade de um dado cliente e ``profissao``, que na verdade é uma property somente leitura e que retorna uma instância da classe ``Profissao``.

Utilização
----------

Abaixo alguns exemplos de utilização:

.. code-block:: python

    >>> for cliente in Cliente.all(): print cliente['nome']
    José da Silva
    João Prado
    Marcos Alvares
    Rodrigo Barbosa
    >>> for cliente in Cliente.get_active_client(): print cliente['nome']
    José da Silva
    João Prado
    Marcos Alvares
    >>> cliente = Cliente.byId(2)
    >>> cliente.as_dict()
    {'apelido': 'Jo\xc3\xa3o', 'ativo': True, 'cpf': '52812396865', 'data_nascimento': datetime.date(1980, 9, 2), 'email': 'joao.prado@mail.com', 'id': 2L, 'nome': 'Jo\xc3\xa3o Prado'}
    >>> cliente.update(data_nascimento=datetime.date(1980, 9, 2))
    1
    >>> cliente['data_nascimento']
    datetime.date(1980, 9, 2)
    >>> cliente.get_age()
    33
    >>> cliente.profissao['nome']
    'Programador'

Como podem ver não é a solução mais elegante, mas é algo simples mas muito poderoso e que torna a abstração dos dados algo muito mais simples e concentrada. No próximo artigo vou compratilhar com vocês um código mais complexo e que implementa a mesma ideia, mas de uma maneira muitoa mais elegante.

Até lá!

.. _DAL: /pt/tag/dal
.. _Web2Py: /pt/tag/web2py
.. _alguns maus hábitos: /pt/reutilizando-consultas-web2py
