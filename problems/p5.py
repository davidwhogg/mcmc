#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import division, print_function

import numpy as np
import matplotlib.pyplot as pl

from p4 import run_mcmc, log_p_gauss
from plot_setup import setup, COLORS, SQUARE_FIGSIZE

setup()  # initialize the plotting styles
np.random.seed(42)


x0 = [-4.0, 5.0]

s = SQUARE_FIGSIZE
s[0] *= 3
fig, axes = pl.subplots(1, 3, sharex=True, sharey=True, figsize=s)
for n, ax in zip([0.0, -1.0, 2.0], axes):
    chain = run_mcmc(log_p_gauss, np.array(x0), nsteps=2e3, prop_sigma=10**n)
    ax.plot(chain[:, 0], chain[:, 1], "o-", color=COLORS["DATA"], ms=2)
    ax.plot(x0[0], x0[1], "o", color=COLORS["MODEL_1"])
    ax.set_xlim(-6.3, 6.3)
    ax.set_ylim(-6.3, 6.3)
    ax.set_xlabel("$x$")
    ax.annotate(r"$\sigma_q = 10^{{{0:.0f}}}$".format(n),
                (1, 0), xycoords="axes fraction",
                xytext=(-5, 5), textcoords="offset points",
                ha="right", va="bottom")

axes[0].set_ylabel("$y$")

fig.savefig("p5.pdf")
