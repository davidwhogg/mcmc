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

inits = 10**np.linspace(-5.0, 3.0, 5)
times = np.empty_like(inits)
for ix, x in enumerate(10**np.linspace(-5.0, 3.0, 5)):
    x += 4.0
    lp = log_p(x)
    for step in range(int(1e5)):
        x_prime = x + np.random.randn()
        lp_prime = log_p(x_prime)
        if np.random.rand() <= np.exp(lp_prime - lp):
            x = x_prime
            lp = lp_prime
        if np.abs(x - 2.0) < np.sqrt(2.0):
            times[ix] = step
            print(ix, inits[ix], times[ix])
            break


fig, ax = pl.subplots(1, 1, figsize=SQUARE_FIGSIZE)
ax.plot(inits, times, color=COLORS["DATA"])
# ax.xaxis.set_major_locator(pl.MaxNLocator(4))
# ax.yaxis.set_major_locator(pl.MaxNLocator(4))
# ax.set_xlabel("step")
# ax.set_ylabel("$x$")

# savefig(fig, "initialization.pdf")
