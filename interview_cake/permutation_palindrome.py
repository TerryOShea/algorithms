def permutation_palindrome(word):
    letters_seen = set()

    for letter in word:
        if letter in letters_seen:
            letters_seen.remove(letter)
        else:
            letters_seen.add(letter)

    return len(letters_seen) < 2

print(permutation_palindrome("civic"))
print(permutation_palindrome("ivicc"))
print(permutation_palindrome("civil"))
