#!/usr/bin/python3

def read_and_write(filename):
    with open(filename + '.csv', 'r') as csv:
        with open(filename + '.tsv', 'w') as tsv:
            tmp = csv.read().replace('\",\"', '\"\t\"').\
                replace(',true,', '\ttrue\t').\
                replace(',false,', '\tfalse\t')
            tsv.write(tmp)


if __name__ == "__main__":
    read_and_write('ds')
