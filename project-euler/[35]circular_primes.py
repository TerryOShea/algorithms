from math import sqrt

def circular_primes(n): 
	total = 1 if n > 2 else 0
	for i in range(3, n, 2): 
		if is_circular_prime(i): 
			total += 1
	return total

def is_circular_prime(n): 
	if not is_prime(n): return False
	for i in range(1, len(str(n))): 
		if not is_prime(int(str(n)[i:] + str(n)[:i])): return False
	return True

def is_prime(n): 
	if n == 2: return True
	if not n % 2: return False
	for i in range(3, int(sqrt(n)) + 1, 2): 
		if not n % i: 
			return False
	return True

print(circular_primes(1000000))