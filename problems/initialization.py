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

inits = np.linspace(0.0, 3.5, 8)
times = np.empty_like(inits)
for ix, x in enumerate(10**inits):
    x = 2.0 + x * np.sqrt(2)
    lp = log_p(x)
    for step in range(int(1e5)):
        x_prime = x + np.random.randn()
        lp_prime = log_p(x_prime)
        if np.random.rand() <= np.exp(lp_prime - lp):
            x = x_prime
            lp = lp_prime
        if np.abs(x - 2.0) < 0.5 * np.sqrt(2.0):
            times[ix] = step
            print(ix, inits[ix], times[ix])
            break


fig, ax = pl.subplots(1, 1, figsize=SQUARE_FIGSIZE)
ax.loglog(inits, times, ".-", color=COLORS["DATA"])
ax.set_xlabel("$\Delta$ initialization; [$\\times \sigma$]")
ax.set_ylabel("approx.\ number of burn-in steps")

savefig(fig, "initialization.pdf")
