#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import division, print_function

import numpy as np
import matplotlib.pyplot as pl

from plot_setup import setup, SQUARE_FIGSIZE, COLORS, savefig

setup()  # initialize the plotting styles
np.random.seed(42)


def log_p(x, a=3.0, b=7.0):
    if a <= x <= b:
        return -np.log(b-a)
    return -np.inf


x = 5.0
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
ax.axhline(0.0, color="k")
ax.hist(chain, 50, histtype="step", color=COLORS["DATA"], normed=True)
x = np.linspace(2.5, 7.5, 5000)
y = np.exp([log_p(_) for _ in x])
ax.plot(x, y, color=COLORS["MODEL_1"])
ax.set_xlim(x.min(), x.max())
ax.set_ylim(-0.01, y.max() + 0.05)
ax.set_xlabel("$x$")
ax.set_ylabel("$p(x)$")

savefig(fig, "MH2.pdf")
