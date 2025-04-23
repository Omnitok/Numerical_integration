def system():
    rho, sigma, beta = 28, 10, 8 / 3

    def x_dash(t, x, y, z): return sigma * (y - x)
    def y_dash(t, x, y, z): return x * (rho - z) - y
    def z_dash(t, x, y, z): return x * y - beta * z

    z0 = 0
    y0 = 0
    x0 = 0.99
    t0 = 0

    return (z_dash, y_dash, x_dash), (z0, y0, x0, t0)
