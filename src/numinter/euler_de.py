import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def euler_de(diff_equations, initial_condition, integration_settings):

    x_dash = diff_equations
    x, t = [initial_condition[0]], [initial_condition[1]]

    h, tn = integration_settings

    i = 0
    #append lists
    while t[i] < tn:
        x.append(x[i] + h * x_dash(t[i], x[i]))
        t.append(t[i]+h)
        i+=1

    return x,t


def euler_de_2coupled(diff_equations, initial_condition, integration_settings):

    z_dash, y_dash, x_dash = diff_equations

    y, x, t = [initial_condition[0]], [initial_condition[1]], [initial_condition[2]]

    h, tn = integration_settings
    
    i = 0

    #append lists
    while t[i] < tn:

        y.append(y[i] + h * y_dash(t[i], x[i], y[i]))
        x.append(x[i] + h * x_dash(t[i], x[i], y[i]))
        t.append(t[i]+h)

        i+=1

    return y,x,t


def euler_de_3coupled(diff_equations, initial_condition, integration_settings):

    z_dash, y_dash, x_dash = diff_equations

    z, y, x, t = [initial_condition[0]], [initial_condition[1]], [initial_condition[2]], [initial_condition[3]]

    h, tn = integration_settings
    
    i = 0

    #append lists
    while t[i] < tn:

        z.append(z[i] + h * z_dash(t[i], x[i], y[i], z[i]))    
        y.append(y[i] + h * y_dash(t[i], x[i], y[i], z[i]))
        x.append(x[i] + h * x_dash(t[i], x[i], y[i], z[i]))
        t.append(t[i]+h)

        i+=1

    return z,y,x,t

def euler_de(diff_equations, initial_condition, integration_settings):

    if len(diff_equations)==3:
        solution = euler_de_3coupled(diff_equations, initial_condition, integration_settings)

    elif len(diff_equations)==2:
        solution = euler_de_2coupled(diff_equations, initial_condition, integration_settings)

    elif len(diff_equations)==1:
        solution = euler_de_single(diff_equations, initial_condition, integration_settings)

    else:
        print('too many diff equations are coupled')

    return solution



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

    initial_condition = (z0,y0,x0,t0)
    diff_equations = (z_dash, y_dash, x_dash)
    integration_settings = (h,tn)

    solution = euler_de(diff_equations, initial_condition, integration_settings)

    z, y, x, t = solution

    fig = plt.figure(figsize=(9, 6))
    ax = fig.add_subplot(111, projection='3d')
    ax.plot(x, y, z)
    plt.show()


    # plt.show()


