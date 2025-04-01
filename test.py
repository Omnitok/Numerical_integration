import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def euler_de(x_dash, x0, t0, h, tn):

    #intialize list with initial values
    x = [x0]
    t = [t0]
    i = 0
    #append lists
    while t[i] < tn:
        x.append(x[i] + h * x_dash(t[i], x[i]))
        t.append(t[i]+h)
        i+=1

    return x,t

def euler_de_2coupled(y_dash, x_dash, y0, x0, t0, h, tn):
    
    #intialize list with initial values
    y = [y0]
    x = [x0]
    t = [t0]

    i = 0

    #append lists
    while t[i] < tn:

        y.append(y[i] + h * y_dash(t[i], x[i], y[i]))
        x.append(x[i] + h * x_dash(t[i], x[i], y[i]))
        t.append(t[i]+h)

        i+=1

    return y,x,t


def euler_de_3coupled(z_dash, y_dash, x_dash, z0, y0, x0, t0, h, tn):
    
    #intialize list with initial values
    z = [z0]
    y = [y0]
    x = [x0]
    t = [t0]

    i = 0

    #append lists
    while t[i] < tn:

        z.append(z[i] + h * z_dash(t[i], x[i], y[i], z[i]))    
        y.append(y[i] + h * y_dash(t[i], x[i], y[i], z[i]))
        x.append(x[i] + h * x_dash(t[i], x[i], y[i], z[i]))
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
    x0 = 1 ## Non-zero initial value
    t0 = 0

    h = 0.01
    tn = 20

    z, y, x, t = euler_de_3coupled(z_dash, y_dash, x_dash, z0, y0, x0, t0, h, tn)

    # z, y, x, t = euler_de_2coupled(y_dash, x_dash, y0, x0, t0, h, tn)

    # fig = plt.figure(figsize=(9, 6))
    # ax = fig.add_subplot(111, projection='3d')
    # ax.plot(t, x, y)


    # plt.show()


    plt.plot(x,y)
    plt.show()


    plt.plot(x,z)
    plt.show()


    plt.plot(y,z)
    plt.show()
