from operator import mul

def get_products_of_all_ints_except_at_index(ints):
    total_product = reduce(mul, ints, 1)
    return [total_product//x for x in ints]

print get_products_of_all_ints_except_at_index([1, 7, 3, 4])