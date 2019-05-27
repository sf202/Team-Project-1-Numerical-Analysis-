"""
    Project I Numerical Analysis II
    By Cristian Cardona
    Group Santiago, Chris, Cristian.
    @instructor: Xiaojing Ye, Math & Stat, Georgia State University
"""

# import commonly used package
import numpy as np

# ======================================
# Modified Euler Method

def modified(def_fn, a, b, ya, N):


    """
        Test the Midpoint Method to solve
        initial value problem y'=f(t,y) with t in [a,b] and y(a) = ya.
        Step size h is computed according to input number of mesh points N
    """
    f = def_fn

    h = (b - a) / N  # step size

    t = np.arange(a, b + h, h)  # all mesh points t=(t_0, t_1, ..., t_N)

    y = np.zeros((N + 1, 1))  # Approximations at mesh points

    y[0] = ya  # set initial value y(t_0) = ya
     # Main code

    for i in range(0, N):
        tau = t[i]  # current mesh point t
        w = y[i]  # current value y(t)


        tau2 = t[i+1]
        # compute y at next time point t using Modified Euler
        y[i + 1] = y[i] + (h/2) *(f(tau, w) + f(tau2, w + h *f(tau, w)))


    return (t,y)