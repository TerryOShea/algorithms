def string_permutations(str):
    if len(str) == 0: return None
    if len(str) == 1: return [str]
    prevs = string_permutations(str[1:])

    perms = set()

    for prev in prevs:
        for i in range(len(prev)):
            perms.add(prev[:i] + str[0] + prev[i:])
    return perms

print(string_permutations("melon"))
