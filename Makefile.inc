.SUFFIXES:
.SUFFIXES: .pdf .tex

LATEX       = pdflatex -interaction=nonstopmode -halt-on-error
RM          = rm -rf

TMP_SUFFS   = pdf aux bbl blg log dvi ps eps out ent
SUFF        = pdf

RM_TMP      = $(foreach d, ${TEX_FILES}, ${RM} $(foreach suff, ${TMP_SUFFS}, ${d}.${suff}))
CHECK_RERUN = grep Rerun $*.log

DOCS        = $(foreach f, ${TEX_FILES}, ${f}.${SUFF})
