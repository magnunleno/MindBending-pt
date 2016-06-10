Customizando a Autenticação de Usuários no Django 1.9
#####################################################
:date: 2016-06-08 14:10
:category: Django
:tags: django, tutorial, email, autenticação
:image: /images/django/django-logo.png

Por padrão, o Django utiliza como identificador único um "nome de usuário" (*username*). Apesar de ser adotada por muitos sites, não é uma prática que me agrada muito, então, uma das primeiras coisas que eu faço quando inicio um projeto Django é customizar o usuário base do projeto e configurar para que o email do usuário seja utilizado para identificá-lo durante o login.

.. image:: {filename}/images/django/django-text.png
        :target: {filename}/images/django/django-text.png
        :alt: Django
        :align: center

Se existem vantagens/desvantagens reais? Além de menos confusão na hora de login e menos campos durante o registro, eu desconheço qualquer outra vantagem. Ou seja, saibam que é apenas uma mania minha, não uma boa prática ou recomendação.

.. more

Novo Projeto e Configurações Básicas
------------------------------------

Vamos começar criando um novo projeto:

.. code-block:: bash

    $ mkvirtualenv -p /usr/bin/python3 MeuProjeto
    $ pip install django==1.9
    $ django-admin startproject MeuProjeto
    $ mkdir MeuProjeto/apps MeuProjeto/templates/users
    $ cd MeuProjeto/apps
    $ django-admin startapp users
    $ cd users
    $ mv apps.py config.py

Em seguida altere a configuração dos *templates* para que ele busque-os em ``MeuProjeto/templates``:

.. code-block:: python

    TEMPLATES = [
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': ['templates/'],
            'APP_DIRS': True,
            'OPTIONS': {
                'context_processors': [
                    'django.template.context_processors.debug',
                    'django.template.context_processors.request',
                    'django.contrib.auth.context_processors.auth',
                    'django.contrib.messages.context_processors.messages',
                ],
            },
        },
    ]


O Modelo e a Migração
---------------------

O primeiro passo é criar um `model` para refletir os dados que você deseja que o usuário possua. Segue abaixo o meu *model* (``MeuProjeto/apps/users/models.py``):

.. code-block:: python

    # Arquivo: /apps/users/models.py
    from django.db import models
    from django.utils.translation import ugettext as _
    from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
    from django.contrib.auth.models import PermissionsMixin


    class EmailUserManager(BaseUserManager):
        def create_user(self, *args, **kwargs):
            email = kwargs["email"]
            email = self.normalize_email(email)
            password = kwargs["password"]
            kwargs.pop("password")

            if not email:
                raise ValueError(_('Users must have an email address'))

            user = self.model(**kwargs)
            user.set_password(password)
            user.save(using=self._db)
            return user

        def create_superuser(self, *args, **kwargs):
            user = self.create_user(**kwargs)
            user.is_superuser = True
            user.save(using=self._db)
            return user


    class MyUser(PermissionsMixin, AbstractBaseUser):
        email = models.EmailField(
            verbose_name=_('Email address'),
            unique=True,
        )
        first_name = models.CharField(
            verbose_name=_('Nome'),
            max_length=50,
            blank=False,
            help_text=_('Inform your name'),
        )
        last_name = models.CharField(
            verbose_name=_('Sobrenome'),
            max_length=50,
            blank=False,
            help_text=_('Inform your last name'),
        )
        USERNAME_FIELD = 'email'
        objects = EmailUserManager()

Como podem ver existem duas classes. A primeira, ``EmailUserManager``, é uma classe auxiliar que é irá mimetizar a API do *Manager* do modelo de usuário original do Django. Isso é necessário pois precisaremos disponibilizar para o Django os métodos  ``MyUser.obejcts.create_user`` e ``MyUser.obejcts.create_superuser``.

Note que herdamos de ``AbstractBaseUser`` (que provê o esqueleto básico de um usuário) e de ``PermissionsMixin`` (que provê funcionalidade de permissionamento). Sem a primeira classe ``MyUser`` não poderia ser utilizado como um modelo de um usuário. Já sem a *Mixin* de permissionamento, a aplicação até funcionaria, mas faltariam funcionalidades de controle de superusuário (``is_superuser``), grupos (``groups``) e permissões (``user_permissions``).

Em seguida precisamos ativar o *app* no arquivo ``MeuProjeto/settings.py`` adicionando a linha ``'apps.users'`` à chave de configuração ``INSTALLED_APPS``. Ao final ela deve conter as seguintes linhas:

.. code-block:: python

    INSTALLED_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'apps.users'
    ]

Agora podemos executar as migrações desse *app*:

.. code-block:: bash

    $ ./manage.py makemigrations
    $ ./manage.py migrate

Por último vamos adicionar em ``MeuProjeto/MeuProjeto/settings.py`` a indicação da classe que servirá como modelo para os usuários. Para isso adicione a seguinte linha: ``AUTH_USER_MODEL = "users.MyUser"``.


Forms, Views e mais Views
-------------------------

Vamos começar pelo mais fácil, um *form* para registro de usuário:

.. code-block:: python

    # Arquivo: apps/users/forms.py
    from django.contrib.auth.forms import UserCreationForm

    from .models import MyUser


    class CustomUserCreationForm(UserCreationForm):
        class Meta:
            model = MyUser
            fields = ['first_name', 'email']

Como podem foram poucas linhas de código graças á possibilidade de herdar do *form* ``UserCreationForm``.

Para apresentar esse *form* customizado vamos criar algumas *views*.

.. code-block:: python

    # Arquivo: /apps/users/views.py
    from django.shortcuts import render
    from django.views.generic import CreateView
    from django.http import HttpResponseRedirect
    from django.contrib.auth.views import login
    from django.contrib.auth.views import logout
    from django.core.urlresolvers import reverse_lazy, reverse

    from .forms import CustomUserCreationForm


    def home(request):
        return render(request, 'users/home.html')


    def login_view(request, *args, **kwargs):
        if request.user.is_authenticated():
            return HttpResponseRedirect(reverse('users:home'))

        kwargs['extra_context'] = {'next': reverse('users:home')}
        kwargs['template_name'] = 'users/login.html'
        return login(request, *args, **kwargs)


    def logout_view(request, *args, **kwargs):
        kwargs['next_page'] = reverse('users:home')
        return logout(request, *args, **kwargs)


    class RegistrationView(CreateView):
        form_class = CustomUserCreationForm
        success_url = reverse_lazy('users:login')
        template_name = "users/register.html"

Vamos com calma aqui. Primeiramente temos uma *view* ``home`` que apenas renderiza um *template* que mostraremos mais abaixo.

Antes de falarmos da *view* ``login_view``, vamos descrever qual é o comportamento esperado de uma tela de login:

#. Apresentar a tela de login caso o usuário não esteja autenticado;
#. Caso um usuário já autenticado tente acessar a tela de login, este deve ser redirecionado e a tela de login não deve ser apresentada.
#. Após o login, redirecionar o usuário para uma tela específica;

Para conseguir o primeiro e o segundo item dessa lista de comportamento adicionamos um ``if`` que verifica se o usuário está logado e, em caso positivo, redireciona-o para uma "home" (*view* ``home``). Já o para o segundo item precisamos informar a próxima tela após a autenticação, para isso customizamos alguns parâmetros através da sobrescrita do dicionário ``kwargs``.

A *view* de logout (``logout_view``) também foi ligeiramente customizada, adicionando apenas o argumento ``next_url`` para que, assim que acessada esta página realiza o processo de logout e em seguida redireciona o usuário.

Por último, temos a *view* que vai renderizar o *form* criado anteriormente. Ela é uma CBV (*Class Based View*) bem simples que herda de ``CreateView`` e customiza o ``form_class`` para o *form* que criamos, a ``succcess_url`` e o ``template_name``.

Agora vamos apresentar estes *templates*. Começando pelo mais simples...

.. code-block:: html

    <!-- Arquivo: templates/users/home.html -->
    <p>Seja bem vindo {% if user.is_authenticated %}{{ user.first_name }}{% else %}usuário anônimo{% endif %}</p>

    {% if user.is_authenticated %}
    <p><a href="{% url 'users:logout' %}">Logout</a>.</p>
    {% else %}
    <p><a href="{% url 'users:register' %}">Registre-se</a>.</p>
    <p><a href="{% url 'users:login' %}">Login</a>.</p>
    {% endif %}

Nada de mais mesmo, apenas apresenta o nome do usuário (ou a string *usuário anônimo*) e alguns links, dependendo se o usuário está logado ou não.

Agora o *template* para registrar o usuário:

.. code-block:: html

    <!-- Arquivo: templates/users/register.html -->
    <h1>Registrarion</h1>

    <form role="form" class="form" method="POST">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit" class="btn btn-warning">Register</button>
    </form>

Por último o formulário para login.

.. code-block:: html

    <!-- Arquivo: templates/users/login.html -->
    <h1>Login</h1>

    <form role="form" class="form" method="POST" action="{{ request.path }}{% if next %}?next={{ next }}{% endif %}">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit" class="btn btn-warning"><i class="fa fa-plus" aria-hidden="true"></i> Login</button>
    </form>

Este tem um pequeno detalhe, que é inserção do atributo ``action`` apontando para a URL atual e tendo como argumento uma variável ``next``, que foi informada na *view* ``login_view``. Este argumento irá garantir que após o login o usuário será redirecionado para esta URL.

Apontamento de URLs
-------------------

Para finalizar vamos realizar o apontamento das URLs:

.. code-block:: python

    # Arquivo: apps/users/urls.py
    from django.conf.urls import url

    from . import views

    app_name = 'users'
    urlpatterns = [
        url(r'^$', views.home, name="home"),
        url(r'^login/$', views.login_view, name="login"),
        url(r'^logout/$', views.logout_view, name="logout"),
        url(r'^register/$', views.RegistrationView.as_view(), name="register"),
    ]

Antes que alguém comente dizendo que eu poderia ter feito boa parte das customizações das *views* de login e logout, assim como a *view* *home* diretamente no arquivo de URLs, eu já adianto que eu não gosto dessa prática. Já adotei esse tipo de prática e percebi que é um *maintenance hell*, aprendi que as *urls* devem possuir apenas apontamento de URLs, nada de variáveis como nome de *templates* e etc.

Mais simples que este arquivo de URLs, somente mesmo o mapeamento de URLs do principais do projeto.

.. code-block:: python

    # Arquivo: MeuProjeto/urls.py
    from django.conf.urls import include, url
    from django.contrib import admin

    import apps.users.urls

    urlpatterns = [
        url(r'^admin/', admin.site.urls),
        url(r'^user/', include('apps.users.urls', namespace="users")),
    ]


Fechamento
----------

Com poucas linhas de código (aproveitando o máximo que o *framework* disponibiliza) já temos a estrutura básica de registro, login e logout de usuários. Claro que ainda não é um primor, e muito pode ser melhorado, principalmente na parte de HTML/CSS, mas este já é um esqueleto básico de 75% das aplicações que você pode vir a desenvolver.

Pontos pendentes:

* Edição de dados de perfil do usuário;
* Troca de senha;
* *Reset* de senha (o famoso "esqueci minha senha");
