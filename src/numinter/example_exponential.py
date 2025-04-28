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

input_dict = {
    "x": {"differential": x_dash, "initial": x0},
    "y": {"differential": y_dash, "initial": y0},
    "t": {"initial": t0}
}

integration_settings = (h,tn,epsilon)

output_dict_explicit = euler_explicit.euler_explicit(input_dict, integration_settings)
y = output_dict_explicit["y"]["solution"]
x = output_dict_explicit["x"]["solution"]
t = output_dict_explicit["t"]["solution"]

plt.scatter(t, x, s=0.2, label='euler_explicit')

output_dict_implicit = euler_implicit.euler_implicit(input_dict, integration_settings)
y = output_dict_implicit["y"]["solution"]
x = output_dict_implicit["x"]["solution"]
t = output_dict_implicit["t"]["solution"]

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
