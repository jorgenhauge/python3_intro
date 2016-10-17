n = 600
while n < 700:
	d = 2
	is_prime = True
	while d < n:
		if n % d == 0:
			is_prime = False
		d += 1
	if is_prime:
		print(n)
	n += 1