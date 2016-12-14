from functools import reduce
from operator import mul

def smallest_multiple(n): 
	prime_factors = []
	for i in range(2, n+1): 
		d, ct = i, 0
		while d > 1 and ct < len(prime_factors): 
			if not d % prime_factors[ct]: 
				d /= prime_factors[ct]
			ct += 1
		if d > 1: 
			prime_factors.append(d)
	return reduce(mul, prime_factors)

print(smallest_multiple(20))
