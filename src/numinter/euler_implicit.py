import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


def euler_implicit(x_dash, x0, t0, h, tn):

    #intialize list with initial values
    x = [x0]
    t = [t0]
    i = 0

    #append lists
    while t[i] < tn:

        x_prev = x[i] ### Initial guess for fixed point iteration
        x_new = np.inf ### Big number to start the loop

        #Fixed point iteration
        while np.abs(x_new - x_prev) > 0.1:
            x_prev = x_new
            x_new = x[i] + h * x_dash(t[i]+h, x_prev)

        # Append it to solutions
        x.append(x_new)
        t.append(t[i]+h)
        i+=1

    return x,t

def euler_implicit_2coupled(y_dash, x_dash, y0, x0, t0, h, tn):

    #intialize list with initial values
    y = [y0]
    x = [x0]
    t = [t0]
    i = 0

    #append lists
    while t[i] < tn:

        x_prev = x[i] ### Initial guess for fixed point iteration
        x_new = np.inf ### Big number to start the loop

        #Fixed point iteration
        while np.abs(x_new - x_prev) > 0.1:
            x_prev = x_new
            x_new = x[i] + h * x_dash(t[i]+h, x_prev)

        y_prev = y[i] ### Initial guess for fixed point iteration
        y_new = np.inf ### Big number to start the loop

        #Fixed point iteration
        while np.abs(y_new - y_prev) > 0.1:
            y_prev = y_new
            y_new = y[i] + h * y_dash(t[i]+h, y_prev)

        # Append it to solutions
        x.append(x_new)
        y.append(y_new)
        t.append(t[i]+h)
        i+=1

    return y,x,t

def euler_implicit_3coupled(z_dash, y_dash, x_dash, z0, y0, x0, t0, h, tn):

    #intialize list with initial values
    z = [z0]
    y = [y0]
    x = [x0]
    t = [t0]
    i = 0

    #append lists
    while t[i] < tn:

        x_prev = x[i] ### Initial guess for fixed point iteration
        x_new = np.inf ### Big number to start the loop

        #Fixed point iteration
        while np.abs(x_new - x_prev) > 0.1:
            x_prev = x_new
            x_new = x[i] + h * x_dash(t[i]+h, x_prev)

        y_prev = y[i] ### Initial guess for fixed point iteration
        y_new = np.inf ### Big number to start the loop

        #Fixed point iteration
        while np.abs(y_new - y_prev) > 0.1:
            y_prev = y_new
            y_new = y[i] + h * y_dash(t[i]+h, y_prev)

        z_prev = z[i] ### Initial guess for fixed point iteration
        z_new = np.inf ### Big number to start the loop

        #Fixed point iteration
        while np.abs(z_new - z_prev) > 0.1:
            z_prev = z_new
            z_new = z[i] + h * z_dash(t[i]+h, z_prev)

        # Append it to solutions
        z.append(z_new)
        x.append(x_new)
        y.append(y_new)
        t.append(t[i]+h)
        i+=1

    return z,y,x,t

if __name__ == '__main__':

    rho, sigma, beta = 28, 10, 8/3

    x_dash = lambda t,x,y,z: sigma*(y-x)
    y_dash = lambda t,x,y,z: x*(rho-z) - y
    z_dash = lambda t,x,y,z: x*y - beta*z

    z0 = 0
    y0 = 0
    x0 = 0.99 ## Non-zero initial value
    t0 = 0

    h = 0.01
    tn = 20

    z, y, x, t = euler_implicit_3coupled(z_dash, y_dash, x_dash, z0, y0, x0, t0, h, tn)

    fig = plt.figure(figsize=(9, 6))
    ax = fig.add_subplot(111, projection='3d')
    ax.plot(x, y, z)
    plt.show()
