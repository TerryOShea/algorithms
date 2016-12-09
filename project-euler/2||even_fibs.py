def even_fibs(upper_limit): 
	prev2, prev1, total = 1, 2, 0
	while prev1 < upper_limit: 
		prev2, prev1 = prev1, prev2 + prev1
		if not prev2 % 2: total += prev2
	return total

print(even_fibs(4000000))