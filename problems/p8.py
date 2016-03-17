#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import division, print_function

import numpy as np
import matplotlib.pyplot as pl

from plot_setup import SQUARE_FIGSIZE, COLORS

from p7 import chain


def acor_function_naive(x):
    xmu = x - np.mean(x)
    var = np.mean(xmu**2)
    f = np.array([var] + [np.mean(xmu[:-delta] * xmu[delta:])
                          for delta in range(1, len(x))]) / var
    return f


def acor_function_fft(x):
    n = len(x)
    f = np.fft.fft(x-np.mean(x), n=2*n)
    acf = np.fft.ifft(f * np.conjugate(f))[:n].real
    return acf / acf[0]


if __name__ == "__main__":
    fig, ax = pl.subplots(1, 1, figsize=SQUARE_FIGSIZE)

    acf1 = acor_function_naive(chain)
    acf2 = acor_function_fft(chain)

    ax.plot(acf1[:60])
    ax.plot(acf2[:60])
    ax.set_xlim(0, 60)
    ax.set_ylabel("$C_x(\Delta)$")
    ax.set_xlabel("$\Delta$")

    fig.savefig("p8.pdf")
