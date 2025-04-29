import argparse
from .parse import parse_setupfile, Path
from .locate import find_input_file, find_output_file, find_output_dir
from .io import save_hdf, save_csv, save_npy, read_npy, read_csv, read_hdf
from .custom_errors import MethodError
from .euler_explicit import euler_explicit
from .euler_implicit import euler_implicit
import importlib.util
import sys

# from .plot import plot_data

METHOD_MAP = {
    "euler_explicit": euler_explicit,
    "euler_implicit": euler_implicit,
}
SAVE_MAP = {
    ".csv": save_csv,
    ".hdf5": save_hdf,
    ".npy": save_npy,
}
READ_MAP = {
    ".csv": read_csv,
    ".hdf5": read_hdf,
    ".npy": read_npy
}


def main():
    """
    TODO:
    2. Module to handle saving and reading data
    """
    setup = parse_setupfile()
    help = setup["help"]
    allowed_methods = setup["allowed_methods"].values()
    data_extensions = setup["data_extensions"].values()
    input_extension = setup["input_extension"].values()

    parser = argparse.ArgumentParser(
        add_help=True, description=setup["desc"]["program"]
    )
    parser.add_argument("input", type=str, help=help["input"])
    parser.add_argument(
        "--method", type=str, help=help["method"], default="euler_explicit"
    )
    parser.add_argument("--step", type=float, help=help["step"], default=0.01)
    parser.add_argument("--hs", type=float, help=help["hs"], default=20)
    parser.add_argument("--epsilon", type=float, default=0.1)
    parser.add_argument("--save", action="store_true", help=help["save"])
    parser.add_argument("--savename", type=str, default="unnamed.hdf5")
    parser.add_argument("--plot", action="store_true", help=help["plot"])

    args = parser.parse_args()
    extension = Path(args.input).suffix

    if extension in input_extension:
        match extension:
            case ".py":
                file = find_input_file(args.input)
                name = file.name
                spec = importlib.util.spec_from_file_location(name, file)
                system = importlib.util.module_from_spec(spec)
                sys.modules[name] = system
                spec.loader.exec_module(system)
                input = system.system()

        if args.method in allowed_methods:
            func = METHOD_MAP[args.method]
            solution = func(input, (args.step, args.hs, args.epsilon))

            if args.save:
                save_format = "." + args.savename.split(".")[-1]
                if save_format in data_extensions:
                    outputdir = find_output_dir()
                    filename = outputdir / args.savename
                    func = SAVE_MAP[save_format]
                    func(filename, solution)

            if args.plot:
                pass
                # plot
        else:
            raise MethodError(
                f"{args.method} not implemented. See -h for allowed methods"
            )

    elif extension in data_extensions:
        input = find_output_file(filename=args.input)
        func = READ_MAP[extension]
        solution = func(input)
        print(solution)
        if args.plot:
            # plot data
            pass
        pass
    else:
        raise FileNotFoundError(
            f"File {args.input} does not conform to the file extensions \
            allowed. See -h for allowed file extensions"
        )
