Processando Arquivos XML - Java vs. Python vs. C
################################################
:date: 2012-10-29 13:47
:category: Linguagens de Programação
:tags: c, código, desenvolvimento, java, processamento, programa, programação, projeto, python, xml
:image: /images/no-java_badge.png

Não sou muito a favor de "rixas" entre comunidades, mas se tem uma
ferramenta que me irrita é o Java. Não me entendam mal, não tenho
problemas com a comunidade, ou com o modelo de negócio da Oracle (nem da
antiga Sun Microsystems), apenas não gosto da linguagem. Admito que ela
muitas vezes tem um ótimo desempenho, mas a sua sintaxe e verbosidade me
frustram e irritam de uma maneira que nem a `linguagem Brainfuck`_
consegue. Como pode uma linguagem exigir que um programador digite tanta
coisa para praticamente NADA!

.. figure:: {filename}/images/java-sucks.png
    :alt: Java Sucks
    :align: center

Estou sendo forçado a escrever códigos em Java para a monografia da
minha Pós-Graduação, e neste trabalho estou lidando com arquivos XML.
Depois de finalizar o código de processamento do arquivo XML eu estava
exausto. Olhei para o código e me senti aterrorizado, como é possível?!
Nem a linguagem C (considerada terrível por muitos) exige que eu digite
tanto para tão pouco! E por que um processo tão simples precisa envolver
tantas classes diferentes? E o pior de tudo, o tempo de execução é
pífio!

.. more

Ambiente de teste
-----------------

Para demonstrar o que estou querendo dizer irei utilizar como teste o
seguinte arquivo XML que armazena 4 notas de 3 alunos diferentes:

.. code-block:: xml

        <alunos>
                <aluno>
                        <nome>Joao</nome>
                        <nota1>7</nota1>
                        <nota2>8</nota2>
                        <nota3>5</nota3>
                        <nota4>10</nota4>
                </aluno>

                <aluno>
                        <nome>Maria</nome>
                        <nota1>8</nota1>
                        <nota2>6</nota2>
                        <nota3>6</nota3>
                        <nota4>9</nota4>
                </aluno>

                <aluno>
                        <nome>Jose</nome>
                        <nota1>5</nota1>
                        <nota2>6</nota2>
                        <nota3>4</nota3>
                        <nota4>5</nota4>
                </aluno>
        </alunos>

Escrevi programas que leem o arquivo e imprimem o nome do aluno seguido
de suas quatro notas.

Código Em Java
--------------

Atenção! O código abaixo é extremamente horrível, desta forma não me
responsabilizo por nenhum colapso nervoso, ataque do coração ou
formações de úlceras gástricas que ele venha a lhe causar, culpe a
Sun/Oracle.

Avisos dados, segue o código:

.. code-block:: java

        import javax.xml.parsers.DocumentBuilderFactory;
        import javax.xml.parsers.DocumentBuilder;
        import org.w3c.dom.Document;
        import org.w3c.dom.NodeList;
        import org.w3c.dom.Node;
        import org.w3c.dom.Element;
        import java.io.File;
        import java.util.ArrayList;
        import java.util.logging.Logger;

        public class ProcessaApp {
            public static void main(String[] args){
                Document doc;
                DocumentBuilder dBuilder;
                DocumentBuilderFactory dbFactory;
                NodeList nodeList;
                
                NodeList alunos;
                String valor;

                try {
                    File fXmlFile = new File("teste.xml");
                    dbFactory = DocumentBuilderFactory.newInstance();
                    dBuilder = dbFactory.newDocumentBuilder();
                    doc = dBuilder.parse(fXmlFile);
                    doc.getDocumentElement().normalize();
                } catch (Exception e) {
                    e.printStackTrace();
                    return;
                }
                
                alunos = doc.getElementsByTagName("aluno");
                
                for (int alunoN = 0; alunoN < alunos.getLength(); alunoN++) {
                    Node nNode = alunos.item(alunoN);
                    if (nNode.getNodeType() == Node.ELEMENT_NODE) {
                        Element eElement = (Element) nNode;
                        System.out.println("-----------");
                        
                        // nome
                        nodeList = eElement.getElementsByTagName("nome");
                        valor = nodeList.item(0).getChildNodes().item(0).getNodeValue();
                        System.out.println("Nome: "+valor);
                        
                        // nota1
                        nodeList = eElement.getElementsByTagName("nota1");
                        valor = nodeList.item(0).getChildNodes().item(0).getNodeValue();
                        System.out.println("Nota 1: "+valor);
                        
                        // nota2
                        nodeList = eElement.getElementsByTagName("nota2");
                        valor = nodeList.item(0).getChildNodes().item(0).getNodeValue();
                        System.out.println("Nota 2: "+valor);
                        
                        // nota3
                        nodeList = eElement.getElementsByTagName("nota3");
                        valor = nodeList.item(0).getChildNodes().item(0).getNodeValue();
                        System.out.println("Nota 3: "+valor);
                        
                        // nota4
                        nodeList = eElement.getElementsByTagName("nota4");
                        valor = nodeList.item(0).getChildNodes().item(0).getNodeValue();
                        System.out.println("Nota 4: "+valor);
                    }
                }
                System.out.println("----FIM----");
            }	
        }


Como eu disse, é um código horrível! E não vejo motivo que justifique a
utilização de 7 classes diferentes (``File``, ``Document``,
``DocumentBuilderFactory``, ``DocumentBuilder``, ``Node``, ``NodeList``
e ``Element``) para uma coisa tão simples. Além disso, olhem que absurdo
a seguinte linha:
``valor = nodeList.item(0).getChildNodes().item(0).getNodeValue()``.
Pelo que posso deduzir, se não houvesse esse encadeamento eu precisaria
de mais umas 3 instâncias para chegar na string que contém o nome e as
notas.

Exemplo de execução:

.. code-block:: bash

    $ javac ProcessaApp.java
    $ java ProcessaApp
    -----------
    Nome: Joao
    Nota 1: 7
    Nota 2: 8
    Nota 3: 5
    Nota 4: 10
    -----------
    Nome: Maria
    Nota 1: 8
    Nota 2: 6
    Nota 3: 6
    Nota 4: 9
    -----------
    Nome: Jose
    Nota 1: 5
    Nota 2: 6
    Nota 3: 4
    Nota 4: 5
    ----FIM----

Código em C
-----------

Para que ninguém alegue que é covardia comparar Java com Python, irei
comparar **primeiro** com C. Notem que o código não é nada complexo e
tão pouco extenso quanto em Java:

.. code-block:: c

        #include <stdio.h>
        #include <stdlib.h>
        #include <string.h>
        #include <libxml/parser.h>

        #define CMP(name1, name2) xmlStrcmp(name1, (const xmlChar *)name2)

        void parseAluno(xmlDocPtr doc, xmlNodePtr cur)
        {
                printf("-----------\n");
                xmlChar *key;

                for (cur=cur->xmlChildrenNode; cur!=NULL; cur=cur->next) {
                        key = xmlNodeListGetString(doc, cur->xmlChildrenNode, 1);
                        if (!CMP(cur->name, "nome")) 
                                printf("Nome: %s\n", key);
                        else if (!CMP(cur->name, "nota1")) 
                                printf("Nota 1: %s\n", key);
                        else if (!CMP(cur->name, "nota2")) 
                                printf("Nota 2: %s\n", key);
                        else if (!CMP(cur->name, "nota3")) 
                                printf("Nota 3: %s\n", key);
                        else if (!CMP(cur->name, "nota4")) 
                                printf("Nota 4: %s\n", key);

                        xmlFree(key);
                }
        }

        int main(int argc, char const *argv[])
        {
                xmlDocPtr doc;
                xmlNodePtr cur;

                doc = xmlParseFile("teste.xml");
                cur = xmlDocGetRootElement(doc);

                for (cur=cur->xmlChildrenNode; cur!=NULL; cur=cur->next) 
                        if (!CMP(cur->name, "aluno"))
                                parseAluno(doc, cur);

                printf("----FIM----\n");
                xmlFreeDoc(doc);

                return 0;
        }

Notem que que eu fui generoso nos espaçamentos deste exemplo em C, e
mesmo assim o código tem 50 linhas, enquanto o código em Java tem 68.
Além disso, em C utilizei-me de uma função para tornar o código menos
endentado, o que o torna um pouco maior. Sem esta função eu economizaria
umas 5 linhas, no mínimo. Para uma linguagem que foi feita para superar
e tornar a programação mais simples que em C, o Java está se saindo
muito mal.

Exemplo de execução:

.. code-block:: bash

    $ clang -Wall -O3 processa.c  `pkg-config --libs --cflags glib-2.0; xml2-config 
       --cflags --libs` -o processa
    $ ./processa
    -----------
    Nome: Joao
    Nota 1: 7
    Nota 2: 8
    Nota 3: 5
    Nota 4: 10
    -----------
    Nome: Maria
    Nota 1: 8
    Nota 2: 6
    Nota 3: 6
    Nota 4: 9
    -----------
    Nome: Jose
    Nota 1: 5
    Nota 2: 6
    Nota 3: 4
    Nota 4: 5
    ----FIM----

Código em Python
----------------

Agora vem a covardia. Vejam o código em Python:

.. code-blocK:: python

        import xml.etree.cElementTree as et

        fd = open('teste.xml')
        parsedXML = et.parse(fd)
        alunos = parsedXML.findall('aluno')

        for alunoNode in alunos:
            aluno = dict((attr.tag, attr.text) for attr in alunoNode)
            print '-----------'
            print 'Nome:', aluno['nome']
            print 'Nota 1:', aluno['nota1']
            print 'Nota 2:', aluno['nota2']
            print 'Nota 3:', aluno['nota3']
            print 'Nota 4:', aluno['nota4']

        print '----FIM----'

Sem comentários, apenas um exemplo de execução:

.. code-block:: bash

    $ python processa.py
    -----------
    Nome: Joao
    Nota 1: 7
    Nota 2: 8
    Nota 3: 5
    Nota 4: 10
    -----------
    Nome: Maria
    Nota 1: 8
    Nota 2: 6
    Nota 3: 6
    Nota 4: 9
    -----------
    Nome: Jose
    Nota 1: 5
    Nota 2: 6
    Nota 3: 4
    Nota 4: 5
    ----FIM----

Tempo de Execução
-----------------

E quanto ao tempo de execução? Bem, realizei testes de execução deste
código com o arquivo citado (o que favorece a linguagem Java, pois esta
não lida bem com arquivos grandes), para não ser tendencioso. Realizei
medições de uma única execução, de dez execuções, de cem execuções e de
mil execuções. Segue uma tabela com os resultados da execução (medidos
com o comando *time*):

.. table::
        :class: table

        ====================== ========== ========== ==========
        Repetições             Java       Python     C     
        ====================== ========== ========== ==========
        **1 repetição**        0.091 seg. 0.025 seg. 0.001 seg.
        **10 repetições**      0.143 seg. 0.027 seg. 0.002 seg.
        **100 repetições**     0.293 seg. 0.034 seg. 0.005 seg.
        **1000 repetições**    1.156 seg. 0.087 seg. 0.038 seg.
        ====================== ========== ========== ==========

Claro que uma imagem vale mais que mil palavras. Então vejam a imagem:

.. figure:: {filename}/images/xml-process.png
    :alt: grafico-comparativo
    :align: center

Sem mais meritíssimo.

.. _linguagem Brainfuck: http://en.wikipedia.org/wiki/Brainfuck
