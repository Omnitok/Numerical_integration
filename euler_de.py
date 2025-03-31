import numpy as np
import matplotlib.pyplot as plt

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

if __name__ == '__main__':

    y_dash = lambda x: x

    y0 = 0
    x0 = 0

    h = 0.1
    xn = 20


    y, x = euler_de(y_dash, y0, x0, h, xn)

    plt.plot(x,y)

    plt.show()

    main()