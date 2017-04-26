def make_matrix(str1, str2):
    matrix = [[0 for x in range(len(str1) + 1)] for y in range(len(str2) + 1)]

    for i in range(len(str1)):
        for j in range(len(str2)):
            if str1[i] == str2[j]:
                matrix[i + 1][j + 1] = matrix[i][j] + 1
            else:
                matrix[i + 1][j + 1] = 0

    return matrix

def longest_common_substring(str1, str2):
    matrix = make_matrix(str1, str2)
    greatest_substring = ""
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] > len(greatest_substring):
                greatest_substring = str2[j - matrix[i][j]:j]

    return greatest_substring

print(longest_common_substring("rat", "cat"))
