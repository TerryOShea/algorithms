from datetime import date

def counting_sundays(): 
	sundaythefirsts = 0
	d1, d2 = date(1901, 1, 1), date(2000, 12, 31)

	while(d1 < d2): 
		if d1.weekday() == 6: 
			sundaythefirsts += 1
		y, m = d1.year, d1.month + 1
		if m > 12: 
			y, m = y + 1, 1
		d1 = date(y, m, 1)

	return sundaythefirsts

print(counting_sundays())