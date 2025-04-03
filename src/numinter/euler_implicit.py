import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def euler_implicit_single(diff_equations, initial_condition, integration_settings):

    x_dash = diff_equations[0]
    x, t = [initial_condition[0]], [initial_condition[1]]

    h, tn = integration_settings

    i = 0

    #append lists
    while t[i] < tn:

        x_prev = x[i] ### Initial guess for fixed point iteration

        #Outside the loop to get it started
        x_curr = x_prev + h * x_dash(t[i]+h, x_prev)

        #Fixed point iteration
        while np.abs(x_curr - x_prev) > 0.1:
            x_prev = x_curr
            x_curr = x[i] + h * x_dash(t[i]+h, x_prev)

        # Append it to solutions
        x.append(x_curr)
        t.append(t[i]+h)
        i+=1

    return x,t

def euler_implicit_2coupled(diff_equations, initial_condition, integration_settings):

    y_dash, x_dash = diff_equations

    y, x, t = [initial_condition[0]], [initial_condition[1]], [initial_condition[2]]

    h, tn = integration_settings
    
    i = 0

    #append lists
    while t[i] < tn:

        x_prev = x[i] ### Initial guess for fixed point iteration
        y_prev = y[i] ### Initial guess for fixed point iteration

        #Outside the loop to get it started
        x_curr = x_prev + h * x_dash(t[i]+h, x_prev, y_prev)
        y_curr = y_prev + h * y_dash(t[i]+h, x_prev, y_prev)

        #Fixed point iteration
        ## Might not stuck?
        while np.abs(x_curr - x_prev) > 0.1 or np.abs(y_curr - y_prev) > 0.1:
            
            x_prev = x_curr
            y_prev = y_curr

            x_curr = x[i] + h * x_dash(t[i]+h, x_prev, y_prev)
            y_curr = y[i] + h * y_dash(t[i]+h, x_prev, y_prev)


        # Append it to solutions
        x.append(x_curr)
        y.append(y_curr)
        t.append(t[i]+h)

        i+=1

    return y,x,t

def euler_implicit_3coupled(diff_equations, initial_condition, integration_settings):

    z_dash, y_dash, x_dash = diff_equations

    z, y, x, t = [initial_condition[0]], [initial_condition[1]], [initial_condition[2]], [initial_condition[3]]

    h, tn = integration_settings

    i = 0

    #append lists
    while t[i] < tn:

        x_prev = x[i] ### Initial guess for fixed point iteration
        y_prev = y[i] ### Initial guess for fixed point iteration
        z_prev = z[i] ### Initial guess for fixed point iteration


        #Outside the loop to get it started
        x_curr = x_prev + h * x_dash(t[i]+h, x_prev, y_prev, z_prev)
        y_curr = y_prev + h * y_dash(t[i]+h, x_prev, y_prev, z_prev)
        z_curr = z_prev + h * z_dash(t[i]+h, x_prev, y_prev, z_prev)

        ## Might not stuck?
        while np.abs(x_curr - x_prev) > 0.1 or np.abs(y_curr - y_prev) > 0.1 or np.abs(z_curr - z_prev) > 0.1:
            
            x_prev = x_curr
            y_prev = y_curr
            z_prev = z_curr

            x_curr = x[i] + h * x_dash(t[i]+h, x_prev, y_prev, z_prev)
            y_curr = y[i] + h * y_dash(t[i]+h, x_prev, y_prev, z_prev)
            z_curr = z[i] + h * z_dash(t[i]+h, x_prev, y_prev, z_prev)


        # Append it to solutions
        z.append(x_curr)
        x.append(y_curr)
        y.append(z_curr)
        t.append(t[i]+h)
        i+=1

    return z,y,x,t

def euler_implicit(diff_equations, initial_condition, integration_settings):

    if len(diff_equations)==3:
        solution = euler_implicit_3coupled(diff_equations, initial_condition, integration_settings)

    elif len(diff_equations)==2:
        solution = euler_implicit_2coupled(diff_equations, initial_condition, integration_settings)

    elif len(diff_equations)==1:
        solution = euler_implicit_single(diff_equations, initial_condition, integration_settings)

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

    h = 0.001
    tn = 20

    initial_condition = (z0,y0,x0,t0)
    diff_equations = (z_dash, y_dash, x_dash)
    integration_settings = (h,tn)

    z, y, x, t = euler_implicit(diff_equations, initial_condition, integration_settings)


    fig = plt.figure(figsize=(9, 6))
    ax = fig.add_subplot(111, projection='3d')
    ax.plot(x, y, z)
    plt.show()

    # x_dash = lambda t, x: t

    # x0 = 0

    # t0 = 0

    # h = 0.01
    # tn = 20

    # x,t = euler_implicit(x_dash, x0, t0, h, tn)

    # plt.plot(t,x)
    # plt.show()