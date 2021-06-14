#!/usr/bin/python3

import sys


def get_mails(filename):
    with open(filename, 'r') as in_f:
        with open('employees.tsv', 'w') as out_f:
            out_f.write('Name\tSurname\tE-mail\n')
            for i in in_f.readlines():
                i_s = i.strip().lower()
                if i_s:
                    name, surname = i_s.split('@')[0].split('.')
                    out_f.write(f'{name.capitalize()}\t{surname.capitalize()}\t{i_s}\n')


def main():
    argv = sys.argv
    if len(argv) == 2:
        mails = get_mails(argv[1])


if __name__ == "__main__":
    main()