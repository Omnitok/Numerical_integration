import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def euler_explicit_single(input_dict, integration_settings):

    h, tn, _ = integration_settings
    x, t = np.zeros((int(tn/h)+1)), np.zeros((int(tn/h)+1))

    x_dash = input_dict["x"]["differential"]
    x[0], t[0] = input_dict["x"]["initial"], input_dict["t"]["initial"]


    #append lists
    for i in range(1,len(t)):
        x[i] = x[i-1] + h * x_dash(t[i-1], x[i-1])
        t[i] = t[i-1] + h

    input_dict["x"]["solution"] = x
    input_dict["t"]["solution"] = t

    return input_dict


def euler_explicit_2coupled(input_dict, integration_settings):

    h, tn, _ = integration_settings
    y,x,t = np.zeros((int(tn/h)+1)), np.zeros((int(tn/h)+1)), np.zeros((int(tn/h)+1))

    x_dash,y_dash = input_dict["x"]["differential"], input_dict["y"]["differential"]
    x[0], y[0], t[0] = input_dict["x"]["initial"], input_dict["y"]["initial"], input_dict["t"]["initial"]


    for i in range(1,len(t)):

        y[i] = y[i-1] + h * y_dash(t[i-1], x[i-1], y[i-1])
        x[i] = x[i-1] + h * x_dash(t[i-1], x[i-1], y[i-1])        
        t[i] = t[i-1] + h

    input_dict["x"]["solution"] = x
    input_dict["y"]["solution"] = y
    input_dict["t"]["solution"] = t

    return input_dict


def euler_explicit_3coupled(input_dict, integration_settings):

    h, tn, _ = integration_settings
    z, y ,x ,t = np.zeros((int(tn/h)+1)), np.zeros((int(tn/h)+1)), np.zeros((int(tn/h)+1)), np.zeros((int(tn/h)+1))

    x_dash,y_dash,z_dash = input_dict["x"]["differential"], input_dict["y"]["differential"], input_dict["z"]["differential"]
    x[0], y[0], z[0], t[0] = input_dict["x"]["initial"], input_dict["y"]["initial"], input_dict["z"]["initial"], input_dict["t"]["initial"]

    
    for i in range(1,len(t)):

        z[i] = z[i-1] + h * z_dash(t[i-1], x[i-1], y[ i-1], z[i-1])    
        y[i] = y[i-1] + h * y_dash(t[i-1], x[i-1], y[i-1], z[i-1])
        x[i] = x[i-1] + h * x_dash(t[i-1], x[i-1], y[i-1], z[i-1])
        t[i] = t[i-1] + h

    input_dict["x"]["solution"] = x
    input_dict["y"]["solution"] = y
    input_dict["z"]["solution"] = z
    input_dict["t"]["solution"] = t

    return input_dict


def euler_explicit(input_dict, integration_settings):

    if len(input_dict)==4:
        output_dict = euler_explicit_3coupled(input_dict, integration_settings)

    elif len(input_dict)==3:
        output_dict = euler_explicit_2coupled(input_dict, integration_settings)

    elif len(input_dict)==2:
        output_dict = euler_explicit_single(input_dict, integration_settings)

    else:
        print('too many diff equations are coupled')

    return output_dict


if __name__ == '__main__':


    rho, sigma, beta = 28, 10, 8/3

    x_dash = lambda t,x,y,z: sigma*(y-x)
    y_dash = lambda t,x,y,z: x*(rho-z) - y
    z_dash = lambda t,x,y,z: x*y - beta*z

    z0 = 0
    y0 = 0
    x0 = 0.99 ## Non-zero initial value
    t0 = 0

    input_dict = {
        "x": {"differential": x_dash, "initial": x0},
        "y": {"differential": y_dash, "initial": y0},
        "z": {"differential": z_dash, "initial": z0},
        "t": {"initial": t0}
    }

    h = 0.01
    tn = 200
    epsilon = 0.1
    
    integration_settings = (h, tn, epsilon)

    output_dict = euler_explicit(input_dict, integration_settings)

    print(output_dict)

    y = output_dict["y"]["solution"]
    x = output_dict["x"]["solution"]
    z = output_dict["z"]["solution"]
    t = output_dict["t"]["solution"]

    fig = plt.figure(figsize=(9, 6))
    ax = fig.add_subplot(111, projection='3d')
    ax.plot(x, y, z)
    plt.show()


