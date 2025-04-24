import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def euler_implicit_single(diff_equations, initial_condition, integration_settings):

    x_dash = diff_equations[0]
    x, t = [initial_condition[0]], [initial_condition[1]]

    h, tn, epsilon = integration_settings

    i = 0

    #append lists
    while t[i] < tn:

        x_prev = x[i] ### Initial guess for fixed point iteration

        #Outside the loop to get it started
        x_curr = x_prev + h * x_dash(t[i]+h, x_prev)

        #Fixed point iteration
        while np.abs(x_curr - x_prev) > epsilon:
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

    h, tn, epsilon = integration_settings
    
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
        while np.abs(x_curr - x_prev) > epsilon or np.abs(y_curr - y_prev) > epsilon:
            
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

    h, tn, epsilon = integration_settings

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
        while np.abs(x_curr - x_prev) > epsilon or np.abs(y_curr - y_prev) > epsilon or np.abs(z_curr - z_prev) > epsilon:
            
            x_prev = x_curr
            y_prev = y_curr
            z_prev = z_curr

            x_curr = x[i] + h * x_dash(t[i]+h, x_prev, y_prev, z_prev)
            y_curr = y[i] + h * y_dash(t[i]+h, x_prev, y_prev, z_prev)
            z_curr = z[i] + h * z_dash(t[i]+h, x_prev, y_prev, z_prev)


        # Append it to solutions
        x.append(x_curr)
        y.append(y_curr)
        z.append(z_curr)

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

    x_dash = lambda t,x,y,z: -x
    y_dash = lambda t,x,y,z: -2*y
    z_dash = lambda t,x,y,z: -3*z

    z0 = 1
    y0 = 1
    x0 = 1
    t0 = 0

    h = 0.1
    tn = 5
    epsilon = 0.1

    initial_condition = (z0, y0, x0, t0)
    diff_equations = (z_dash, y_dash, x_dash)
    integration_settings = (h, tn, epsilon)

    fig = plt.figure(figsize=(9, 6))
    ax = fig.add_subplot(111, projection='3d')


    z, y, x, t = euler_implicit(diff_equations, initial_condition, integration_settings)


    ### Analytical solution to test
    x_true = np.exp(-np.array(t))
    y_true = np.exp(-2*np.array(t))
    z_true = np.exp(-3*np.array(t))


    ax.scatter(x, y, z, s=2, label='x numerical euler_implicit')
    ax.plot(x_true, y_true, z_true, c= 'k', label='x analytical')


    plt.legend()
    plt.show()
