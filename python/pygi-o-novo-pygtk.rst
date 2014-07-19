PyGI, o "novo" PyGTK
####################
:date: 2011-04-13 10:45
:category: Python
:tags: gnome3, pygi, pygtk, python
:image: /images/python.png
:featured: /images/python.png
:description: A biblioteca PyGTK será substituída pela PyGI.

Há algum tempo tenho lido no `Planet Gnome`_ informações de que o módulo `PyGTK será descontinuada`_. Conforme esse último link, possivelmente o PyGTK 2.24 foi a última versão lançada. Esse módulo será substituída por `GObject Introspection`_, ou como está sendo chamada PyGI.

.. image:: {filename}/images/pygtk.png
        :align: center
        :alt: PyGTK

Para aqueles que querem mais informações sobre essa mudança, sugiro acompanhar a `Ubuntu App Development Week`_ pois houveram 2 sessões sobre o abandono do PyGTK e como funcionará o novo PyGI. A primeira delas foi `GObject Introspection: The New Way For Developing GNOME Apps in Python, JavaScript and Others`_, com Tomeu Vizoso, e a outra foi `PyGTK is dead, long live PyGI! Using gobject-introspection in Python`_, com Martin Pitt.

.. more

Baseado em outras bibliotecas que foram descontinuadas, eu afirmo com certeza que o PyGTK ainda estará por aqui por um certo tempo, então nada de pânico e/ou desespero para migrar suas aplicações, teremos tempo para isso. Além do mais, ainda não há (pelo menos eu não encontrei) uma documentação específica. De acordo com o que eu li, o módulo PyGI já está disponível em diversas distribuições, basta testar da seguinte forma:

.. code-block:: bash

    $ python -c 'from gi.repository import Gtk; print Gtk'

O único problema é que ainda estão todas desatualizadas. Essas mudanças ainda serão disponibilizadas na versão beta do Ubuntu 11.04 e no Debian Unstable.

Uma coisa é certa, assim que eu tiver acesso à versão atualizada do módulo PyGI eu postarei alguns tutoriais aqui sobre como escrever aplicações GTK usando o Python e o PyGI. Até lá...

.. _Planet Gnome: http://planet.gnome.org/
.. _PyGTK será descontinuada: http://www.johnstowers.co.nz/blog/index.php/2011/04/03/end-of-an-era-pygtk/
.. _GObject Introspection: https://live.gnome.org/PyGObject/IntrospectionPorting
.. _Ubuntu App Development Week: http://ubuntu-news.org/2011/03/31/announcing-ubuntu-app-developer-week-2/
.. _`GObject Introspection: The New Way For Developing GNOME Apps in Python, JavaScript and Others`: https://wiki.ubuntu.com/MeetingLogs/appdevweek1104/GObjectIntrospection
.. _PyGTK is dead, long live PyGI! Using gobject-introspection in Python: https://wiki.ubuntu.com/MeetingLogs/appdevweek1104/PyGI

