Makefile Para Java
##################
:date: 2014-07-18 17:14
:category: Java
:tags: java, makefile, command line, programação, gnu
:image: 
:description: Melhor do que 


.. code-block:: makefile

        # Ignore isso...
        space:=$(empty) $(empty)

        # Binários
        JAVAC=/usr/bin/javac
        JAVA=/usr/bin/java
        JAR=/usr/bin/jar

        # Diretórios...
        BINDIR=bin
        JARDIR=jars

        # Adicione qualquer classpath externo que você precise
        USERCLASSPATH=.

        # Criando classpath dinâmico
        TMPCLASSPATH=$(USERCLASSPATH):$(realpath $(BASE)$(BINDIR))
        ifneq (,$(wildcard $(jars)/*))
                CLASSPATH=$(TMPCLASSPATH):$(subst $(space),:,$(foreach jar,$(wildcard $(JARDIR)/*.jar),$(realpath $(jar))))
        endif

        # Flags de compilação
        JCFLAGS=-g -d $(BASE)$(BINDIR) -classpath $(CLASSPATH)
        # Flags de execução
        JFLAGS=-classpath $(CLASSPATH)

        %.class: %.java
                $(eval BASE=$(dir $<))
                rm -rf $(BASE)$(BINDIR) && mkdir $(BASE)$(BINDIR)
                $(JAVAC) $(JCFLAGS) $*.java

        %: %.class
                cd $(BASE)$(BINDIR) && $(JAVA) $(JFLAGS) $(subst /,.,$(subst .class,,$<))

        %.jar: %.class
                -mkdir -p $(JARDIR)
                $(JAR) cfe $(JARDIR)/$(subst /,-,$(subst .class,.jar,$<)) $(subst /,.,$(subst .class,,$<)) -C $(BASE)$(BINDIR)/ .

        clean:
                -find . -type d -name $(BINDIR) | xargs -I{} rm -rf {}
                -rm -rf $(JARDIR)

        PHONY: clean
