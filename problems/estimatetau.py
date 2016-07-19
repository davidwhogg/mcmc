#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import division, print_function

import numpy as np
import matplotlib.pyplot as pl

from plot_setup import SQUARE_FIGSIZE, savefig

from convergence import chain


def autocorr_function(x):
    n = len(x)
    f = np.fft.fft(x - np.mean(x), n=2*n)
    acf = np.fft.ifft(f * np.conjugate(f))[:n].real
    return acf / acf[0]


if __name__ == "__main__":
    fig, ax = pl.subplots(1, 1, figsize=SQUARE_FIGSIZE)

    acf = autocorr_function(chain)

    ax.plot(acf[:61])
    ax.set_xlim(0, 60)
    ax.set_ylabel("$C_x(\Delta)$")
    ax.set_xlabel("$\Delta$")

    savefig(fig, "estimatetau.pdf")
