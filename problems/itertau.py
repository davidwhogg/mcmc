#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import division, print_function

import numpy as np
import matplotlib.pyplot as pl

from plot_setup import SQUARE_FIGSIZE, COLORS, savefig

from estimatetau import autocorr_function


def autocorr_time_simple(acf, window):
    return 1 + 2 * np.sum(acf[1:window])


def autocorr_time_iterative(acf, c=10, low=10):
    high = int(len(acf) / c)
    for M in np.arange(low, high).astype(int):
        tau = autocorr_time_simple(acf, M)
        if tau > 1.0 and M > c * tau:
            return tau
    raise RuntimeError("chain too short to estimate tau reliably")


if __name__ == "__main__":
    from estimatetau import chain

    m = len(chain)
    N = 2 ** np.arange(2, 19)

    fig, ax = pl.subplots(1, 1, figsize=SQUARE_FIGSIZE)

    for s in [slice(0, m//2), slice(m//4, 3*m//4), slice(m//2, m),
              slice(None)]:
        acf = autocorr_function(chain[s])
        taus = np.array([autocorr_time_simple(acf, n) for n in N])
        tau = autocorr_time_iterative(acf)
        ax.plot(N, taus, "-", color=COLORS["DATA"])
        print("tau: {0}".format(tau))

    ax.plot(N, taus, ".-", color=COLORS["MODEL_2"])
    ax.axhline(tau, color=COLORS["MODEL_2"], ls="dashed")

    ax.set_title(r"$\tau_x = {0:.2f}$".format(tau))
    ax.set_ylim(0, 25)
    ax.set_xlim(2, 5e5)
    ax.set_xscale("log")
    ax.set_ylabel(r"$\tau_x$")
    ax.set_xlabel("window size")

    savefig(fig, "itertau.pdf")
