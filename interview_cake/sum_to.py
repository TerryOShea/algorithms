def sum_to(flight_length, movie_lengths):
    if len(movie_lengths) < 2:
        return False

    seen = set()
    for length in movie_lengths:
        if (flight_length - length) in seen:
            return True
        seen.add(length)
    return False

# print(sum_to(46, [20, 18, 43, 26, 30]))
# LEARNED: set() or set([1, 2, 3, 4])
# LEARNED: set_name.add(el)
# LEARNED: if el in set_name
