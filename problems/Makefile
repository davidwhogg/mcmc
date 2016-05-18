ALL_FILES=p1.pdf p2.pdf p3.pdf p4a.pdf p4b.pdf p5.pdf p6.pdf p7.pdf p8.pdf \
		  p9.pdf p10.pdf p11.pdf

default: $(ALL_FILES)

%.pdf: %.py
	python $<

clean:
	rm -f $(ALL_FILES)
