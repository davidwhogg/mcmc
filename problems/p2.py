#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import division, print_function

from plot_setup import SQUARE_FIGSIZE, COLORS

import numpy as np
import matplotlib.pyplot as pl

np.random.seed(42)


def log_p(x):
    return -0.5 * (x - 2)**2 / 2.0  # Mean = 2, Variance = 2


x = 0.0
lp = log_p(x)
chain = np.empty(2e4)
for step in range(len(chain)):
    x_prime = x + np.random.randn()
    lp_prime = log_p(x_prime)
    if np.random.rand() < np.exp(lp_prime - lp):
        x = x_prime
        lp = lp_prime
    chain[step] = x


