include Makefile.inc

# Enter the name(s) of the .tex file(s) that you want to compile.
TEX_FILES = mcmc
DIRS      =

# You shouldn't need to edit below here.
default: subdirs ${DOCS}

.tex.pdf:
	${LATEX} $*.tex
	( ${CHECK_RERUN} && ${LATEX} $*.tex ) || echo "Done."
	( ${CHECK_RERUN} && ${LATEX} $*.tex ) || echo "Done."

subdirs: force_look
	$(foreach d, ${DIRS}, (echo "Looking into ${d}:"; cd ${d}; ${MAKE} ${MFLAGS}) )

force_look:
	true

clean:
	$(RM_TMP)
	$(foreach d, ${DIRS}, (echo "Cleaning ${d}:"; cd ${d}; $(MAKE) clean) )
