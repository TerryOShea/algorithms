from math import sqrt

def non_abundant_sums(): 
	abundants = []
	for i in range(1, 28123): 
		if factor_sum(i) > i: 
			abundants.append(i)

	is_abundant_sum = [0] * 28124
	for i in range(len(abundants)): 
		for j in range(i, len(abundants)): 
			s = abundants[i] + abundants[j]
			if s <= 28123: 
				is_abundant_sum[s] = 1
			else: 
				break

	total = 0
	for i in range(1, 28124): 
		if not is_abundant_sum[i]: 
			total += i
	return total

def factor_sum(n): 
	total = 1
	for i in range(2, int(sqrt(n))+1): 
		if not n % i: 
			total += i + n//i
	if int(sqrt(n))**2 == n: total -= int(sqrt(n))
	return total

print(non_abundant_sums())