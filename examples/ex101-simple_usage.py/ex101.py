#%%[markdown]
'''
# Example 101: Simple usage

This HAS NOT BEEN TESTED YET
'''

#%%[code]
# import 
import numpy as np
import matplotlib.pyplot as plt

from  pymfoil.mfoil import mfoil


#%%[code]


# make a NACA 2412 airfoil
m = mfoil(naca='4415', npanel=199)
print('NACA geom name =', m.geom.name, '  num. panels =', m.foil.N)
# add a flap
#m.geom_flap(np.r_[0.8,0],5)
# derotate the geometry
#m.geom_derotate()
# add camber
#m.geom_addcamber(np.array([[0,0.3,0.7,1],[0,-.03,.01,0]]))
# set up a compressible viscous run (note, alpha is in degrees)
m.setoper(alpha=2.5, Re=5*10**6, Ma=0.0)
# request plotting, specify the output file for the plot
m.param.doplot, m.post.rfile = True, 'results.pdf'
# set the verbosity (higher -> more output to stdout)
m.param.verb = 1
# run the solver
print('Running the solver.')
m.solve()
# run the derivative ping check
#print('Derivative ping check.')
#m.ping()
plt.show()



# %%
