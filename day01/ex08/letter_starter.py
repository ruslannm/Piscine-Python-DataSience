#!/usr/bin/python3

import sys

def get_name(email):
    with open('employees.tsv', 'r') as in_f:
        for i in in_f.readlines():
            i_list = i.split('\t')
            if i_list[2].strip('\n') == email.lower():
                return i_list[0]
    return None


def get_letter(email):
    return f'Dear {get_name(email)}, welcome to our team. We are sure that it will be a pleasure to work with you. Our company hires only that kind of professionals.'


def main():
    argv = sys.argv
    if len(argv) == 2:
        print(get_letter(argv[1]))


if __name__ == "__main__":
    main()