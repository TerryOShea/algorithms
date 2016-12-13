def multiples_3_and_5(upper_limit): 
	total = 0
	for i in range(3, upper_limit, 3): 
		total += i
	for j in range(5, upper_limit, 5): 
		if j % 15: total += j
	return total

print(multiples_3_and_5(1000))
