def digit_powers(n):
	total = 0
	upper_bound = len(str(len(str(9**n))*(9**n)))*(9**n)
	for i in range(2, upper_bound): 
		power_digits = sum([(int(x))**n for x in str(i)])
		if i == power_digits: total += power_digits
	return total

print(digit_powers(5))