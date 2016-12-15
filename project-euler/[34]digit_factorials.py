from math import factorial

f_ref = [factorial(x) for x in range(10)]

def digit_factorials(): 
	total = 0

	# Since 9!*7 and 9!*8 are both 7-digit numbers, the largest digit-factorials-sum number must be 
	# less than 9!*7 = 2540160, so that will be our upper bound
	for i in range(10, 2540160): 
		if equals_digit_factorials_sum(i): 
			total += i
	return total

def equals_digit_factorials_sum(n): 
	total = 0
	a = n
	while a > 0: 
		total += f_ref[a%10]
		a //= 10
	return total == n

print(digit_factorials())