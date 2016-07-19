#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import division, print_function

import numpy as np
import matplotlib.pyplot as pl
from plot_setup import setup, SQUARE_FIGSIZE, COLORS, savefig

from itertau import autocorr_function, autocorr_time_iterative
from tuning import log_p_gauss, run_mcmc, sigs

setup()  # initialize the plotting styles
np.random.seed(42)


taus = np.empty((len(sigs), 2))
for i, sig in enumerate(sigs):
    chain, acc = run_mcmc(log_p_gauss, np.array([0.0, 0.0]), prop_sigma=sig,
                          nsteps=2e5)
    for j in range(2):
        acf = autocorr_function(chain[:, j])
        taus[i, j] = autocorr_time_iterative(acf)
    print(sig, acc, taus[i])

fig, ax = pl.subplots(1, 1, figsize=SQUARE_FIGSIZE)
ax.plot(sigs, taus[:, 0], ".-", color=COLORS["MODEL_1"])
ax.plot(sigs, taus[:, 1], ".-", color=COLORS["MODEL_2"])
ax.set_xscale("log")
ax.set_xlabel(r"$\sigma_q$")
ax.set_ylabel(r"$\tau_x$")
ax.set_xlim(0.2, 40)
ax.set_ylim(0, 450)
ax.yaxis.set_major_locator(pl.MaxNLocator(5))
savefig(fig, "tuningtau.pdf")
