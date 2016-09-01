#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import division, print_function

import numpy as np
import matplotlib.pyplot as pl
from scipy.optimize import minimize

from plot_setup import setup, SQUARE_FIGSIZE, COLORS, savefig

setup()  # initialize the plotting styles
np.random.seed(42)


def log_p(x, mean=2.0, variance=2.0):
    return -0.5 * (x - mean)**2 / variance - 0.5*np.log(2*np.pi*variance)


neg_log_p = lambda x: -log_p(x)
r = minimize(neg_log_p, [1e3])

x = r.x[0]
lp = log_p(x)
chain = np.empty(6000)
for step in range(len(chain)):
    x_prime = x + np.random.randn()
    lp_prime = log_p(x_prime)
    if np.random.rand() <= np.exp(lp_prime - lp):
        x = x_prime
        lp = lp_prime
    chain[step] = x


fig, ax = pl.subplots(1, 1, figsize=SQUARE_FIGSIZE)
ax.plot(chain, color=COLORS["DATA"])
ax.xaxis.set_major_locator(pl.MaxNLocator(4))
ax.yaxis.set_major_locator(pl.MaxNLocator(4))
ax.set_xlabel("step")
ax.set_ylabel("$x$")

savefig(fig, "optimization.pdf")
