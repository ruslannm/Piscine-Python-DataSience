#!/usr/bin/python3

import sys

def shift_str(str, shift):
    try:
        str.encode('ascii')
    except UnicodeEncodeError:
        raise Exception("The script does not support your language yet.")
    new_str = ''
    lower = [chr(i) for i in range(ord('a'), ord('z') + 1)]
    upper = [chr(i) for i in range(ord('A'), ord('Z') + 1)]
    for i in str:
        if i in lower:
            new_str += lower[(lower.index(i) + shift) % 26]
        elif i in upper:
            new_str += upper[(upper.index(i) + shift) % 26]
        else:
            new_str += i
    return new_str


def main():
    argv = sys.argv
    if len(argv) == 4:
        try:
            shift = int(argv[3])
        except ValueError:
            raise Exception('Incorrect argument')    
        if argv[1] == 'encode':
            print(shift_str(argv[2], shift))
        elif argv[1] == 'decode':
            print(shift_str(argv[2], -shift))
        else:
            raise Exception('Incorrect operation')
    else:
        raise Exception('Incorrect number of arguments')


if __name__ == "__main__":
    main()