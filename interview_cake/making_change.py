def making_change(money_amount, denoms): 
	d = [0] * (money_amount + 1)
	d[0] = 1
	for i in range(len(denoms)): 
		for j in range(denoms[i], money_amount+1): 
			d[j] += d[j-denoms[i]]
	return d[money_amount]

print(making_change(4, [1, 2, 3]))