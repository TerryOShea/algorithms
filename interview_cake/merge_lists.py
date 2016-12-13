def merge_lists(a1, a2): 
	merged = []
	i, j = 0, 0
	while i < len(a1) and j < len(a2): 
		if a1[i] < a2[j]:
			merged.append(a1[i])
			i += 1
		else: 
			merged.append(a2[j])
			j += 1
	merged.extend(a1[i:] if i < len(a1) else a2[j:])
	return merged

print(merge_lists([3, 4, 6, 10, 11, 15], [1, 5, 8, 12, 14, 19]))