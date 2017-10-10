#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import division, print_function

import numpy as np
import matplotlib.pyplot as pl

from plot_setup import setup, SQUARE_FIGSIZE, COLORS, savefig

setup()  # initialize the plotting styles
np.random.seed(42)


x = 0.0
chain = np.empty(int(1e6))
for step in range(len(chain)):
    x += np.random.randn()
    chain[step] = x

# Thin the chain for plotting purposes.
chain = chain[::1000]
mn, mx = np.min(chain), np.max(chain)
mid = 0.5 * (mn + mx)
rng = 0.5 * (mx - mn) * 1.1

fig, ax = pl.subplots(1, 1, figsize=SQUARE_FIGSIZE)
ax.plot(np.arange(len(chain)) * 1e-2, chain, color=COLORS["DATA"])
ax.yaxis.set_major_locator(pl.MaxNLocator(5))
ax.set_xlabel("mcmc step [$\\times 10^5$]")
ax.set_ylabel("$x$")
ax.set_ylim(mid-rng, mid+rng)

savefig(fig, "improper.pdf")
