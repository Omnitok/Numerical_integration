import numpy as py

def euler_backwards(y_dasj, y0, x0, h, xn):
    y = [y0]
    x = [x0]
    i = 0
    while x[i] < xn:
        y.append(y[i + 1] + h * y_dash(x[i + 1])
        x.append(x[i] + h)
        i = i+1
    return x, y
