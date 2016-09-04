include Makefile.inc

# Enter the name(s) of the .tex file(s) that you want to compile.
TEX_FILES = mcmc
DIRS      = problems

# You shouldn't need to edit below here.
default: mcmc.pdf

.PHONY: problems

problems: force_look
	$(foreach d, ${DIRS}, (echo "Looking into ${d}:"; cd ${d}; ${MAKE} ${MFLAGS}) )

mcmc.pdf: mcmc.tex problems
	${LATEX} mcmc.tex
	( ${CHECK_RERUN} && ${LATEX} mcmc.tex ) || echo "Done."
	( ${CHECK_RERUN} && ${LATEX} mcmc.tex ) || echo "Done."

# subdirs: force_look
# 	$(foreach d, ${DIRS}, (echo "Looking into ${d}:"; cd ${d}; ${MAKE} ${MFLAGS}) )

force_look:
	true

clean:
	$(RM_TMP)
	$(foreach d, ${DIRS}, (echo "Cleaning ${d}:"; cd ${d}; $(MAKE) clean) )
