#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import division, print_function

import numpy as np
import matplotlib.pyplot as pl

from plot_setup import setup, SQUARE_FIGSIZE, COLORS, savefig

setup()  # initialize the plotting styles
np.random.seed(42)


def log_p(x, mean=2.0, variance=2.0):
    return -0.5 * (x - mean)**2 / variance - 0.5*np.log(2*np.pi*variance)


x = 0.0
lp = log_p(x)
chain = np.empty(int(2e4))
for step in range(len(chain)):
    x_prime = x + np.random.randn()
    lp_prime = log_p(x_prime)
    if np.random.rand() <= np.exp(lp_prime - lp):
        x = x_prime
        lp = lp_prime
    chain[step] = x


fig, ax = pl.subplots(1, 1, figsize=SQUARE_FIGSIZE)
ax.hist(chain, 100, histtype="step", color=COLORS["DATA"], normed=True)
x = 2 + np.linspace(-4.5, 4.5, 5000)
ax.plot(x, np.exp(log_p(x)), color=COLORS["MODEL_1"])
ax.set_xlim(x.min(), x.max())
ax.yaxis.set_major_locator(pl.MaxNLocator(4))
ax.set_xlabel("$x$")
ax.set_ylabel("$p(x)$")

savefig(fig, "MH.pdf")
