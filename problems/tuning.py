#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import division, print_function

import numpy as np
import matplotlib.pyplot as pl
from plot_setup import setup, SQUARE_FIGSIZE, COLORS, savefig

from twod_a import log_p_gauss, run_mcmc

setup()  # initialize the plotting styles
np.random.seed(42)


sigs = 2.0 ** np.arange(-2, 6)

if __name__ == "__main__":
    acc_fracs = np.empty_like(sigs)
    for i, sig in enumerate(sigs):
        _, acc_fracs[i] = run_mcmc(log_p_gauss, np.array([0.0, 0.0]),
                                   prop_sigma=sig)

    fig, ax = pl.subplots(1, 1, figsize=SQUARE_FIGSIZE)
    ax.axhline(0.25, color=COLORS["DATA"])
    ax.plot(sigs, acc_fracs, ".-", color=COLORS["MODEL_2"])
    ax.set_xscale("log")
    ax.set_xlabel(r"$\sigma_q$")
    ax.set_ylabel("acceptance fraction")
    ax.set_xlim(0.2, 40)
    savefig(fig, "tuning.pdf")
