import numpy as np
import h5py
from pathlib import Path


def save_hdf(filename: Path, data: dict):
    """Save solution in hdf5 format

    Args:
        filename: Filename of output file
        data: Dictionary with the solutions for each variable
    """
    with h5py.File(filename, "w") as fh:
        for name, variable in data.items():
            solution = variable["solution"]
            initial = variable["initial"]

            fh[name]["solution"] = solution
            fh[name]["initial"] = initial


def save_csv(filename: Path, data: dict):
    """Save solution in csv format

    Args:
        filename: Filename of output file
        data: Dictionary with the solutions for each variable
    """
    pass


def save_npy(filename: Path, data: dict):
    """Save solution in numpy format

    Args:
        filename: Filename of output file
        data: Dictionary with the solutions for each variable
    """
    pass
