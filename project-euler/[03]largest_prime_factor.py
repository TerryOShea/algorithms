from math import sqrt

def largest_prime_factor(n): 
	smaller_factors_max = 0
	for i in range(1, int(sqrt(n)) + 1): 
		if not n % i:
			if is_prime(n//i): return n//i
			if is_prime(i): smaller_factors_max = i
	return smaller_factors_max

def is_prime(n): 
	if n == 2: return True
	if not n % 2: return False
	for i in range(3, int(sqrt(n)) + 1, 2): 
		if not n % i: return False
	return True

print(largest_prime_factor(600851475143))
