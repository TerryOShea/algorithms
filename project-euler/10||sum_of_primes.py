from math import sqrt

def sum_of_primes(n): 
	if n < 3: return 0
	total, i = 2, 3
	while i < n: 
		if is_prime(i): 
			total += i
		i += 2
	return total

def is_prime(n): 
	for i in range(3, int(sqrt(n)) + 1, 2): 
		if not n % i: return False
	return True

print(sum_of_primes(2000000))