INPUT=rapport_premiere_annee_WA.tex
OUTPUT=rapport_premiere_annee_WA.pdf
DEP=$(wildcard preamble.tex img/.*png img/*.jpg sections/*.tex)

all: $(INPUT) $(DEP)
	pdflatex $(INPUT)

run: $(OUTPUT)
	open $(OUTPUT)

clean:
	rm -f *.aux *.bbl *.blg *.dvi *.fdb_latexmk *.fls *.log *.out *.toc *.synctex.gz *.ent