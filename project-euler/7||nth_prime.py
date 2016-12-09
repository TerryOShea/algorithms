from math import sqrt 

def nth_prime(n): 
	i, ct = 1, 1
	while ct <= n: 
		i += 1
		if is_prime(i): ct += 1
	return i

def is_prime(n): 
	if n == 2: return True
	if not n % 2: return False
	for i in range(3, int(sqrt(n)) + 1, 2): 
		if not n % i: return False
	return True

print(nth_prime(10001))