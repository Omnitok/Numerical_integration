import numpy as np
import h5py


def save_hdf(filename, data):
    with h5py.File(filename, "w") as fh:

