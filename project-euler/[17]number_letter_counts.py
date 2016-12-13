#good up to 10,000
def number_letter_counts(n): 
	ones = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
	extras = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
	tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

	ct = 0
	for i in range(1, n+1): 
		if i % 100 in range(10, 20): ct += len(extras[(i%100)-10])
		else: ct += len(ones[i%10]) + len(tens[(i%100)//10])
		ct += len(ones[(i%1000)//100])
		ct += len(ones[i//1000])
		if i > 99 and (i%1000) not in range(0, 100): ct += 7 #hundred
		if i > 999: ct += 8 #thousand
		if i > 100 and i % 100: ct += 3 #and
	return ct

print(number_letter_counts(1000))