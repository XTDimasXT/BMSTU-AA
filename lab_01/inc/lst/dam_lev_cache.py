from functions import *

def damerau_levenshtein_distance_recursive_cache(str1, str2, flag_output=False):
    n, m = len(str1), len(str2)
    matrix = create_levenshtein_matrix(n + 1, m + 1)

    for i in range(n + 1):
        for j in range(m + 1):
            matrix[i][j] = -1

    recursive_cache(str1, str2, n, m, matrix)

    if flag_output:
        print("\nМАТРИЦА:")
        print_matrix(matrix, str1, str2)

    result = matrix[n][m]

    return result


def recursive_cache(str1, str2, n, m, matrix):
    if matrix[n][m] != -1:
        return matrix[n][m]
    
    if n == 0:
        matrix[n][m] = m
        return matrix[n][m]
    
    if n > 0 and m == 0:
        matrix[n][m] = n
        return matrix[n][m]

    action_add = recursive_cache(str1, str2, n - 1, m, matrix) + 1
    action_delete = recursive_cache(str1, str2, n, m - 1, matrix) + 1
    action_change = recursive_cache(str1, str2, n - 1, m - 1, matrix)

    if str1[n - 1] != str2[m - 1]:
        action_change += 1 

    matrix[n][m] = min(action_add, action_delete, action_change)

    if n > 1 and m > 1 and str1[n - 1] == str2[m - 2] and str1[n - 2] == str2[m - 1]:
        matrix[n][m] = min(matrix[n][m], recursive_cache(str1, str2, n - 2, m - 2, matrix) + 1)

    return matrix[n][m]