import euler_explicit
import euler_implicit
import numpy as np
import matplotlib.pyplot as plt

x_dash = lambda t, x, y: -x + 6*y
y_dash = lambda t, x, y: x - 2*y

x0 = 2
y0 = 0

t0 = 0

h = 0.01
tn = 20
epsilon = 0.1

initial_condition = (y0,x0,t0)
diff_equations = [y_dash, x_dash]
integration_settings = (h,tn,epsilon)

solution_explicit = euler_explicit.euler_explicit(diff_equations, initial_condition, integration_settings)
y, x, t = solution_explicit
plt.scatter(t, x, s=0.2, label='euler_explicit')

solution_implicit = euler_implicit.euler_implicit(diff_equations, initial_condition, integration_settings)
y, x, t = solution_implicit
plt.scatter(t, x, s=0.2, label='euler_implicit')

t = np.array(t)
fx = lambda t: (2/5) * (3*np.e**t + 2*np.e**(-4*t))
fy = lambda t: (2/5) * (np.e**t - np.e**(-4*t))


plt.scatter(t, fx(t), s=0.2, label='analytical solution')

plt.legend()
plt.show()

# plt.scatter(t, y, s=0.2, label='euler_explicit')
# plt.scatter(t, fy(t), s=0.2, label='analytical solution')

# plt.legend()
# plt.show()
