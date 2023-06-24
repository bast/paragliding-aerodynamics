import numpy as np
from scipy.optimize import curve_fit


# this is the function we want to fit
def func(x, a, b, c):
    return a * x * x + b * x + c


def fit(xs, ys):
    # non-linear least squares to fit func to data
    p_opt, p_cov = curve_fit(func, xs, ys)

    # these are the fitted values a, b, c
    a, b, c = p_opt

    # produce 100 values in the range we want to cover along x
    xs_fit = np.linspace(min(xs), max(xs), 100)

    # compute fitted y values
    ys_fit = [func(x, a, b, c) for x in xs_fit]

    return xs_fit, ys_fit
