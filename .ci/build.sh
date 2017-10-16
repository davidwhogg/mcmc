#!/bin/bash -x

# Do the problems
cd problems
make
cd ..

# Set up tectonic & build
conda install -c conda-forge -c pkgw-forge tectonic
tectonic --help
tectonic mcmc.tex
