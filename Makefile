# Basic setup {{{
PY?=python3
PELICAN?=pelican
PELICANOPTS=
VENV=~/venv/pelican-3.4/bin/activate
# }}}

# Dirs setup {{{
BASEDIR=$(CURDIR)
INPUTDIR=$(BASEDIR)/content
OUTPUTDIR=$(BASEDIR)/output
TMPDIR=/tmp/MindBending-pt
NGINXDIR=/var/www/MindBending
# }}}

# Configs setup {{{
CONFFILE=$(BASEDIR)/.conf/pelicanconf.py
NGINXCONF=$(BASEDIR)/.conf/pelicannginx.py
RELATIVECONF=$(BASEDIR)/.conf/pelicanrelative.py
# }}}

# Listing files {{{
PNG_FILES=$(shell find . -name "*.png")
JPG_FILES=$(shell find . -name "*.jpg")
# }}}

# Flags {{{
DEBUG ?= 0
ifeq ($(DEBUG), 1)
	PELICANOPTS += -D
endif

VERB ?= 0
ifeq ($(VERB), 1)
	PELICANOPTS += -v
endif
# }}}

help:
	@echo 'Makefile for a pelican Web site                                                   '
	@echo '                                                                                  '
	@echo 'Usage:                                                                            '
	@echo '   make html                        (re)generate the web site                     '
	@echo '   make clean                       remove the generated files                    '
	@echo '   make regenerate                  regenerate files upon modification            '
	@echo '   make serve [PORT=8000]           serve site at http://localhost:8000           '
	@echo '   make devserver [PORT=8000]       start/restart develop_server.sh               '
	@echo '   make stopserver                  stop local server                             '
	@echo '   make relative                    build with relative paths (open with browser) '
	@echo '   make nginx                       build with settings for NGINX                 '
	@echo '   make "image_path"                optimize image (PNG or JPG)                   '
	@echo '      ex: make pt/images/java/integracao-vim-make.png                             '
	@echo '                                                                                  '
	@echo 'Set the DEBUG variable to 1 to enable debugging, e.g. make DEBUG=1 html           '
	@echo 'Set the VERB variable to 1 to enable vebosing, e.g. make VERB=1 html              '
	@echo '                                                                                  '

html:
	. $(VENV); $(PELICAN) $(INPUTDIR) -o $(OUTPUTDIR) -s $(CONFFILE) $(PELICANOPTS)

relative:
	. $(VENV); $(PELICAN) $(INPUTDIR) -o $(OUTPUTDIR) -s $(RELATIVECONF) $(PELICANOPTS)

clean:
	[ ! -d $(OUTPUTDIR) ] || rm -rf $(OUTPUTDIR)/*
	[ ! -d $(TMPDIR) ] || rm -rf $(TMPDIR)/*

clean-nginx:
	[ ! -d $(NGINXDIR) ] || rm -rf $(NGINXDIR)/*

regenerate:
	. $(VENV); $(PELICAN) -r $(INPUTDIR) -o $(OUTPUTDIR) -s $(CONFFILE) $(PELICANOPTS)

serve:
ifdef PORT
	. $(VENV); cd $(OUTPUTDIR) && $(PY) -m pelican.server $(PORT)
else
	. $(VENV); cd $(OUTPUTDIR) && $(PY) -m pelican.server
endif

devserver:
ifdef PORT
	$(BASEDIR)/develop_server.sh restart $(PORT)
else
	$(BASEDIR)/develop_server.sh restart
endif

stopserver:
	kill -9 `cat pelican.pid`
	kill -9 `cat srv.pid`
	@echo 'Stopped Pelican and SimpleHTTPServer processes running in background.'

nginx:
	. $(VENV); $(PELICAN) $(INPUTDIR) -o $(TMPDIR) -s $(NGINXCONF) $(PELICANOPTS)
	rm -rf $(NGINXDIR)/*
	cp -r $(TMPDIR)/* $(NGINXDIR)/

$(PNG_FILES):
	optipng -o7 -quiet $@ -out $@

$(JPG_FILES):
	jpegtran -copy none -progressive -outfile $@ $@

.PHONY: help html relative clean clean-nginx regenerate serve devserver stopserver nginx $(PNG_FILES) $(JPG_FILES)
