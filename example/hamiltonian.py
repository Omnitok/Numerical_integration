import numpy as np


def system():
    m, l, w = 1, 1, 1

    def td(t, theta, p): return p / (m * l**2)
    def pd(t, theta, p): return -m * (l**2) * (w**2) * np.sin(theta)

    theta0 = np.pi * 5 / 6
    p0 = 0
    t0 = 0

    dct = {
        "x": {"differential": td, "initial": theta0},
        "y": {"differential": pd, "initial": p0},
        "t": {"initial": t0},
    }
    return dct
