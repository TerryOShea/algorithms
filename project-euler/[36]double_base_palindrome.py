def double_base_palindrome(n): 
	total = 0
	for i in range(1, n, 2): 
		if is_palindrome(str(i)) and is_palindrome(bin(i)[2:]): 
			total += i
	return total

def is_palindrome(s): 
	return s == s[::-1]

print(double_base_palindrome(1000000))