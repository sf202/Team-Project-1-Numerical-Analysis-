"""
    Project I Numerical Analysis II
    By Cristian Cardona
    Group Santiago, Chris, Cristian.
    @instructor: Xiaojing Ye, Math & Stat, Georgia State University
"""

# import commonly used package
import numpy as np

import exmp_fn  # import a collection of example functions from textbook

# ======================================
# Modified Euler Method

def Moulton(def_fn, a, b, ya, N):

    
    # defining function and true solution of an example function
    sol = exmp_fn.exmp3_sol

    """
        Test the Runge Kutta 4th Order to solve
        initial value problem y'=f(t,y) with t in [a,b] and y(a) = ya.
        Step size h is computed according to input number of mesh points N
    """
    f = def_fn

    h = (b - a) / N  # step size

    t = np.arange(a, b + h, h)  # all mesh points t=(t_0, t_1, ..., t_N)

    y = np.zeros((N + 1, 1))  # Approximations at mesh points
    

    
    y[0] = ya  # set initial value y(t_0) = ya
     # Main code
     
     # compute exact solution for comparison
    z = sol(t)
    
    y[1] = z[1]
    y[2]=  z[2]

    
# 0 -9
    m =0

    for i in range(2, N):
        tauZ = t[m]  # current mesh point t i =0 
        tauOne = t[m+1]
        tauTwo = t[m+2]
        tauThree = t[m+3]
        
        wZero = y[m]  # current value y(t) actual value
        wOne = z[m+1]
        wTwo =z[m+2]
        wThree = z[m+3]  
        
        y[i+1] = wTwo + (h/24)*(9*f(tauThree,wThree)+19*f(tauTwo,wTwo)-
         5*f(tauOne,wOne)+f(tauZ,wZero))
         
        m = m +1
        
           
        
        
        # compute y at next time point t 
       # y[i + 1] = y[i] + (h/2) *(f(tau, w) + f(tau2, w + h *f(tau, w)))
           

    return (t,y)