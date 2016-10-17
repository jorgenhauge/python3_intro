#!/usr/bin/env python3
import sys

def is_prime(n):
	return n >= 2 and all(n % d != 0 for d in range(2, n))

if len(sys.argv) != 2:
	sys.exit('Usage: is_prime [number]')
elif len(sys.argv) == 2:
	number = int(sys.argv[1])

if is_prime(number):
	sys.exit(0)
else:
	sys.exit(1)