import argparse
# from .plot import plot_data


def main():
    """
    TODO:
    1. set configuration for desc and other cli stuff
    2. functions for reading and parsing input file
    3. module to handle saving and reading data


    """
    parser = argparse.ArgumentParser(add_help=True)
    parser.add_argument("input", type=str)
    args = parser.parse_args()

    # do stuf with args
