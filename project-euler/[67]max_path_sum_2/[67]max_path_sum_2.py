def max_path_sum_2(tri): 
	rows, nums = 1, 1
	while nums < len(tri): 
		rows += 1
		nums += rows

	for i in range(rows - 2, -1, -1): 
		for j in range(i+1): 
			# for every row except the bottom, adds to each number the max of the 2 numbers below
			tri[(((i**2)+i)/2)+j] += max(tri[((((i+1)**2)+i+1)/2)+j], tri[((((i+1)**2)+i+1)/2)+j+1])

	return tri[0]

triangle = []
with open('triangle.txt') as f: 
	for line in f: 
		[triangle.append(int(x)) for x in line.split()]
print(max_path_sum_2(triangle))