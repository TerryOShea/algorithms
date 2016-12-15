def names_scores(a): 
	return sum([(i+1)*sum([ord(y)-64 for y in x[1:-1]]) for i, x in enumerate(sorted(a))])

with open('names.txt') as f: 
	print(names_scores(f.readline().split(',')))