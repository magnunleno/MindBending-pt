Web2py: Abstraindo a DAL Corretamente
#####################################
:date: 2013-09-06 15:12
:category: Web2Py
:tags: abstração, banco, dados, dal, database, descriptors, descritores, metaclasse, python, web, web2py
:image: /images/web2py_logo.png
:slug: web2py-abstraindo-dal-corretamente

Por mais que o Web2Py já possua uma camada de abstração para o acesso ao
banco de dados, `conhecida como DAL`_, e que ela seja excelente, eu não
acho que ele incetiva da forma correta a segmentação e `reutilização de
códigos`_. Como eu já `mostrei anteriormente aqui`_ é possível
implementar um modelo simples que "corrige" esses problemas, entretanto,
a forma que apresentei não é a mais elegante de todas, pois ela utiliza
a sintaxe de dicionários para controlar o acesso às colunas do banco de
dados.

.. image:: {filename}/images/abstracting-abstraction.jpg
	:align: center
	:target: {filename}/images/abstracting-abstraction.jpg
	:alt: Yo dawg, heard you like abstractions

A forma mais Pythonica de controlar este tipo acesso é através de
*Properties*. Mas convenhamos, é extremante exaustivo escrever códigos
para *getters* e *setters* para cada coluna de cada tabela do banco de
dados.

.. more

Por isso comecei a estudar sobre o conceito de *Descriptors*, que pode
ser compreendido claramente `aqui`_. Entretanto, os *descriptors*,
precisam ser criados na declaração das classes, na forma de atributos de
classe, ou seja, seria necessário "re-declarar" todos os campos da
tabela. Algo que também não me agrada muito a fazer...

Então comecei a estudar sobre *metaclasses* no Python. Algo um pouco
complicado de se entender, mas que eu gosto de resumir da seguinte
forma: Metaclasses são códigos para modificar a declaração de classes
durante sua criação.

Mas vamos começar devagar e pelo começo...

A Base de Dados
---------------

A base de dados deste exemplo é similar ao utilizado no `exemplo
anterior`_.

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

*Descriptors*
-------------

O *descriptor* abaixo possui três métodos: ``__init__``, ``__get__`` e
``__set__``. O métodos ``__init__`` se restringe a armazenar o *field* e
a tabela. Já o método ``__get__`` é mais complexo, mas o que ele faz é
retornar o consultar o banco de dados e retornar um valor. Por último, o
método ``__set__`` atualiza o valor em um banco de dados.

Desta forma, a classe referente à tabela ``cliente`` possuirá 7
*descriptors*: nome, cpf, data\_nascimento, email, apelido, ativo e
profissao.

O código abaixo é extremamente auto explicativo...

.. code-block:: python

    class AttributeRecord(object):
        '''
        Descriptor for abstract any type of data from the DAL.
        '''
        def __init__(self, field):
            '''
            Initialize the descriptor storing the field and table with witch it will
            "bind to".
            '''
            self.field = field
            self.table = field.table

        def __get__(self, obj, type=None):
            '''
            The get method for the descriptor.
            - If object is None, it means that it's bean accessed thought the class
            (Ex: Client.name) and should return the database field itself.
            - If the object is not none it means it's bound to some object, and
            should return it's contents.
            '''
            # TODO: Implement some kind of cache
            if not obj:
                return self.field

            if self.field.name == 'id':
                # The id attribute should not be fetched from DB
                return obj._id

            if self.field.type.startswith('reference '):
                # If reference another table, get the stored id and return the
                # instantiated record object
                table = getattr(db, self.field.type.split(' ')[-1])
                id = db(
                        self.table.id == obj._id
                        ).select(self.field).first()[self.field.name]
                return table._record(id=id)

            if not obj.id:
                # Object initialized improperly or unknown
                raise TypeError("Unknown object")

            return db(
                    self.table.id == obj._id
                    ).select(self.field).first()[self.field.name]

        def __set__(self, obj, value):
            '''
            The set method for the descriptor.
            It will automatically update the value in the database.
            '''
            if not obj:
                raise TypeError("Unbound descriptor")

            if not obj.id:
                # Object initialized improperly or unknown
                raise TypeError("Unknown object")

            if self.field.name == 'id':
                # Object ID is "write only"
                raise TypeError("Sorry, can't change object ID")

            db(self.table.id == obj._id).update(**{self.field.name:value})

Metaclasse
----------

A metaclasse desta implementação se restringe a algumas linhas de
código, que simplesmente inserem os *descriptors* na classe que será
criada. Para isso é utilizada a instrução ``setattr``, que insere um
novo atributo na classe.

.. code-block:: python

    class MetaRecord(type):
        '''
        The metaclass responsible for initializing the descriptors for each record
        '''
        def __init__(kls, name, bases, attributes):
            '''
            Initialize the record class with it's descriptors
            '''
            if kls._table is None:
                # Record doesn't have a table. Must be the CommonRecord
                return

            # Stores in the table a reference for this class
            kls._table._record = kls

            for name in kls._table._fields:
                field = getattr(kls._table, name)
                attr = AttributeRecord(field)
                setattr(kls, name, attr)

A Classe Comum
--------------

Essa é a parte mais complexa, uma classe que será comum a todas as
outras classes, e que terá como base a metaclasse apresentada
anteriormente.

Esta classe possui vários métodos para fazer consultas e inserções à
base de dados. Os métodos desta classe são, até certo ponto, genéricos e
se aplicam a qualquer tabela da base de dados. As consultas mais
específicas devem ser implementadas na especificação da classe abaixo.

.. code-block:: python

    class CommonRecord(object):
        '''
        The base class for the Database Records
        It has some basic methods for querying and inserting data.
        '''
        __metaclass__ = MetaRecord
        _table = None
        def __new__(kls, *args, **kwargs):
            '''
            Blocks the instantiation of the CommonRecord base class
            '''
            if kls == CommonRecord:
                raise TypeError("This is a model class and should not " +\
                           "be instantiated")
            return super(CommonRecord, kls).__new__(kls, *args, **kwargs)

        def __init__(self, id=None):
            '''
            Basic init method that stores the ID.
            '''
            self._id = long(id)

        @classmethod
        def exists(kls, id):
            '''
            Returns True or False if the record with matching ID exists.
            '''
            return not db(kls._table.id == id).isempty()

        @classmethod
        def byId(kls, id):
            '''
            Method that returns a record based in the informed ID.
            '''
            if kls.exists(id):
                return kls(id)
            raise TypeError("Id '%i' unknown"%id)

        @classmethod
        def all(kls, orderby=None, groupby=None):
            '''
            Returns all records from the table.
            Arguments:
                orderby: Should be a Field (Ex: Client.name)
                groupby: Should be a Field
            '''
            return (kls(row.id) for row in db(kls._table).select(
                kls._table.id, orderby=orderby, groupby=groupby,
                ))

        @classmethod
        def search(kls, query=None, orderby=None, groupby=None):
            '''
            Search for all records that match the criteria specified in query.
                query: Should be a Query (Ex: Client.id > 10)
                orderby: Should be a Field (Ex: Client.name)
                groupby: Should be a Field
            '''
            if not query:
                query = kls._table

            return (kls(row.id) for row in db(query).select(
                kls._table.id, orderby=orderby, groupby=groupby,
                ))

        @classmethod
        def count(kls, query=None):
            '''
            Returns how many records are returned with the criteria in query.
                query: Should be a Query (Ex: Client.id > 10)
            '''
            if not query:
                query = kls._table

            return db(query).count()

        @classmethod
        def isempty(kls, query=None):
            '''
            Returns True/False if the criteria in query has any matching.
                query: Should be a Query (Ex: Client.id > 10)
            '''
            if not query:
                query = kls._table

            return db(query).isempty()

        @classmethod
        def insert(kls, **fields):
            '''
            Insert a new record in the table. The fields must be specified like
            below:
                Client.insert(name="John", active=True)
                # or
                clientData = {'name':"John", 'active':True}
                Client.insert(**clientData)
            '''
            id = kls._table.insert(**fields)
            return kls(id)

        @classmethod
        def deleteById(kls, id):
            '''
            This method deletes a record based in it's ID.
            '''
            return bool(db(kls._table.id == id).delete())

        def delete(self):
            '''
            This method deletes the current record instance.
            '''
            ret_code = db(self._table.id == self._id).delete()
            self._id = None
            return bool(ret_code)

        def as_dict(self, *fields):
            '''
            This method returns many fields in a dictionary format. It's specially
            useful to avoid many database requisitions.
            '''
            fields = self.__check_fields(fields)
            return db(self._table.id == self._id).select(*fields).first().as_dict()

        def __check_fields(self, fields):
            '''
            This restricted method is used to check the existence of the informed
            fields (in string) and return as instances of Field.
            '''
            if not fields:
                return (self._table.ALL, )

            error = filter(lambda x : not isinstance(x, Field), fields)
            if error:
                error = map(str, error)
                raise TypeError('Invalid fields: %s'%', '.join(error))
                return None

            return fields

Especificações
--------------

Para cada tabela da sua aplicação você precisa criar uma especificação
da classe ``CommonRecord`` e informar a tabela da base de dados. Veja
exemplos abaixo:

.. code-block:: python

    class Cliente(CommonRecord):
        _table = db.cliente

    class Profissao(CommonRecord):
        _table = db.profissao

Automatizando especificações
----------------------------

Caso você esteja pensando "minha aplicação tem muitas tabelas, vou ter
que escrever uma classe para cada tabela na mão?". Não, não vai. Eu
pensei nessa possibilidade e após um tempo pesquisando e assistindo
algumas palestras sobre coisas muito absurdas no Python, eu descobri
como escrever códigos para não precisar escrever código :).

E este código eu não vou explicar, pois fica de dever de casa para
vocês.

.. code-block:: python

    def g_autoGenerateClasses():
        import inspect
        caller = inspect.currentframe().f_back
        for tableName in db.tables:
            className = map(str.capitalize, tableName.split('_'))
            className.append('DAL')
            className = ''.join(className)
            table = getattr(db, tableName)
            caller.f_locals.update(**{className: type(className, (CommonDAL, ), {
                '__metaclass__' : MetaRecord, '_table':table
                })})

Basta chamar esta função após a declaração de todas as suas tabelas no
web2py e ela se encarregará de criar automaticamente uma classe para
cada tabela. Se você tem uma tabela chamada ``cliente`` e outra chamada
``cliente_profissao`` essa função gerará duas classes com os seguintes
nomes: ``Cliente`` e ``ClienteProfissao``.

Funcionamento Básico
--------------------

A Parte mais básica dessa camada de abstração é retornar um *Record* da
base de dados e permitir o acesso aos seus atributos.

.. code-block:: python

    >>> c = Cliente.byId(2)
    >>> c.nome
    'Jo\xc3\xa3o Prado'
    >>> c.ativo
    True
    >>> c.as_dict()
    {'apelido': 'Jo\xc3\xa3o', 'ativo': True, 'cpf': '52812396865', 'data_nascimento': datetime.date(1981, 9, 2), 'email': 'joao.prado@mail.com', 'id': 2L, 'nome': 'Jo\xc3\xa3o Prado', 'profissao': 2L}

Mas de nada adianta você poder acessar os atributos se você não pode
atualizá-lo. A forma como o *descriptor* é escrito permite que, ao
atualizar um valor no *descriptor* este é automaticamente atualizado no
banco de dados. Veja o exemplo abaixo:

.. code-block:: python

    >>> c = Cliente.byId(2)
    >>> c.nome
    'Jo\xc3\xa3o Prado'
    >>> c.ativo = False
    >>> c.ativo
    False
    >>> c.ativo = True

Outro ponto chave é a capacidade desta abstração de reconhecer
referências a outras tabelas:

.. code-block:: python

    >>> c = Cliente.byId(2)
    >>> c.profissao.nome
    'Programador'
    >>> c.profissao.id
    2L

Funcionalidades De Busca
------------------------

De nada adiantaria essa camada de abstração se não fosse possível
realizar buscas por meio dela. Veja como buscar todos os clientes da
tabela:

.. code-block:: python

    >>> for c in Cliente.all(): print c.id
    1
    2
    3
    4

O método ``all`` também suporta argumentos de ordenação e agrupamento:

.. code-block:: python

    >>> for c in Cliente.all(orderby=Cliente.data_nascimento): print c.id
    3
    1
    2
    4

Com a classe básica também é possível verificar se existe ou não algum
cliente na base:

.. code-block:: python

    >>> Cliente.exists(10)
    False
    >>> Cliente.exists(2)
    True

Também é possível verificar quantos itens existem ou se a tabela está
vazia:

.. code-block:: python

    >>> Cliente.count()
    4
    >>> Cliente.isempty()
    False

Claro que isso não é grande coisa, é muito mais útil verificar quantos
itens existem dada uma certa condição:

.. code-block:: python

    >>> Cliente.count(Cliente.data_nascimento > datetime.date(1981, 1, 1))
    2
    >>> Cliente.isempty(Cliente.id > 10)
    True
    >>> Cliente.exists(Cliente.id == 5)
    False

Para realizar consultas mais complexas, utilize o método ``search`` que
suporta também argumentos de ordenação e agrupamentos:

.. code-block:: python

    >>> for i in Cliente.search(Cliente.data_nascimento > datetime.date(1981, 1, 1)): print i.data_nascimento
    1981-09-02
    1982-01-05

E de nada adiantaria todo esse trabalho se não fosse possível realizar a
inserção e deleção de dados nas tabelas:

.. code-block:: python

    >>> c = Cliente.insert(nome="Teste", data_nascimento=datetime.date.today())
    >>> c.id, c.nome
    (5L, 'Teste')
    >>> c.delete()
    True
    >>> Cliente.insert(nome="Teste", data_nascimento=datetime.date.today())
    >>> Cliente.byId(6).nome
    'Teste'
    >>> Cliente.deleteById(6)
    >>> Cliente.exists(Cliente.id == 6)
    False

Vale ressaltar que esta camada de abstração não é capaz de realizar a
deleção de em várias tabelas ao mesmo tempo.

Trabalhos Futuros
-----------------

Como me diverti muito fazendo isso, acho que vou acabar aprimorando esse
trabalho e colocando tudo num repositório. Entretanto essa abordagem tem
um problema: a redução no tempo de resposta. Como é necessário realizar
análises e o modelo possui consultas pulverizadas, ele tem um tempo de
resposta inferior às requisições feitas diretamente à DAL. Desta forma,
uma das minhas metas no futuro é escrever essa camada de abstração
usando a consulta direta ao banco de dados, sem o uso da DAL. Já fiz
alguns testes e consegui desempenhos melhores que o uso direto da DAL.

Outro ponto que quero melhorar é a necessidade de declarar as tabelas
usando a DAL e depois se utilizar deste método. A longo prazo meu
objetivo é estudar uma forma de aproximar essa abordagem à forma que o
Django funciona, declarando os atributos diretamente na classe e essa
sim, por traz dos panos, chama a DAL para criar o banco de dados.

Mas por enquanto é só. Até a próxima...

.. _conhecida como DAL: /pt/conhecendo-dal-framework-web2py
.. _reutilização de códigos: /pt/reutilizando-consultas-web2py
.. _mostrei anteriormente aqui: /pt/abstraindo-dal-web2py
.. _aqui: http://docs.python.org/2/howto/descriptor.html
.. _exemplo anterior: /pt/abstraindo-dal-web2py
