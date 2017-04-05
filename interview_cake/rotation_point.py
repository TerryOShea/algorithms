def rotation_point(words):
    first_word = words[0]
    floor_idx = 0
    ceil_idx = len(words) - 1

    while floor_idx < ceil_idx:
        midpoint = floor_idx + ((ceil_idx - floor_idx)//2)

        if words[midpoint] >= first_word:
            floor_idx = midpoint
        else:
            ceil_idx = midpoint

        if floor_idx + 1 == ceil_idx:
            return ceil_idx

print(rotation_point(['ptolemaic', 'retrograde', 'supplant', 'undulate', 'xenoepist', 'asymptote', 'babka', 'banoffee', 'engender', 'karpatka', 'othellolagkage']))
