import argparse
from .parse import Path
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
READ_MAP = {".csv": read_csv, ".hdf5": read_hdf, ".npy": read_npy}
ARG_HELP = {
    "input": "Path to input file with equations, constants and initial values.",
    "plot": "Plot data",
    "save": "Saves integrated data",
    "method": "Method, allowed is euler_implicit or euler_explicit",
    "step": "Stepsize",
    "hs": "End value for step",
    "savename": "Filename of the file to save data to. Allowed extensions: .npy, .hdf5, .csv",
    "eps": "Error term for implicit Euler",
}


def main():
    allowed_methods = ["euler_implicit", "euler_explicit"]
    data_extensions = [".csv", ".hdf5", ".npy"]
    input_extensions = [".py"]

    parser = argparse.ArgumentParser(
        add_help=True, description="CLI tool to solve ODEs"
    )
    parser.add_argument("input", type=str, help=ARG_HELP["input"])
    parser.add_argument(
        "--method", type=str, help=ARG_HELP["method"], default="euler_explicit"
    )
    parser.add_argument("--step", type=float, help=ARG_HELP["step"], default=0.01)
    parser.add_argument("--hs", type=float, help=ARG_HELP["hs"], default=20)
    parser.add_argument("--epsilon", type=float, default=0.1, help=ARG_HELP["eps"])
    parser.add_argument("--save", action="store_true", help=ARG_HELP["save"])
    parser.add_argument(
        "--savename", type=str, default="unnamed.csv", help=ARG_HELP["savename"]
    )
    parser.add_argument("--plot", action="store_true", help=ARG_HELP["plot"])

    args = parser.parse_args()
    input_file = Path(args.input)
    input_extension = input_file.suffix

    if input_extension in input_extensions and input_file.exists():
        match input_extension:
            case ".py":
                name = input_file.name
                spec = importlib.util.spec_from_file_location(name, input_file)
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
                    func = SAVE_MAP[save_format]
                    func(args.savename, solution)

            if args.plot:
                pass
                # plot
        else:
            raise MethodError(
                f"{args.method} not implemented. See -h for allowed methods"
            )

    elif input_extension in data_extensions and input_file.exists():
        func = READ_MAP[input_extension]
        solution = func(input_file)
        if args.plot:
            # plot data
            pass
    else:
        raise FileNotFoundError(
            f"File {args.input} do not conform to the file extensions \
            allowed. See -h for allowed file extensions"
        )
