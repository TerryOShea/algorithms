from math import factorial

def lex_perm(a, n): 
	l = len(a)
	n -= 1 #so "millionth" = 999999 if we're indexing from 0
	final = ""

	for _ in range(l): 
		i = n//factorial(len(a)-1)
		n -= i*factorial(len(a)-1)
		final += str(a[i])
		a = a[:i] + a[i+1:]
	return final

print(lex_perm([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 1000000))