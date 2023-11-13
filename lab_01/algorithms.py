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
    
    print("\МАТРИЦА:")
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
            if (i > 1 and j > 1 and str1[i - 1] == str2[j - 2] and str1[i - 2] == str2[j - 1]):
                action_swap = matrix[i - 2][j - 2] + 1
                
            matrix[i][j] = min(action_add, action_delete, action_change, action_swap)
    
    print("\МАТРИЦА:")
    print_matrix(matrix, str1, str2)
    
    result = matrix[n][m]
    
    return result


def damerau_levenshtein_distance_recursive(str1, str2):
    return 0


def damerau_levenshtein_distance_recursive_cache(str1, str2):
    return 0


