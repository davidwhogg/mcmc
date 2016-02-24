#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import division, print_function

from plot_setup import SQUARE_FIGSIZE, COLORS

import numpy as np
import matplotlib.pyplot as pl

np.random.seed(42)


def compute_stats(K, a=0.0, b=1.0):
    a, b = sorted((a, b))
    x = np.random.uniform(a, b, size=K)

    # Analytic results:
    p = 1. / (b - a)
    a_mu = 0.5 * p * (b**2 - a**2)
    a_var = p * ((b - a_mu)**3 - (a - a_mu)**3) / 3.
    a_skew = 0.25 * p * ((b-a_mu)**4-(a-a_mu)**4) / a_var**(3./2)
    a_kurt = p * ((b-a_mu)**5-(a-a_mu)**5) / a_var**2 / 5.0

    # Sample estimates of stats:
    s_mu = np.mean(x)
    s_var = np.var(x)
    s_skew = np.mean((x - s_mu)**3) / s_var**(3./2)
    s_kurt = np.mean((x - s_mu)**4) / s_var**2

    return (
        (a_mu, a_var, a_skew, a_kurt),
        (s_mu, s_var, s_skew, s_kurt),
    )


K = 4**np.arange(1, 11)
a_stats, s_stats = map(np.array, zip(*(compute_stats(k) for k in K)))

fig, axes = pl.subplots(2, 2, sharex=True, figsize=2*SQUARE_FIGSIZE)

for i, (ax, title) in enumerate(zip(
        axes.flat, ("mean", "variance", "skewness", "kurtosis"))):
    mu = a_stats[0, i]
    ax.axhline(mu, color=COLORS["DATA"])
    ax.plot(np.log2(K), s_stats[:, i], "-o", color=COLORS["MODEL_1"], ms=3)
    d = np.max(np.abs(np.array(ax.get_ylim()) - mu))
    ax.set_ylim(mu + d * np.array([-1, 1]))
    ax.set_ylabel(title)

[ax.set_xlabel(r"$\log_2 K$") for ax in axes[1]]

fig.savefig("p1.pdf")
