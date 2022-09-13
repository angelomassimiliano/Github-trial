import sys
import numpy as np


def main():
    # script = sys.argv[0]  # name of the script .py
    # filename = sys.argv[1]  # name of the file you want to read w/ the script
    print(np.loadtxt(sys.stdin))

if __name__ == '__main__':
    main()

