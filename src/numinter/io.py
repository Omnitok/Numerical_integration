import numpy as np
import h5py
from pathlib import Path
import csv


def save_hdf(filename: Path, data: dict) -> None:
    """Save solution in hdf5 format

    Args:
        filename: Filename of output file
        data: Dictionary with the solutions for each variable
    """
    with h5py.File(filename, "w") as fh:
        for name, variable in data.items():
            solution = variable["solution"]
            fh[name] = solution


def save_csv(filename: Path, data: dict) -> None:
    """Save solution in csv format

    Args:
        filename: Filename of output file
        data: Dictionary with the solutions for each variable
    """
    save_dict = {}
    for name, variable in data.items():
        solution = variable["solution"]
        save_dict[name] = solution

    with open(filename, "w", newline="") as fh:
        fieldnames = save_dict.keys()
        writer = csv.DictWriter(fh, fieldnames=fieldnames)
        writer.writeheader()
        lens = map(len, save_dict.values())
        if len(set(lens)) == 1:
            vals = save_dict.values()
            arr_len = len(list(vals)[0])
            for i in range(arr_len):
                row = {key: save_dict[key][i] for key in fieldnames}
                writer.writerow(row)


def save_npy(filename: Path, data: dict) -> None:
    """Save solution in numpy format

    Args:
        filename: Filename of output file
        data: Dictionary with the solutions for each variable
    """
    save_dict = {}
    for name, variable in data.items():
        solution = variable["solution"]
        save_dict[name] = solution

    np.save(filename, save_dict)


def read_hdf(filename: Path) -> dict:
    """Function to read hdf data

    Args:
        filename: Path to file

    Returns:
        Dictionary with input data
    """
    with h5py.File(filename, "r") as fh:
        data = {key: value[:] for key, value in fh.items()}
    return data


def read_csv(filename: Path) -> dict:
    """Function to read csv data

    Args:
        filename: Path to file

    Returns:
        Dictionary with data
    """
    with open(filename, "r") as fh:
        reader = csv.DictReader(fh)
        data = {key: np.array([]) for key in reader.fieldnames}
        for row in reader:
            for key, value in row.items():
                data[key] = np.append(data[key], np.float64(value))

    return data


def read_npy(filename: Path) -> dict:
    """Function to read numpy data

    Args:
        filename: Path to file

    Returns:
        Dictionary with data
    """
    data = np.load(filename, allow_pickle=True)
    return data.item()
