#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import division, print_function

import corner
import numpy as np

from twod_a import run_mcmc
from plot_setup import setup, savefig

setup()  # initialize the plotting styles
np.random.seed(42)


def log_p_uniform(x):
    if 3 <= x[0] <= 7 and 1 <= x[1] <= 9:
        return 0.0
    return -np.inf


chain, _ = run_mcmc(log_p_uniform, np.array([5.0, 5.0]), nsteps=1e5)
fig = corner.corner(chain, labels=["$x$", "$y$"],
                    range=[(2.5, 7.5), (0.5, 9.5)],
                    plot_density=False, plot_contours=False)
savefig(fig, "twod_b.pdf", dpi=300)
