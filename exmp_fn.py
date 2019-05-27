"""
    Collection of test functions in Numerical Analysis I/II
    @instructor: Xiaojing Ye
"""

import numpy as np


#### Example 5 number 1a 5.6





def exmp1_def_fn(tau, w):
    # defining function f of example 1: y' = f(t,y)
    return (w/tau)-(w/tau)**2

def exmp1_sol(t):
    # real solution of IVP in example 1: y' = f(t,y) with IV y0 on t
    return (t)/(1+np.log(t))








"""
def exmp1_def_fn(tau,w):
    # defining function f of example 1: y' = f(t,y)
    return (tau*np.exp(3*tau))-2*w
#(tau*np.exp(3*tau))
def exmp1_sol(t):
    # real solution of IVP in example 1: y' = f(t,y) with IV y0 on t
    return (t*np.exp(3*t))/(5)-(np.exp(3*t))/(25)+(np.exp(-2*t))/(25)
"""
















""" ================================================================
    Example 1: IVP of ODE y' = y - t^2 + 1
                with initial value y(0) = 0.5
                Exact solution is y(t) = (t+1)^2 - exp(t)/2
"""

def exmp2_def_fn(tau, w):
    # defining function f of example 1: y' = f(t,y)
   return w - tau**2 + 1.0

def exmp2_sol(t):
    # real solution of IVP in example 1: y' = f(t,y) with IV y0 on t
    return (t+1.0)**2 - np.exp(t)/2.0




""" ================================================================
    Example 2: IVP of ODE y' = 1/t^2 - y/t - y^2
                with initial value y(1) = -1
                Exact solution is y(t) = -1/t
    Exercise 5.3 No.10 on page 282 (Burden 9th edtn)
"""

def exmp3_def_fn(tau, w):
    # defining function f of example 1: y' = f(t,y)
    return 1.0/(tau**2) - w/tau - w**2

def exmp3_sol(t):
    # real solution of IVP in example 1: y' = f(t,y) with IV y0 on t
    return -1.0/t