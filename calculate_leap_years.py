def is_divisible_by(numerator, denominator):
	return numerator % denominator == 0

def is_leap_year(year):
	if is_divisible_by(year, 400):
		return True
	elif is_divisible_by(year, 100):
		return False
	return is_divisible_by(year, 4)


year = 1582
count = 0

for i in range(year, 2017):
	if is_leap_year(i):
		count += 1
print('Number of leap year since: {} is: {}'.format(year, count))

