import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def euler_implicit_single(input_dict, integration_settings):

    h, tn, epsilon = integration_settings
    x,t = np.zeros((int(tn/h)+1)), np.zeros((int(tn/h)+1))

    x_dash = input_dict["x"]["differential"]
    x[0], t[0] = input_dict["x"]["initial"], input_dict["t"]["initial"]

    #append lists
    for i in range(1,len(t)):

        x_prev = x[i-1] ### Initial guess for fixed point iteration

        #Outside the loop to get it started
        x_curr = x_prev + h * x_dash(t[i-1]+h, x_prev)

        #Fixed point iteration
        while np.abs(x_curr - x_prev) > epsilon:
            x_prev = x_curr
            x_curr = x[i-1] + h * x_dash(t[i-1]+h, x_prev)

        # Append it to solutions
        x[i] = x_curr
        t[i] = t[i-1]+h

    input_dict["x"]["solution"] = x
    input_dict["t"]["solution"] = t

    return input_dict

def euler_implicit_2coupled(input_dict, integration_settings):

    h, tn, epsilon = integration_settings
    y, x, t = np.zeros((int(tn/h)+1)), np.zeros((int(tn/h)+1)), np.zeros((int(tn/h)+1))


    x_dash,y_dash = input_dict["x"]["differential"], input_dict["y"]["differential"]
    x[0], y[0], t[0] = input_dict["x"]["initial"], input_dict["y"]["initial"], input_dict["t"]["initial"]


    #append lists
    for i in range(1,len(t)):

        x_prev = x[i-1] ### Initial guess for fixed point iteration
        y_prev = y[i-1] ### Initial guess for fixed point iteration

        #Outside the loop to get it started
        x_curr = x_prev + h * x_dash(t[i-1]+h, x_prev, y_prev)
        y_curr = y_prev + h * y_dash(t[i-1]+h, x_prev, y_prev)

        #Fixed point iteration
        ## Might not stuck?
        while np.abs(x_curr - x_prev) > epsilon or np.abs(y_curr - y_prev) > epsilon:
            
            x_prev = x_curr
            y_prev = y_curr

            x_curr = x[i-1] + h * x_dash(t[i-1]+h, x_prev, y_prev)
            y_curr = y[i-1] + h * y_dash(t[i-1]+h, x_prev, y_prev)


        # Append it to solutions
        x[i] = x_curr
        y[i] = y_curr
        t[i] = t[i-1]+h

    input_dict["x"]["solution"] = x
    input_dict["y"]["solution"] = y
    input_dict["t"]["solution"] = t


    return input_dict

def euler_implicit_3coupled(input_dict, integration_settings):

    h, tn, epsilon = integration_settings
    z, y, x, t = np.zeros((int(tn/h)+1)), np.zeros((int(tn/h)+1)), np.zeros((int(tn/h)+1)), np.zeros((int(tn/h)+1))

    x_dash,y_dash,z_dash = input_dict["x"]["differential"], input_dict["y"]["differential"], input_dict["z"]["differential"]
    x[0], y[0], z[0], t[0] = input_dict["x"]["initial"], input_dict["y"]["initial"], input_dict["z"]["initial"], input_dict["t"]["initial"]


    #append lists
    for i in range(1,len(t)):

        x_prev = x[i-1] ### Initial guess for fixed point iteration
        y_prev = y[i-1] ### Initial guess for fixed point iteration
        z_prev = z[i-1] ### Initial guess for fixed point iteration


        #Outside the loop to get it started
        x_curr = x_prev + h * x_dash(t[i-1]+h, x_prev, y_prev, z_prev)
        y_curr = y_prev + h * y_dash(t[i-1]+h, x_prev, y_prev, z_prev)
        z_curr = z_prev + h * z_dash(t[i-1]+h, x_prev, y_prev, z_prev)

        ## Might not stuck?
        while np.abs(x_curr - x_prev) > epsilon or np.abs(y_curr - y_prev) > epsilon or np.abs(z_curr - z_prev) > epsilon:
            
            x_prev = x_curr
            y_prev = y_curr
            z_prev = z_curr

            x_curr = x[i-1] + h * x_dash(t[i-1]+h, x_prev, y_prev, z_prev)
            y_curr = y[i-1] + h * y_dash(t[i-1]+h, x_prev, y_prev, z_prev)
            z_curr = z[i-1] + h * z_dash(t[i-1]+h, x_prev, y_prev, z_prev)


        # Append it to solutions
        x[i] = x_curr
        y[i] = y_curr
        z[i] = z_curr

        t[i] = t[i-1]+h

    input_dict["x"]["solution"] = x
    input_dict["y"]["solution"] = y
    input_dict["z"]["solution"] = z
    input_dict["t"]["solution"] = t


    return input_dict

def euler_implicit(input_dict, integration_settings):

    if len(input_dict)==4:
        output_dict = euler_implicit_3coupled(input_dict, integration_settings)

    elif len(input_dict)==3:
        output_dict = euler_implicit_2coupled(input_dict, integration_settings)

    elif len(input_dict)==2:
        output_dict = euler_implicit_single(input_dict, integration_settings)

    else:
        print('too many diff equations are coupled')

    return output_dict


if __name__ == '__main__':

    x_dash = lambda t,x,y,z: -x
    y_dash = lambda t,x,y,z: -2*y
    z_dash = lambda t,x,y,z: -3*z

    z0 = 1
    y0 = 1
    x0 = 1
    t0 = 0

    input_dict = {
        "x": {"differential": x_dash, "initial": x0},
        "y": {"differential": y_dash, "initial": y0},
        "z": {"differential": z_dash, "initial": z0},
        "t": {"initial": t0}
    }


    h = 0.1
    tn = 5
    epsilon = 0.1

    integration_settings = (h, tn, epsilon)

    output_dict = euler_implicit(input_dict, integration_settings)

    print(output_dict)
    
    x = output_dict["x"]["solution"]
    z = output_dict["z"]["solution"]
    y = output_dict["y"]["solution"]
    t = output_dict["t"]["solution"]


    ### Analytical solution to test
    x_true = np.exp(-np.array(t))
    y_true = np.exp(-2*np.array(t))
    z_true = np.exp(-3*np.array(t))

    fig = plt.figure(figsize=(9, 6))
    ax = fig.add_subplot(111, projection='3d')

    ax.scatter(x, y, z, s=2, label='x numerical euler_implicit')
    ax.plot(x_true, y_true, z_true, c= 'k', label='x analytical')


    plt.legend()
    plt.show()
