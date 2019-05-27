"""
    Project I Numerical Analysis II
    By Cristian Cardona
    Group Santiago, Chris, Cristian.
    @instructor: Xiaojing Ye, Math & Stat, Georgia State University
"""

# import commonly used package
import numpy as np

# ======================================
# Predictor Corrector method

def Predictor(def_fn, a, b, ya, N):


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
     # 0-2 Gives you w1 w2, w3
    for i in range(0, 3):
        tau = t[i]  # current mesh point t
        w = y[i]  # current value y(t)
                
        kone = h*f(tau,w)
        ktwo = h*f(tau+h/2,w+kone/2)
        ktres= h*f(tau+h/2,w+ktwo/2)
        kfour= h*f(tau+h,w+ktres)
        
        y[i+1] = w + (kone+2*ktwo+2*ktres+kfour)/(6)
        
        
    
        
    
    m = 0
    for i in range(3,N) :
        wZ = y[m]
        wOne = y[m+1]
        wTwo = y[m+2]
        wThree = y[m+3] 
        
        tauZ = t[m]  # current mesh point t i =0 
        tauOne = t[m+1]
        tauTwo = t[m+2]
        tauThree = t[m+3]
        tauFour = t[m+4]
        
        # need to make predictor method and corrector as well
        
        wpFour = wThree + (h/24)*(55*f(tauThree,wThree)-59*f(tauTwo,wTwo)+
            37*f(tauOne,wOne)-9*f(tauZ,wZ))
        
        wcFour = wThree + (h/24)*(9*f(tauFour,wpFour)+19*f(tauThree,wThree)-
                         5*f(tauTwo,wTwo)+ f(tauOne,wOne))
        
        
        
        
        y[i+1] = wcFour
        
        
        
        m = m+1
        # compute y at next time point t 
       # y[i + 1] = y[i] + (h/2) *(f(tau, w) + f(tau2, w + h *f(tau, w)))
           

    return (t,y)