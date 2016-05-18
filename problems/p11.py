#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import division, print_function

import numpy as np
import matplotlib.pyplot as pl
from plot_setup import setup, SQUARE_FIGSIZE, COLORS

from p9 import autocorr_time_iterative

setup()  # initialize the plotting styles
np.random.seed(42)


def log_p_gauss(x):
    V = np.array([[2.0, 1.2], [1.2, 2.0]])
    alpha = np.linalg.solve(V, x)
    return -0.5 * np.dot(x, alpha)


def run_mcmc(log_p, x, prop_sigma=1.0, nsteps=1e5):
    lp = log_p(x)
    chain = np.empty((nsteps, len(x)))
    acc = 0
    for step in range(len(chain)):
        x_prime = np.array(x)
        x_prime[np.random.randint(len(x))] += prop_sigma * np.random.randn()
        lp_prime = log_p(x_prime)
        if np.random.rand() <= np.exp(lp_prime - lp):
            acc += 1
            x[:] = x_prime
            lp = lp_prime
        chain[step] = x
    return chain, acc / len(chain)


sigs = 2.0 ** np.arange(-2, 5)
taus = np.empty((len(sigs), 2))
for i, sig in enumerate(sigs):
    chain, _ = run_mcmc(log_p_gauss, np.array([0.0, 0.0]), prop_sigma=sig)
    taus[i, 0] = autocorr_time_iterative(chain[:, 0])
    taus[i, 1] = autocorr_time_iterative(chain[:, 1])
    print(taus[i])

fig, ax = pl.subplots(1, 1, figsize=SQUARE_FIGSIZE)
ax.plot(sigs, taus[:, 0], ".-", color=COLORS["MODEL_1"])
ax.plot(sigs, taus[:, 1], ".-", color=COLORS["MODEL_2"])
ax.set_xscale("log")
ax.set_xlabel(r"$\sigma_q$")
ax.set_ylabel(r"$\tau_x$")
ax.set_xlim(0.2, 20)
fig.savefig("p11.pdf")
