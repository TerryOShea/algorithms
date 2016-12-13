def sum_square_diff(n): 
	total = 0
	for i in range(1, n+1): 
		total -= i**2
	return total + sum(range(1, n+1))**2

print(sum_square_diff(100))
