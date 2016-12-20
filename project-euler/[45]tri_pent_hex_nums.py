from math import sqrt

# all hexagonal numbers are triangular numbers, so we're just looking
# for pentagonal-hexagonal numbers. 
# this according to the formula x^2 - 3y^2 = -2, where x = 6n-1, y = 4m-1, 
# and n is the nth pentagonal number and m is the mth hexagonal number
# (formula from http://mathworld.wolfram.com/HexagonalPentagonalNumber.html)
# this finds the nth triangular-pentagonal-hexagonal number
def tri_pent_hex_nums(n): 
	a, i, ct = [], 2, 0
	while ct < n:
		t = sqrt(((i**2)+2)/3)
		if abs(int(t) - t) < 1e-10: 
			if not (i+1)%6 and not (int(t)+1)%4: 
				a = (((i+1)//6) * (3 * ((i+1)//6) - 1))//2
				ct += 1
		i += 1
	return a
print(tri_pent_hex_nums(3))