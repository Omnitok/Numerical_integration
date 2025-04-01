import numpy as np
X = lambda t, p0, m = 1, l=1: p0/(m*l**2)
Y = lambda t, phi, m = 1, l=1, omega=1: -m*l**2*omega**2*np.sin(phi) 