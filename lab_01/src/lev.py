from functions import *

def levenshtein_distance(str1, str2, flag_output=False):
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
    
    if flag_output:
        print("\nМАТРИЦА:")
        print_matrix(matrix, str1, str2)

    result = matrix[n][m]
    
    return result