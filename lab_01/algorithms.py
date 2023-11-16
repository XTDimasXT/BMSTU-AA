from functions import *

def levenshtein_distance(str1, str2):
    n, m = len(str1), len(str2)
    matrix = create_levenshtein_matrix(n + 1, m + 1)
    
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            action_add = matrix[i - 1][j] + 1
            action_delete = matrix[i][j - 1] + 1
            action_change = matrix[i - 1][j - 1]
            
            if str1[i - 1] != str2[j - 1]:
                action_change += 1
                
            matrix[i][j] = min(action_add, action_delete, action_change)
    
    print("\nМАТРИЦА:")
    print_matrix(matrix, str1, str2)

    result = matrix[n][m]
    
    return result
    

def damerau_levenshtein_distance(str1, str2):
    n, m = len(str1), len(str2)
    matrix = create_levenshtein_matrix(n + 1, m + 1)
    
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            action_add = matrix[i - 1][j] + 1
            action_delete = matrix[i][j - 1] + 1
            action_change = matrix[i - 1][j - 1]
            
            if str1[i - 1] != str2[j - 1]:
                action_change += 1
                
            action_swap = n
            if i > 1 and j > 1 and str1[i - 1] == str2[j - 2] and str1[i - 2] == str2[j - 1]:
                action_swap = matrix[i - 2][j - 2] + 1
                
            matrix[i][j] = min(action_add, action_delete, action_change, action_swap)
    
    print("\nМАТРИЦА:")
    print_matrix(matrix, str1, str2)
    
    result = matrix[n][m]
    
    return result


def damerau_levenshtein_distance_recursive(str1, str2):
    n, m = len(str1), len(str2)

    flag = 0
    if n == 0 or m == 0:
        return abs(n - m)

    if str1[-1] != str2[-1]:
        flag = 1

    result = min(
        damerau_levenshtein_distance_recursive(str1[:-1], str2) + 1,
        damerau_levenshtein_distance_recursive(str1, str2[:-1]) + 1,
        damerau_levenshtein_distance_recursive(str1[:-1], str2[:-1]) + flag)
    
    if n > 1 and m > 1 and str1[-1] == str2[-2] and str1[-2] == str2[-1]:
        result = min(result, damerau_levenshtein_distance_recursive(str1[:-2], str2[:-2]) + 1)

    return result


def damerau_levenshtein_distance_recursive_cache(str1, str2):
    n, m = len(str1), len(str2)
    matrix = create_levenshtein_matrix(n + 1, m + 1)

    for i in range(n + 1):
        for j in range(m + 1):
            matrix[i][j] = -1

    recursive_cache(str1, str2, n, m, matrix)

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