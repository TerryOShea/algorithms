def cake_thief(cake_tuples, weight_capacity):
    """
    takes a list of cake tuples (weight, value) and a weight capacity
    returns the maximum value the weight capacity can hold
    """
    max_values_at_capacities = [0] * (weight_capacity + 1)
    for current_capacity in range(weight_capacity + 1):
        current_max_value = 0
        for cake_weight, cake_value in cake_tuples:
            if cake_weight == 0 and cake_value != 0:
                return float('inf')
            if cake_weight <= current_capacity:
                max_value_using_cake = cake_value + max_values_at_capacities[current_capacity - cake_weight]
                current_max_value = max(current_max_value, max_value_using_cake)
        max_values_at_capacities[current_capacity] = current_max_value
    return max_values_at_capacities[-1]

CAKES = [
    (7, 160),
    (3, 90),
    (2, 15)
]
print(cake_thief(CAKES, 20))
