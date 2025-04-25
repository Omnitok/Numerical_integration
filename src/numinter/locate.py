from pathlib import Path
from .custom_errors import DirectoryNotFoundError


def find_input_file(filename: str) -> Path:
    """Locating the input file

    Args:
        filename: Name of the input file

    Returns:
        Path to the input file
    """
    cwd = Path(__file__)
    inputdir = "inputs"

    for parent in cwd.parents:
        input_path = parent / inputdir / filename
        if input_path.exists():
            return input_path
    raise FileNotFoundError(f"{filename} can not be found")


def find_setup() -> Path:
    """Function to find the setup file for the CLI

    Returns:
        Path to the setup file

    Raises:
        FileNotFoundError: Raised if the file not could be located
    """
    cwd = Path(__file__)
    setupfile = "setup.cfg"

    for parent in cwd.parents:
        setup_path = parent / setupfile
        if setup_path.exists():
            return setup_path
    raise FileNotFoundError("'setup.cfg' can not be found")


def find_outputdir() -> Path:
    """Function to locate output directory

    Returns:
        Path to output directory

    Raises:
        DirectoryNotFoundError: Raised if directory can not be found
    """
    cwd = Path(__file__)
    outputdir = "outputs"

    for parent in cwd.parents:
        output_path = parent / outputdir
        if output_path.exists():
            return output_path
    raise DirectoryNotFoundError("output directory can not be located")


def find_outputfile(filename: str):
    """Function to find output file

    Args:
        filename: Name of the output file

    Raises:
        FileNotFoundError: Raise if file can not be found in
            output directory
    """
    outputdir = find_outputdir()
    outputfile = outputdir / filename

    if outputfile.exists():
        return outputfile
    raise FileNotFoundError(f"can not find {filename}")
