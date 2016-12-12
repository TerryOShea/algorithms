def reciprocal_cycles(n):
    maxlength, d = 0, 0
    for i in range(n, 0, -1):
        if i < maxlength + 1: break
        remainders, x = [], 1
        while True:
            x = (x % i)
            if not x or x in remainders: break
            remainders.append(x)
            x *= 10
        if len(remainders) > maxlength:
            maxlength = len(remainders)
            d = i
    return maxlength

print(reciprocal_cycles(999))
