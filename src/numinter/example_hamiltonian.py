import euler_explicit
import euler_implicit
import numpy as np
import matplotlib.pyplot as plt

m,l,w = 1,1,1

theta_dash = lambda t, theta, p: p/(m*l**2)
p_dash = lambda t,theta, p: -m*(l**2)*(w**2)*np.sin(theta)

p = 0
theta = np.pi * 5/6

t0 = 0

h = 0.001
tn = 120

initial_condition = (p,theta,t0)
diff_equations = (p_dash, theta_dash)
integration_settings = (h,tn)

solution_explicit = euler_explicit.euler_explicit(diff_equations, initial_condition, integration_settings)

solution_implicit = euler_implicit.euler_implicit(diff_equations, initial_condition, integration_settings)

y, x, t = solution_explicit

plt.scatter(x, y, s = 0.1, label = 'euler_explicit')

y, x, t = solution_implicit

plt.scatter(x, y, s = 0.1, label = 'euler_implicit')

plt.legend()
plt.show()