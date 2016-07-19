ALL_FILES=simple_stats.pdf MH.pdf MH2.pdf twod_a.pdf twod_b.pdf prop_mean.pdf \
		  p6.pdf p7.pdf p8.pdf \
		  p9.pdf p10.pdf p11.pdf

default: $(ALL_FILES)

%.pdf: %.py
	python -W ignore $<

clean:
	rm -f $(ALL_FILES)
