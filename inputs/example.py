def system():
    rho, sigma, beta = 28, 10, 8 / 3

    def xd(t, x, y, z): return sigma * (y - x)
    def yd(t, x, y, z): return x * (rho - z) - y
    def zd(t, x, y, z): return x * y - beta * z

    z0 = 0
    y0 = 0
    x0 = 0.99
    t0 = 0

    dct = {
        "x": {"differential": xd, "initial": x0},
        "y": {"differential": yd, "initial": y0},
        "z": {"differential": zd, "initial": z0},
        "t": {"initial": t0}
    }

    return dct
