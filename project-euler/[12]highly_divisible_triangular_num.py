from math import sqrt

def highly_divisible_triangular_num(n): 
	i, t = 1, 1
	while num_of_factors(t) <= n: 
		i += 1
		t = (i**2 + i)//2
	return t

def num_of_factors(n): 
	ct = 2
	for i in range(2, int(sqrt(n)) + 1): 
		if not n % i: 
			ct += 1 if i*i == n else 2
	return ct

#"the first to have over 500 divisors"
print(highly_divisible_triangular_num(500))