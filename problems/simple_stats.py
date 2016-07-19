#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import division, print_function


import numpy as np
import matplotlib.pyplot as pl
from plot_setup import setup, SQUARE_FIGSIZE, COLORS, savefig

setup()  # initialize the plotting styles

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

shape = np.array([2, 1.5])*SQUARE_FIGSIZE
fig, axes = pl.subplots(2, 2, sharex=True, figsize=shape)

for i, (ax, title) in enumerate(zip(
        axes.flat, ("mean", "variance", "skewness", "kurtosis"))):
    mu = a_stats[0, i]
    ax.axhline(mu, color=COLORS["DATA"])
    ax.plot(np.log2(K), s_stats[:, i], "-o", color=COLORS["MODEL_1"], ms=3)
    d = np.max(np.abs(np.array(ax.get_ylim()) - mu))
    ax.set_ylim(mu + d * np.array([-1, 1]))
    ax.set_ylabel(title)
    ax.yaxis.set_label_coords(-0.3, 0.5)
    ax.yaxis.set_major_locator(pl.MaxNLocator(5))
    ax.xaxis.set_major_locator(pl.MaxNLocator(6))

[ax.set_xlabel(r"$\log_2 K$") for ax in axes[1]]

savefig(fig, "simple_stats.pdf")
