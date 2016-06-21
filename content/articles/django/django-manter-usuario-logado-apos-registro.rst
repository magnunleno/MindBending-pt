Django: Logando o Usuário Logo Após o Registro
##############################################
:date: 2016-06-21 16:20
:category: Django
:tags: django, tutorial, email, autenticação, login
:image: /images/django/django-logo.png

No meu `último artigo`_ eu demonstrei como customizar a autenticação no Django. Hoje um colega do `Grupo de Django no Telegram`_ levantou a questão de como logar usuário automaticamente após este efetuar o registro. Apesar de achar que este não é um fluxo ideia, o correto seria haver uma confirmação de email antes que o usuário faça login, resolvi brincar com a ideia para ajudar esse colega.

.. image:: {filename}/images/django/django-text.png
        :target: {filename}/images/django/django-text.png
        :alt: Django
        :align: center

Lembrando que o código deste artigo usa como base o código do meu `último artigo`_. Então, antes de seguir neste texto, leia o anterior e obtenha os códigos fonte.

.. more

Em suma, a única alteração que temos que fazer é no arquivo de ``views`` inserindo os seguintes *imports*:

.. code-block:: python

    from django.contrib.auth import authenticate
    from django.contrib.auth import login as auth_login


Note que eu "renomeei" o import da função ``login``, pois esta conflitava com o nome da *view* ``login``.

Agora, só é necessário realizar uma adequação na view ``RegistrationView`` para que ela fique da seguinte forma:

.. code-block:: python

    class RegistrationView(CreateView):
        form_class = CustomUserCreationForm
        success_url = reverse_lazy('users:login')
        template_name = "users/register.html"

        def post(self, request, *args, **kwargs):
            form = self.get_form()
            is_valid = form.is_valid()
            response = super().post(request, *args, **kwargs)
            if is_valid:
                new_user = authenticate(
                    username=form.cleaned_data['email'],
                    password=form.cleaned_data['password1'],
                )
                auth_login(request, new_user)
                return HttpResponseRedirect(reverse_lazy('users:home'))
            return response

Em suma, apenas sobrescrevemos o método ``post``. Tem um pequeno detalhe que é validação do ``form`` antes de chamar ``super().post()``, pois, se chamado posteriormente, a validação do form sempre será negativa, pois o usuário já existe na base. Em seguida não tem mais nenhum segredo.

Pronto, *as simple as that*.

.. _último artigo: /pt/customizando-a-autenticacao-de-usuarios-no-django-19
.. _Grupo de Django no Telegram: https://telegram.me/django_group_initial_steps
