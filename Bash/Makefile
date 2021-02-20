.POSIX:

PREFIX = /usr/local

all: install

tuxi:

install:
	mkdir -p ${DESTDIR}${PREFIX}/bin
	cp pygrater ${DESTDIR}${PREFIX}/bin/pygrater
	cp pygrater.py ${DESTDIR}${PREFIX}/bin/pygrater
	cp google_page_pull.py ${DESTDIR}${PREFIX}/bin/pygrater
	cp response_parser.py ${DESTDIR}${PREFIX}/bin/pygrater
	cp string_beautifier.py ${DESTDIR}${PREFIX}/bin/pygrater
uninstall:
	rm -f ${DESTDIR}${PREFIX}/bin/pygrater

.PHONY: all install uninstall