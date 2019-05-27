"""
    Test Runge-Kutta-4th-Order
"""
import numpy as np
import matplotlib.pyplot as plt

import na
import naTwo 
import naThree
import naFour
import naFive
import naSix
import naSeven   # import a set of algorithms in GSU Numerical Analysis (na) course
import exmp_fn  # import a collection of example functions from textbook

N = 20 # number of mesh points
a = 1.0 # left end point of interval [a,b]
b = 2.0# right end point of interval [a,b]
ya = -1.0 # initial value y(a)

# defining function and true solution of an example function
def_fn = exmp_fn.exmp3_def_fn
sol = exmp_fn.exmp3_sol



# run runge's Adams BashForth method from na.py
(t,y) = na.AdamsBashForth(def_fn, a, b, ya, N)

(tTwo,yTwo) = naTwo.Moulton(def_fn, a, b, ya, N)
(tThree,yThree) = naThree.Predictor(def_fn, a, b, ya, N)
(tFour,yFour) = naFour.euler(def_fn, a, b, ya, N)
(tFive,yFive) = naFive.midpoint(def_fn, a, b, ya, N)
(tSix,ySix) = naSix.modified(def_fn, a, b, ya, N)
(tSeven,ySeven) = naSeven.rungeKuttaFour(def_fn, a, b, ya, N)
# compute exact solution for comparison
z = sol(t)  


#print ('t',t)
print (' testAdamBash4th\n y', y)
print ('test Moultons',yTwo)
print ('test Predictor',yThree)
print('test Euler',yFour)
print('test Midpoint',yFive)
print('test Modified Euler',ySix)
print ('test Runge Kutta Four  ', ySeven)
print('\n')






print('Errors at time mesh points:')
print('AdamBash4th')
print(np.abs(np.transpose(np.ravel(y)-z)))
print (' \n  Moultons')
print(np.abs(np.transpose(np.ravel(yTwo)-z)))
print ('\n  Predictor')
print(np.abs(np.transpose(np.ravel(yThree)-z)))
print('\n Euler')
print(np.abs(np.transpose(np.ravel(yFour)-z)))
print('\n Midpoint')
print(np.abs(np.transpose(np.ravel(yFive)-z)))
print('\n Modified Euler')
print(np.abs(np.transpose(np.ravel(ySix)-z)))
print ('\n Runge Kutta Four  ')
print(np.abs(np.transpose(np.ravel(ySeven)-z)))
print('\n')

# plot comparison of exact solution z(t) and approximation y(t)
plt.rcParams.update({'font.size': 10})	# set plot font size
plt.plot(t, z, 'b-', linewidth=2,)	# plot true solution z

# "these" are the numerical methods graphed
plt.plot(t, y, 'r--', marker='v', linewidth=1,markersize=12)	# AdamsBashForth
plt.plot(tTwo, yTwo, 'k--', marker='8', linewidth=1,markersize=11) # Moultons
plt.plot(tThree, yFour, 'm--.', marker='*', linewidth=1,markersize=15) #Predictor
plt.plot(tFour, yFour, 'y-', marker='H', linewidth=1,markersize=13) # Euler
plt.plot(tFive, yFive, 'p--', marker='s', linewidth=1,markersize=8) # Midpoint
plt.plot(tSix, ySix, 'k--', marker='p', linewidth=1,markersize=7) #  Modified Euler
plt.plot(tSeven, ySeven, 'c--', marker='D', linewidth=1,markersize=6)  #Runge Kutta Four
 



plt.xlabel('t')	# set x-axis label as t
plt.ylabel('y(t),')	# set y-axis label as y(t)

plt.legend(['Exact solution', 'Adams Bashforth Four Step Explicit','Moultons','PredictorCorrector','Euler','Midpoint','Modified Euler','Runge Kutta Four'], loc=0,fontsize =8)	# set legend and location




# save plot in pdf format
plt.savefig('ex3number333.pdf', format='pdf', dpi=300)