def single_riffle(shuffled_deck, half1, half2):
    i, j, runner = 0, 0, 0

    while runner < len(shuffled_deck):
        if i < len(half1) and half1[i] == shuffled_deck[runner]:
            i += 1
        elif j < len(half2) and half2[j] == shuffled_deck[runner]:
            j += 1
        else: return False
        runner += 1

    return True

half1 = [1, 3, 7, 7]
half2 = [2, 4, 6, 8]
shuffled_deck = [1, 2, 3, 4, 6, 7, 8, 7]

print(single_riffle(shuffled_deck, half1, half2))
