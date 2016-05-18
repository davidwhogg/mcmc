# -*- coding: utf-8 -*-

from __future__ import division, print_function

import numpy as np
from cycler import cycler
from matplotlib import rcParams

__all__ = ["COLORS", "SQUARE_FIGSIZE", "setup"]

COLORS = dict(
    DATA="k",
    MODEL_1="#1f77b4",
    MODEL_2="#ff7f0e",
)

SQUARE_FIGSIZE = np.array((4, 4))


def setup():
    rcParams["agg.path.chunksize"] = 10000  # huh?
    rcParams["font.size"] = 16
    rcParams["font.family"] = "sans-serif"
    rcParams["font.sans-serif"] = ["Computer Modern Sans"]
    # rcParams["font.family"] = "serif"
    # rcParams["font.serif"] = ["Computer Modern Roman"]
    rcParams["text.usetex"] = True
    rcParams["text.latex.preamble"] = r"\usepackage{cmbright}"
    rcParams["figure.autolayout"] = True
    rcParams["axes.prop_cycle"] = cycler("color", (
        "#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#9467bd", "#8c564b",
        "#e377c2", "#7f7f7f", "#bcbd22", "#17becf",
    ))  # d3.js color cycle


def savefig(fig, fn, **kwargs):
    kwargs["bbox_inches"] = "tight"
    fig.savefig(fn, **kwargs)
