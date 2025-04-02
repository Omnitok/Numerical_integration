import matplotlib.pyplot as plt
import numpy as np
from equation import X, Y
# use implicit euler method?
#X = lambda t, p0, m = 1, l=1: p0/(m*l**2)
#Y = lambda t, phi, m = 1, l=1, omega=1: -m*l**2*omega**2*np.sin(phi) 

# eq of motion
# f(x0 + h) = f(x0) + h*F(x0)

y0, x0 = 1, 1
h = 0.01  # Step size
steps = 10000

t0 = -1
# Explicit Euler Method

x_vector = np.zeros(steps)
x_vector[0] = x0
y_vector = np.zeros(steps)
y_vector[0] = y0
t = np.zeros(steps)


for i in range(steps - 1):
    t[i] = t0 + i*h
    # implicit according to 
    # https://en.wikipedia.org/wiki/Explicit_and_implicit_methods#Illustration_using_the_forward_and_backward_Euler_methods
    x_vector[i + 1] = (-1 + np.sqrt(1 + 4*h*X(t[i], y_vector[i]))) /(2*h)
    y_vector[i + 1] = (-1 + np.sqrt(1 + 4*h*Y(t[i], x_vector[i]))) /(2*h)

plt.figure(figsize = (12, 8))
plt.plot(x_vector,y_vector, 'bo--', label='Approximate')
plt.title('Approximate and Exact Solution \
for Simple ODE')
plt.xlabel('t')
plt.ylabel('f(t)')
plt.grid()
plt.legend(loc='lower right')
plt.show()