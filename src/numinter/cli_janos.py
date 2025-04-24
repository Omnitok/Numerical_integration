import argparse
from plot import plot_data

#def main():
parser = argparse.ArgumentParser(add_help=True)

parser.add_argument("x", help="The x position")
parser.add_argument("y", help="the y position")

args = parser.parse_args()
plot_data(args.x, args.y)

