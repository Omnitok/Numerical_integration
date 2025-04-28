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

input_dict = {
    "x": {"differential": x_dash, "initial": x0},
    "y": {"differential": y_dash, "initial": y0},
    "z": {"differential": z_dash, "initial": z0},    
    "t": {"initial": t0}
}

h = 0.0001
tn = 20
epsilon = 0.1


integration_settings = (h,tn, epsilon)


fig = plt.figure(figsize=(9, 6))
ax = fig.add_subplot(111, projection='3d')

output_dict_explicit = euler_explicit.euler_explicit(input_dict, integration_settings)

x = output_dict_explicit["x"]["solution"]
z = output_dict_explicit["z"]["solution"]
y = output_dict_explicit["y"]["solution"]
t = output_dict_explicit["t"]["solution"]

ax.plot(x, y, z, label='euler_explicit')


output_dict_implicit = euler_implicit.euler_implicit(input_dict, integration_settings)

x = output_dict_implicit["x"]["solution"]
z = output_dict_implicit["z"]["solution"]
y = output_dict_implicit["y"]["solution"]
t = output_dict_implicit["t"]["solution"]

ax.plot(x, y, z, label = 'euler_implicit')

plt.legend()
plt.show()

