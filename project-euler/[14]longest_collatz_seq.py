def longest_collatz_seq(n): 
	maxlength, maxnum, seen = 0, 0, {}
	for i in range(2, n): 
		b, lg = i, 1
		while b > 1 and b not in seen: 
			b = b//2 if not b % 2 else 3*b + 1
			lg += 1
		if b in seen: lg += seen[b] - 1
		seen[i] = lg
		if lg > maxlength: 
			maxlength = lg
			maxnum = i
	return maxnum

print(longest_collatz_seq(1000000))