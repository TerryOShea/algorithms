def pandigital_products(): 
	prods = []

	# i*j must be at most a 4-digit number--a 5-digit i*j would mean a 2-digit * a 2-digit, impossible to get to 5 digits with those
	# i*j must be at least a 4-digit number--a 3-digit i*j would mean a 3-digit * a 3-digit, impossible to get 3 digits with those
	# so i and j must be a 1-digit and a 4-digit or a 2-digit and a 3-digit
	# we could optimize further than the i and j ranges below, but this is good enough for now

	for i in range(1234, 9877): 
		for j in range(1, 10):
			if are_pandigital(i, j): 
				prods.append(i*j)

	for i in range(123, 988): 
		for j in range(12, 99): 
			if are_pandigital(i, j): 
				prods.append(i*j)

	return sum(set(prods))

# checks that: 
#     a, b, and a*b do not have 0
#     a, b, a*b have 9 digits between them
#     those 9 digits are unique
def are_pandigital(a, b): 
	c = get_digits(a)
	c.extend(get_digits(b))
	c.extend(get_digits(a*b))
	return 0 not in c and len(c) == 9 and len(set(c)) == 9

# returns an array of the digits in n
def get_digits(n): 
	a = []
	while n: 
		a.append(n % 10)
		n //= 10
	return a

print(pandigital_products())