def num_spiral_diagonals(n):
    total = 1
    for i in range(3, n+1, 2):
        total += 4*(i**2)-12*((i-1)//2)
    return total
print(num_spiral_diagonals(1001))
