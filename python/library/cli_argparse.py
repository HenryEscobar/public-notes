# argparse template
# RTFM: https://docs.python.org/3/library/argparse.html

import argparse
import sys

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Template file for a simple CLI")
    parser.add_argument('filename', nargs='*', default=sys.stdin, type=argparse.FileType("r"), help="Input file")
    args = parser.parse_args()

    if type(args.filename) != list:
        print("-=" * 15, " STDIN ", "=-" * 15)
    
    for f in args.filename:
        if type(f) == str:
            print(f.rstrip())
        else:
            print("-=" * 15, f.name, "=-" * 15)
            for line in f:
                print(line.rstrip())

