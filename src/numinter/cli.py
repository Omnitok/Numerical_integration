import argparse
from .parse import parse_setupfile, Path
from .locate import find_input_file
from .custom_errors import MethodError
# from .plot import plot_data


def main():
    """
    TODO:
    1. functions for reading and parsing input file
    2. module to handle saving and reading data
    """
    setup = parse_setupfile()
    help = setup["help"]
    allowed_methods = setup["allowed_methods"].values()
    data_extensions = setup["data_extensions"].values()
    input_extension = setup["input_extension"]["yaml"]

    parser = argparse.ArgumentParser(
        add_help=True, description=setup["desc"]["program"]
    )
    parser.add_argument("input", type=str, help=help["input"])
    parser.add_argument(
        "--method", type=str, help=help["method"], default="euler_explicit"
    )
    parser.add_argument("--step", type=str, help=help["step"], default=0.01)
    parser.add_argument("--hs", type=str, help=help["hs"], default=20)
    parser.add_argument("--save", action="store_true", help=help["save"])
    parser.add_argument("--plot", action="store_true", help=help["plot"])

    args = parser.parse_args()
    extension = Path(args.input).suffix

    if extension in input_extension:
        if args.method in allowed_methods:
            file = find_input_file(args.input)
            # parse_file
            # solve problem in file
            if args.save:
                pass
                # save file
            if args.plot:
                pass
                # plot data
        else:
            raise MethodError(
                f"{args.method} not implemented. See -h for allowed methods"
            )

    elif extension in data_extensions:
        # read data based on extension
        if args.plot:
            # plot data
            pass
        pass
    else:
        raise FileNotFoundError(
            f"File {args.input} does not conform to the file extensions allowed. See -h for allowed file extensions"
        )
