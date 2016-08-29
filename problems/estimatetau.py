#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import division, print_function

import numpy as np
import matplotlib.pyplot as pl

from plot_setup import SQUARE_FIGSIZE, savefig

from convergence import chain


# This method is really very slow! Probably best to just avoid calling it.
def autocorr_function_naive(x):
    print("Warning: running naive autocorrelation function method. "
          "This will be slow!")
    mu = np.mean(x)
    r = x - mu
    C = np.empty(len(r) // 2)
    for i in range(1, len(C)):
        C[i] = np.mean(r[i:] * r[:-i])
    C /= np.mean(r ** 2)
    C[0] = 1.0
    return C


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
