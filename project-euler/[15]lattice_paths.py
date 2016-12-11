from math import factorial 

def lattice_paths(n): 
	return factorial(2*n)/((factorial(n))**2)

print lattice_paths(20)