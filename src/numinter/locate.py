from pathlib import Path
from hashlib import sha256


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
    raise FileNotFoundError("'setup.cfg' ca not be found")


def hashval(file: Path) -> str:
    """Function to hash file content with sha256


    Args:
        file: Path to the file that should be hashed

    Returns:
        Hash value of the content
    """
    hasher = sha256()
    content = file.read_bytes()
    hasher.update(content)
    return hasher.hexdigest()
