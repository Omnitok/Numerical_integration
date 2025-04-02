from pathlib import Path
from hashlib import sha256


class HashError(Exception):
    def __init__(self, message):
        self.message = message


def find_file(filename: str) -> Path:
    cwd = Path(__file__)
    return cwd


def find_setup() -> Path | None:
    cwd = Path(__file__)
    setupfile = "setup.cfg"
    for parent in cwd.parents:
        setup_path = parent / setupfile

        if setup_path.exists():
            return setup_path
        else:
            raise FileNotFoundError(f"{setupfile} could not be found")
    return None


def hashval(file: Path) -> str:
    hasher = sha256()
    content = file.read_bytes()
    hasher.update(content)
    return hasher.hexdigest()
