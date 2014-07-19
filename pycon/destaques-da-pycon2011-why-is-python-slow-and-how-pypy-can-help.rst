Destaques da PyCon2011 - Why Is Python Slow And How PyPy Can Help
#################################################################
:date: 2011-10-26 08:30
:category: PyCon
:tags: bytecode, compilada, compilador, cpython, desempenho, interpretada, interpretado, jit, linguagem, máquina, máquina virtual, palestra, pycon2011, pypy, python, video, virtual
:image: /images/pycon2010.png
:series: Destaques da Pycon 2011

Dando prosseguimento à série de artigos `Destaques da PyCon2011`_, hoje
não só sugiro sugiro mas insisto que assistam a palestra ministrada por
Maciej Fijałkowski e Alex Gaynor sobre a máquina virtual para o Python
chamado **PyPy**. Eu sempre me perguntei como o **PyPy** (que é escrito
em Python) pode ser mais rápido que o CPython (que é escrito em C). Esta
palestra não só sanou minha dúvida como também me deixou muito curioso e
me fez realizar algumas pesquisas sobre o próprio **PyPy** e o JIT.

.. raw:: html
        
        <p style="text-align: center;"><object width="600" height="366" id="player"><param value="http://blip.tv/scripts/flash/showplayer.swf?file=http://blip.tv/rss/flash/4897756" name="movie"><param value="true" name="allowFullScreen"><param value="always" name="allowscriptaccess"><param value="transparent" name="wmode"><embed width="600" height="366" allowfullscreen="true" allowscriptaccess="always" type="application/x-shockwave-flash" src="http://blip.tv/scripts/flash/showplayer.swf?file=http://blip.tv/rss/flash/4897756"></object></p>

Para aqueles que ficaram perdidos durante a palestra, segue abaixo uma
breve explicação do que é o **PyPy** e o JIT.

.. more

O que é o PyPy?
---------------

O **PyPy** é um Projeto *OpenSource*, ativo há 8 anos, que tem como
objetivo criar um novo interpretador para a linguagem Python. Sua versão
estável possui uma compatibilidade de 99,99% (mais informações sobre
incompatibilidades disponível no `site oficial`_) e oferece um ganho de
desempenho significativo sem modificar a linguagem. Para garantir o alto
nível de compatibilidade, seus testes unitários possuem por volta de 150
mil linhas de código. Para termos uma melhor noção do ganho de
desempenho oferecido pelo **PyPy**, basta visitar o site `**PyPy** Speed
Center`_, todos os gráficos são normalizados com base no tempo de
resposta do interpretador padrão do Python, o CPython.

.. image:: {filename}/images/pypy_logo.png
	:align: center
	:target: {filename}/images/pypy_logo.png
	:alt: PyPy Logo

Atualmente o **PyPy** (em sua versão 1.6) é compatível com o Python
2.7.1 e está disponível nas plataformas x86 e x86\_64 `aqui`_. De acordo
com sua `página oficial`_, uma versão para a plataforma ARM está sendo
desenvolvida.

Mas Como Eles Podem Ser Mais Rápidos?!
--------------------------------------

Todo o esforço do **PyPy** se resume em "fazer o seu computador
trabalhar menos", através do uso do JIT, *Just-In-Time* (somente quando
necessário, em uma tradução livre). Diferente de uma máquina virtual
comum, uma máquina que utiliza o JIT realiza uma tradução do *bytecode*
para código de máquina nativo durante sua execução.

A ideia de uma máquina virtual que suporta o conceito de JIT é combinar
as vantagens do conceito de máquinas virtuais (que se utilizam de
*bytecode* para garantir a portabilidade) e da compilação tradicional
(que converte o código fonte diretamente para código de máquina). Também
são realizadas todas as possíveis otimizações baseadas na análise do
código fonte, obtendo-se um conjunto de *bytecodes* otimizados e
semanticamente equivalente ao programa fonte original.

.. _Destaques da PyCon2011: /pt/series/destaques-da-pycon-2011/
.. _site oficial: http://pypy.org/compat.html
.. _**PyPy** Speed Center: http://speed.pypy.org/
.. _aqui: http://pypy.org/download.html
.. _página oficial: http://pypy.org/features.html
