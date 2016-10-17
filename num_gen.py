import sys
import random

numdb = []
newnumdb = []

with open('numgen.dat') as f:
    numdb = [line.strip() for line in f]


def generate_number(ndigits=8):
    return ''.join([random.choice('0123456789') for _ in range(ndigits)])


def print_to_file(number):
    with open('numgen.dat', 'a') as f:
        [print(n, file=f, end='\n') for n in number]


def is_unique(number):
    if number in numdb + newnumdb:
        return False
    elif any(number.startswith(n) or n.startswith(number) for n in numdb + newnumdb):
        return False
    return True


if len(sys.argv) != 2:
    sys.exit('Usage: num_gen.py [n]')
elif len(sys.argv) == 2:
    count = 0
    while count < int(sys.argv[1]):
        number = generate_number()
        if is_unique(number):
            newnumdb.append(number)
            count += 1
            print(number)
    print_to_file(newnumdb)
