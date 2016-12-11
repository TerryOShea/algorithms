def n_length_fib(n): 
	if n == 1: return 1
	prevs = [1, 1]
	index = 2
	while True: 
		prevs[index%2] = sum(prevs)
		index += 1
		if len(str(max(prevs))) >= n: return index

print(n_length_fib(1000))