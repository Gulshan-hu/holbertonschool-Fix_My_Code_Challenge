#!/usr/bin/env python3
import sys

def print_square(size):
    """
    Print a square with the character #
    """
    for i in range(size):
        for j in range(size):
            print("#", end="")
        print("")

if __name__ == "__main__":
    if len(sys.argv) <= 1:
        print("Missing argument")
        sys.exit(1)

    size = int(sys.argv[1])
    print_square(size)
