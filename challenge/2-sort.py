#!/usr/bin/env python3
import sys

def sort_arguments():
    args = sys.argv[1:]
    sorted_args = sorted([int(x) for x in args])
    for arg in sorted_args:
        print(arg)

if __name__ == "__main__":
    sort_arguments()
