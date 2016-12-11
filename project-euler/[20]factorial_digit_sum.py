from operator import add, mul
from functools import reduce

def factorial_digit_sum(n): 
	return reduce(add, [int(x) for x in str(reduce(mul, range(2, n+1)))])

print(factorial_digit_sum(100))