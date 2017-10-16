#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import division, print_function

import emcee
import corner
import numpy as np
import matplotlib.pyplot as pl

from plot_setup import setup, SQUARE_FIGSIZE, COLORS, savefig

setup()  # initialize the plotting styles
np.random.seed(42)


def log_p(x):
    return -(100.0*(x[1]-x[0]**2)**2 + (1-x[0])**2) / 20.0


coords = 1.0 + 1e-5*np.random.randn(32, 2)
nwalkers, ndim = coords.shape
sampler = emcee.EnsembleSampler(nwalkers, ndim, log_p)
coords, _, _ = sampler.run_mcmc(coords, 10000, progress=True)
sampler.reset()
sampler.run_mcmc(coords, 250000, progress=True)

samples = sampler.get_chain(thin=25*32, flat=True)

fig = corner.corner(samples, 50,
                    range=[(-10.2, 10.2), (-5.0, 55.0)],
                    labels=[r"$\theta_1$", r"$\theta_2$"],
                    truths=np.mean(samples, axis=0),
                    quantiles=[0.16, 0.5, 0.84])
savefig(fig, "rosenbrock2.pdf")
