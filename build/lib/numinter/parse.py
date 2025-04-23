from .locate import find_setup, Path
from configparser import ConfigParser
import sympy as sp
import yaml
from sympy import symbols, Function, sympify, lambdify
import importlib.util
import sys



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

    #    t = sp.symbols("t")
    #    vars = {var: sp.Function(var)(t) for var in data["variables"]}
    #    inits = data["initials"]
    #
    #    eqs = list()
    #    for eq in data["equations"]:
    #        eqs.append(sp.sympify(eq["rhs"], locals={**vars}))
    #
    #    lst = []
    #    for var in vars.values():
    #        lst.append(var)
    #
    #    _vars = (t, *lst)
    #    system = list()
    #    for eq in eqs:
    #        system.append(sp.lambdify(_vars, eq))
    t = symbols("t")
    inits = data["initials"]
    var_names = data["variables"]
    var_funcs = {name: Function(name)(t) for name in var_names}
    exprs = [sympify(expr, locals=var_funcs) for expr in data["functions"]]
    vars_in_order = [t] + [var_funcs[name] for name in var_names]
    functions = [lambdify(vars_in_order, expr) for expr in exprs]

    return functions, inits
