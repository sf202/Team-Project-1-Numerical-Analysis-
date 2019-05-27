"""
    Several example functions appeared in Numerical Analysis I/II
    @instructor: Xiaojing Ye, Math & Stat, Georgia State University
"""

# import commonly used packages
import numpy as np


# ==============================
# Euler's method
def euler(def_fn, a, b, ya, N):
    
    """
        Test the Euler's method to solve
        initial value problem y'=f(t,y) with t in [a,b] and y(a) = ya.
        Step size h is computed according to input number of mesh points N
    """
    
    f = def_fn  # call the input defining function as f
    
    h = (b-a)/N # step size
    
    t = np.arange(a, b+h, h)    # all mesh points t=(t_0, t_1, ..., t_N)
    y = np.zeros((N+1,1))   # Euler approximations at mesh points
    y[0] = ya    # set initial value y(t_0) = ya
    
    # main iterations
    for i in range(0, N):
        
        tau = t[i]  # current mesh point t
        w = y[i]    # current value y(t)
        
        # compute y at next time point t using Euler's method
        y[i+1] = y[i] + h * f(tau, w)
    
    return (t, y)