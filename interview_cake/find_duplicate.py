def find_duplicate(arr):
    """
    Given an list of numbers 1..n with a length of n+1 (so there's at least one duplicate),
    returns an integer that appears more than once
    """

    # (modifying the array)
    for i in range(len(arr)):
        value = abs(arr[i])
        if arr[value] < 1:
            return value
        arr[value] *= -1

    return None

print(find_duplicate([6, 2, 4, 1, 4, 3, 4]))
