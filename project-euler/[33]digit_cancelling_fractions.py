from operator import mul
from fractions import Fraction

def digit_cancelling_fractions(): 
	nums, dens = [], []
	for i in range(11, 100): 
		for j in range(i+1, 100): 
			if curious_frac(i, j): 
				nums.append(i)
				dens.append(j)
	return Fraction(reduce(mul, nums), reduce(mul, dens)).denominator

# returns whether fraction a/b is "curious", like 49/98 = 4/8, the 9s cancelling each other out
def curious_frac(a, b): 
	return (a%10 or b%10) and \
	((a//10 == b%10 and Fraction(a, b) == Fraction(a%10, (b//10 if b//10 else 1))) or \
		(a%10 == b//10 and Fraction(a, b) == Fraction(a//10, (b%10 if b%10 else 1))))

print(digit_cancelling_fractions())