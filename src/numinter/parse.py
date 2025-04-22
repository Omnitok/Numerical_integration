from .locate import find_setup, Path
from configparser import ConfigParser
import sympy as sp
import yaml


def parse_setupfile() -> ConfigParser:
    """Parses the content of the setting.ini file

    Args:
        file: Path to settings.ini

    Returns:
        ConfigParser object with content from setting.ini
    """
    file = find_setup()
    setup = ConfigParser()
    setup.read(file)
    return setup


def parse_inputfile(file: Path):
    """Parse input file

    Function to parse input files with a set of equations

    Args:
        file: Input file
    """
    with open(file, "r") as fh:
        data = yaml.safe_load(fh)

    t = sp.symbols("t")
    vars = {var: sp.Function(var)(t) for var in data["variables"]}
    inits = data["initials"]

    eqs = list()
    for eq in data["equations"]:
        eqs.append(sp.sympify(eq["rhs"], locals={**vars}))

    lst = []
    for var in vars.values():
        lst.append(var)

    _vars = (t, *lst)
    system = sp.lambdify(_vars, eqs)
    print(type(system))
