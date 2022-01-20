INPUT=slides.md
OUTPUT=slides.pdf
DEP=$(wildcard *.sty img/*.jpg img/*.png)
THEME=Custom

all: $(INPUT) $(DEP)
	pandoc -st beamer -V theme:$(THEME) -V lang:fr-FR $(INPUT) -o $(OUTPUT)

run: $(OUTPUT)
	code $(OUTPUT)

clean:
	rm -f $(OUTPUT)
