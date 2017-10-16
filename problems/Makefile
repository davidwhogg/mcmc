ALL_FILES=simple_stats.pdf MH.pdf MH2.pdf twod_a.pdf twod_b.pdf MH_sigma.pdf prop_mean.pdf \
		  improper.pdf logprior.pdf \
		  convergence.pdf estimatetau.pdf \
		  itertau.pdf tuning.pdf tuningtau.pdf \
		  initialization.pdf optimization.pdf rosenbrock2.pdf

default: $(ALL_FILES)

%.pdf: %.py
	python -W ignore $<

clean:
	rm -f $(ALL_FILES)
