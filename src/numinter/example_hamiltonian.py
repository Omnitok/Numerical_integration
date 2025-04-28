import euler_explicit
import euler_implicit
import numpy as np
import matplotlib.pyplot as plt

m,l,w = 1,1,1

theta_dash = lambda t, theta, p: p/(m*l**2)
p_dash = lambda t,theta, p: -m*(l**2)*(w**2)*np.sin(theta)

theta0 = np.pi * 5/6
p0 = 0

t0 = 0

input_dict = {
    "x": {"differential": theta_dash, "initial": theta0},
    "y": {"differential": p_dash, "initial": p0},
    "t": {"initial": t0}
}


h = 0.001
tn = 20
epsilon = 0.1

integration_settings = (h,tn,epsilon)

output_dict_explicit = euler_explicit.euler_explicit(input_dict, integration_settings)

y = output_dict_explicit["y"]["solution"]
x = output_dict_explicit["x"]["solution"]
t = output_dict_explicit["t"]["solution"]

plt.scatter(x, y, s = 0.1, label = 'euler_explicit')


output_dict_implicit = euler_implicit.euler_implicit(input_dict, integration_settings)
y = output_dict_explicit["y"]["solution"]
x = output_dict_explicit["x"]["solution"]
t = output_dict_explicit["t"]["solution"]

plt.scatter(x, y, s = 0.1, alpha=0.1, label = 'euler_implicit')

plt.legend()
plt.show()