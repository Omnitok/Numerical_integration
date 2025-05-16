# numinter
Numerical Integration CLI tool written in Python. First group assignment in the 
Ph.D. course *Software development for researchers*, aimed to challenge our 
collaboration. It utilizes two different methods to perform the integration

1. Euler explicit,
2. Euler implicit,

and is chosen as an argument in the command given to the tool. The tool also
have optional arguments for plotting and saving solutions to a file, and integration
settings


## Installation 
Install with *build* and *pip*:

```bash
python -m build
```

```bash
pip install .
```

## Usage

Define your system of coupled equations in a Python files, seen in the `example` directory. Follow the pattern in the below to describe the Lorenz system.
```python
def system():
    rho, sigma, beta = 28, 10, 8 / 3

    def xd(t, x, y, z): return sigma * (y - x)
    def yd(t, x, y, z): return x * (rho - z) - y
    def zd(t, x, y, z): return x * y - beta * z

    z0 = 0
    y0 = 0
    x0 = 0.99
    t0 = 0

    dct = {
        "x": {"differential": xd, "initial": x0},
        "y": {"differential": yd, "initial": y0},
        "z": {"differential": zd, "initial": z0},
        "t": {"initial": t0}
    }

    return dct
```
In the above example we have three coupled equations, **xd**, **yd** and **zd** defined 
as Python functions, *rho*, *sigma* and *beta* is constants and *z0*, *y0*, *x0* and *t0*
are initial values for each of the variables. 

Call the CLI with `numinter` followed by the filename with your system of equations, which 
is the only mandatory argument. However you have a bunch of optional ones that can be seen 
if you call `numinter -h`.

### Examples
Down bellow will some examples usages be shown and explanations of the outputs:

```bash
numinter lorenz.py --method euler_implicit --step 0.001 --hs 100 --save --plot --savename lorenz.hdf5
```

In the above example is the system of equations defined in `lorenz.py` and this is given as 
the input file. The integration method is chosen with the optional argument `--method`. Integration
settings are set using the optional arguments `--step` and `--hs`. The optional argument `--plot` 
plots the solution and `--save` and `--savename` is associated with saving the solution and will 
be placed in the directory in the current working directory, together with the plot.

![alt text](https://github.com/Omnitok/Numerical_integration/blob/main/example/lorenz.png "Lorenz system example")
