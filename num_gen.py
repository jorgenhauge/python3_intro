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


def check_and_add(num):
    global numdb, newnumdb
    print('checking', num, end=': ')
    if num in numdb + newnumdb:
        print('number already exists, not added')
        return False
    elif any(num.startswith(n) for n in numdb + newnumdb):
        print('an existing number is a prefix, not added')
        return False
    elif any(n.startswith(num) for n in numdb + newnumdb):
        print('this is a prefix for an existing number, not added')
        return False
    else:
        print('New number added')
        newnumdb.append(num)
        return True


if len(sys.argv) != 2:
    sys.exit('Usage: num_gen.py [n]')
elif len(sys.argv) == 2:
    count = 0
    while count <= int(sys.argv[1]):
        numb = generate_number()
        if check_and_add(numb):
            count += 1
    print_to_file(newnumdb)
