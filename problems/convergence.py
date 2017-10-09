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
chain = np.empty(int(1e6))
for step in range(len(chain)):
    x_prime = x + np.random.randn()
    lp_prime = log_p(x_prime)
    if np.random.rand() <= np.exp(lp_prime - lp):
        x = x_prime
        lp = lp_prime
    chain[step] = x


if __name__ == "__main__":
    s = SQUARE_FIGSIZE
    s[0] *= 2
    fig, (ax1, ax2) = pl.subplots(1, 2, figsize=s)

    ax1.plot(np.arange(len(chain))/1e3, chain, color=COLORS["DATA"],
             rasterized=True)
    ax1.set_xlim(0, len(chain) / 1e3)
    ax1.set_ylim(2-5.5, 2+5.5)
    ax1.set_ylabel("$x$")
    ax1.set_xlabel("thousands of steps")

    for i in range(4):
        a = int(i*len(chain)/4)
        b = int((i+1)*len(chain)/4)
        print(i+1, np.mean(chain[a:b]), np.var(chain[a:b]))
        ax2.hist(chain[a:b], 50, histtype="step")
    ax2.set_xlim(2-5.5, 2+5.5)
    ax2.set_yticklabels([])
    ax2.set_ylabel("$p(x)$")
    ax2.set_xlabel("$x$")

    savefig(fig, "convergence.pdf", dpi=300)
