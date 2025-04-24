import euler_explicit
import euler_implicit
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

rho, sigma, beta = 28, 10, 8/3

x_dash = lambda t,x,y,z: sigma*(y-x)
y_dash = lambda t,x,y,z: x*(rho-z) - y
z_dash = lambda t,x,y,z: x*y - beta*z

z0 = 0
y0 = 0
x0 = 0.9 ## Non-zero initial value
t0 = 0

h = 0.0001
tn = 20
epsilon = 0.1

initial_condition = (z0,y0,x0,t0)
diff_equations = (z_dash, y_dash, x_dash)
integration_settings = (h,tn, epsilon)


fig = plt.figure(figsize=(9, 6))
ax = fig.add_subplot(111, projection='3d')

solution_explicit = euler_explicit.euler_explicit(diff_equations, initial_condition, integration_settings)

z, y, x, t = solution_explicit
ax.plot(x, y, z, label='euler_explicit')


solution_implicit = euler_implicit.euler_implicit(diff_equations, initial_condition, integration_settings)

z, y, x, t = solution_implicit
ax.plot(x, y, z, label = 'euler_implicit')

plt.legend()
plt.show()

