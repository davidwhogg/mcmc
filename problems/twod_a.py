#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import division, print_function

import corner
import numpy as np

from plot_setup import setup, savefig

setup()  # initialize the plotting styles
np.random.seed(42)


def log_p_gauss(x):
    V = np.array([[2.0, 1.2], [1.2, 2.0]])
    alpha = np.linalg.solve(V, x)
    return -0.5 * np.dot(x, alpha)


def run_mcmc(log_p, x, prop_sigma=1.0, nsteps=2e4, thin=1):
    lp = log_p(x)
    chain = np.empty((int(nsteps) // int(thin), len(x)))
    acc = 0
    for step in range(len(chain)):
        for i in range(thin):
            x_prime = np.array(x)
            x_prime[np.random.randint(len(x))] += prop_sigma*np.random.randn()
            lp_prime = log_p(x_prime)
            if np.random.rand() <= np.exp(lp_prime - lp):
                acc += 1
                x[:] = x_prime
                lp = lp_prime
            if i == thin - 1:
                chain[step] = x
    return chain, acc / (len(chain) * thin)


if __name__ == "__main__":
    chain, _ = run_mcmc(log_p_gauss, np.array([0.0, 0.0]))
    fig = corner.corner(chain, labels=["$x$", "$y$"],
                        range=[(-4.5, 4.5), (-4.5, 4.5)],
                        plot_density=False, plot_contours=False)
    savefig(fig, "twod_a.pdf", dpi=300)
