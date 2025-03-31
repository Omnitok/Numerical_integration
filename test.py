import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def euler_de(y_dash, y0, x0, h, xn):

    #intialize list with initial values
    y = [y0]
    x = [x0]
    i = 0
    #append lists
    while x[i] < xn:
        y.append(y[i] + h * y_dash(x[i]))
        x.append(x[i]+h)
        i+=1

    return y,x

def euler_de_2coupled(z_dash, y_dash, z0, y0, x0, h, xn):
    
    #intialize list with initial values
    z = [z0]
    y = [y0]
    x = [x0]

    i = 0

    #append lists
    while x[i] < xn:

        y.append(y[i] + h * y_dash(x[i], y[i], z[i]))
        z.append(z[i] + h * z_dash(x[i], y[i], z[i]))
        x.append(x[i]+h)

        i+=1

    return z,y,x


if __name__ == '__main__':

#    y_dash = lambda x,y,z: x
    y_dash = lambda x: x
    z_dash = lambda x,y,z: x**2

    z0 = 0
    y0 = 0
    x0 = 0

    h = 0.1
    xn = 20


#    z, y, x = euler_de_2coupled(z_dash, y_dash, z0, y0, x0, h, xn)
    y, x = euler_de(y_dash, y0, x0, h, xn)

    fig = plt.figure(figsize=(9, 6))
    ax = fig.add_subplot(111, projection='3d')
    ax.plot(x, y)
    

    plt.show()
