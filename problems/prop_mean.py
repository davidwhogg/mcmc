#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import division, print_function

import numpy as np
import matplotlib.pyplot as pl

from twod_a import log_p_gauss
from plot_setup import setup, COLORS, SQUARE_FIGSIZE, savefig

setup()  # initialize the plotting styles
np.random.seed(42)


def run_broken_mcmc(log_p, x, prop_sigma=1.0, prop_mean=0.5, nsteps=2e3,
                    broken=True):
    lp = log_p(x)
    chain = np.empty((int(nsteps), len(x)))
    for step in range(len(chain)):
        x_prime = np.array(x)
        ind = np.random.randint(len(x))
        x_prime[ind] += prop_mean + prop_sigma * np.random.randn()
        lp_prime = log_p(x_prime)
        if broken:
            if np.random.rand() <= np.exp(lp_prime - lp):
                x[:] = x_prime
                lp = lp_prime
        else:
            r = lp_prime - lp
            delta = x[ind] - x_prime[ind]
            r += -0.5 * ((delta - 0.5)**2 - (delta + 0.5)**2)
            if np.random.rand() <= np.exp(r):
                x[:] = x_prime
                lp = lp_prime
        chain[step] = x
    return chain


x0 = [-4.0, 5.0]

s = SQUARE_FIGSIZE
s[0] *= 2
fig, axes = pl.subplots(1, 2, sharex=True, sharey=True, figsize=s)
for broken, ax in zip([True, False], axes):
    chain = run_broken_mcmc(log_p_gauss, np.array(x0), broken=broken)
    chain = np.concatenate(([x0], chain))
    ax.plot(chain[:, 0], chain[:, 1], "o-", color=COLORS["DATA"], ms=2)
    ax.plot(x0[0], x0[1], "o", color=COLORS["MODEL_1"])
    ax.set_xlim(-6.3, 6.3)
    ax.set_ylim(-6.3, 6.3)
    ax.set_xlabel("$x$")
    ax.annotate("incorrect acceptance" if broken else "corrected acceptance",
                (1, 0), xycoords="axes fraction",
                xytext=(-5, 5), textcoords="offset points",
                ha="right", va="bottom")

axes[0].set_ylabel("$y$")

savefig(fig, "prop_mean.pdf")
