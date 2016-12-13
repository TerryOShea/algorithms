from math import sqrt

def pythagorean_triplet(): 
	a, b = 0, 0
	for i in range(1, 333): 
		for j in range(2, 500): 
			if (-2)*i*j + 2000*i + 2000*j == 1000000: 
				return i*j*sqrt(i**2 + j**2)

print(int(pythagorean_triplet()))
