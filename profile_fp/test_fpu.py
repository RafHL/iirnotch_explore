import cProfile
import numpy as np
import fixedpoint_oldbin as fixedpoint

cProfile.run('[fixedpoint.approx([v],d) for d in range(54) for v in np.linspace(0,1,num=10000)]')
